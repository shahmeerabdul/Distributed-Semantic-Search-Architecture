"""
Main Application Entry Point
DSA Search Engine with TF-IDF Ranking - Modern CustomTkinter UI
"""
import customtkinter as ctk
from search_gui import SearchEngineGUI

def main():
    """Main function to start the application"""
    root = ctk.CTk()
    app = SearchEngineGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
