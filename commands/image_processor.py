import click
import datetime
import os
from rich.console import Console
from pathlib import Path
import cv2
import numpy as np

console = Console()

def process_image(current_image_name, new_image_name):
    # setting up image paths
    image_path = Path(__file__).resolve().parent.parent / "resources" / "images"
    input_path = image_path / current_image_name
    output_path = image_path / new_image_name
    
    # validate if input file exists
    if not input_path.exists():
        console.print(f"[bold red]Error:[/bold red] Input file '{current_image_name}' not found in '{image_path}'.")
        return
    
    # load the image
    image = cv2.imread(str(input_path))
    if image is None:
        console.print(f"[bold red]Error:[/bold red] Unable to load image: {input_path}")
        return

    console.print("[bold green]Processing image...[/bold green]")

    # Convert image to greyscale
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    console.print("- Converted to greyscale")

    # Apply CLAHE for contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(grey_image)
    console.print("- Applied adaptive histogram equalization (CLAHE)")

    # Apply bilateral filter for noise reduction while preserving edges
    filtered_image = cv2.bilateralFilter(enhanced_image, d=9, sigmaColor=75, sigmaSpace=75)
    console.print("- Applied bilateral filtering for noise reduction")

    # Apply unsharp mask for sharpening
    gaussian_blur = cv2.GaussianBlur(filtered_image, (9, 9), 10.0)
    sharpened_image = cv2.addWeighted(filtered_image, 1.5, gaussian_blur, -0.5, 0)
    console.print("- Applied unsharp mask for sharpening")

    # Apply adaptive thresholding for better text visibility
    threshold_image = cv2.adaptiveThreshold(
        sharpened_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, blockSize=11, C=2
    )
    console.print("- Applied adaptive thresholding")

    # Save the processed image
    output_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure output directory exists
    cv2.imwrite(str(output_path), threshold_image)
    console.print(f"[bold green]Processed image saved to:[/bold green] {output_path}")
    
    
@click.command(help="A script for enhancing the visibility of text in images.\n\n"
                     "This script processes an image to make text clearer by:\n"
                     "- Converting it to grayscale\n"
                     "- Enhancing contrast\n"
                     "- Reducing noise\n"
                     "- Sharpening the image\n"
                     "- Applying adaptive thresholding\n\n"
                     "NOTE: Ensure that a folder named 'resources/images/' exists in the parent directory, "
                     "and the input image is placed inside it.")
@click.option("-cn", "--current-image-name", required=True, help="The name of the input image (must be inside 'resources/images').")
@click.option("-nn", "--new-image-name", required=True, help="The name of the output image (will be saved to 'resources/images').")
def image_processor(current_image_name, new_image_name):
    # pass click options to function
    process_image(current_image_name, new_image_name)

if __name__ == "__main__":
    image_processor()