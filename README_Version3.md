# GenAI Code Generator

A simple AI code generator for internship project submission.

## Features

- Generates code in your chosen programming language (Python by default).
- Uses OpenAI GPT to create functions from natural language prompts.
- Simple terminal interface.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Add your OpenAI API key to `.env` (see `.env` example).

3. Run:
   ```
   python app.py
   ```

## Example Usage

```
Enter the programming language (default: Python): JavaScript
Describe what you want the code to do (or type 'exit' to quit): Sort an array in ascending order.
```

The app will generate a JavaScript function for sorting an array.

## How it works

- The app takes a user prompt and desired language.
- It asks GPT for a code snippet matching the description.

## Security

- **Never share your `.env` file or API key publicly.**
- The `.env` file is ignored by Git (`.gitignore`).