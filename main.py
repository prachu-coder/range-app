from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class RangeApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.input_box = TextInput(
            hint_text="Enter a number",
            multiline=False,
            input_type="number"
        )

        button = Button(text="Run")

        self.output = Label(
            text="Result will appear here"
        )

        button.bind(on_press=self.run_code)

        layout.add_widget(self.input_box)
        layout.add_widget(button)
        layout.add_widget(self.output)

        return layout

    def run_code(self, instance):
        try:
            o = self.input_box.text
            u = o
            p = range(int(u))

            result = str(p)

            for a in p:
                result += f"\n{a}"

            self.output.text = result

        except ValueError:
            self.output.text = "Please enter a number."


if __name__ == "__main__":
    RangeApp().run()
