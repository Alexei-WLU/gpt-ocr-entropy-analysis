# https://platform.openai.com/docs/api-reference/chat/create?lang=python
# https://platform.openai.com/docs/guides/vision

import os
import sys
import time
import copy
import json
import base64


from openai import OpenAI
import math

def pause():
    programPause = input("Press the <ENTER> key to continue...")


# Get the API key from the environment variable
key = os.getenv('OPENAI_API_KEY')

# If the key is not found, raise an error
if key is None:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key= key)

deployment_model= "gpt-4o"
number_of_completions=1

token_print_limit = 3


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "2106.13823v3-P3-300.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)


system_prompt= """
You are an advanced Optical Character Recognition (OCR) system designed specifically for mathematical content, integrated with LaTeX conversion and verification capabilities. Your primary tasks are:

1. **Accurately recognize mathematical equations** from provided images of research paper pages. This includes handling complex mathematical symbols, operators, fractions, integrals, summations, subscripts, superscripts, and other mathematical notations.

2. **Convert the recognized equations** into syntactically correct and semantically accurate LaTeX code. "Semantically accurate" means that the LaTeX code must exactly match the original equation in terms of symbols, structure, and formatting as it is visually represented.

3. **Provide the recognized equations in the following LaTeX output format**:
```
\begin{equation}
[LaTeX code of the equation] \tag{equation number if present}
\end{equation}

\begin{equation}
[LaTeX code of the equation] \tag{equation number if present}
\end{equation}
```
- Ensure that each equation is formatted properly and includes the correct LaTeX syntax.
- The "equation number" should be included only if it appears in the image.

4. **In your response**, provide only the LaTeX code in the specified format without any explanations or comments.
"""

user_prompt= """
Please thorothly  process the attached image of a research paper page and extract all mathematical equations present.

Provide only the  LaTeX code in the following output format:
```
\begin{equation}
[LaTeX code of the equation] \tag{equation number if present}
\end{equation}

\begin{equation}
[LaTeX code of the equation] \tag{equation number if present}
\end{equation}
```
"""


messages = [
    {"role": "system", "content": system_prompt},
    {
        "role": "user",
        "content": [
            {"type": "text", "text": user_prompt},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}",
                    "detail": "high"
                }
            }
        ]
    }
]


def get_input_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            input_text = file.read()
        return input_text.strip()  # Strip leading/trailing whitespace if needed
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return ""





def print_conversation_history(conversation_history):
    for message in conversation_history:
        role = message.get("role", "unknown")
        content = message.get("content", "")
        print(f"{role.capitalize()}: {content}\n")


# this is  first  {"role": "system", "content": system_prompt}
system_prompt= """
"""

# this is  first  {"role": "user", "content": formatted_user_prompt}
user_prompt = ""


# Optional  first {"role": "assistant", "content": assistant_message}
assistant_message=""


def chat_with_gpt(conversation):
    while True:
        try:
            # Make the GPT-4 API call with the current conversation history
            completion = client.chat.completions.create(
                model=deployment_model,
                messages=conversation,
                seed=12345,
                temperature=0, # zero for deterministic output
                logprobs=True,  # Request logprobs for each token in the output text
                max_tokens=3000
            )
            
            # Extract the assistant's response
            assistant_message = completion.choices[0].message.content.strip()
            
            # choice = completion.choices[0]
                        
            # Append the assistant's response to the conversation
            conversation.append({"role": "assistant", "content": assistant_message})
            
            print('\nSuccessful chat request...')
            
            # print(f"system_fingerprint={completion.system_fingerprint}")

            time.sleep(1)  # Optional delay before continuing
            return completion
            
        except Exception as e:
            print(f'Error occurred: {e}')
            print('Retrying chat request in 5 seconds...')
            time.sleep(5)  # Wait before retrying

# Initialize conversation with a system message to define the assistant's role
conversation_history = [
    {"role": "system", "content": system_prompt}
]


file_path = ''  
user_input = get_input_from_file(file_path)



        # Check if the input is non-empty
if user_input.strip():  # .strip() ensures that even strings with only spaces are not appended
    conversation_history.append({"role": "user", "content": user_input})
    print("\nUser_input:")
    print(user_input)
        
