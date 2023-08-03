import openai

# Set your OpenAI API key here
openai.api_key = "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"

def get_response(input_str):
    try:
        # Define the system message (same as in your original code)
        system_message = "YOUR_SYSTEM_MESSAGE_HERE"
        
        # Concatenate the system message with the input string
        combined_input = system_message + "\n" + input_str

        # Use the OpenAI API to generate the response
        response = openai.Completion.create(
            engine="text-davinci-002",  # Choose the language model engine you want to use
            prompt=combined_input,
            max_tokens=150  # Adjust the length of the response as needed
        )

        # Extract the generated text from the response
        generated_text = response['choices'][0]['text']
        
        # Split the response into a list of individual responses
        choice_list = generated_text.split("\n")

        return choice_list
    except openai.error.InvalidRequestError as e:
        # Handle the OpenAI API error
        return ["Server is so busy... Please wait for some time."]
    except Exception as e:
        # Handle other unexpected errors
        return ["Network error..."]

# Example usage:
input_str = "Can you tell me a joke?"
response_list = get_response(input_str)
for response in response_list:
    print(response)
