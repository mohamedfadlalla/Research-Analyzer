import gradio as gr
import subprocess
import shutil
import os
from scidownl import scihub_download
from google.colab import files

def process_pdf(input_path):
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_dir = f"/content/output/{base_name}"
    
    # Clean and create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Run the marker_single command
    subprocess.run([
        "marker_single", input_path, output_dir,
        "--batch_multiplier", "2",
        "--max_pages", "20",
        "--langs", "English"
    ], capture_output=True, text=True)
    
    # Create zip file of the extracted content
    zip_path = f"{output_dir}.zip"
    shutil.make_archive(output_dir, 'zip', output_dir)
    
    return zip_path

def download_paper(doi):
    output_path = "/content/paper.pdf"
    scihub_download(doi, paper_type="doi", out=output_path)
    return output_path

def gradio_app(file, doi):
    if doi:
        input_path = download_paper(doi)
    elif file:
        input_path = file.name
        shutil.move(input_path, "/content/paper.pdf")
        input_path = "/content/paper.pdf"
    else:
        return "Please provide a PDF file or a DOI."

    zip_path = process_pdf(input_path)
    return zip_path

iface = gr.Interface(
    fn=gradio_app,
    inputs=[
        gr.File(label="Upload PDF"),
        gr.Textbox(label="Enter DOI", placeholder="10.1234/example.doi")
    ],
    outputs=gr.File(label="Download Extracted Content"),
    title="PDF Extractor",
    description="Upload a PDF or enter a DOI and download the extracted content in a zip file."
)

iface.launch(share=True)
