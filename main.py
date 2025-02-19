import gradio as gr
import os

def main(save_pdf,pdf_file,chosen_model):
    return 'HALO'

with gr.Blocks() as demo:
    with gr.Row():
        title = gr.HTML("<h1>Document Translator</h1>")
    with gr.Row():
        with gr.Column():
            pdf_file = gr.UploadButton(file_types=[".pdf"])
            save_pdf = gr.Textbox(label="Result Pdf File Name")
            chosen_model = gr.Dropdown(choices=["RCNN X101","RCNN R50", "Fast RCNN R50", "P RCNN R50"], label="ocr_model", info="Choose OCR Model")
        with gr.Column():
            translate_btn = gr.Button(value="Translate Document")
            translate_btn.click(fn=main, inputs = [save_pdf,pdf_file,chosen_model], outputs=gr.File(label="Download Annotated PDF", file_types=[".pdf"]))

if __name__ == "__main__":      
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_port=port, server_name="0.0.0.0")