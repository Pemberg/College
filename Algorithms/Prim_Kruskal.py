import random
import time
import matplotlib.pyplot as plt
import numpy as np


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Inicjalizacja liczby wierzchołków grafu
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]  # Inicjalizacja macierzy sąsiedztwa

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight  # Dodawanie krawędzi do macierzy sąsiedztwa
        self.graph[v][u] = weight  # Dodawanie krawędzi do macierzy sąsiedztwa (graf nieskierowany)

    def prim_mst(self):
        key = [float('inf')] * self.V  # Inicjalizacja kluczy do wierzchołków
        mst_set = [False] * self.V  # Inicjalizacja zbioru MST
        parent = [None] * self.V  # Inicjalizacja tablicy rodziców
        key[0] = 0  # Ustawienie klucza początkowego
        parent[0] = -1  # Ustawienie rodzica początkowego węzła

        for _ in range(self.V):
            u = self.min_key(key, mst_set)  # Wybór wierzchołka o najmniejszym kluczu spośród nieodwiedzonych
            mst_set[u] = True  # Dodanie wierzchołka do zbioru MST
            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not mst_set[v]
                    and self.graph[u][v] < key[v]
                ):
                    key[v] = self.graph[u][v]  # Aktualizacja klucza
                    parent[v] = u  # Ustawienie rodzica wierzchołka

        return parent

    def kruskal_mst(self):
        result = []  # Inicjalizacja listy wynikowej
        i = 0
        e = 0
        edges = self.get_edges()  # Pobranie wszystkich krawędzi grafu
        edges.sort(key=lambda x: x[2])  # Sortowanie krawędzi według wag

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)  # Inicjalizacja tablicy rodziców
            rank.append(0)  # Inicjalizacja tablicy rang

        while e < self.V - 1:
            if i >= len(edges):
                break
            u, v, weight = edges[i]  # Wybór krawędzi o najmniejszej wadze spośród nieodwiedzonych
            i += 1
            x = self.find(parent, u)  # Wyszukiwanie korzenia drzewa, do którego należy wierzchołek u
            y = self.find(parent, v)  # Wyszukiwanie korzenia drzewa, do którego należy wierzchołek v
            if x != y:  # Jeśli korzenie drzew są różne, krawędź nie tworzy cyklu
                e += 1  # Zwiększanie licznika odwiedzonych krawędzi
                result.append((u, v, weight))  # Dodanie krawędzi do listy wynikowej
                self.union(parent, rank, x, y)  # Łączenie drzew

        return result

    def min_key(self, key, mst_set):
        min_val = float('inf')  # Ustawienie początkowej wartości minimalnej
        min_index = -1  # Ustawienie początkowego indeksu minimalnego
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:  # Jeśli klucz jest mniejszy od aktualnego minimum i wierzchołek nie jest w MST
                min_val = key[v]  # Aktualizacja wartości minimalnej
                min_index = v  # Aktualizacja indeksu minimalnego
        return min_index

    def find(self, parent, i):
        if parent[i] == i:  # Jeśli wierzchołek jest korzeniem drzewa
            return i  # Zwracanie indeksu korzenia
        return self.find(parent, parent[i])  # Rekurencyjne wyszukiwanie korzenia

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)  # Wyszukiwanie korzenia drzewa z wierzchołkiem x
        y_root = self.find(parent, y)  # Wyszukiwanie korzenia drzewa z wierzchołkiem y
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root  # Przypisanie korzenia y do korzenia x
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root  # Przypisanie korzenia x do korzenia y
        else:
            parent[y_root] = x_root  # Przypisanie korzenia x do korzenia y
            rank[x_root] += 1  # Zwiększenie rangi korzenia x

    def get_edges(self):
        edges = []  # Inicjalizacja listy krawędzi
        for i in range(self.V):
            for j in range(i + 1, self.V):
                if self.graph[i][j] != 0:  # Jeśli istnieje krawędź między wierzchołkami i i j
                    edges.append((i, j, self.graph[i][j]))  # Dodanie krawędzi do listy krawędzi
        return edges


def generate_random_graph(n):
    graph = Graph(n)  # Utworzenie nowego obiektu klasy Graph
    for i in range(n):
        num_paths = random.randint(1, n - 1)  # Losowanie liczby ścieżek z danego wierzchołka
        for _ in range(num_paths):
            weight = random.randint(1, n)  # Losowanie wagi krawędzi
            dest = random.randint(0, n - 1)  # Losowanie docelowego wierzchołka
            graph.add_edge(i, dest, weight)  # Dodanie krawędzi do grafu
    return graph


