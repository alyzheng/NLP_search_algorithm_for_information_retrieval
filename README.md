# NLP_search_algorithm_information_retrieval

Welcome to the Proof of Concept (POC) Machine Learning System designed to showcase our Natural Language Processing (NLP) search algorithm. This system allows you to predict and evaluate search results in a user-friendly manner. Follow the steps below to set up and run the system locally.

## Getting Started

### Requirements

Before you begin, make sure you have the following prerequisites installed on your system:

- python
- uvicorn
- fastapi
- sentence_transformer

You can install the packages by using "pip install"
  
### Step 1: Download the Repository

Start by downloading the project's "app" folder to your local machine. You can do this by cloning the GitHub repository:

```sh
git clone https://github.com/yourusername/your-repo.git
```

### Step 2: Run the POC ML System

1. Open a terminal or command prompt.

2. Change the working directory to the "app" folder, where you downloaded the project.

- For example: cd C:\Documents\NLP_search_algorithm_for_fetch_rewards-main>

```sh
cd /path/to/your/repository
```

3. Navigate to the "app" folder

```sh
cd app
```


4. Start the POC ML system by running the following command to initiates the local server for the POC ML system:

```sh
uvicorn app:app
```

### Step 3: Access the Swagger UI

1. Open your preferred web browser (e.g., Chrome).

2. Navigate to [http://localhost:8000/docs](http://localhost:8000/docs).
You will be greeted by the Swagger UI, which provides a user-friendly interface to interact with the API.

- **Be careful**: By default, our ML application is served at port 8000, not the URL provided by the command line"Uvicorn running on...".
  

### Step 4: Interact with the Swagger UI

1.  Click the down arrow to expand the POST function.
    
2.  Click the “Try it out” button.

3.  Change the "string" part under the Request body to a user query(e.g., 'target').
  
4.  Click "Execute" to send the request and see the results.

## Deployment Sample

The final deployment sample is as below:

![image](https://github.com/alyzheng/NLP_search_algorithm_for_fetch_rewards/assets/114775966/2e23587c-cbd2-4284-aaaa-41c86b46a078)
![image](https://github.com/alyzheng/NLP_search_algorithm_for_fetch_rewards/assets/114775966/4c85b171-3d01-4d82-b348-5bac988eb426)

## Usage

Explore the API documentation within the Swagger UI to understand the available endpoints and make use of the NLP search algorithm.

## Contributing

We welcome contributions and feedback from the community. Feel free to submit issues, feature requests, or pull requests to help us improve this POC ML system.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
