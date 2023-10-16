


































































































































































































































































































































































































































































































































































































import pandas as pd
from nltk.util import ngrams
from nltk.metrics import jaccard_distance
from sentence_transformers import SentenceTransformer, CrossEncoder, util
import os
import pickle

data = pd.read_excel("output.xlsx")
data = data.fillna("")

offer_embedding_string = []
for index, row in data.iterrows():
    sentence = 'for the brand: ' + row['brand'] + ', the retailer is ' + row['retailer'] + ', the product category is ' + row['child_category'] + ', which belongs to parent category ' + row['parent category'] + ', now the offer is: ' + row['offer']
    offer_embedding_string.append(sentence)

bi_encoder = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
bi_encoder.max_seq_length = 256
top_k = 32

if "offer_embeddings.pkl" not in os.listdir():
    offer_embeddings = bi_encoder.encode(offer_embedding_string, convert_to_tensor=True, show_progress_bar=True)
    with open("../../../../Desktop/fetch oa/app/offer_embeddings.pkl", "wb") as f:
        pickle.dump(offer_embeddings, f)
else:
    with open("../../../../Desktop/fetch oa/app/offer_embeddings.pkl", "rb") as f:
        offer_embeddings = pickle.load(f)

offer_user_string = []
for index, row in data.iterrows():
    sentence =  'brand: ' + row['brand'] + ' | retailer: ' + row['retailer'] + ' | category: ' + row['child_category'] + ' | parent category: ' + row['parent category'] + ' | offer: ' + row['offer']
    offer_user_string.append(sentence)

mapping = {}
for i in range(len(offer_embedding_string)):
    key = offer_embedding_string[i]
    value = offer_user_string[i]
    mapping[key] = value

cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')


def deduplicate(input_list):
    return sorted(set(input_list))


def get_obj_string_list(name):
    obj_string = []
    for index, row in data.iterrows():
        sentence =  row[name]
        if not pd.isna(sentence) and sentence != "":
            obj_string.append(sentence.lower())
    return deduplicate(obj_string)


def get_ngrams(name, n):
    characters = [c for c in name.lower()]
    return list(ngrams(characters, n))


def ngram_fuzzy_search(search_text):
    retail_string = get_obj_string_list("retailer")
    brand_string = get_obj_string_list("brand")
    cat_string = deduplicate(get_obj_string_list("child_category") + get_obj_string_list("parent category"))
    entry_string = deduplicate(cat_string + brand_string + retail_string)

    input_text = search_text
    n = 2
    input_ngrams = get_ngrams(input_text, n)
    similarities = []

    for entry in entry_string:
        entry_ngrams = get_ngrams(entry, n)
        similarity = 1 - jaccard_distance(set(input_ngrams), set(entry_ngrams))
        similarities.append((similarity, entry))

    threshold = 0.3
    k = 3
    filtered_similarities = [(similarity, entry) for similarity, entry in similarities if similarity >= threshold]
    sorted_similarities = sorted(filtered_similarities, key=lambda x: x[0], reverse=True)
    queries = sorted_similarities[:k]
    #     input_text = "targt"
    return queries


def cross_encode(encode_name):
    queries = ngram_fuzzy_search(encode_name)
    res = []

    for query_sim, query in queries:
        question_embedding = bi_encoder.encode(query, convert_to_tensor=True)
        hits = util.semantic_search(question_embedding, offer_embeddings, top_k=top_k)
        hits = hits[0]  # Get the hits for the first query
        cross_inp = [[query, offer_embedding_string[hit['corpus_id']]] for hit in hits]
        cross_scores = cross_encoder.predict(cross_inp)

        # Sort results by the cross-encoder scores
        for idx in range(len(cross_scores)):
            hits[idx]['cross-score'] = cross_scores[idx]

        for hit in hits:
            embed_str = offer_embedding_string[hit["corpus_id"]]
            user_str = mapping[embed_str]
            have_offer = not user_str.strip().endswith("offer:")
            res.append((hit['cross-score'], user_str, have_offer, query_sim, query))

    res = sorted(res, key=lambda x: x[0], reverse=True)
    return res


def my_search(search_name):
    DEBUG = False
    offer_list = cross_encode(search_name)
    res = []
    updated_offer_list = []
    for offer in offer_list:
        cross_score, user_str, have_offer, query_score, query = offer
        combined_score = cross_score + 10 * query_score
        updated_offer_list.append((combined_score, have_offer, user_str, query))

    updated_offer_list = sorted(updated_offer_list, key=lambda x: x[0], reverse=True)
    if DEBUG:
        print("===============VIS================")
        for offer in updated_offer_list[:20]:
            print("score:", offer[0], "have_offer:", offer[1], "user_str:", offer[2])
            print("=====")

    with_offer = [offer for offer in updated_offer_list if offer[1]]
    with_offer_sorted = sorted(with_offer, key=lambda x: x[0], reverse=True)
    for offer in with_offer_sorted[0:5]:
        res.append((offer[0],offer[2]))

    for offer in updated_offer_list[0:5]:
        if (offer[0], offer[2]) in res:
            continue
        res.append((offer[0], offer[2]))

    return list(res)


# print(my_search('target'))