def measure_time(graph):
    start = time.time()  # Początek pomiaru czasu
    graph.prim_mst()  # Wywołanie metody dla algorytmu Prima
    prim_time = time.time() - start  # Obliczenie czasu wykonania dla algorytmu Prima

    start = time.time()  # Początek pomiaru czasu
    graph.kruskal_mst()  # Wywołanie metody dla algorytmu Kruskala
    kruskal_time = time.time() - start  # Obliczenie czasu wykonania dla algorytmu Kruskala

    return prim_time, kruskal_time


def generate_monte_carlo_times(n, num_iterations):
    monte_carlo_times = []  # Inicjalizacja listy czasów Monte Carlo
    for _ in range(num_iterations):
        monte_carlo_time = np.random.uniform(0.1, 1.0)  # Generowanie losowego czasu Monte Carlo
        monte_carlo_times.append(monte_carlo_time)  # Dodanie czasu Monte Carlo do listy
    return monte_carlo_times


def plot_results(num_vertices, prim_monte_carlo_times, prim_avg_times, kruskal_monte_carlo_times, kruskal_avg_times):
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)  # Pierwszy wykres
    plt.plot(num_vertices, prim_avg_times, label='Średni wynik algorytmu Prima')
    plt.xlabel('Liczba wierzchołków')
    plt.ylabel('Czas wykonania (ms)')
    plt.title('Algorytm Prima')
    plt.legend()

    plt.subplot(1, 2, 2)  # Drugi wykres
    plt.plot(num_vertices, kruskal_avg_times, label='Średni wynik algorytmu Kruskala')
    plt.xlabel('Liczba wierzchołków')
    plt.ylabel('Czas wykonania (ms)')
    plt.title('Algorytm Kruskala')
    plt.legend()

    plt.tight_layout()
    plt.show()


def main():
    num_iterations = 500  # Liczba iteracji dla eksperymentu Monte Carlo
    num_vertices = [5, 10, 15, 20]  # Liczba wierzchołków dla grafów
    prim_monte_carlo_times = []  # Inicjalizacja listy czasów Monte Carlo dla algorytmu Prima
    kruskal_monte_carlo_times = []  # Inicjalizacja listy czasów Monte Carlo dla algorytmu Kruskala
    prim_avg_times = []  # Inicjalizacja listy średnich czasów wykonania dla algorytmu Prima
    kruskal_avg_times = []  # Inicjalizacja listy średnich czasów wykonania dla algorytmu Kruskala

    for n in num_vertices:
        total_prim_time = 0  # Suma czasów wykonania dla algorytmu Prima
        total_kruskal_time = 0  # Suma czasów wykonania dla algorytmu Kruskala

        for _ in range(num_iterations):
            graph = generate_random_graph(n)  # Generowanie losowego grafu
            prim_time, kruskal_time = measure_time(graph)  # Pomiar czasu wykonania dla obu algorytmów
            total_prim_time += prim_time  # Dodanie czasu wykonania dla algorytmu Prima
            total_kruskal_time += kruskal_time  # Dodanie czasu wykonania dla algorytmu Kruskala

            prim_monte_carlo_times.extend(generate_monte_carlo_times(n, num_iterations))  # Generowanie czasów Monte Carlo dla algorytmu Prima
            kruskal_monte_carlo_times.extend(generate_monte_carlo_times(n, num_iterations))  # Generowanie czasów Monte Carlo dla algorytmu Kruskala

        avg_prim_time = total_prim_time / num_iterations  # Obliczenie średniego czasu wykonania dla algorytmu Prima
        avg_kruskal_time = total_kruskal_time / num_iterations  # Obliczenie średniego czasu wykonania dla algorytmu Kruskala

        prim_avg_times.append(avg_prim_time)  # Dodanie średniego czasu wykonania dla algorytmu Prima do listy
        kruskal_avg_times.append(avg_kruskal_time)  # Dodanie średniego czasu wykonania dla algorytmu Kruskala do listy

    plot_results(num_vertices, prim_monte_carlo_times, prim_avg_times, kruskal_monte_carlo_times, kruskal_avg_times)


if __name__ == "__main__":
    main()