from PIL import Image
import os
import sys

def resize_image(input_path, output_path, scale_factor=4):
    try:
        with Image.open(input_path) as img:
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
        
def save_as_jpg(image_path, jpg_path):
    try:
        with Image.open(image_path) as img:
            # Convert to RGB if the image is in RGBA mode
            if img.mode == 'RGBA':
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[3])  # Use alpha channel as mask
                rgb_img.save(jpg_path, "JPEG", quality=95)
            else:
                img.save(jpg_path, "JPEG", quality=95)
                
        print(f"JPG saved to {jpg_path}")
        return jpg_path
    except Exception as e:
        print(f"Error saving JPG: {e}")
        return None

# Main execution
if __name__ == "__main__":
    # Define paths
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get input file path from command line or use default
    if len(sys.argv) > 1:
        input_image = sys.argv[1]
    else:
        input_image = os.path.join(project_dir, "input_logo.png")
    
    # Get scale factor from command line or use default
    if len(sys.argv) > 2:
        try:
            scale_factor = float(sys.argv[2])
        except ValueError:
            print("Scale factor must be a number. Using default value of 4.")
            scale_factor = 4
    else:
        scale_factor = 4
    
    # Define output paths
    resized_image = os.path.join(project_dir, "sanem_giyim_logo.png")
    pdf_output = os.path.join(project_dir, "sanem_giyim_logo.pdf")
    jpg_output = os.path.join(project_dir, "sanem_giyim_logo.jpg")
    
    # Check if input file exists
    if os.path.exists(input_image):
        # Resize the image
        if resize_image(input_image, resized_image, scale_factor):
            # Save as PDF, PNG is already saved from resize_image function
            save_as_pdf(resized_image, pdf_output)
            # Save as JPG
            save_as_jpg(resized_image, jpg_output)
    else:
        print(f"Input file {input_image} not found.")
