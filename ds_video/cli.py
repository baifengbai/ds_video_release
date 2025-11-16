import argparse
from .converter import convert_markdown_to_video

def main():
    parser = argparse.ArgumentParser(description="Convert markdown to video using ds-markdown and ffmpeg")
    
    # Positional arguments
    parser.add_argument("input", help="Input markdown file path")
    parser.add_argument("output", help="Output video file path")
    
    # Optional arguments
    parser.add_argument("--background-color", default="white", help="Background color of the video (default: white)")
    parser.add_argument("--duration", type=int, default=5, help="Duration of the video in seconds (default: 5)")
    parser.add_argument("--width", type=int, default=1920, help="Width of the video (default: 1920)")
    parser.add_argument("--height", type=int, default=1080, help="Height of the video (default: 1080)")
    
    args = parser.parse_args()
    
    try:
        convert_markdown_to_video(
            input_data=args.input,
            output_path=args.output,
            is_file=True,
            background_color=args.background_color,
            duration=args.duration,
            width=args.width,
            height=args.height
        )
        print(f"Video conversion completed successfully: {args.output}")
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()