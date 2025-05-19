import requests
import io
from PIL import Image
import os
import sys

def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Save the original image
        with open(save_path, 'wb') as f:
            f.write(response.content)
        
        print(f"Image downloaded and saved to {save_path}")
        return save_path
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

def resize_image(image_path, output_path, scale_factor=2):
    try:
        with Image.open(image_path) as img:
            # Get original dimensions
            original_width, original_height = img.size
            print(f"Original dimensions: {original_width}x{original_height}")
            
            # Calculate new dimensions
            new_width = int(original_width * scale_factor)
            new_height = int(original_height * scale_factor)
            
            # Resize image while preserving aspect ratio
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            
            # Save as PNG for lossless quality
            resized_img.save(output_path, format="PNG", quality=100)
            
            print(f"Resized image saved to {output_path}")
            print(f"New dimensions: {new_width}x{new_height}")
            return output_path
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None

def save_as_pdf(image_path, pdf_path):
    try:
        with Image.open(image_path) as img:
            # Convert to RGB if the image is in RGBA mode
            if img.mode == 'RGBA':
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[3])  # Use alpha channel as mask
                rgb_img.save(pdf_path, "PDF", resolution=300.0, quality=100)
            else:
                img.save(pdf_path, "PDF", resolution=300.0, quality=100)
                
        print(f"PDF saved to {pdf_path}")
        return pdf_path
    except Exception as e:
        print(f"Error saving PDF: {e}")
        return None

# Main execution
if __name__ == "__main__":
    # Define paths
    project_dir = os.path.dirname(os.path.abspath(__file__))
    original_image = os.path.join(project_dir, "original_logo.png")
    resized_image = os.path.join(project_dir, "resized_logo.png")
    pdf_output = os.path.join(project_dir, "logo_for_sign.pdf")
    
    # Process the image
    if len(sys.argv) > 1:
        image_url = sys.argv[1]
        scale_factor = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0
        
        # Download the image
        if download_image(image_url, original_image):
            # Resize the image
            if resize_image(original_image, resized_image, scale_factor):
                # Save as PDF
                save_as_pdf(resized_image, pdf_output)
    else:
        print("Usage: python process_logo.py <image_url> [scale_factor]")
