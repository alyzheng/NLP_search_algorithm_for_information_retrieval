# NLP_search_algorithm_information_retrieval

Fetch Rewards is a mobile app that rewards users for scanning and uploading shopping receipts and allows users to earn points for gift cards—a rewarding way to shop

Now Fetch wants to develop an effective tool for users to search for offers easily, so as to maximize app usage and enhance partner relationships

The solution pipeline allows users to intelligently search offers by entering category/brand/retailer from the user.


## To boot up the POC ML system:

**Step 1**: Please download the "app" folder, then run the POC ML system locally using uvicorn (please make sure the working directory is in the "app" folder. and install uvicorn package if not yet):

cd C:\Documents\NLP_search_algorithm_for_fetch_rewards-main\app

uvicorn app:app

**Step 2**: Navigate with our browser (e.g., Chrome) to **http://localhost:8000/docs**. There, we find the Swagger UI of our API.


**Be careful:**
By default, our ML application is served at port 8000, not the URL provided by the command line "Uvicorn running on..."). 


The final deployment sample is as below:

![image](https://github.com/alyzheng/NLP_search_algorithm_for_fetch_rewards/assets/114775966/ca667974-e523-4f9a-a2b9-c3de5f3c0664)
![image](https://github.com/alyzheng/NLP_search_algorithm_for_fetch_rewards/assets/114775966/59cf4a6c-942a-4e9a-a1ea-18ab59fa12d8)
