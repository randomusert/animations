import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import subprocess

def run_manim_command(script_path, class_name):
    if not script_path or not class_name:
        messagebox.showwarning("Input Error", "Please provide both script path and class name.")
        return

    try:
        # Construct the Manim command
        command = f"manim -pql {script_path} {class_name}"
        
        # Run the Manim command
        result = subprocess.check_output(command, shell=True, text=True)
        
        # Display success message
        
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Execution Error", f"Error running Manim:\n{e.output}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def browse_file():
    # Open file dialog to select the Manim script
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    script_entry.delete(0, tk.END)  # Clear current entry
    script_entry.insert(0, file_path)  # Insert selected file path

# Create the main Tkinter window
root = tk.Tk()
root.title("Manim Animation Runner")
root.geometry("500x300")

# Label and entry for script path
tk.Label(root, text="Manim Script Path:").pack(pady=5)
script_entry = tk.Entry(root, width=50)
script_entry.pack(pady=5)

# Button to browse for script file
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)

# Label and entry for class name
tk.Label(root, text="Class Name to Render:").pack(pady=5)
class_entry = tk.Entry(root, width=30)
class_entry.pack(pady=5)

# Button to run the Manim animation
run_button = tk.Button(
    root,
    text="Run Animation",
    command=lambda: run_manim_command(script_entry.get(), class_entry.get())
)
run_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
