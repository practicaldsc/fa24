from lec_utils import *
from ipywidgets import interact

# Gradient descent part ---
def make_scatter(df):

    fig = px.scatter(df,
               x='departure_hour',
               y='minutes',
               size=np.ones(len(df)) * 50,
               size_max=8)
    fig.update_xaxes(title='Home Departure Time (AM)')
    fig.update_yaxes(title='Minutes')
    fig.update_layout(title='Commuting Time vs. Home Departure Time')
    fig.update_layout(width=700)
    
    return fig

### Classification part ---

def show_decision_boundary(model, X_train, y_train, title=''):
    from sklearn.inspection import DecisionBoundaryDisplay

    import matplotlib.colors
    cmap = matplotlib.colors.ListedColormap(["orange", "blue"])

    disp = DecisionBoundaryDisplay.from_estimator(
        model, X_train, response_method='predict', cmap=cmap, grid_resolution=400,
        alpha=0.5,
    )
    disp.ax_.scatter(X_train.loc[y_train == 0, 'Glucose'], X_train.loc[y_train == 0, 'BMI'], color='orange', s=25, label='no diabetes');
    disp.ax_.scatter(X_train.loc[y_train == 1, 'Glucose'], X_train.loc[y_train == 1, 'BMI'], color='blue', s=25, label
    ='diabetes');
    plt.title(title, fontsize=20)
    plt.legend();

def visualize_k(k, X_train, y_train):
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    show_decision_boundary(model, X_train, y_train)
    plt.title(f'Decision Boundary when $k={k}$')

def visualize_depth(depth, X_train, y_train):
    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier(max_depth=depth)
    model.fit(X_train, y_train)
    show_decision_boundary(model, X_train, y_train)
    plt.title(f'Decision Boundary for a Tree of Depth {depth}')

def plot_sigmoid(w0, w1):
    xs = np.linspace(-10, 10)
    inps = w0 + w1 * xs
    ys = 1 / (1 + np.e ** (-inps))
    
    title = r'$y = \sigma(' + (f'{w0} +' if w0 != 0 else '') +  (f'{w1}x' if w1 != 1 else 'x') + r')$'

    fig = px.line(x=xs, y=ys, title=title)
    
    return fig

def show_three_sigmoids():
    fig1 = plot_sigmoid(w0=0, w1=1)
    fig2 = plot_sigmoid(w0=-15, w1=5)
    fig3 = plot_sigmoid(w0=-0.5, w1=-0.4)

    combined_fig = make_subplots(rows=1, cols=3,
                                 subplot_titles = [figi.layout.title['text'] for figi in [fig1, fig2, fig3]])

    combined_fig.add_trace(fig1.data[0], row=1, col=1)
    combined_fig.add_trace(fig2.data[0], row=1, col=2)
    combined_fig.add_trace(fig3.data[0], row=1, col=3)

    combined_fig.update_layout(width=1200)
    
    return combined_fig

def show_logistic(model_logistic, X_train, y_train, t=0.5, show_training=False, show_threshold=False):
    num_points = 50
    glucoses = np.linspace(0, 210, num_points)
    bmis = np.linspace(0, 80, num_points)
    (gridX, gridY) = np.meshgrid(glucoses, bmis)

    # Reshape grid for predict_proba
    grid = np.column_stack((gridX.ravel(), gridY.ravel()))
    grid = pd.DataFrame(grid, columns=['Glucose', 'BMI'])
    Z = model_logistic.predict_proba(grid)[:, 1].reshape(gridX.shape)

    surface = go.Surface(x=gridX, y=gridY, z=Z, colorscale='Blues', name='Predicted Probabilities', showscale=False)

    data = go.Scatter3d(x=X_train['Glucose'], y=X_train['BMI'], z=y_train, 
                        mode='markers', marker={'size': 5, 'color': 'black'},
                        name='Training Data')
    
    threshold = go.Surface(x=gridX, y=gridY, z=Z * 0 + t, colorscale='greens', showscale=False)
    
    figs = [surface]
    
    if show_training:
        figs.append(data)

    if show_threshold:
        figs.append(threshold)
        
    fig = go.Figure(figs)
        
    fig.update_layout(title=f'Predicted Probability of Diabetes Given Glucose and BMI' + (f'<br>Threshold = {t}' if t != 0.5 else ''), 
                      width=1000, height=800, scene = dict(
        xaxis_title = "Glucose",
        yaxis_title = "BMI",
        zaxis_title = "Probability"), showlegend=True)
    
    return fig
    