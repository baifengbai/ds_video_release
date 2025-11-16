import os
import tempfile
import asyncio
from playwright.async_api import async_playwright
from jinja2 import Template
import subprocess
import shutil


def convert_markdown_to_html(markdown_content, background_color="white"):
    """
    Convert markdown content to HTML using ds-markdown
    """
    # Read the HTML template
    template_path = os.path.join(os.path.dirname(__file__), "template.html")
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
    
    # Render the template with markdown content
    template = Template(template_content)
    html_content = template.render(
        markdown_content=markdown_content,
        background_color=background_color
    )
    
    return html_content


async def html_to_video(html_content, output_path, duration=5, width=1920, height=1080):
    """
    Convert HTML content to video using Playwright's video recording with typing animation
    """
    import os
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    
    async with async_playwright() as p:
        # Launch browser with video recording enabled
        browser = await p.chromium.launch(headless=True)
        
        # Create context with video recording configuration
        context = await browser.new_context(
            viewport={"width": width, "height": height},
            device_scale_factor=1,
            record_video_dir=os.path.dirname(output_path) or ".",
            record_video_size={"width": width, "height": height}
        )
        
        # Create new page
        page = await context.new_page()
        
        # Capture console logs for debugging
        page.on("console", lambda msg: print(f"BROWSER CONSOLE: {msg.type} {msg.text}"))
        page.on("console", lambda msg: [print(f"BROWSER CONSOLE ARG: {arg}") for arg in msg.args])
        
        # Set HTML content containing the typing animation
        await page.set_content(html_content)
        
        # Wait for the specified duration to allow typing animation to complete
        await page.wait_for_timeout(int(duration * 1000))
        
        # Get the recorded video
        video = page.video
        if not video:
            raise RuntimeError("Video recording was not started")
        
        # Save the recorded video
        recorded_video_path = await video.path()
        
        # Close context and browser
        await context.close()
        await browser.close()
        
        # Move the recorded video to the output path
        os.replace(recorded_video_path, output_path)


async def _convert_markdown_to_video_async(
    input_data,
    output_path,
    is_file=True,
    background_color="white",
    duration=5,
    width=1920,
    height=1080
):
    """
    Async implementation of markdown to video conversion with typing animation
    """
    # Read markdown content
    if is_file:
        with open(input_data, "r", encoding="utf-8") as f:
            markdown_content = f.read()
    else:
        markdown_content = input_data
    
    # Calculate the minimum required duration based on content length
    # Typing speed: 30ms per character, plus initial delay and buffer
    typing_speed_ms = 30
    initial_delay_ms = 500  # 0.5 seconds before typing starts
    buffer_time_ms = 1000   # 1 second buffer after typing ends
    content_length = len(markdown_content)
    calculated_duration_ms = content_length * typing_speed_ms + initial_delay_ms + buffer_time_ms
    calculated_duration_s = calculated_duration_ms / 1000
    
    # Use the longer duration between calculated and user-provided
    final_duration = max(duration, calculated_duration_s)
    
    # Convert markdown to HTML with typing animation
    html_content = convert_markdown_to_html(markdown_content, background_color)
    
    # Debug: Save HTML content to file for inspection
    with open("test_output.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # Convert HTML to video with proper duration for typing animation
    await html_to_video(html_content, output_path, duration=final_duration, width=width, height=height)


def convert_markdown_to_video(
    input_data,
    output_path,
    is_file=True,
    background_color="white",
    duration=5,
    width=1920,
    height=1080
):
    """
    Convert markdown to video
    
    Args:
        input_data: Path to markdown file or markdown content string
        output_path: Path to output video file
        is_file: Whether input_data is a file path (default: True)
        background_color: Background color of the video (default: white)
        duration: Duration of the video in seconds (default: 5)
        width: Width of the video (default: 1920)
        height: Height of the video (default: 1080)
    """
    # Run async function
    asyncio.run(_convert_markdown_to_video_async(
        input_data=input_data,
        output_path=output_path,
        is_file=is_file,
        background_color=background_color,
        duration=duration,
        width=width,
        height=height
    ))