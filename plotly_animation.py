import plotly.graph_objects as go
import numpy as np


x = np.linspace(-4 * np.pi, 4 * np.pi, 100)

fig = go.Figure(
    data=[go.Scatter(x=x, y=np.sin(x), mode='lines')],
    layout=go.Layout(
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])]
    ),
    frames=[go.Frame(data=[go.Scatter(x=x, y=np.sin(x + phi))])
            for phi in np.linspace(0, 2 * np.pi, 100)]
)

fig.show()
