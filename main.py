from graph_factory import GraphFactory

def main():
    print("EDgraph")
    while True:
        try:
            graph_type = input("функция: ")
            gf = GraphFactory(graph_type)
            g = gf.get_graph()
            g.build()
        except:
            print("Не соответствует заданию")


if __name__ == "__main__":
    main()