import gradio as gr

def upload_file(files):
    file_paths = [file.name for file in files]
    for file in files:
        print(file)
    return file_paths

with gr.Blocks() as demo:
    file_output = gr.File()
    upload_button = gr.UploadButton("Click to Upload a File", file_count="multiple")
    upload_button.upload(upload_file, upload_button, file_output)

demo.launch()