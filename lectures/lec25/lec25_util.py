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

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve
from sklearn.linear_model import LogisticRegression

def predict_thresholded(X_train, y_train, X, T):
    model_logistic_multiple = LogisticRegression()
    model_logistic_multiple.fit(X_train, y_train)
    probs = model_logistic_multiple.predict_proba(X)[:, 1]
    return (probs >= T).astype(int)

def plot_vs_threshold(X_train, y_train, metric):

    fn_dict = {'Precision': precision_score, 'Recall': recall_score, 'Accuracy': accuracy_score, 'F1 Score': f1_score}

    metric_fn = fn_dict[metric]

    thresholds = np.arange(0, 1.005, 0.005)
    values = []
    for t in thresholds:
        preds = predict_thresholded(X_train, y_train, X_train, t)
        value = metric_fn(y_train, preds)
        values.append(value)
        
    fig = px.line(x=thresholds, y=values,
                  title=f'{metric} vs. Threshold',
                  labels={'x': 'Threshold', 'y': f'Training {metric}'})
    
    return fig.update_layout(width=800)

def pr_curve(X_train, y_train):

    precisions = []
    recalls = []

    thresholds = np.arange(0, 1.005, 0.005)
    values = []
    for t in thresholds:
        preds = predict_thresholded(X_train, y_train, X_train, t)
        precision = precision_score(y_train, preds)
        recall = recall_score(y_train, preds)
        precisions.append(precision)
        recalls.append(recall)
        
    fig = px.line(x=recalls, y=precisions, hover_name='Threshold = ' + pd.Series(thresholds).astype(str),
                  title=f'Precision vs. Recall',
                  labels={'x': 'Recall', 'y': f'Precision'})
    
    return fig.update_layout(width=800)


def draw_roc_curve(X_train, y_train):
    model_logistic_multiple = LogisticRegression()
    model_logistic_multiple.fit(X_train, y_train)
    probs = model_logistic_multiple.predict_proba(X_train)[:, 1]

    fprs, tprs, thresholds = roc_curve(y_train.to_numpy(), probs)
        
    fig = px.line(x=fprs, y=tprs, hover_name='Threshold = ' + pd.Series(thresholds).astype(str),
                  title=f'ROC Curve<br>(True Positive Rate vs. False Positive Rate)',
                  labels={'x': 'False Positive Rate', 'y': 'True Positive Rate'})
    
    return fig.update_layout(width=800)

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def show_confusion(X_train, y_train, T):
    fig = ConfusionMatrixDisplay.from_predictions(
        y_train, predict_thresholded(X_train, y_train, X_train, T), cmap='Blues'
    )
    plt.grid(False)
    plt.title(f'Confusion Matrix for Logistic Regression\n with Threshold {T}')

    cm = fig.confusion_matrix

    # Annotate each box with small text
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j+0.4, i+0.25, 
                        ['True Negatives (TN)', 'False Positives (FP)', 'False Negatives (FN)', 'True Positives (TP)'][i*2 + j], 
                        horizontalalignment='right',
                        verticalalignment='top',
                        fontsize=12,  # Small font size
                        color='white' if cm[i, j] > cm.max() / 2 else 'black'  # Adjust text color for readability
            )

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

    fig.update_yaxes(range=(-0.03, 0.03))

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

def lin_sep_1D():
    df = pd.DataFrame().assign(x=[1, 2, 4, 9, 12, 15, 16, 20, 20.5], y=[0] * 5 + [1] * 4)
    df['Glucose'] = df['x'] * 10
    df['Outcome'] = df['y'].astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'})
    return df.plot(kind='scatter', x='Glucose', y=[0] * df.shape[0], color='Outcome', size_max=10, size=[5] * df.shape[0], width=600, height=200, 
                   title='Linearly Separable, d=1',
                   color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},)

def lin_sep_1D_elevated():
    df = pd.DataFrame().assign(x=[1, 2, 4, 9, 12, 15, 16, 20, 20.5], y=[0] * 5 + [1] * 4)
    df['Glucose'] = df['x'] * 10
    df['Outcome'] = df['y'].astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'})
    return df.plot(kind='scatter', x='Glucose', y='y', color='Outcome', size_max=10, size=[5] * df.shape[0], width=800, height=400, 
                   title='Linearly Separable, d=1',
                   color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},)

