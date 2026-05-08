import subprocess
import threading


def run_fastapi():
    subprocess.run([
        "uvicorn",
        "app.main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
        "--reload"
    ])


def run_gradio():
    subprocess.run([
        "python",
        "ui/gradio_app.py"
    ])


thread1 = threading.Thread(target=run_fastapi)
thread2 = threading.Thread(target=run_gradio)

thread1.start()
thread2.start()
