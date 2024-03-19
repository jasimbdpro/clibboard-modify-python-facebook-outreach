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
                text_to_paste = "Hello " + last_copied_text + ",\nI am Jasim Uddin, an expert Graphic Designer using Adobe Photoshop, Adobe Illustrator, Canva, etc., as primary tools, and I have satisfied over hundreds of clients over the last 5 years with my design abilities. If you need Social Media Posts, Stories, Reels for Instagram, Facebook, TikTok, etc., Web Banner Design, Email Template, and Signature Design, as well as Social Media Marketing services, feel free to contact me. I will be happy to answer any questions, ready to show my previous work examples, and client testimonials.\n\nBest Regards:\nJasim Uddin\njasimbdpro@gmail.com\n+8801827104738"
                copy_to_clipboard(text_to_paste)
                print("Text modified and copied to clipboard:", text_to_paste)
        time.sleep(1)  # Adjust sleep time as needed

if __name__ == "__main__":
    main()
