from lec_utils import *
from ipywidgets import interact

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

def show_one_feature_plot(X_train, y_train):
    fig = px.scatter(X_train.assign(Diabetes=y_train, 
                          Outcome=y_train.astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'})),
           x='Glucose',
           y='Diabetes',
           color='Outcome',
           color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},
           width=800)
    return fig

from sklearn.linear_model import LinearRegression

def show_one_feature_plot_with_linear_model(X_train, y_train):
    model_simple = LinearRegression()
    model_simple.fit(X_train[['Glucose']], y_train)
    
    x = np.linspace(35, 225)
    y = model_simple.intercept_ + model_simple.coef_[0] * x

    fig = show_one_feature_plot(X_train, y_train)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        name='Linear Model',
        line=dict(color='#097054', width=4)
    ))
    
    return fig

def show_one_feature_plot_with_linear_model_clipped(X_train, y_train):
    model_simple = LinearRegression()
    model_simple.fit(X_train[['Glucose']], y_train)
    
    x = np.linspace(35, 225)
    y = model_simple.intercept_ + model_simple.coef_[0] * x
    y = np.clip(y, 0, 1)

    fig = show_one_feature_plot(X_train, y_train)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        name='Clipped Linear Model',
        line=dict(color='#097054', width=4)
    ))
    
    return fig

from sklearn.linear_model import LogisticRegression

def show_one_feature_plot_with_logistic(X_train, y_train):
    model_logistic = LogisticRegression()
    model_logistic.fit(X_train[['Glucose']].to_numpy(), y_train)

    x = np.linspace(0, 250)
    y = model_logistic.predict_proba(x.reshape(-1, 1))[:, 1]

    fig = show_one_feature_plot(X_train, y_train)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        name='Logistic Regression Model',
        line=dict(color='#097054', width=4)
    ))
    
    return fig

def show_one_feature_plot_with_logistic_and_y_threshold(X_train, y_train, T):
    model_logistic = LogisticRegression()
    model_logistic.fit(X_train[['Glucose']].to_numpy(), y_train)

    x = np.linspace(0, 250)
    y = model_logistic.predict_proba(x.reshape(-1, 1))[:, 1]

    fig = show_one_feature_plot(X_train, y_train)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        name='Logistic Regression Model',
        line=dict(color='#097054', width=4)
    ))

    fig.add_trace(go.Scatter(
        x=[x[0] - 15, x[-1] + 15],
        y=[T, T],
        name=f'Threshold of T = {T}',
        line=dict(color='purple', width=4)
    ))

    fig.update_xaxes(range=(x[0], x[-1]))
    
    return fig

def show_one_feature_plot_with_logistic_and_x_threshold(X_train, y_train, T):
    model_logistic = LogisticRegression()
    model_logistic.fit(X_train[['Glucose']].to_numpy(), y_train)

    x = np.linspace(0, 250)
    y = model_logistic.predict_proba(x.reshape(-1, 1))[:, 1]

    fig = show_one_feature_plot(X_train, y_train)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        name='Logistic Regression Model',
        line=dict(color='#097054', width=4)
    ))

    w0, w1 = model_logistic.intercept_[0], model_logistic.coef_[0][0]

    T_ops = (np.log(T / (1 - T)) - w0) / w1

    fig.add_trace(go.Scatter(
        x=[T_ops, T_ops],
        y=[0, 1],
        name=f'Threshold of T = {T}',
        line=dict(color='purple', width=4)
    ))

    fig.update_xaxes(range=(x[0], x[-1]))
    
    return fig

def show_one_feature_plot_in_1D(X_train, y_train, thres=True):

    fig = px.scatter(X_train.assign(Diabetes=y_train, 
                          Outcome=y_train.astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'})),
           x='Glucose',
           y=[0] * X_train.shape[0],
           color='Outcome',
           color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},
           size_max=10,
           size=[5] * X_train.shape[0],
           width=1000)
    
    if thres:
        fig.add_trace(go.Scatter(
            x=[139.17, 139.17],
            y=[-0.1, 0.1],
            name=f'Threshold of Glucose = 139.17',
            line=(dict(color='purple', width=4))
        ))

    fig.update_yaxes(range=(-0.03, 0.03))

    fig.add_annotation(
        x=170,
        y=0.015,
        text="<span style='color:blue'>classified as <b>diabetes</b> ➡️</span>",
        showarrow=False
    )

    fig.add_annotation(
        x=100,
        y=0.015,
        text="<span style='color:orange'>⬅️ classified as <b>no diabetes</b></span>",
        showarrow=False
    )

    return fig

def make_prop_plot(X_train, y_train):
    col = 'Glucose'
    vals = X_train[col]
    bins = np.linspace(vals.min() - 3, vals.max() + 3, 12)
    fig = (
        pd.cut(X_train[col], bins)
        .to_frame()
        .assign(Outcome=y_train)
        .groupby(col, observed=True)
        .agg(['mean', 'size'])
        .reset_index()
        .pipe(lambda df: df.assign(left=df[col].apply(lambda x: int(x.left))))
        .pipe(lambda df: px.scatter(
            x=df['left'], y=df['Outcome']['mean'], size=np.ones(df.shape[0]) * 3, size_max=12,
#             color=df['Outcome']['mean']
        ))
    #     .plot(kind='scatter', x='left', y='mean')
        .update_xaxes(range=(vals.min() - 40, vals.max() + 20))
        .update_layout(width=800, 
                       xaxis_title='Glucose', 
                       yaxis_title='Proportion of Individuals with Diabetes',
                       coloraxis_showscale=False)
    )
    
    return fig

