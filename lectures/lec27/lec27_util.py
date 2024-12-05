from lec_utils import *
from ipywidgets import interact

def show_image_and_label(row):
    true_label = row.loc['true']
    pred_label = row.loc['pred']
    X = row.iloc[:-2]

    return show_image(X, true_label, pred_label)

def show_image(row, true_label=None, pred_label=None):
    title = ''
    if true_label:
        title += f'True Label: {true_label}'
        
    if pred_label:
        if title != '':
            title += '<br>'
        title += f'Predicted label: {pred_label}'

    fig = px.imshow(row.to_numpy().reshape((28, 28)), color_continuous_scale='greys', title=title)
    fig.layout.coloraxis.showscale = False
    fig.update_layout(xaxis_visible=False, xaxis_showticklabels=False, yaxis_visible=False, yaxis_showticklabels=False)
    return fig


def show_confusion(y_test, y_pred, normalize=None, title=''):
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred, normalize=normalize)
    # Create the heatmap
    fig = px.imshow(cm, color_continuous_scale='blues', title=title)
    
    # Add text annotations
    annotations = []
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            annotations.append(
                go.Annotation(
                    x=j,
                    y=i,
                    text=f'{round(cm[i, j], 2) if normalize else cm[i, j]}',
                    showarrow=False,
                    font=dict(color='black' if cm[i, j] < cm.max() / 2 else 'white', size=14)
                )
            )
    
    # Update the layout to include annotations
    fig.update_layout(
        annotations=annotations,
        xaxis_title='Predicted label',
        yaxis_title='Actual label',
        width=800,
        height=600
    )
    
    # Update axes tick values
    fig.update_xaxes(tickvals=np.arange(cm.shape[1]))
    fig.update_yaxes(tickvals=np.arange(cm.shape[0]))
    
    # Customize hover template
    fig.update_traces(
        hovertemplate='Predicted: %{x}<br>Actual: %{y}<br>Count: %{z}<extra></extra>'
    )
    
    return fig

def visualize_probs(probs):
    fig = px.bar(x=np.arange(10), y=probs.flatten(), title='Distribution of Predicted Probabilities')
    fig.update_xaxes(title='Class', tickvals=np.arange(10))
    fig.update_yaxes(title='Predicted Probability')
    
    # Find the index of the tallest bar
    max_prob_index = np.argmax(probs.flatten())
    
    # Create a color list with default blue, but orange for the tallest bar
    colors = ['blue'] * 10
    colors[max_prob_index] = 'orange'
    
    # Update bar colors
    fig.update_traces(marker_color=colors)
    
    fig.update_layout(width=800, height=300)
    return fig

def plot_model_coefficients(model_coefficients):
    # Create subplot grid
    fig = make_subplots(rows=2, cols=5, 
                        subplot_titles=[f'Class {i} Coefficients' for i in range(10)])
    
    # Populate subplots
    for i in range(10):
        row = i // 5 + 1
        col = i % 5 + 1
        
        heatmap = go.Heatmap(
            z=model_coefficients[i].reshape((28, 28)), 
            colorscale='RdBu',
            showscale=False
        )
        
        fig.add_trace(heatmap, row=row, col=col)
    
    # Update layout to remove axes
    fig.update_xaxes(showticklabels=False, showgrid=False, zeroline=False)
    fig.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)
    
    # Update layout
    fig.update_layout(
        width=900,
        height=450,
    )
        
    return fig

def show_2_pcs(X_train_approx, y_train, color=False):
    df = pd.DataFrame(X_train_approx).assign(color=y_train.astype(int))
    df = df.sort_values('color', ascending=True)
    df['color'] = df['color'].astype(str)
    fig = px.scatter(x=df.iloc[:, 0], y=df.iloc[:, 1], color=(None if color == False else df['color']),
                     color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(title='PC 2 vs. PC 1 in the MNIST Training Set', 
                      xaxis_title='Principal Component 1', 
                      yaxis_title='Principal Component 2')
    return fig

x = 5