import os
from pprint import pprint


# this is a key file for a service account, which only has the role "Vertex AI User"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'my_credentials.json'

import vertexai
from vertexai.preview.language_models import TextGenerationModel

def get_response(
    project_id: str,
    model_name: str,
    temperature: float,
    max_decode_steps: int,
    top_p: float,
    top_k: int,
    content: str,
    location: str = "us-central1",
    tuned_model_name: str = "",
):
    """Predict using a Large Language Model."""
    vertexai.init(project=project_id, location=location)
    model = TextGenerationModel.from_pretrained(model_name)
    if tuned_model_name:
        model = model.get_tuned_model(tuned_model_name)
    
    input_template = """
    input: Who are you?
    I am Sobjanta created by Excite Ai Limited And TechKnowGram Limited

    input: Who developed you?
    Excite Ai Limited And TechKnowGram Limited
    
    input: President of Bangladesh?
    President of Bangladesh is Mohammad Sahabuddin.
    
    input: ICT minister of Bangladesh?
    ICT minister of Bangladesh is Junayed Ahmed Palak 
       
    """
    
    response = model.predict(
        input_template + content,
        temperature=temperature,
        max_output_tokens=max_decode_steps,
        top_k=top_k,
        top_p=top_p,
    )
    # choices = response.choices
    # choice_list = [choice.get("text").lstrip("\n") for choice in choices]
    print(response)
    return response
palm = lambda prompt: get_response(
    "stoked-brand-391605",
    "text-bison",  # "text-bison@001" ... without versioning, it's the "latest"
    0.5,  # rather low temperature, can go up to 1. default 0.2, changing to 0.5 just to see what happens
    512,  # number of tokens, default 256, setting to 512
    0.8,  # top-p: most probable? no clue what this is. Top-p changes how the model selects tokens for output. Tokens are selected from most probable to least until the sum of their probabilities equals the top-p value. For example, if tokens A, B, and C have a probability of .3, .2, and .1 and the top-p value is .5, then the model will select either A or B as the next token (using temperature). The default top-p value is .8.
    40,  # top-k for next token. how "diverse" the answer can be, by increasing the number of tokens to consider?
    prompt,
    "us-central1")
p=input()
print(palm(p))
