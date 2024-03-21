
# Multilingual Markdown Converter

This tool allows you to translate Markdown documents from one language to another using OpenAI's API, while retaining the original formatting of the document. The process includes tokenizing the input document, splitting it into chunks, translating each piece, and then reconstructing the translated output to resemble the original formatting.

![project-image](https://github.com/filling258/multilingual-markdown-converter/assets/35015261/fd801bc1-b802-4b5e-a772-586bd2c57699)

## Features

- Supports Plain Text/Markdown file as the input
- Utilizes tiktoken for tokenizing the input text
- Breaks the input into chunks at multiple newlines
- Routes each segment through OpenAI for translation
- Assembles the translated output while keeping original formatting

## Usage
