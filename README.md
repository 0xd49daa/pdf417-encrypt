# PDF417 Encryption Tool

This tool is designed to securely store sensitive data on paper. The data is encrypted to ensure its safety, and the PDF417 barcode format is used for its error correction capabilities, allowing for reliable reading even if the paper is damaged.

## Prerequisites

Make sure you have the following Python packages installed:

- `pycryptodome`
- `pdf417gen`
- `pillow`
- `pdf417decoder`

You can install them using pip:

```bash
pip install pycryptodome pdf417gen pillow pdf417decoder
```

## Usage

The tool provides two main functionalities: encrypt and decrypt.

### Encrypting a File

To encrypt a file and generate a PDF417 barcode:

`python main.py encrypt|decrypt <input_file> <output_file>`