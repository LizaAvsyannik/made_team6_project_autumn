import itertools
import numpy as np
from typing import List, Dict

import plotly.graph_objects as go
from plotly.subplots import make_subplots

COLORS = ["#D55E00", "#0072B2", "#CC79A7", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#000000"]


def visualize_barchart(topics: Dict,
                       top_n_authors: int = 5,
                       width: int = 500,
                       height: int = 250) -> go.Figure:
    # Initialize figure
    subplot_titles = [f"{' '.join(topic['topic'].split('_')[1:])}" for topic in topics]
    columns = 4
    rows = int(np.ceil(len(topics) / columns))
    fig = make_subplots(rows=rows,
                        cols=columns,
                        shared_xaxes=False,
                        horizontal_spacing=.1,
                        vertical_spacing=.4 / rows if rows > 1 else 0,
                        subplot_titles=subplot_titles)

    colors = itertools.cycle(COLORS)
    # Add barchart for each topic
    row = 1
    column = 1
    for topic in topics:
        most_common = topic['authors'].most_common(top_n_authors)
        authors = [author + "  " for author, _ in most_common]
        n_cit = [score for _, score in most_common]

        fig.add_trace(
            go.Bar(x=n_cit,
                   y=authors,
                   orientation='h',
                   marker_color=next(colors)),
            row=row, col=column)

        if column == columns:
            column = 1
            row += 1
        else:
            column += 1

    # Stylize graph
    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        title={
            'text': "<b>Topic Word Scores",
            'x': .5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(
                size=22,
                color="Black")
        },
        width=width * 4,
        height=height * rows if rows > 1 else height * 1.3,
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell"
        ),
    )

    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    return fig