else:
    print("User_input is empty. Not added to conversation history.")




while True:
    print("\n")
    user_input = input("Type in user message (or exit to exit): ")


    # Option to exit the chat loop
    if user_input.lower() == "exit":
        print("Ending the chat.")
        break

    
        # Check if the input is non-empty
    if user_input.strip():  # .strip() ensures that even strings with only spaces are not appended
        conversation_history.append({"role": "user", "content": user_input})
        # print(f"User_input being added: {user_input}")
    else:
        print("User_input is empty. Not added to conversation history.")

    # pause()

    # Append the user's input to the conversation history
    # conversation_history.append({"role": "user", "content": user_input})
    
    # Get the assistant's response
    resp = chat_with_gpt(messages)
    response = resp.choices[0]

    assistant_message = response.message.content.strip()
    
    # Print the assistant's response
    print(f"{assistant_message}")
    

    # print(f"response.logprobs.content = {response.logprobs.content}")

    # Extract logprobs if available
    logprobs_data = response.logprobs.content if response.logprobs else None

    # Initialize total entropy
    total_entropy = 0
    logprob_sum =0

    log2_constant = math.log(2)  # Constant to convert nats to bits


    # Exclude newline, "Title", and "Abstract" from logprobs_data
    # excluded_tokens = ['\n', ':', 'Title', 'Abstract']
    excluded_tokens = ['```', 'python', ' ', '', '\n', 'latex', 'json', 'tag']

    
    # Exclude tokens that are in excluded_tokens or consist entirely of whitespace
    logprobs_data = [token_logprob_data for token_logprob_data in logprobs_data 
                    if token_logprob_data.token not in excluded_tokens 
                    and token_logprob_data.token.strip() != '']

    num_tokens = len(logprobs_data)
    
    
    if token_print_limit > num_tokens:
        token_print_limit = num_tokens

    
    # Get the first three  and last three tokens (or fewer if less than 10 tokens)
    first_tokens = logprobs_data[:token_print_limit]
    last_tokens = logprobs_data[-token_print_limit:] if len(logprobs_data) > token_print_limit else []
    
    
    # Calculate Shannon entropy in bits based on the logprobs of each token
    for token_logprob_data in logprobs_data:
        logprob = token_logprob_data.logprob  # Extract logprob of the token
        prob = math.exp(logprob)  # Convert logprob to probability
        entropy_in_nats = -prob * logprob  # Shannon entropy in nats
        entropy_in_bits = entropy_in_nats / log2_constant  # Convert nats to bits
        total_entropy += entropy_in_bits  # Accumulate total entropy in bits
        logprob_sum += logprob
        

        # Now print probabilities for the first 5 tokens
    print(f"\nProbabilities of the first {token_print_limit} tokens:")
    for token_logprob_data in first_tokens:
        logprob = token_logprob_data.logprob  # Extract logprob of the token
        prob = math.exp(logprob)  # Convert logprob to probability
        print(f"'{token_logprob_data.token}'  {prob:.6f}")

    # Only print last 5 tokens if they are not the same as the first 5
    if len(last_tokens) > 0:
        print(f"\nProbabilities of the last {token_print_limit} tokens:")
        for token_logprob_data in last_tokens:
            logprob = token_logprob_data.logprob  # Extract logprob of the token
            prob = math.exp(logprob)  # Convert logprob to probability
            print(f"'{token_logprob_data.token}' {prob:.6f}")


    total_prob = math.exp(logprob_sum)
    # Output the tokens
    tokens = [token.token for token in logprobs_data]  # Extract tokens (using attribute access)
    # print(f"Tokens: {tokens}")

    # Normalize entropy by the number of tokens to get average entropy per token
    average_entropy = total_entropy / num_tokens if num_tokens > 0 else 0

    # Output the total and normalized entropy in bits
    print(f"  Number of output tokens: {num_tokens}; Total Entropy: {total_entropy:.2f} bits; Normalized Entropy: {average_entropy:.3f} bits; Logprob_sum={logprob_sum:.6f}; image_file={image_path}; Total_prob={total_prob:.2e}; System_fingerprint= {resp.system_fingerprint}")
 
     
        

# Call the function to print the conversation history
print("\n\n Printing _conversation_history:")
print_conversation_history(conversation_history)