def non_lin_sep_1D():
    df = pd.DataFrame().assign(Glucose=[1, 2, 20.5, 9, 12, 16, 15, 20, 4], y=[0] * 5 + [1] * 4)
    df['Glucose'] = df['Glucose'] * 10
    df['Outcome'] = df['y'].astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'})
    return df.plot(kind='scatter', x='Glucose', y=[0] * df.shape[0], color='Outcome', size_max=10, size=[5] * df.shape[0], width=800, height=200, 
                   title='NOT Linearly Separable, d=1', color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'})

def bad_example_1D():
    df = pd.DataFrame().assign(Glucose=[1, 2, 20.5, 9, 12, 16, 15, 20, 4], y=[0] * 5 + [1] * 4)
    df['Glucose'] = df['Glucose'] * 10
    df['Outcome'] = df['y'].astype(str).replace({'0': 'no diabetes', '1': 'yes diabetes'})
    return df.plot(kind='scatter', x='Glucose', y='y', color='Outcome', size_max=10, size=[5] * df.shape[0], width=800, height=200, 
                   title='NOT Linearly Separable, d=1', color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'})


def lin_sep_2D():

    # Set random seed for reproducibility
    np.random.seed(42)

    # Generate linearly separable data
    # Class 1: Points clustered around (2, 2)
    class1_x = np.random.normal(2, 0.5, 10)
    class1_y = np.random.normal(2, 0.5, 10)

    # Class 2: Points clustered around (5, 5)
    class2_x = np.random.normal(3.5, 0.5, 10)
    class2_y = np.random.normal(3.5, 0.5, 10)

    # Create DataFrame
    df = pd.DataFrame({
        'x': np.concatenate([class1_x, class2_x]),
        'y': np.concatenate([class1_y, class2_y]),
        'Outcome': ['no diabetes']*10 + ['yes diabetes']*10
    })

    df['x'] = df['x'] * 35
    df['y'] = 20 + df['y'] * 5

    # Create Plotly figure
    fig = px.scatter(df, x='x', y='y', color='Outcome', 
                     title='Linearly Separable, d=2',
                     labels={'x': 'Glucose', 'y': 'BMI'},
                     color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},
                     size_max=10, size=[5] * df.shape[0], width=800)


    return fig

def non_lin_sep_2D():

    # Set random seed for reproducibility
    np.random.seed(42)

    # Generate linearly separable data
    # Class 1: Points clustered around (2, 2)
    class1_x = np.random.normal(2, 1.5, 10)
    class1_y = np.random.normal(2, 1.5, 10)

    # Class 2: Points clustered around (5, 5)
    class2_x = np.random.normal(3.5, 2.5, 10)
    class2_y = np.random.normal(3.5, 2.5, 10)

    # Create DataFrame
    df = pd.DataFrame({
        'x': np.concatenate([class1_x, class2_x]),
        'y': np.concatenate([class1_y, class2_y]),
        'Outcome': ['no diabetes']*10 + ['yes diabetes']*10
    })

    df['x'] = df['x'] * 35
    df['y'] = 20 + df['y'] * 5

    # Create Plotly figure
    fig = px.scatter(df, x='x', y='y', color='Outcome', 
                     title='NOT Linearly Separable, d=2',
                     labels={'x': 'Glucose', 'y': 'BMI'},
                     color_discrete_map={'no diabetes': 'orange', 'yes diabetes': 'blue'},
                     size_max=10, size=[5] * df.shape[0], width=800)


    return fig

def penguin_scatter_3d(penguins):
    return px.scatter_3d(penguins, 
                x='bill_length_mm', 
                y='body_mass_g', 
                z='bill_depth_mm',
                color='species', 
                title='Bill Depth vs. Bill Length and Body Mass',
                width=800, height=600)

def penguin_scatter_2d(penguins):
    return px.scatter(penguins, 
                x='bill_length_mm', 
                y='body_mass_g', 
                color='species', 
                title='Body Mass vs. Bill Length',
                width=900, height=500,
                size_max=10,
                size=[5] * penguins.shape[0])

def penguin_decision_boundary(model, X_train, y_train, title=''):
    from sklearn.inspection import DecisionBoundaryDisplay

    import matplotlib.colors
    cmap = matplotlib.colors.ListedColormap(["blue", "orange", "green"])

    disp = DecisionBoundaryDisplay.from_estimator(
        model, X_train, response_method='predict', cmap=cmap, grid_resolution=400,
        alpha=0.5,
    )
    disp.ax_.scatter(X_train.loc[y_train == 'Adelie', 'bill_length_mm'], X_train.loc[y_train == 'Adelie', 'body_mass_g'], color='blue', s=25, label='Adelie');
    disp.ax_.scatter(X_train.loc[y_train == 'Chinstrap', 'bill_length_mm'], X_train.loc[y_train == 'Chinstrap', 'body_mass_g'], color='orange', s=25, label='Chinstrap');
    disp.ax_.scatter(X_train.loc[y_train == 'Gentoo', 'bill_length_mm'], X_train.loc[y_train == 'Gentoo', 'body_mass_g'], color='green', s=25, label='Gentoo');
    plt.title(title, fontsize=20)
    plt.xlabel("Bill Length")
    plt.ylabel("Body Mass")
    plt.legend();