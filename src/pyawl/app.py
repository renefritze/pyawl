import kivy
kivy.require('1.9.1')
try:
    from kivy.uix.recycleview import RecycleView
except ImportError:
    from kivy.garden.recycleview import RecycleView
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.metrics import sp
from kivy.app import App
import pyawl.scrape

KV = """
<ContactSeparator@Widget>:
    canvas.before:
        Color:
            rgb: (.5, .5, .5)
        Rectangle:
            pos: self.pos
            size: self.size

<WishlistItem@BoxLayout>:
    index: 0
    image: ""
    title: ""
    spacing: "10dp"

    canvas.before:
        Color:
            rgb: (1, 1, 1) if root.index % 2 == 0 else (.95, .95, .95)
        Rectangle:
            pos: self.pos
            size: self.size

    AsyncImage:
        source: root.image
        size_hint_x: None
        width: self.height
        allow_stretch: True
    Label:
        font_size: "20sp"
        text: root.title
        color: (0, 0, 0, 1)
        text_size: (self.width, None)

# app example
BoxLayout:
    orientation: "vertical"
    BoxLayout:
        padding: "2sp"
        spacing: "2sp"
        size_hint_y: None
        height: "48sp"

        Button:
            text: "Toggle"
            on_release: app.toggle()

    RecycleView:
        id: listview
"""


class PyAwlApp(App):

    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })

    def build(self):
        self.root = Builder.load_string(KV)
        rv = self.root.ids.listview
        rv.key_viewclass = "viewclass"
        rv.key_size = "height"
        self.reload_list()

    def reload_list(self):
        wishlist = []
        for idx, item in enumerate(pyawl.scrape.parse()):
            wishlist.append({
                "index": idx,
                "viewclass": "WishlistItem",
                "image": item.image,
                "title": item.title
            })

        self.root.ids.listview.data = wishlist

    def toggle(self):
        pass