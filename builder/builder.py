class HtmlElement:
    indent_size = 2

    def __init__(self, name=None, text=None):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')  # opening outer element <ul>

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')  # outer text

        for e in self.elements:
            lines.append(e.__str(indent + 1))  # inner elements <li>..text..</li>

        lines.append(f'{i}</{self.name}>')  # closing outer element </ul>
        return '\n'.join(lines)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)

    def __str__(self):
        return self.__str(0)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

    def __str__(self):
        return str(self.__root)


# ordinary builder
builder = HtmlBuilder('ul')   # outer elem
builder.add_child('li', 'hello')
builder.add_child('li', 'world')
builder.add_child('li', 'here')
builder.add_child('li', 'I')
builder.add_child('li', 'am')
print('Ordinary builder:')
print(builder)

print('\n')

# chained builder
builder = HtmlElement.create('ul')  # outer elem
builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world').add_child_fluent('li', 'here').\
    add_child_fluent('li', 'I').add_child_fluent('li', 'am')
print('Chained builder:')
print(builder)
