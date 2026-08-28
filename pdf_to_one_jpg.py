from pdf2image import convert_from_path
from PIL import Image

def pdf_to_single_jpg(pdf_path, output_jpg_path):
    # 1. Convert all PDF pages into a list of PIL Images
    print("Converting PDF pages...")
    pages = convert_from_path(pdf_path, dpi=150) # Adjust DPI for higher/lower quality
    
    # 2. Calculate the total width and height for the final single image
    # We take the maximum width found among pages, and sum up all heights
    total_width = max(page.width for page in pages)
    total_height = sum(page.height for page in pages)
    
    # 3. Create a blank canvas matching the total dimensions
    merged_image = Image.new('RGB', (total_width, total_height), color=(255, 255, 255))
    
    # 4. Paste each page image sequentially from top to bottom
    current_y = 0
    for page in pages:
        merged_image.paste(page, (0, current_y))
        current_y += page.height
    
    # 5. Save the final combined image
    print("Saving single combined JPG...")
    merged_image.save(output_jpg_path, 'JPEG')
    print(f"Success! Saved to {output_jpg_path}")

# Example usage:
# pdf_to_single_jpg('C:\Users\intel\online-retail-powerbi-analytics\Visual Previews', 'final_long_image.jpg')

# ... (Keep all your existing code at the top the same) ...

if __name__ == "__main__":
    # Paste your copied path here (keep the 'r' in front)
    input_pdf = r"C:\Users\intel\online-retail-powerbi-analytics\Visual Previews\Tata_Data_Visualisation_Task.pdf" 
    
    # Save the output image in that same exact folder
    output_image = r"C:\Users\intel\online-retail-powerbi-analytics\Visual Previews\Tata_Data_Visualisation_Task.jpg"
    
    pdf_to_single_jpg(input_pdf, output_image)

