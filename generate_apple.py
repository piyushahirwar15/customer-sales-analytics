"""
generate_apple.py

Generates and saves a visual representation of an apple as a PNG image.
Requires: matplotlib
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path


def draw_apple(ax):
    # --- Apple body (two overlapping circles to form apple shape) ---
    left_circle = plt.Circle((-0.18, 0.0), 0.52, color="#CC2200", zorder=2)
    right_circle = plt.Circle((0.18, 0.0), 0.52, color="#CC2200", zorder=2)
    ax.add_patch(left_circle)
    ax.add_patch(right_circle)

    # Slightly darker centre overlap for depth
    center_ellipse = patches.Ellipse((0, -0.05), 0.55, 0.88, color="#BB1F00", zorder=3)
    ax.add_patch(center_ellipse)

    # --- Indentation at top ---
    top_indent = plt.Circle((0, 0.48), 0.14, color="white", zorder=4)
    ax.add_patch(top_indent)

    # Re-draw a small red area to keep natural look
    top_fill = plt.Circle((0, 0.50), 0.10, color="#BB1F00", zorder=5)
    ax.add_patch(top_fill)

    # --- Highlight / shine ---
    shine = patches.Ellipse((-0.22, 0.22), 0.20, 0.30,
                             angle=20, color="white", alpha=0.30, zorder=6)
    ax.add_patch(shine)

    # --- Stem ---
    stem_x = [0.04, 0.10]
    stem_y = [0.48, 0.80]
    ax.plot(stem_x, stem_y, color="#5C3317", linewidth=6, solid_capstyle="round", zorder=7)

    # --- Leaf ---
    leaf_verts = [
        (0.10, 0.68),
        (0.38, 0.90),
        (0.42, 0.72),
        (0.22, 0.60),
        (0.10, 0.68),
    ]
    leaf_codes = [
        Path.MOVETO,
        Path.CURVE4,
        Path.CURVE4,
        Path.CURVE4,
        Path.CLOSEPOLY,
    ]
    leaf_path = Path(leaf_verts, leaf_codes)
    leaf_patch = patches.PathPatch(leaf_path, facecolor="#228B22",
                                   edgecolor="#145214", linewidth=1.5, zorder=8)
    ax.add_patch(leaf_patch)

    # Leaf vein
    ax.plot([0.10, 0.36], [0.68, 0.82], color="#145214",
            linewidth=1.0, alpha=0.7, zorder=9)


def generate_apple_image(output_path="apple.png"):
    fig, ax = plt.subplots(figsize=(5, 5), facecolor="white")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    draw_apple(ax)

    plt.tight_layout(pad=0)
    fig.savefig(output_path, dpi=150, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print(f"Apple image saved to: {output_path}")


if __name__ == "__main__":
    generate_apple_image("apple.png")
