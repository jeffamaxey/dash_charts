"""Coordinate chart."""

import numpy as np
import plotly.graph_objects as go

from . import helpers


class CoordinateChart(helpers.CustomChart):
    """Coordinate Chart.

    Example Use: visualizing a discrete dataset

    """

    def __init__(self, title='', xLbl='', yLbl='', customLayoutParams=(), gridDims=None, coord=None):
        """Initialize chart parameters.

        title -- optional, string title for chart. Defaults to blank
        xLbl/yLbl -- optional, X and Y Axis axis titles. Defaults to blank
        customLayoutParams -- Custom parameters in format (ParentKey, SubKey, and Value) to customize 'go.layout'
        gridDims -- tuple of two values with the rectangular grid size
        coord -- dictionary with keys ['x', 'y'] with lists of the coordinate location from the top left corner

        """
        super().__init__(title, xLbl, yLbl, customLayoutParams)
        # Plot each point in the grid for plotting values
        width = float(np.max(coord['x']) + np.min(coord['x']))
        height = float(np.max(coord['y']) + np.min(coord['y']))
        self.grid = {'x': [], 'y': []}
        for rIdx in range(gridDims[0]):
            yOffset = height * (gridDims[0] - rIdx)
            yGrid = [yOffset - _y for _y in coord['y']]
            for cIdx in range(gridDims[1]):
                xOffset = width * cIdx
                self.grid['x'].extend([xOffset + _x for _x in coord['x']])
                self.grid['y'].extend(yGrid)
        # Store points used to create the black grid borders
        self.borders = [{
            'x': [cIdx * gridDims[1]] * 2,
            'y': [0, height * gridDims[0]],
        } for cIdx in range(gridDims[1] + 1)] + [{
            'x': [0, width * gridDims[1]],
            'y': [rIdx * height] * 2,
        } for rIdx in range(gridDims[0] + 1)]

    def formatData(self, df, borderOp=0.2, borderLine={'color': 'black'}, markerKwargs={}):
        """Format and return the data for the chart.

        df -- Pandas dataframe with columns names: ['values']
        markerKwargs -- optional keyword arguments to pass to scatterMarker()

        """
        chartData = [
            go.Scatter(
                hoverinfo='none',
                line=borderLine,
                mode='lines',
                opacity=borderOp,
                showlegend=False,
                x=border['x'],
                y=border['y'],
            ) for border in self.borders
        ] + [
            go.Scatter(
                hoverinfo='text',
                mode='markers',
                showlegend=False,
                text=df['values'],
                x=self.grid['x'],
                y=self.grid['y'],
                marker=self.scatterMarker(df, **markerKwargs),
            ),
        ]
        # FIXME: Add text labels for each grid section
        # FIXME: Support case for values that are None (combine to DF, then dropna)
        return chartData

    def scatterMarker(self, df, colorscale='Viridis', size=16, symbol='circle'):
        """Return a dictionary for the scatter plot.

        df -- Pandas dataframe
        colorscale -- plotly colorscale name or list of values (Reds, Bluered, Jet, Viridis, Cividis, etc.)
        size -- marker size
        symbol -- marker symbol (square, circle, circle-open, x, etc.)

        See: https://plot.ly/python/colorscales/

        """
        return {
            'color': df['values'],
            'colorscale': colorscale,
            'showscale': True,
            'size': size,
            'symbol': symbol,
        }

    def createLayout(self):
        """Override the default layout and add additional settings."""
        layout = super().createLayout()
        for axis in ['xaxis', 'yaxis']:
            layout[axis]['showgrid'] = False
            layout[axis]['showticklabels'] = False
            layout[axis]['zeroline'] = False
        layout['yaxis']['scaleanchor'] = 'x'
        layout['yaxis']['scaleratio'] = 1
        return layout