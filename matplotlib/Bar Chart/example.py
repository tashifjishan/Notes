import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe

# -----------------------------
# Data
# -----------------------------
categories = ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
values = [95, 82, 76, 61, 55, 48]

# -----------------------------
# Colors
# -----------------------------
background = "#F5F7FB"
text = "#1F2937"
grid = "#E5E7EB"

bar_colors = [
    "#4F46E5",
    "#6366F1",
    "#7C83FD",
    "#9AA5FF",
    "#B8C0FF",
    "#D5DAFF"
]

# -----------------------------
# Figure
# -----------------------------
fig, ax = plt.subplots(figsize=(12,7), dpi=180)

fig.patch.set_facecolor(background)
ax.set_facecolor(background)

# Remove all spines
for s in ax.spines.values():
    s.set_visible(False)

# Grid
ax.grid(axis='y',
        color=grid,
        linewidth=1,
        linestyle='--',
        alpha=0.6)

ax.set_axisbelow(True)

# -----------------------------
# Rounded Bars
# -----------------------------
width = 0.65
x = np.arange(len(categories))

bars = []

for i, (xi, value) in enumerate(zip(x, values)):

    patch = FancyBboxPatch(
        (xi-width/2, 0),
        width,
        value,

        boxstyle="round,pad=0.02,rounding_size=0.18",

        linewidth=0,
        facecolor=bar_colors[i],

        zorder=3
    )

    # Soft shadow
    patch.set_path_effects([
        pe.SimplePatchShadow(
            offset=(3,-3),
            alpha=0.18,
            shadow_rgbFace=(0,0,0)
        ),
        pe.Normal()
    ])

    ax.add_patch(patch)
    bars.append(patch)

# -----------------------------
# Axis
# -----------------------------
ax.set_xlim(-0.6, len(categories)-0.4)
ax.set_ylim(0,110)

ax.set_xticks(x)
ax.set_xticklabels(
    categories,
    fontsize=13,
    fontweight='medium',
    color=text
)

ax.tick_params(axis='y',
               labelsize=11,
               colors="#6B7280")

# -----------------------------
# Value Labels
# -----------------------------
for xi, value in zip(x, values):

    ax.text(
        xi,
        value+2.5,
        f"{value}",

        ha='center',
        va='bottom',

        fontsize=12,
        fontweight='bold',

        color=text
    )

# -----------------------------
# Title
# -----------------------------
ax.set_title(
    "Programming Language Popularity",
    fontsize=24,
    fontweight='bold',
    color=text,
    pad=30
)

ax.set_ylabel(
    "Popularity Score",
    fontsize=13,
    color="#6B7280",
    labelpad=15
)

# -----------------------------
# Subtitle
# -----------------------------
fig.text(
    0.125,
    0.91,
    "Survey results from 2025 • Modern minimal design",
    fontsize=12,
    color="#6B7280"
)

# -----------------------------
# Footer
# -----------------------------
fig.text(
    0.99,
    0.02,
    "Created with Matplotlib",
    ha="right",
    fontsize=10,
    color="#9CA3AF"
)

plt.tight_layout()
plt.show()