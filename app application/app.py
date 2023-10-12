from fastapi import FastAPI
import joblib
from my_search_module import my_search
from pydantic import BaseModel
from typing import List


# FastAPI
api_title = " FetchRewardApp"
api_description = "This is a very fancy project, with auto docs for the API and everything"
app = FastAPI(title=api_title, description=api_description)


class SearchRequest(BaseModel):
    search_name: str


class SearchResult(BaseModel):
    score: float
    user_str: str


@app.post("/search", response_model=List[SearchResult])
def search(search_request: SearchRequest):
    search_name = search_request.search_name
    results = my_search(search_name)
    # Convert the results to the desired format
    search_results = [SearchResult(score=score, user_str=user_str) for score, user_str in results]
    return search_results

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)






