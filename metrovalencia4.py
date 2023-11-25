from pathlib import Path
from splinemaps import MapHandler


def main():
    figures_dir = Path("figures")
    figures_dir.mkdir(exist_ok=True)

    map = MapHandler("resources/metrovalencia4.png")
    map.plot_spline(figures_dir / "metrovalencia4.png")
    map.plot_lerp(figures_dir / "metrovalencia4_lerp.png")

    ejemplo = MapHandler("resources/ejemplo.png")
    ejemplo.plot_spline(figures_dir / "ejemplo.png")


if __name__ == "__main__":
    main()
