from datetime import datetime

import dominate
from dominate.tags import *

from delivery import Delivery


class GUI:

    def __init__(self):
        self.doc = dominate.document(title="Delivery Status")
        self.delivery = Delivery()
        self.style = "delivery.css"
        self.template = "template.css"
        self.reset = "reset.css"
        self.css_directory = "../css/"

    def create_html(self) -> None:
        with self.doc.head:
            link(rel="stylesheet", href=f"{self.css_directory}{self.reset}")
            link(rel="stylesheet", href=f"{self.css_directory}{self.template}")
            link(rel="stylesheet", href=f"{self.css_directory}{self.style}")
            script(type="application/javascript", src="refresh.js")
        with self.doc:
            with div(cls="container"):
                with header(cls="page-header"):
                    h1("Delivery Status")
                    hr()
                with div(cls="card"):
                    with div(cls="card-body"):
                        with header(cls="card-header"):
                            h2("Item")
                            hr()
                            try:
                                p(self.delivery.delivery_status()[3])
                            except TypeError:
                                pass
                        with div(cls="card-content"):
                            with div(cls="card-content-item"):
                                h2("Tracking Number")
                                p(self.delivery.delivery_status()[0])
                            with div(cls="card-content-item"):
                                h2("Delivery Status")
                                p(self.delivery.delivery_status()[1])
                            with div(cls="card-content-item"):
                                h2("Last Update")
                                p(f"{self.delivery.delivery_status()[2]} {datetime.now().strftime('%H:%M %p')}")

    def save_html(self) -> None:
        with open("index.html", "w") as f:
            f.write(self.doc.render())
            f.close()

    def update(self):
        self.create_html()
        self.save_html()
