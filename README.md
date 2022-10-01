# Tokopedia-Product-Reviews-Finder
A Python script to find reviews on a Tokopedia product

- [Tokopedia-Product-Reviews-Finder](#tokopedia-product-reviews-finder)
  - [Requirements](#requirements)
  - [Usage](#usage)
    - [Basic Usage](#basic-usage)
    - [Save to file](#save-to-file)

## Requirements
`Python` and `requests` package

## Usage
### Basic Usage

`python main.py Tokopedia_URL text_to_find`

Example:

`python main.py https://www.tokopedia.com/skintific/skintific-5x-ceramide-barrier-repair-moisture-gel-30g-30g cocok`

You can use regex for the `text_to_find` argument. To find two or more words, wrap the text with double quotes `"cocok untuk kulit"`. Regex usage example: `"cocok|sensitif"` to find the word cocok or sensitif.

### Save to file
If you want to save the output to a file, use:

`python main.py Tokopedia_URL text_to_find --save-to filename`

Example:

`python main.py https://www.tokopedia.com/skintific/skintific-5x-ceramide-barrier-repair-moisture-gel-30g-30g cocok --save-to output.txt`
