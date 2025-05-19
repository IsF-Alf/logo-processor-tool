# Logo Processing Tool

A professional tool for resizing logos and images for signage, printing, and digital use while maintaining quality. This tool allows you to enlarge small logos to high-resolution formats suitable for large-scale printing and digital applications.

## Key Features

- **High-Quality Enlargement**: Resize small logos to much larger dimensions without pixelation or quality loss
- **Aspect Ratio Preservation**: Maintains the original proportions of your images perfectly
- **Multi-Format Export**: Automatically saves in three essential formats (PDF, PNG, JPG) with a single click
- **Professional Output**: Uses high-quality algorithms (Lanczos resampling) for the best possible results
- **Transparent Background Support**: Properly handles transparent PNG images when converting to other formats
- **User-Friendly Interface**: Simple, intuitive GUI requires no technical knowledge
- **Preview Functionality**: See the results before processing
- **Customizable Scale Factor**: Choose exactly how much to enlarge your image (1x-10x)
- **Batch Processing Ready**: Process multiple images with the command-line version

## Why Use This Tool?

### Common Problems This Tool Solves:

- **Low-Resolution Logos**: Often clients provide small logos that need to be enlarged for signs, banners, or high-quality prints
- **Format Compatibility**: Different applications require different formats (PDF for printing, PNG for web with transparency, JPG for general use)
- **Quality Loss When Resizing**: Standard resizing often results in pixelation and blurry edges
- **Time-Consuming Manual Process**: Converting between multiple formats manually takes time

### Perfect For:

- Sign makers and print shops
- Graphic designers
- Marketing professionals
- Anyone needing to prepare logos for large-format printing

## Usage Instructions

### Command Line Usage

```bash
python process_logo_simple.py [input_image_path] [scale_factor]
```

- `input_image_path`: Path to the image file to be processed (if not specified, "input_logo.png" is used)
- `scale_factor`: Enlargement factor (if not specified, 4 is used)

Example:
```bash
python process_logo_simple.py company_logo.png 5
```
This will resize the logo to 5x its original size and save it in all three formats.

### GUI Usage

Run the `logo_gui.py` file for the graphical interface:

```bash
python logo_gui.py
```

#### Step-by-Step GUI Instructions:

1. Click "Browse" to select your logo file
2. Adjust the scale factor slider (1x-10x) to set how much you want to enlarge the image
3. (Optional) Set the output folder and filename
4. Click "Preview" to see how the resized image will look
5. Click "Process" to generate all three formats (PDF, PNG, JPG)
6. Your processed files will be saved in the selected output folder

### Executable Version

For users without Python installed, we provide a standalone Windows executable:

1. Download the `LogoProcessorTool.exe` from the [Releases page](https://github.com/aagedik/logo-processor-tool/releases)
2. Run the executable - no installation required
3. Follow the same steps as the GUI version above

## Technical Details

### How It Works

This tool uses advanced image processing techniques to ensure the highest quality output:

- **Lanczos Resampling Algorithm**: A high-quality interpolation method that preserves sharp edges and details
- **Transparent Background Handling**: Properly preserves transparency in PNG files and correctly converts to white backgrounds for PDF/JPG
- **High DPI Output**: PDF files are generated at 300 DPI, suitable for professional printing
- **Lossless PNG Processing**: PNG files are saved with maximum quality settings
- **Optimized JPG Compression**: JPG files use 95% quality setting for an optimal balance of quality and file size

## Requirements

- Python 3.6+
- Pillow (PIL Fork)
- Tkinter (for GUI)

## Installation

```bash
pip install pillow
```

## Examples

### Before and After

Here are some examples of what this tool can do:

| Original (Small Logo) | Processed Result |
|:---------------------:|:----------------:|
| Small logo (e.g., 300x200 px) | Enlarged to 1200x800 px with preserved quality |
| Logo with transparency | Transparency preserved in PNG, white background in PDF/JPG |
| Low-resolution logo | High-resolution output suitable for printing |

### Sample Workflow

1. Client provides a small logo (e.g., 400x300 pixels)
2. You need it for a large sign (needs to be 1600x1200 pixels)
3. Use Logo Processing Tool to resize it to 4x its original size
4. Get high-quality outputs in all three formats
5. Use the PDF for printing, PNG for digital use with transparency, JPG for web

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Ideas for contributions:
- Add more output formats (SVG, TIFF, etc.)
- Implement batch processing in the GUI
- Add more image processing options (cropping, color adjustments, etc.)
- Create versions for other platforms (Mac, Linux)

## License

MIT

## Contributors

- agedik
- [aagedik](https://github.com/aagedik)

## Contact

[aagedik@gmail.com]
