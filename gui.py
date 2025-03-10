from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QTextEdit
import networkx as nx
from ford_fulkerson import FordFulkerson
from graph_visualizer import draw_graph

class FordFulkersonGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.ford_fulkerson = None
        self.n = 0
        self.edges = []

    def initUI(self):
        self.setWindowTitle("Ford-Fulkerson - PyQt6")
        self.setGeometry(100, 100, 400, 500)
        layout = QVBoxLayout()

        self.inputField = QLineEdit(self)
        self.inputField.setPlaceholderText("Ejemplo: 0 1 10")
        layout.addWidget(self.inputField)

        self.addButton = QPushButton("Agregar Arista", self)
        self.addButton.clicked.connect(self.add_edge)
        layout.addWidget(self.addButton)

        self.removeNodeField = QLineEdit(self)
        self.removeNodeField.setPlaceholderText("Nodo a eliminar")
        layout.addWidget(self.removeNodeField)

        self.removeNodeButton = QPushButton("Eliminar Nodo", self)
        self.removeNodeButton.clicked.connect(self.remove_node)
        layout.addWidget(self.removeNodeButton)

        self.sourceField = QLineEdit(self)
        self.sourceField.setPlaceholderText("Nodo fuente")
        layout.addWidget(self.sourceField)

        self.sinkField = QLineEdit(self)
        self.sinkField.setPlaceholderText("Nodo sumidero")
        layout.addWidget(self.sinkField)

        self.runButton = QPushButton("Ejecutar Ford-Fulkerson", self)
        self.runButton.clicked.connect(self.run_algorithm)
        layout.addWidget(self.runButton)

        self.outputLabel = QLabel("Flujo Máximo: ", self)
        layout.addWidget(self.outputLabel)

        self.edgesList = QTextEdit(self)
        self.edgesList.setReadOnly(True)
        layout.addWidget(self.edgesList)

        self.setLayout(layout)

    def add_edge(self):
        text = self.inputField.text()
        parts = text.split()
        if len(parts) == 3:
            try:
                u, v, capacity = map(int, parts)
                self.edges.append((u, v, capacity))
                self.edgesList.append(f"Arista: {u} -> {v} con capacidad {capacity}")
                self.n = max(self.n, u + 1, v + 1)
                self.inputField.clear()
            except ValueError:
                self.edgesList.append("Entrada inválida.")
        else:
            self.edgesList.append("Formato incorrecto.")

    def remove_node(self):
        try:
            node = int(self.removeNodeField.text())
            self.edges = [edge for edge in self.edges if edge[0] != node and edge[1] != node]
            self.edgesList.append(f"Nodo {node} eliminado y conexiones removidas.")
        except ValueError:
            self.edgesList.append("Ingrese un número válido para el nodo a eliminar.")

    def run_algorithm(self):
        if len(self.edges) < 1:
            self.outputLabel.setText("No hay aristas.")
            return

        try:
            source = int(self.sourceField.text())
            sink = int(self.sinkField.text())
        except ValueError:
            self.outputLabel.setText("Fuente y sumidero deben ser números válidos.")
            return

        if source == sink or source < 0 or sink < 0 or source >= self.n or sink >= self.n:
            self.outputLabel.setText("Fuente y sumidero no válidos.")
            return

        self.ford_fulkerson = FordFulkerson(self.n, source, sink)
        for u, v, capacity in self.edges:
            self.ford_fulkerson.add_edge(u, v, capacity)

        max_flow, flow = self.ford_fulkerson.max_flow()
        self.outputLabel.setText(f"Flujo Máximo: {max_flow}")
        draw_graph(self.edges, flow, source, sink)

if __name__ == "__main__":
    app = QApplication([])
    window = FordFulkersonGUI()
    window.show()
    app.exec()
