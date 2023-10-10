# NLP_search_algorithm_for_fetch_rewards

### Case Background and Business Problem

Fetch Rewards is a mobile app that rewards users for scanning and uploading shopping receipts,
and allows users to earn points for gift cards—a rewarding way to shop

Now Fetch wants to develop an effective tool for users to search for offers easily, so as to maximize
app usage and enhance partner relationships

### Requirements

The tool should return a list of relevant offers when a user searches for a category/brand/retailer.

The tool should return the score used to measure the similarity of text

The tool is expected to provide a good user experience

### Task Definition

Task: Information retrieval

Input & Output: User query & A list of offers highly relevant to user’s query

Database: Three dataset comprising categories, brands, retailers, and associated offers

Objective: Given user query and database, retrieve and present the top 'k' offers that are most
relevant to the user's query

### Pipeline: Core Retriever

The main question is how to build an effective retriever when working with a database of entries.
Typically, two solutions are considered for the Information Retrieval (IR) task.

**1. BM 25 Frequency-based Retriever**
Pros:
    a. BM25 is computationally efficient (no training needed) and scales well for a mobile app
       environment with potentially large datasets
    b. It can be effective for simple search tasks, such as category, brand, or retailer lookup
Cons:
    a. BM25 does not consider the semantic meaning or context of the user query, which may
       result in suboptimal ranking, so the algorithm might not select the potential offers that
       best fit with users’ query
    b. BM25 does not adapt to changing user behavior or preferences
**2. Neural Retriever (SentenceTransformer)**
Pros:
    a. Better performance on information retrieval benchmark, which is to say, the potential
       offers that returned to the user will be more accurate
    b. Align well with user intent by capturing complex semantic relationships between queries,
       which will generate relevant and context-aware potential offers relevant to the user
       queries
Cons:
    a. Rely on large amounts of labeled data for training, and the availability of such data for
       specific retail domains and offer categories may vary, affecting the performance of the
       algorithm


**_3. Solution Retriever_**
I chose Neural Retriever as the solution method, for 1) Its better performance to understand user’s
query 2) Its limitation can be avoided by using pre-trained models

To further improve the performance, I chose to deploy a rerank algorithm for the retrieved offers,
to better adapt to complex semantic search situations.

### Pipeline: User-friendly Features

_User Scenario 1 : User Query with Typo_
Suppose a user enters his query with typos (e.g., ’targt’ instead of ‘target’), how to ensure the tool
could identify the actual query?

**_App Feature 1_** : _Ngram Fuzzy Search_
Before encoding, I chose Ngram fuzzy search to understand the user query, which involves
matching the user's query with relevant terms in the dataset. This process efficiently corrects typos
and enhances search accuracy and user experience.

_User Scenario 2 : Lengthy Offer Output_
Suppose a user enters their query, then a lengthy result is presented to him (e.g., for the brand
prego, the retailer is mcalisters deli, the product category is red pasta sauce, which belongs to
parent category pasta sauce, now the offer is...).
How can we make this offer output more readable and user-friendly?

**_App Feature 2 :_** _Design User-friendly Results Presentation Formats_
Different from the lengthy string used for algorithmic processing, I created a user-friendly output
string to provide users with a quick and informative overview of offers, significantly enhancing their
app experience.


### Appendix: Technical Specifications

_1. Character-level Matching (Ngram Fuzzy Search)_
    _a._ Ngram Similarity Calculation
    Begin by calculating character-level similarity between the user’s typo query and potential
    actual queries.
    _b._ Threshold-Based Filtering
    Next, filter out potential queries that fall below a defined threshold.

```
Search Query Query Identification Select^ Relevant Offers^ Present Offers
```
```
Ngram Fuzzy Search
(App Feature 1)
```
```
SentenceTransformer
(Solution Retriever)
```
```
User-friendly Formats
(App Feature 2)
```

_c._ Top-K Potential Queries
Finally, return the top-K potential queries based on their similarity scores.

_2. SentenceTransformer_
    _a._ Semantic Representation
    Begin by converting database entries and user query into vectorized representations using
    SentenceTransformer.
    _b._ Bi-Encoder to Retrieve
    Next, use bi-encoder to calculate cosine similarity scores between representations of query
    and available offers, then retrieves a list of potentially offers relevant to the query.
    _c._ Cross-Encoder to Rerank
    Finally, use cross-encoder to score the retrieved offers within the context of the query, then
    generate the ultimate search results.


