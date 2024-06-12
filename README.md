
# PDF Insight Extractor 
    
- using Anthropic Claude AI API/ Open AI GPT API and streamlit a UI library in Python

## Getting Started Steps: 
1. create a vertuial environment using the below command
    python3 -m venv env

2. activate vertuial environment
    source env/bin/activate

3. create a .env system file to store the API key

4. use the below command to include the above .env file in the system
    source .env


## Resume Insight Extractor - extract useful data from resume

- To run this application use the below command.
    
    streamlit run resume_insight_extractor.py


## Blog Post Insight Extractor - summarise blog post, extract title, keywords, sentiment, summary, and more
- To run this application use the below command.
    
    streamlit run blog_post_insight_extractor.py

## command to create the docker image
    docker build -t jeevan-gupta/pdf-insight-extractor:v1.0 .

## command to run docker image
- by image name

      docker run -p 8080:8501 --name pdf-insight-extractor jeevan-gupta/pdf-insight-extractor:v1.0
    
- by image ID

      docker run -p 8080:8501 --name pdf-insight-extractor 00dcbe620058

*after running the above command you will be able to access the application at the below URL:*
    
    http://localhost:8080
