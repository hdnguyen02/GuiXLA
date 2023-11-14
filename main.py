import webview
import os


def on_loaded(window):
    window.pywebview.api.changeMessage = load_image


def load_image():
    print("load image")


if __name__ == '__main__':
    absolute_path = os.path.abspath("index.html")
    webview.create_window("XLA Gui", absolute_path)
    webview.start()
