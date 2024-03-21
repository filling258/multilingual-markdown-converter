
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

Follow these steps to use this translation workflow:

1. Clone the repository
2. Install the necessary requirements with `pip install -r requirements.txt`
3. Set your OpenAI API key
4. Execute the Jupyter notebook
   - `input_path` should be the filepath to your document
   - Define the `input_language` and `output_language`
   - Run the cells of the notebook
5. The translated document will be displayed in the final cell

## Configuration

The configuration options to note:

- `input_path` - Path of the input file
- `input_language` - Source language code
- `output_language` - Destination language code
- `split_string` - String pattern to divide the input into parts

## Example Uses

This can be used to translate Markdown or Plain Text documents like:

- README files
- Documentation and Wikis
- Blog posts or articles
- Books

## Limitations

- Tested for Markdown and plain text formatting only
- Translation accuracy is dependent on OpenAI's translation model
- Only supports OpenAI's GPT models currently
- Cannot process multiple translations sequentially - only one file at a time
- Does not allow for simultaneous processing of multiple translation segments

## Acknowledgment

- [tiktoken](https://github.com/openai/tiktoken) for effective encoding and tokenization
- [OpenAI API](https://openai.com/api/) for reliable translation services

## License

MIT