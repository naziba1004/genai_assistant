import os
from langchain_core.prompts import PromptTemplate
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

# Google Model parameters
GOOGLE_PARAMETERS = {
    "temperature": 0.7,
    "max_tokens": None,
}

# watsonx credentials
IBM_CREDENTIALS = {
    "url": "https://ca-tor.ml.cloud.ibm.com",
    "api_key": os.getenv("IBM_API_KEY"),
    "space_id": "be554f0d-5d70-4ef8-96bd-0237d44058e4"
}

# IBM Model parameters
IBM_PARAMETERS = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 256,
}

# Model IDs

GEMINI_MODEL_ID = "gemini-3-flash-preview"
LLAMA_MODEL_ID = "meta-llama/llama-3-3-70b-instruct"
MISTRAL_MODEL_ID = "mistralai/mistral-small-3-1-24b-instruct-2503"

# Prompt templates

GEMINI_TEMPLATE = PromptTemplate(
    template="System: {system_prompt}\n{format_prompt}\nHuman: {user_prompt}",
    input_variables=["system_prompt", "format_prompt", "user_prompt"]
)

LLAMA_TEMPLATE = PromptTemplate(
    template='''<|begin_of_text|><|start_header_id|>system<|end_header_id|>
{system_prompt}\n{format_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>
{user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
''',
    input_variables=["system_prompt", "format_prompt", "user_prompt"]
)

MISTRAL_TEMPLATE = PromptTemplate(
    template="<s>[INST]{system_prompt}\n{format_prompt}\n{user_prompt}[/INST]",
    input_variables=["system_prompt", "format_prompt", "user_prompt"]
)
