"""
Simple Gradio chat application that communicates with an LLM via OpenAI API.
Works with OpenAI API or local LLMs with OpenAI-compatible endpoints.
"""

import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI client
client = OpenAI(
    api_key = "",   # Not needed for local LLM via Docker Model Runner w/ Docker Compose
    base_url = os.getenv("CHAT_MODEL_URL")   # This was set in Docker Compose
)

# Model configuration
MODEL_NAME = os.getenv("CHAT_MODEL_NAME")   # This was set in Docker Compose
SYSTEM_PROMPT = "You are a helpful AI assistant."

# Create function to interact with LLM
def chat_with_llm(message, history):
    """
    Send a message to the LLM and return the response.

    Args:
        message: The user's message
        history: The chat history in Gradio messages format [{'role': 'user'/'assistant', 'content': '...'}, ...]

    Returns:
        The updated chat history with the LLM's response
    """
    # Build messages list with system prompt and history
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # Add history (already in OpenAI format)
    messages.extend(history)

    # Add the current message
    messages.append({"role": "user", "content": message})

    try:
        # Call the LLM
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
            stream=True
        )

        # Stream the response
        full_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                # Yield the updated history with the current message and partial response
                yield history + [
                    {"role": "user", "content": message},
                    {"role": "assistant", "content": full_response}
                ]

    except Exception as e:
        yield history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": f"Error: {str(e)}\n\nPlease check your API configuration."}
        ]


# Create Gradio interface
with gr.Blocks(title="LLM Chat") as demo:
    gr.Markdown("# 🤖 Chat with LLM")
    gr.Markdown(
        f"Connected to: `{os.getenv("CHAT_MODEL_URL")}` | "
        f"Model: `{MODEL_NAME}`"
    )

    chatbot = gr.Chatbot(
        height=500,
        show_label=False,
        type='messages'
    )

    with gr.Row():
        msg = gr.Textbox(
            placeholder="Type your message here...",
            show_label=False,
            scale=4,
            container=False
        )
        submit_btn = gr.Button("Send", scale=1, variant="primary")

    with gr.Row():
        clear_btn = gr.Button("Clear Chat")

    # Event handlers
    msg.submit(chat_with_llm, [msg, chatbot], [chatbot])
    msg.submit(lambda: "", None, [msg])

    submit_btn.click(chat_with_llm, [msg, chatbot], [chatbot])
    submit_btn.click(lambda: "", None, [msg])

    clear_btn.click(lambda: None, None, [chatbot])


if __name__ == "__main__":
    # Get host and port from environment variables
    host = "0.0.0.0"
    port = 8000

    demo.launch(
        server_name=host,
        server_port=port,
        share=False
    )
