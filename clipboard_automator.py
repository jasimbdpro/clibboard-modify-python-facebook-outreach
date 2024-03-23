import pyperclip
import win32clipboard
import time

def copy_to_clipboard(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text)
    win32clipboard.CloseClipboard()

def get_clipboard_content():
    win32clipboard.OpenClipboard()
    clipboard_data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return clipboard_data

def main():
    last_copied_text = ""
    while True:
        current_copied_text = get_clipboard_content()
        if current_copied_text != last_copied_text:
            last_copied_text = current_copied_text
            if last_copied_text and not last_copied_text.startswith("Hello"):
                if last_copied_text.endswith('\n'):
                    last_copied_text = last_copied_text[:-1]  # Remove the last character (newline)
                text_to_paste = "Hello " + last_copied_text + ",\nI am Jasim Uddin, an expert Graphic Designer for Real Estate Agent using Adobe Photoshop, Adobe Illustrator, Canva etc as primary tools and I satisfied over hundreds of clients over last 5 years by creating amazing design for their business.  If you want me to create Social Media Posts Design, Story, Reels for Instagram, Facebook, Tiktok business etc, Web Banner Design, Email Template and Signature Design, Social Media Marketing services, feel free to contact me. I am happy to answer any questions, and I am ready to show my previous creation/work examples, and client testimonials.\n\nBest Regards:\nJasim Uddin\njasimbdpro@gmail.com\n+8801827104738"

                copy_to_clipboard(text_to_paste)
                print("Text modified and copied to clipboard:", text_to_paste)
        time.sleep(1)  # Adjust sleep time as needed

if __name__ == "__main__":
    main()
