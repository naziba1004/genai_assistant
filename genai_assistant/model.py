from langchain_ibm import ChatWatsonx
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
import config

# Function to initialize google model
def google_initialize_model():
    return ChatGoogleGenerativeAI(
        model=config.GEMINI_MODEL_ID,
        temperature=config.GOOGLE_PARAMETERS['temperature'],
        max_tokens=config.GOOGLE_PARAMETERS['max_tokens'],
    )

# Function to initialize ibm model
def ibm_initialize_model(model_id):
    return ChatWatsonx(
        model_id=model_id,
        url=config.IBM_CREDENTIALS['url'],
        api_key=config.IBM_CREDENTIALS['api_key'],
        space_id=config.IBM_CREDENTIALS['space_id'],
        params=config.IBM_PARAMETERS
    )

# Initialize models
gemini_llm = google_initialize_model()
llama_llm = ibm_initialize_model(config.LLAMA_MODEL_ID)
mistral_llm = ibm_initialize_model(config.MISTRAL_MODEL_ID)

# Define JSON output structure
class AIResponse(BaseModel):
    summary: str = Field(description="Summary of the user's message")
    sentiment: int = Field(description="Sentiment score from 0 (negative) to 100 (positive)")
    response: str = Field(description="Suggested response to the user")
    action: str = Field(description="Recommended action for the support rep")

# JSON output parser
json_parser = JsonOutputParser(pydantic_object=AIResponse)

# Main response function
def get_ai_response(model, template, system_prompt, user_prompt):
    chain = template | model | json_parser
    return chain.invoke({'system_prompt':system_prompt, 'user_prompt':user_prompt, 'format_prompt':json_parser.get_format_instructions()})

# Model-specific response functions

def gemini_response(system_prompt, user_prompt):
    return get_ai_response(gemini_llm, config.GEMINI_TEMPLATE, system_prompt, user_prompt)

def llama_response(system_prompt, user_prompt):
    return get_ai_response(llama_llm, config.LLAMA_TEMPLATE, system_prompt, user_prompt)

def mistral_response(system_prompt, user_prompt):
    return get_ai_response(mistral_llm, config.MISTRAL_TEMPLATE, system_prompt, user_prompt)
