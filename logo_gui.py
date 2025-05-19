import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import threading

def resize_image(input_path, output_path, scale_factor=4):
    try:
        with Image.open(input_path) as img:
            # Get original dimensions
            original_width, original_height = img.size
            
            # Calculate new dimensions
            new_width = int(original_width * scale_factor)
            new_height = int(original_height * scale_factor)
            
            # Resize image while preserving aspect ratio
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            
            # Save as PNG for lossless quality
            resized_img.save(output_path, format="PNG", quality=100)
            
            return output_path, original_width, original_height, new_width, new_height
    except Exception as e:
        raise Exception(f"Resizing error: {e}")

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
                
        return pdf_path
    except Exception as e:
        raise Exception(f"PDF saving error: {e}")

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
                
        return jpg_path
    except Exception as e:
        raise Exception(f"JPG saving error: {e}")

class LogoProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Logo Processing Tool - agedik")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Variables
        self.input_path = tk.StringVar()
        self.output_dir = tk.StringVar()
        self.output_name = tk.StringVar(value="processed_logo")
        self.scale_factor = tk.DoubleVar(value=4.0)
        self.preview_img = None
        self.original_img = None
        
        # Set default output directory to the current directory
        self.output_dir.set(os.path.dirname(os.path.abspath(__file__)))
        
        # Create UI
        self.create_ui()
        
    def create_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Logo Processing Tool", font=("Arial", 18, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Input file section
        input_frame = ttk.LabelFrame(main_frame, text="Input File", padding=10)
        input_frame.pack(fill=tk.X, pady=5)
        
        input_entry = ttk.Entry(input_frame, textvariable=self.input_path, width=60)
        input_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        browse_btn = ttk.Button(input_frame, text="Browse", command=self.browse_input)
        browse_btn.pack(side=tk.RIGHT, padx=5)
        
        # Output settings section
        output_frame = ttk.LabelFrame(main_frame, text="Output Settings", padding=10)
        output_frame.pack(fill=tk.X, pady=5)
        
        # Output directory
        dir_frame = ttk.Frame(output_frame)
        dir_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(dir_frame, text="Output Folder:").pack(side=tk.LEFT, padx=5)
        dir_entry = ttk.Entry(dir_frame, textvariable=self.output_dir, width=45)
        dir_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        browse_dir_btn = ttk.Button(dir_frame, text="Browse Folder", command=self.browse_output_dir)
        browse_dir_btn.pack(side=tk.RIGHT, padx=5)
        
        # Output filename
        name_frame = ttk.Frame(output_frame)
        name_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(name_frame, text="Output Filename:").pack(side=tk.LEFT, padx=5)
        name_entry = ttk.Entry(name_frame, textvariable=self.output_name)
        name_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Scale factor
        scale_frame = ttk.Frame(output_frame)
        scale_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(scale_frame, text="Scale Factor:").pack(side=tk.LEFT, padx=5)
        scale_slider = ttk.Scale(scale_frame, from_=1.0, to=10.0, variable=self.scale_factor, orient=tk.HORIZONTAL)
        scale_slider.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        scale_value = ttk.Label(scale_frame, textvariable=tk.StringVar(value="4.0"))
        scale_value.pack(side=tk.LEFT, padx=5)
        
        def update_scale_label(*args):
            scale_value.config(text=f"{self.scale_factor.get():.1f}")
        
        self.scale_factor.trace_add("write", update_scale_label)
        
        # Preview section
        preview_frame = ttk.LabelFrame(main_frame, text="Preview", padding=10)
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.preview_canvas = tk.Canvas(preview_frame, bg="white")
        self.preview_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Info section
        self.info_var = tk.StringVar(value="Please select a logo file")
        info_label = ttk.Label(main_frame, textvariable=self.info_var, font=("Arial", 10))
        info_label.pack(pady=5)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, length=100, mode='indeterminate')
        
        # Buttons section
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        process_btn = ttk.Button(btn_frame, text="Process", command=self.process_logo)
        process_btn.pack(side=tk.RIGHT, padx=5)
        
        preview_btn = ttk.Button(btn_frame, text="Preview", command=self.preview_resize)
        preview_btn.pack(side=tk.RIGHT, padx=5)
        
        # Credits
        credits_label = ttk.Label(main_frame, text="© 2025 agedik | aagedik@gmail.com", font=("Arial", 8))
        credits_label.pack(side=tk.BOTTOM, pady=(10, 0))
        
    def browse_input(self):
        filetypes = [
            ("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp"),
            ("PNG Files", "*.png"),
            ("JPEG Files", "*.jpg;*.jpeg"),
            ("All Files", "*.*")
        ]
        filename = filedialog.askopenfilename(title="Select Logo File", filetypes=filetypes)
        if filename:
            self.input_path.set(filename)
            self.load_preview(filename)
            
            # Set default output name based on input filename
            base_name = os.path.splitext(os.path.basename(filename))[0]
            self.output_name.set(base_name)
    
    def browse_output_dir(self):
        directory = filedialog.askdirectory(title="Select Output Folder")
        if directory:
            self.output_dir.set(directory)
    
    def load_preview(self, path):
        try:
            # Load and display preview
            self.original_img = Image.open(path)
            self.update_preview(self.original_img)
            
            # Update info
            width, height = self.original_img.size
            self.info_var.set(f"Original Size: {width}x{height} pixels")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading image: {e}")
    
    def update_preview(self, img):
        # Resize for preview (maintain aspect ratio)
        canvas_width = self.preview_canvas.winfo_width() or 400
        canvas_height = self.preview_canvas.winfo_height() or 300
        
        img_width, img_height = img.size
        ratio = min(canvas_width/img_width, canvas_height/img_height)
        new_width = int(img_width * ratio)
        new_height = int(img_height * ratio)
        
        preview_img = img.resize((new_width, new_height), Image.LANCZOS)
        self.preview_img = ImageTk.PhotoImage(preview_img)
        
        # Center the image
        x = (canvas_width - new_width) // 2
        y = (canvas_height - new_height) // 2
        
        self.preview_canvas.delete("all")
        self.preview_canvas.create_image(x, y, anchor=tk.NW, image=self.preview_img)
    
    def preview_resize(self):
        if not self.original_img:
            messagebox.showinfo("Bilgi", "Önce bir görsel dosyası seçin")
            return
        
        try:
            # Get original dimensions
            original_width, original_height = self.original_img.size
            
            # Calculate new dimensions
            scale = self.scale_factor.get()
            new_width = int(original_width * scale)
            new_height = int(original_height * scale)
            
            # Update info
            self.info_var.set(f"Original: {original_width}x{original_height} → New: {new_width}x{new_height} pixels")
            
            # Show a scaled preview (not the full resized image to save memory)
            preview_scale = min(2.0, scale)  # Limit preview scale to 2x for performance
            preview_width = int(original_width * preview_scale)
            preview_height = int(original_height * preview_scale)
            preview = self.original_img.resize((preview_width, preview_height), Image.LANCZOS)
            
            self.update_preview(preview)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error creating preview: {e}")
    
    def process_logo(self):
        if not self.input_path.get():
            messagebox.showinfo("Information", "Please select an image file")
            return
        
        if not self.output_name.get():
            messagebox.showinfo("Information", "Please specify an output filename")
            return
        
        # Show progress
        self.progress.pack(fill=tk.X, pady=5)
        self.progress.start()
        self.info_var.set("Processing...")
        self.root.update()
        
        # Process in a separate thread to keep UI responsive
        threading.Thread(target=self._process_thread, daemon=True).start()
    
    def _process_thread(self):
        try:
            input_path = self.input_path.get()
            output_dir = self.output_dir.get()
            output_name = self.output_name.get()
            scale_factor = self.scale_factor.get()
            
            # Define output paths
            png_output = os.path.join(output_dir, f"{output_name}.png")
            pdf_output = os.path.join(output_dir, f"{output_name}.pdf")
            jpg_output = os.path.join(output_dir, f"{output_name}.jpg")
            
            # Resize and save as PNG
            result, orig_w, orig_h, new_w, new_h = resize_image(input_path, png_output, scale_factor)
            
            # Save as PDF and JPG
            save_as_pdf(png_output, pdf_output)
            save_as_jpg(png_output, jpg_output)
            
            # Update UI in the main thread
            self.root.after(0, self._process_complete, orig_w, orig_h, new_w, new_h, output_dir)
            
        except Exception as e:
            self.root.after(0, self._process_error, str(e))
    
    def _process_complete(self, orig_w, orig_h, new_w, new_h, output_dir):
        self.progress.stop()
        self.progress.pack_forget()
        
        self.info_var.set(f"Processing complete! Original: {orig_w}x{orig_h} → New: {new_w}x{new_h} pixels")
        
        msg = f"Logo successfully processed!\n\n" \
              f"Saved in PNG, PDF and JPG formats.\n" \
              f"Output folder: {output_dir}"
        
        messagebox.showinfo("Success", msg)
        
        # Ask if user wants to open the output folder
        if messagebox.askyesno("Open Folder", "Do you want to open the output folder?"):
            os.startfile(output_dir)
    
    def _process_error(self, error_msg):
        self.progress.stop()
        self.progress.pack_forget()
        self.info_var.set("Error occurred!")
        messagebox.showerror("Processing Error", f"An error occurred while processing the logo:\n{error_msg}")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = LogoProcessorApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Critical Error", f"An error occurred while starting the application:\n{e}")
