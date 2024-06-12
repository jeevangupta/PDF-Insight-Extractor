
# PDF Insight Extractor 
    
- using Anthropic Claude AI API/ Open AI GPT API and streamlit a UI library in Python

## Getting Started Steps: 
1. create vertuial environment using below command
    python3 -m venv env

2. activate vertuial environment
    source env/bin/activate

3. create .env system file to store API key

4. use below command to include above .env file in system
    source .env


## Resume Insight Extractor - extract usefull data from resume

- To run this applitcation use below command.
    
    streamlit run resume_insight_extractor.py


## Blog Post Insight Extractor - summarise blog post, extract title, keywords, sentiment, summary, and more
- To run this applitcation use below command.
    
    streamlit run blog_post_insight_extractor.py

## command to create docker image
    docker build -t jeevan-gupta/pdf-insight-extractor:v1.0 .

## command to run docker image
- - by image name
    docker run -p 8080:8501 --name pdf-insight-extractor jeevan-gupta/pdf-insight-extractor:v1.0
    
- - by image id
    docker run -p 8080:8501 --name pdf-insight-extractor --env-file=.env 00dcbe620058

- - after running the above command you will be able to access the application at below URL:
    http://localhost:8080