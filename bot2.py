import openai
import re
import gradio as gr

openai.api_key = "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"

def generate_response(user_input):

    prompt = f"User: {user_input}\nAI: "
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1024)["choices"][0]["text"]
    response = re.sub(r'[\n\r]+', '', response)
    return response

def chatbot_interface(user_input):
    bot_response = generate_response(user_input)
    return bot_response

inputs = gr.inputs.Textbox(lines=7, label=" Stellen Sie Fragen bitte:")
outputs = gr.outputs.Textbox(label="Mein Antwort :")

# Create the Gradio interface
chatbot = gr.Interface(fn=chatbot_interface, inputs=inputs, outputs=outputs, title="Chat mit Shakibot")

# Run the Gradio interface
if __name__ == "__main__":
    chatbot.launch()
