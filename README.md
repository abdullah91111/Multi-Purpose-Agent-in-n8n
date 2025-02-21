# Multi Purpose Agent - n8n Application

## Overview

This repository contains an n8n application with four workflows designed to process URLs and PDF documents using AI. The main workflow, **Multi Purpose Agent**, orchestrates three sub-workflows that provide specific functionalities:

- **LinkedIn Tool for Multi Purpose Agent** – Generates LinkedIn posts from provided URLs or PDFs.
- **Summary Tool for Multi Purpose Agent** – Creates summaries for given URLs or PDFs.
- **Question and Answer Tool for Multi Purpose Agent** – Answers questions based on content from URLs or PDFs.

This application is designed to run on a self-hosted n8n instance with Docling for document processing.

---

## Setup Instructions

### 1. Start n8n and Docling API

Both the **n8n** and **Docling API** containers need to be running and must be on the same Docker network for proper communication.

- To create a Docker network:
  ```sh
  docker network create n8n-network
  ```
- Run the **Docling API** container and connect it to the network:
  ```sh
  docker run -d --name docling-api --network n8n-network docling-api-image
  ```
- Run the **n8n** container and connect it to the network:
  ```sh
  docker run -d --name n8n --network n8n-network -p 5678:5678 n8nio/n8n
  ```

### 2. Content Processing Setup

#### If Not Using `self-hosted-ai-starter-kit`:

- Add the following to your `.env` file:
  ```sh
  NODE_FUNCTION_ALLOW_EXTERNAL=axios,url,path,file-type,jsdom,@mozilla/readability
  ```

- Add the following dependencies to your `Dockerfile`:
  ```sh
  RUN npm install -g axios url file-type neo4j-driver @mozilla/readability \
      jsdom marked pdf.js-extract pdf-parse-fork tiktoken firebase-admin \
      canvas json5 katex marked-katex-extension pdfjs-dist ioredis amqplib \
      pdf-img-convert flexsearch puppeteer turndown sanitize-html \
      commonmark path
  ```

- Ensure that both the **Docling API** and **n8n** containers are running and are on the same network (`n8n-network`).

- Add the Docling URL to the **Convert File HTTP Node** in all three sub-workflows.

- Configure the n8n **HTTP Node** to send requests to:
  ```
  http://docling-api:5000/process/
  ```
  Ensure `"docling-api"` matches the actual container name of your Docling API instance.

### 3. Import Workflows

Import the provided JSON file into n8n. The repository contains **four workflows**, including the main **Multi Purpose Agent** and three sub-workflows.

### 4. Configure Credentials

The application requires **Google Drive credentials** in n8n for processing Google Drive links.

- Configure the Google Drive credential **once** in n8n.
- Apply this credential to the **Google Drive nodes** in all three sub-workflows by selecting the configured credential.

---

## Usage

The **Multi Purpose Agent** listens for user prompts and processes URLs or PDF links accordingly. The supported prompts include:

- **LinkedIn Post Creation:**
  ```
  Create a LinkedIn post for "<URL or PDF Link>"
  ```
- **Summary Generation:**
  ```
  Create a summary for "<URL or PDF Link>"
  ```
- **Q&A Processing:**
  ```
  What is Machine Learning? "<URL or PDF Link>"
  ```

Once a request is received, the main workflow routes it to the appropriate sub-workflow.

