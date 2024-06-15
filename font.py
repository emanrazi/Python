import tkinter as tk

# Dictionary mapping font names to the sample text
font_samples = {
    "System": "System: The quick brown fox jumps over the lazy dog",
    "Terminal": "Terminal: The quick brown fox jumps over the lazy dog",
    "Modern": "Modern: The quick brown fox jumps over the lazy dog",
    "Roman": "Roman: The quick brown fox jumps over the lazy dog",
    "Script": "Script: The quick brown fox jumps over the lazy dog",
    "Courier": "Courier: The quick brown fox jumps over the lazy dog",
    "Arial": "Arial: The quick brown fox jumps over the lazy dog",
    "Arial Black": "Arial Black: The quick brown fox jumps over the lazy dog",
    "Calibri": "Calibri: The quick brown fox jumps over the lazy dog",
    "Comic Sans MS": "Comic Sans MS: The quick brown fox jumps over the lazy dog",
    "Consolas": "Consolas: The quick brown fox jumps over the lazy dog",
    "Georgia": "Georgia: The quick brown fox jumps over the lazy dog",
    "Impact": "Impact: The quick brown fox jumps over the lazy dog",
    "Lucida Console": "Lucida Console: The quick brown fox jumps over the lazy dog",
    "Segoe UI": "Segoe UI: The quick brown fox jumps over the lazy dog",
    "Times New Roman": "Times New Roman: The quick brown fox jumps over the lazy dog",
    "Verdana": "Verdana: The quick brown fox jumps over the lazy dog",
    "Papyrus": "Papyrus: The quick brown fox jumps over the lazy dog",
    "Arial Narrow": "Arial Narrow: The quick brown fox jumps over the lazy dog",
    "Arial Rounded MT Bold": "Arial Rounded MT Bold: The quick brown fox jumps over the lazy dog",
    "Baskerville Old Face": "Baskerville Old Face: The quick brown fox jumps over the lazy dog",
    "Bauhaus 93": "Bauhaus 93: The quick brown fox jumps over the lazy dog",
    "Bell MT": "Bell MT: The quick brown fox jumps over the lazy dog",
    "Book Antiqua": "Book Antiqua: The quick brown fox jumps over the lazy dog"
}

class FontDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("Font Style Demo")
        
        # Frame to hold the labels
        frame = tk.Frame(self.root, bg="white")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Display sample text with different fonts
        for font_name, sample_text in font_samples.items():
            self.add_font_sample(frame, font_name, sample_text)
    
    def add_font_sample(self, frame, font_name, sample_text):
        label = tk.Label(frame, text=sample_text, font=(font_name, 14), bg="white")
        label.pack(anchor="w", padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = FontDemo(root)
    root.geometry("700x800")  # Set the window size
    root.mainloop()
