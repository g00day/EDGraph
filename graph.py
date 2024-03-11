import matplotlib.pyplot as plt


class Graph:

    def __init__(self, x:float, 
                y:float, title:str,
                x_label:str="x", y_label:str="y"):
        self.x = x
        self.y = y
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def build(self):
        # Метод строит график по входным данным переданным в инициализаторе
        fig, ax = plt.subplots()
        ax.set_title(self.title)
        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)
        ax.plot(self.x, self.y)
        plt.show()


