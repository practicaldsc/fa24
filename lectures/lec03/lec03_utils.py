import plotly.graph_objects as go
import numpy as np

def show_projection_plot():

    # Define vectors
    u = np.array([1, 0, 0])
    v = np.array([0, 1, 1])
    proj = np.array([4, 5, 5])
    y = np.array([4, 2, 8])
    e = y - proj

    # Create a meshgrid for the plane
    xx, yy = np.meshgrid(np.linspace(-2, 10, 12), np.linspace(-2, 10, 12))

    # Calculate z values for the plane spanned by u and v
    zz = yy

    # Create traces for vectors
    def create_vector_trace(vector, name, color, start=[0, 0, 0], visible=True):
        return go.Scatter3d(x=[start[0], start[0] + vector[0]], y=[start[1], start[1] + vector[1]], z=[start[2], start[2] + vector[2]],
                            mode='lines+text',
                            name=name,
                            line=dict(color=color, width=7),
                            text=['', name],
                            textposition='top center' if 'e' not in name else 'bottom right',
                            textfont=dict(size=15, color=color),
                            visible=visible)

    vector_trace_u = create_vector_trace(u, r'u = [1, 0, 0]', 'blue')
    vector_trace_v = create_vector_trace(v, 'v = [0, 1, 1]', 'blue')
    vector_trace_proj = create_vector_trace(proj, 'proj = [4, 5, 5]', 'purple', visible='legendonly')
    vector_trace_y = create_vector_trace(y, 'y = [4, 2, 8]', 'orange', visible='legendonly')
    vector_trace_e = create_vector_trace(e, 'e = [0, -3, 3]', 'red', start=proj, visible='legendonly')

    # Create the surface plot for the plane
    plane_trace = go.Surface(x=xx, y=yy, z=zz, name='Span of u and v', 
                             colorscale='blues', showscale=False, opacity=0.5)

    # Create the layout
    layout = go.Layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='data',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1)
            )
        ),
        width=1000, height=800,
        title='The projection of y onto span(u, v)'
    )

    # Create the figure and add traces
    fig = go.Figure(data=[vector_trace_u, vector_trace_v, vector_trace_y, vector_trace_proj, vector_trace_e, plane_trace], layout=layout)

    # Show the plot
    return fig