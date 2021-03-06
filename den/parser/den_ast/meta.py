from .node import Node
import uuid


# Meta code sections


class meta:
    class Program(Node):
        def __init__(self, block, position, name=None):
            self.block = block
            if name is None:
                self.name = f"{uuid.uuid4()}"
            else:
                self.name = "_".join(name.split(".")[:-1])
            self.position = position

        def add_name(self, name):
            self.name = "_".join(name.split(".")[:-1])

    class Block(Node):
        def __init__(self, statements, position):
            self.statements = statements
            self.position = position
            self.label = None  # e.g. entry

        def push(self, statement):
            self.statements.append(statement)
