OPERATORS = ['*', '+']
PRECENDENCE = {'*':0, '+':1}

class Node():
    """Represents a node of an expression tree"""
    value = None
    parent = None
    left_child = None
    right_child = None

    def __init__(self, value=None, parent=None, left_child=None, right_child=None):
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def evaluate(self):
        """Evaluates the expression tree starting at this node"""
        if self.value.isdigit():
            return int(self.value)
        elif self.value in OPERATORS:
            if self.value == "+":
                return self.left_child.evaluate() + self.right_child.evaluate()
            elif self.value == "*":
                return self.left_child.evaluate() * self.right_child.evaluate()

    def to_dot_str(self):
        """Traverses this node's children and assembles a directed graph DOT string"""
        dotstr = "digraph {\n"
        dotstr += '{0} [label="{1}"]\n'.format(id(self), self.value)
        nodes_visited = []
        nodes_to_visit = list(filter(None, [self.left_child, self.right_child]))

        while len(nodes_to_visit) > 0:
            node = nodes_to_visit.pop()
            nodes_visited = nodes_visited + [node]
            nodes_to_visit = list(filter(None, nodes_to_visit + [node.left_child, node.right_child]))

        for node in nodes_visited:
            dotstr += '{0} [label="{1}"]\n'.format(id(node), node.value)    # node labels
        for node in nodes_visited:
            dotstr += '{0}->{1};\n'.format(node.parent, node)   # node edges

        dotstr += "}"
        return dotstr

    def __str__(self):
        return str(id(self))

def is_greater_precedence(op1, op2):
    return PRECENDENCE[op1] >= PRECENDENCE[op2]

def get_postfix_expression(line):
    """Converts a given infix expression to a list of tokens in postfix order"""
    output = []
    operators = []
    for c in line:
        if c.isdigit():
            output.append(c)
        elif c in OPERATORS:
            while operators and operators[-1] != '(' and not is_greater_precedence(c, operators[-1]):   # remove is_greater_precedence for Part1 soln
                output.append(operators.pop())
            operators.append(c)
        elif c == '(':
            operators.append(c)
        elif c == ')':
            while operators[-1] != '(':
                output.append(operators.pop())
            if operators[-1] == '(':
                operators.pop()
    
    while operators:
        output.append(operators.pop())

    return output

def build_tree(postfix):
    """Constructs an expression tree of Node objects from a given postfix expression"""
    stack = []
    for c in postfix:
        if c.isdigit():
            stack.append(Node(value=c))
        elif c in OPERATORS:
            l = stack.pop()
            r = stack.pop()
            p = Node(value=c, left_child=l, right_child=r)
            l.parent = p
            r.parent = p
            stack.append(p)

    return stack.pop()

with open('input.txt') as f:
    lines = [l.replace(' ', '').strip() for l in f.readlines()]

    results = []
    for line in lines:
        postfix = get_postfix_expression(line)
        et = build_tree(postfix)
        results.append(et.evaluate())
    
    print(sum(results))
