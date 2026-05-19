from model import gemini_response, llama_response, mistral_response

def call_all_models(system_prompt, user_prompt):
    gemini_result = gemini_response(system_prompt, user_prompt)
    llama_result = llama_response(system_prompt, user_prompt)
    mistral_result = mistral_response(system_prompt, user_prompt)

    print("Gemini Response:\n", gemini_result)
    print("\nLlama Response:\n", llama_result)
    print("\nMistral Response:\n", mistral_result)

# Example call to test all models
call_all_models("You are a helpful assistant who provides concise and accurate answers", "What is the capital of Canada? Tell me a cool fact about it as well")
