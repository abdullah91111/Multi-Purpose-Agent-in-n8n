from fastapi import FastAPI, HTTPException, UploadFile, File
from io import BytesIO
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import DocumentStream
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from docling.document_converter import PdfFormatOption

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Docling API is up and running!"}

@app.post("/process/")
async def process_data(file: UploadFile = File(...)):
    try:
        # Read the uploaded file into memory as binary stream
        pdf_file = await file.read()
        buf = BytesIO(pdf_file)
        
        # Convert the uploaded PDF using Docling
        source = DocumentStream(name=file.filename, stream=buf)
        
        # Configure the document converter options (custom options can be added)
        pipeline_options = PdfPipelineOptions(do_table_structure=True)
        doc_converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
            }
        )

        # Convert the document
        result = doc_converter.convert(source)
        
        # Export the converted document to markdown (you can change the format as needed)
        markdown_output = result.document.export_to_markdown()
        
        return {"converted_document": markdown_output}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing data: {str(e)}")
