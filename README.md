# ds-video

A Python library to convert markdown content to video using ds-markdown and ffmpeg.

## Features

- Convert markdown content to video with white background
- Support for rich markdown features (tables, code blocks, math formulas, etc.)
- Customizable video settings
- Command-line interface for easy use

## Demo 

<video controls width="600">
  <source src="output_with_typing_final.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Installation

### Prerequisites

- Python 3.7 or higher
- ffmpeg (must be installed and available in PATH)

### Install the library

```bash
pip install .
```

### Setup Playwright

```bash
playwright install
```

## Usage

### Command-line Interface

```bash
ds-video input.md output.mp4
```

### Python API

```python
from ds_video import convert_markdown_to_video

# Convert markdown file to video
convert_markdown_to_video("input.md", "output.mp4")

# Convert markdown string to video
markdown_content = "# Hello World\n\nThis is a test."
convert_markdown_to_video(markdown_content, "output.mp4", is_file=False)
```

### Custom Options

```bash
ds-video input.md output.mp4 --background-color white --duration 10
```

## Configuration Options

- `--background-color`: Background color of the video (default: white)
- `--duration`: Duration of each slide in seconds (default: 5)
- `--width`: Width of the video (default: 1920)
- `--height`: Height of the video (default: 1080)

## Examples

### Basic Conversion

```bash
ds-video README.md output.mp4
```

### Custom Background Color

```bash
ds-video input.md output.mp4 --background-color #f0f0f0
```

## License

MIT
