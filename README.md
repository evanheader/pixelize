# Pixelize

A tiny Python tool that pixelates images using OpenCV. Select an image via a file dialog, choose the pixelation block size and whether to convert to greyscale, and save the pixelated result.

## Demo

Before (left): `images/cat3.jpg` — After (right): `pixelized_output.png`

![Before](images/cat3.jpg) ![After](pixelized_output.png)

## Features

- Select any image via a file dialog
- Adjustable pixelation (block size)
- Optional greyscale output
- Saves the output as `pixelized_output.png` and displays it

## Files

- `pixelize.py` — main script that runs the GUI file picker and does the pixelation
- `images/` — example images included with the project
- `pixelized_output.png` — an example output image created by the script

## Usage

Requirements: Python 3.8+, OpenCV and NumPy. Install dependencies (recommended inside a virtualenv):

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python pixelize.py
```

Follow the file dialog to pick an image. When prompted:

- Enter a pixelation amount (integer block size), e.g. `8` or `16`.
- Enter `y` to produce a greyscale pixelated image, or `n` for color.

The script will write `pixelized_output.png` in the current directory and open a preview window.

## Notes and suggestions

- The script uses a simple average color per block. This keeps the implementation small and fast.
- For large images or very small block sizes, processing may take longer and use more memory.
- If you want to process a directory of images, consider modifying the script to loop over files and provide output file naming.

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.
