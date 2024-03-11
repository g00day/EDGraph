from graph import Graph
import numpy as np

import funcs as f


class GraphFactory:
    """ Фабрика графиков 
     Принимает в себя лишь только тип графика(переменную) 
    """

    def __init__(self, graph_type:str):
        self.graph_type = graph_type
        self.t = np.linspace(0, 5, 100) # все графики имеют в качестве абсциссы время(t)

    def set_function(self) -> Graph:
        # Этот метод возвращает необходимую функцию 
        # в зависимости от self.graph_type
        d = {"I = q * t": f.I, 
             "Q = I * t": f.Q, 
             "E = 0.5 * I(t)^2":f.E,
             "W = Q(t) * U / 2": f.W}
        return d[self.graph_type]
        
    def get_graph(self) -> Graph:
        # Этот метод возвращает объект графика(Graph)
        func = self.set_function()(self.t)
            
        g = Graph(self.t, func, self.graph_type, "t", self.graph_type)
        return g