def plot_sigmoid(w0, w1):
    xs = np.linspace(-10, 10, 10000)
    inps = w0 + w1 * xs
    ys = 1 / (1 + np.e ** (-inps))
    
    title = r'$y = \sigma(' + (f'{w0}' if w0 != 0 else '') + ('+' if w1 >= 0 else '-') + (f'{np.abs(w1)}x' if w1 != 1 else 'x') + r')$'
    title = fr'w0 = {w0}, w1 = {w1}'

    fig = px.line(x=xs, y=ys, title=title)
    fig.update_traces(line=dict(width=4))
    
    return fig

def show_three_sigmoids():
    fig1 = plot_sigmoid(w0=0, w1=1)
    fig2 = plot_sigmoid(w0=15, w1=5)
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
    

def show_logistic_mse_surface(X_train, y_train):

    def sigma(t):
        return 1 / (1 + np.e ** (-t))

    def mse(y_actual, y_pred):
        return np.mean((y_actual - y_pred)**2)

    def mse_for_logistic_model(w):
        w0, w1 = w
        return mse(y_train, sigma(w0 + w1 * X_train['Glucose']))

    num_points = 50 # increase for better resolution, but it will run more slowly. 

    # if (num_points <= 100):

    uvalues = np.linspace(-10, 2, num_points)
    vvalues = np.linspace(-0.05, 0.1, num_points)
    (u,v) = np.meshgrid(uvalues, vvalues)
    thetas = np.vstack((u.flatten(),v.flatten()))

    MSE = np.array([mse_for_logistic_model(t) for t in thetas.T])

    loss_surface = go.Surface(x=u, y=v, z=np.reshape(MSE, u.shape), showscale=False)

    # minimizer = go.Scatter3d(x=[w0_star], y=[w1_star], z=[mse_for_departure_model([w0_star, w1_star])], 
    #                          mode='markers', name='optimal parameters',
    #                          marker=dict(size=10, color='gold'))

    fig = go.Figure(data=[loss_surface])
    # fig.add_trace(opt_point)

    fig.update_layout(title='Mean Squared Error Loss Surface<br>for Logistic Regression', scene = dict(
        xaxis_title = "w0",
        yaxis_title = "w1",
        zaxis_title = r"R(w0, w1)"),
        width=600, height=600)
    
    return fig

def show_logistic_ce_surface(X_train, y_train, reg_lambda = 0):

    def sigma(t):
        return 1 / (1 + np.e ** (-t))

    def mce(y_actual, y_pred):
        return -np.mean(
            y_actual * np.log(y_pred) + (1 - y_actual) * np.log(1 - y_pred)
        )

    def mce_for_logistic_model(w):
        w0, w1 = w
        return mce(y_train, sigma(w0 + w1 * X_train['Glucose'])) + reg_lambda * (w0 ** 2 + w1 ** 2)

    num_points = 50 # increase for better resolution, but it will run more slowly. 

    # if (num_points <= 100):

    uvalues = np.linspace(-20, 15, num_points)
    vvalues = np.linspace(-0.05, 0.1, num_points)
    (u,v) = np.meshgrid(uvalues, vvalues)
    thetas = np.vstack((u.flatten(),v.flatten()))

    MSE = np.array([mce_for_logistic_model(t) for t in thetas.T])

    loss_surface = go.Surface(x=u, y=v, z=np.reshape(MSE, u.shape), showscale=False)

    # minimizer = go.Scatter3d(x=[w0_star], y=[w1_star], z=[mse_for_departure_model([w0_star, w1_star])], 
    #                          mode='markers', name='optimal parameters',
    #                          marker=dict(size=10, color='gold'))

    fig = go.Figure(data=[loss_surface])
    # fig.add_trace(opt_point)

    title = 'Mean Cross-Entropy Loss Surface<br>for Logistic Regression'
    if reg_lambda != 0:
        title += f'<br>L2 Regularized with Lambda = {reg_lambda}'

    fig.update_layout(title=title, scene = dict(
        xaxis_title = "w0",
        yaxis_title = "w1",
        zaxis_title = r"R(w0, w1)"),
        width=600, height=600)
    
    return fig

def make_two_feature_scatter(X_train, y_train):
    fig = (
        X_train.assign(Outcome=y_train.astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'}))
                .plot(kind='scatter', x='Glucose', y='BMI', color='Outcome', 
                    color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},
                    title='Relationship between Glucose, BMI, and Diabetes')
                .update_layout(width=800)
    )
    return fig

def show_squared_loss_individual():
    ps = np.linspace(0, 1)
    fs = (1 - ps) ** 2

    fig = px.line(x=ps, y=fs)
    fig.update_layout(xaxis_title='$p_i$', yaxis_title='$(1 - p_i)^2$',
                     title='Squared loss is bounded to (0, 1) when predicting probabilities!')
    
    return fig

def show_ce_loss_individual_1():
    ps = np.linspace(0, 1, 1000)
    fs = -np.log(ps)

    fig = px.line(x=ps, y=fs)
    fig.update_layout(xaxis_title='$p_i$', yaxis_title='$- \log p_i$',
                     title='Cross Entropy Loss when yi = 1')
    
    return fig

def show_ce_loss_individual_0():
    ps = np.linspace(0, 1, 1000)
    fs = -np.log(1 - ps)

    fig = px.line(x=ps, y=fs)
    fig.update_layout(xaxis_title='$p_i$', yaxis_title='$- \log (1 - p_i)$',
                     title='Cross Entropy Loss when yi = 0')
    
    return fig