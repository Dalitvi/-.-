class Renderer:
    def render_simple_page(self, title, content):
        pass

    def render_product_page(self, product):
        pass


class HTMLRenderer(Renderer):
    def render_simple_page(self, title, content):
        print(f"HTML page : {title}      Content : {content}")

    def render_product_page(self, product):
        print(f"HTML product {product.name}     Description : {product.description}    Image  <{product.img_url}>   Product ID : # {product.id}\n")


class JSONRenderer(Renderer):
    def render_simple_page(self, title, content):
        print(f"JSON page  : {title}      Content : {content}")

    def render_product_page(self, product):
        print(f"JSON product {product.name}     Description : {product.description}    Image  <{product.img_url}>   Product ID : # {product.id}\n")


class XMLRenderer(Renderer):
    def render_simple_page(self, title, content):
        print(f"XML page : {title}      Content : {content}")

    def render_product_page(self, product):
        print(f"XML product {product.name}     Description : {product.description}    Image <{product.img_url}>   Product ID : # {product.id}\n")


class Page:
    def __init__(self, renderer):
        self.renderer = renderer

    def view(self):
        pass


class SimplePage(Page):
    def __init__(self, renderer, title, content):
        super().__init__(renderer)
        self.title = title
        self.content = content

    def view(self):
        self.renderer.render_simple_page(self.title, self.content)


class ProductPage(Page):
    def __init__(self, renderer, product):
        super().__init__(renderer)
        self.product = product

    def view(self):
        self.renderer.render_product_page(self.product)


class Product:
    def __init__(self, name, description, img_url, id):
        self.name = name
        self.description = description
        self.img_url = img_url
        self.id = id


# Main function to demonstrate functionality
def main():
    html_renderer = HTMLRenderer()
    json_renderer = JSONRenderer()
    xml_renderer = XMLRenderer()

    simple_page = SimplePage(html_renderer, "HTML Page", "Shop1 HTML")
    simple_page.view()
    
    product = Product("bread", "fresh", "crea.jpg", 1)
    product_page = ProductPage(html_renderer, product)
    product_page.view()

    simple_page = SimplePage(json_renderer, "JSON Page", "Shop2 JSON")
    simple_page.view()
    
    product2 = Product("apples", "red", "apple.jpg", 2)
    product_page = ProductPage(json_renderer, product2)
    product_page.view()

    simple_page = SimplePage(xml_renderer, "XML Page", " Shop3 XML")
    simple_page.view()
    product_page = ProductPage(xml_renderer, product2)
    product_page.view()


# Run the demonstration
if __name__ == "__main__":
    main()
