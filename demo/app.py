
import gradio as gr
from gradio_goodtab import GoodTab


example = GoodTab().example_value()

demo = gr.Interface(
    lambda x:x,
    GoodTab(),  # interactive version of your component
    GoodTab(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()
