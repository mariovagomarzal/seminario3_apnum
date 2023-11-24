from dataclasses import dataclass, field
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import pandas as pd


# Constantes
TERMINACION_PARADAS = "-paradas"


@dataclass
class MapHandler:
    path: str | Path
    imagen: np.ndarray = field(init=False)
    paradas: list[tuple[float, float]] = field(init=False)

    def __post_init__(self):
        """
        Carga la imagen del mapa y las coordenadas asociadas a las paradas.
        """
        self.path = Path(self.path)
        self.imagen = plt.imread(self.path)

        # Carga el csv con el nombre de la imagen + "-paradas"
        paradas_path = Path(
            self.path.parent,
            self.path.stem + TERMINACION_PARADAS + ".csv"
        )
        df = pd.read_csv(paradas_path)

        # Almanena las coordenadas 'x' e 'y' en una lista de tuplas
        self.paradas = [
            (row['x'], row['y'])
            for _, row in df.iterrows()
        ]

    def plot_spline(self, path: str | Path):
        fig, ax = plt.subplots()

        # Añade la imagen del mapa como fondo
        ax.imshow(self.imagen)

        # Añade las paradas como puntos rojos
        ax.scatter(*zip(*self.paradas), c='r', s=10)

        # Detrmina los splines interpoladores de cada componente
        # y construye la curva paramétrica
        t = sp.symbols('t')
        t_vals = np.linspace(0, 1, len(self.paradas))
        x_spline = sp.lambdify(
            t,
            sp.interpolating_spline(3, t, t_vals, [x for x, _ in self.paradas])
        )
        y_spline = sp.lambdify(
            t,
            sp.interpolating_spline(3, t, t_vals, [y for _, y in self.paradas])
        )

        # Evalúa los splines en los valores de t
        spline_vals = [(x_spline(i), y_spline(i)) for i in t_vals]

        # Añade la curva paramétrica como una línea azul
        ax.plot(*zip(*spline_vals), c='b')

        # Guarda la figura
        fig.savefig(path, dpi=500)

    def plot_lerp(self, path: str | Path):
        fig, ax = plt.subplots()

        # Añade la imagen del mapa como fondo
        ax.imshow(self.imagen)

        # Añade las paradas como puntos rojos
        ax.scatter(*zip(*self.paradas), c='r', s=10)

        # Añade la curva paramétrica como una línea azul
        ax.plot(*zip(*self.paradas), c='b')

        # Guarda la figura
        fig.savefig(path, dpi=500)
