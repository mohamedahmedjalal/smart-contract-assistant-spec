import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000"


def upload_file(file):
    files = {
        "file": open(file.name, "rb")
    }

    response = requests.post(f"{API_URL}/upload", files=files)

    return response.json()["summary"]




def ask_question(message, history):
    # Handle message being a dict or string
    query = message["text"] if isinstance(message, dict) else message
    
    
    response = requests.post(f"{API_URL}/chat", json={"question": query})
    data = response.json()
    
    
    answer = data.get("answer", "No answer found.")
    if isinstance(answer, dict) and "content" in answer:
        answer = answer["content"]
        
    
    history.append({"role": "user", "content": query})
    history.append({"role": "assistant", "content": answer})
    
    
    return history, history
    
    
    if isinstance(answer, dict) and "content" in answer:
        return answer["content"]
    return answer


with gr.Blocks() as demo:
    gr.Markdown("# Smart Contract Summary & Q&A Assistant")

    with gr.Tab("Upload"):
        file_input = gr.File(
            label="Upload PDF or DOCX"
        )

        summary_output = gr.Textbox(
            label="Contract Summary",
            lines=15,
        )

        upload_btn = gr.Button("Process Contract")

        upload_btn.click(
            upload_file,
            inputs=file_input,
            outputs=summary_output,
        )

    with gr.Tab("Chat"):
        chatbot = gr.Chatbot()

        msg = gr.Textbox(
            placeholder="Ask a question about the contract..."
        )

        state = gr.State([])

        msg.submit(
            ask_question,
            inputs=[msg, state],
            outputs=[chatbot, state],
        )

demo.launch()
