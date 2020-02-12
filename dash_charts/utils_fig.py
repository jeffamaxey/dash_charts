"""Utilities for custom Dash figures."""

import dash_core_components as dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
from plotly.subplots import make_subplots

# TODO: Methods for convert df to json > dump to UI / load from UI > convert to DF
# TODO: Methods for making charts/callbacks that update when data changes in a SQL database


def min_graph(**kwargs):
    """Return dcc.Graph element with Plotly overlay removed.

    See: https://community.plot.ly/t/is-it-possible-to-hide-the-floating-toolbar/4911/7

    Args:
        kwargs: any kwargs to pass to the dash initializer other than `assets_folder`

    Returns:
        Dash `dcc.Graph` object

    """
    return dcc.Graph(config={'displayModeBar': False}, **kwargs)


def format_callback(lookup, outputs, inputs, states):
    """Format list of [Output, Input, State] for `@app.callback()`.

    Args:
        lookup: dict with generic key that maps to unique string
        outputs: list of tuples with id and key
        inputs: list of tuples with id and key
        states: list of tuples with id and key

    Returns:
        list of lists for `@app.callback()`

    """
    return ([Output(lookup[_id], key) for _id, key in outputs],
            [Input(lookup[_id], key) for _id, key in inputs],
            [State(lookup[_id], key) for _id, key in states])


def map_args(raw_args, inputs, states):
    """Map the function arguments into a dictionary with keys for the unique input and state names.

    Args:
        raw_args: list of arguments passed to callback
        inputs: list of unique input element ids
        states: list of unique state element ids

    Returns:
        Returns dictionary with arguments mapped to the unique ids

    """
    input_args = raw_args[:len(inputs)]
    state_args = raw_args[len(inputs):]

    results = {}
    for keys, args in ((inputs, input_args), (states, state_args)):
        for arg_idx, uniq_id, key in enumerate(keys):
            results[uniq_id].update([key, args[arg_idx]])
    return results


class CustomChart:
    """Base Class for Custom Charts."""

    axis_range = {}  # If None or empty dict, will enable autorange. Add X/Y keys to set range

    def __init__(self, title, x_label, y_label, cust_layout_params=()):
        """Initialize Custom Dash Chart and store parameters as data members.

        Args:
            title: String title for chart  (can be an empty string for blank)
            x_label: XAxis string label (can be an empty string for blank)
            y_label: YAxis string label (can be an empty string for blank)
            cust_layout_params: Custom parameters in format [ParentKey, SubKey, Value] to customize 'go.layout'

        """
        self.title = title
        self.labels = {'x': x_label, 'y': y_label}
        self.cust_layout_params = cust_layout_params

    def create_figure(self, raw_df, **kwargs_data):
        """Create the figure dictionary.

        Args:
            raw_df: data to pass to formatter method
            kwargs_data: keyword arguments to pass to the data formatter method

        Returns:
            Dictionary with keys `data` and `layout` for Dash

        """
        return {
            'data': self.create_traces(raw_df, **kwargs_data),
            'layout': go.Layout(self.apply_cust_layout(self.create_layout())),
        }

    def create_traces(self, raw_df, **kwargs_data):
        """Return traces for plotly chart.

        Args:
            raw_df: data to pass to formatter method
            kwargs_data: keyword arguments to pass to the data formatter method

        Raises:
            NotImplementedError: Must be overridden by child class

        """
        raise NotImplementedError('create_traces must be implemented by child class')

    def create_layout(self):
        """Return the standard layout. Can be overridden and modified when inherited.

        Returns:
            dict: layout for Dash figure

        """
        layout = {
            'title': go.layout.Title(text=self.title),
            'xaxis': {
                'automargin': True,
                'title': self.labels['x'],
            },
            'yaxis': {
                'automargin': True,
                'title': self.labels['y'],
                'zeroline': True,
            },
            'legend': {'orientation': 'h'},
            'hovermode': 'closest',
        }

        # Optionally apply the specified range
        for axis in ['x', 'y']:
            axis_name = f'{axis}axis'
            if axis in self.axis_range:
                layout[axis_name]['range'] = self.axis_range[axis]
            else:
                layout[axis_name]['autorange'] = True

        return layout

    def apply_cust_layout(self, layout):
        """Extend and/or override layout with custom settings.

        Args:
            layout: base layout dictionary. Typically from self.create_layout()

        Returns:
            dict: layout for Dash figure

        """
        for parent_key, sub_key, value in self.cust_layout_params:
            if sub_key is not None:
                layout[parent_key][sub_key] = value
            else:
                layout[parent_key] = value

        return layout


class MarginalChart(CustomChart):
    """Base Class for Custom Charts with Marginal X and Marginal Y Plots."""

    def create_figure(self, raw_df, **kwargs_data):
        """Create the figure dictionary.

        Args:
            raw_df: data to pass to formatter method
            kwargs_data: keyword arguments to pass to the data formatter method

        Returns:
            Dash figure object

        """
        # Initialize figure with subplots
        fig = make_subplots(
            rows=2, cols=2,
            shared_xaxes=True, shared_yaxes=True,
            vertical_spacing=0.02, horizontal_spacing=0.02,
            row_width=[0.8, 0.2], column_width=[0.8, 0.2],
        )
        # Populate the traces of each subplot
        traces = [
            (self.create_traces, 2, 1),
            (self.create_marg_top, 1, 1),
            (self.create_marg_right, 2, 2),
        ]
        for (trace_func, row, col) in traces:
            for trace in trace_func(raw_df, **kwargs_data):
                fig.add_trace(trace, row, col)
        # Apply axis labels
        fig.update_xaxes(title_text=self.labels['x'], row=2, col=1)
        fig.update_yaxes(title_text=self.labels['y'], row=2, col=1)
        # Replace the default blue/white grid introduced in Plotly v4
        fig.update_xaxes(showgrid=True, gridcolor='white')
        fig.update_yaxes(showgrid=True, gridcolor='white')
        fig['layout'].update(self.apply_cust_layout(self.create_layout()))
        return fig

    def create_traces(self, raw_df, **kwargs_data):
        """Return traces for the main plotly chart.

        Args:
            raw_df: data to pass to formatter method
            kwargs_data: keyword arguments to pass to the data formatter method

        Returns:
            list: trace data points. Must be overridden by child class or will otherwise be empty

        """
        return []

    def create_marg_top(self, raw_df, **kwargs_data):
        """Return traces for the top marginal chart.

        Args:
            raw_df: data to pass to formatter method
            kwargs_data: keyword arguments to pass to the data formatter method

        Returns:
            list: trace data points. Must be overridden by child class or will otherwise be empty

        """
        return []

    def create_marg_right(self, raw_df, **kwargs_data):
        """Return traces for the right marginal chart.

        Args:
            raw_df: data to pass to formatter method
            kwargs_data: keyword arguments to pass to the data formatter method

        Returns:
            list: trace data points. Must be overridden by child class or will otherwise be empty

        """
        return []

    def create_layout(self):
        """Remove axis lables from base layout as they would be applied to (row=1,col=1).

        Returns:
            dict: updated layout for Dash figure

        """
        layout = super().create_layout()
        layout['xaxis']['title'] = ''
        layout['yaxis']['title'] = ''
        layout['plot_bgcolor'] = '#F0F0F0'
        return layout