from lec_utils import *
from ipywidgets import interact

from IPython.display import Markdown

def display_poly(coefs, precision=2):
    from IPython.display import Markdown
    
    out = '$$'
    not_first_flag = False
    for exp, coef in enumerate(coefs):
        format_coef = f"{abs(coef):.{precision}f}"
        if exp == 0 and not np.isclose(coef, 0):
            out += format_coef
            not_first_flag = True
        else:
            if coef < 0:
                sign = '-'
            elif coef > 0:
                if not_first_flag:
                    sign = '+'
                else:
                    sign = ''
            if not np.isclose(coef, 0):
                out += sign + format_coef + 'x' + ('^{' + str(exp) + '}' if exp != 1 else '')
                not_first_flag = True
        
    display(Markdown(out + '$$'))

def display_features(poly_model, precision=2):
    display_poly(np.append(
    poly_model.intercept_,
    poly_model.coef_
), precision=precision)
    

def display_commute_coefs(best_estimator):
    names = np.append(
        'intercept', 
        best_estimator[:-1].get_feature_names_out())
    
    coefs = np.append(
        best_estimator[-1].intercept_,
        best_estimator[-1].coef_
    )
    
    assert len(names) == len(coefs), 'length of names != length of coefs'
    
    frame = pd.DataFrame().assign(feature=names, coef=coefs).set_index('feature')
    
    return frame

def f(w):
    return 5 * (w**4) - (w**3) - 5 * (w**2) + 2 * w - 9

def df(w):
    return 20 * (w**3) - 3 * (w**2) - 10 * w + 2

def create_tangent_line(w):
    slope = df(w)
    intercept = f(w) - slope * w
    return lambda w: intercept + slope * w

def draw_f():
    ws = np.linspace(-1.25, 1.25, 1000)
    ys = f(ws)

    fig = px.line(x=ws, y=ys)
    fig.update_layout(xaxis_title='$w$', 
                  yaxis_title='$f(w)$', 
                  title='$f(w) = 5w^4 - w^3 - 5w^2 + 2w - 9$',
                  width=1000, height=700)
    
    return fig
    
def show_tangent(w0):
    fig = draw_f()
    tan_fn = create_tangent_line(w0)
    fig2 = go.Figure(fig.data)
    fig2.add_trace(go.Scatter(x=[w0], y=[f(w0)], marker={'color': 'red', 'size': 20}, showlegend=False))
    fig2.add_trace(go.Scatter(x=[-5, 5], y=[tan_fn(-5), tan_fn(5)], line={'color': 'red'}, name='Tangent Line'))
    fig2.update_xaxes(range=[-1.25, 1.25]).update_yaxes(range=[-12, -4])
    fig2.update_layout(title=f'Tangent line to f(w) at w = {round(w0, 2)}<br>Slope of tangent line: {round(df(w0), 5)}', 
                       xaxis_title=r'$w$', 
                       yaxis_title=r'$f(w) = 5w^4 - w^3 - 5w^2 + 2w - 9$', 
                       showlegend=False)
    return fig2.update_layout(width=1000, height=700)

def minimizing_animation(w0, alpha):

    play_button = {'label': '▶️ Start animation', 'method': 'animate', 'args': [None]}

    stop_button = dict(label='⏯️ Stop animation', method='animate', visible = True,
                args=[(), {'frame': {'duration': 0, 'redraw': False}, 'mode': 'next', 'fromcurrent': True}])

    w = w0
    ws = []
    dfws = []
    for i in range(50):
        ws.append(w)
        dfws.append(df(w))
        w = w - alpha * df(w)

    fig = draw_f()
        
    grad_anim = go.Figure(
        data=[fig.data[0], go.Scatter(x=[ws[0]], y=[f(ws[0])], marker={'size': 20}, showlegend=False)],
        frames=[
            go.Frame(data=[fig.data[0], go.Scatter(x=[ws[i]], y=[f(ws[i])], marker={'size': 20}, showlegend=False)])
            for i in range(50)
        ],
        layout=go.Layout(updatemenus=[dict(
            type="buttons",
            buttons=[play_button, stop_button])],
             title=f'Gradient Descent<br>Initial Guess = {w0}&nbsp;&nbsp;&nbsp;&nbsp;Step Size = {alpha}'))
    

    grad_anim.update_layout(width=1000, height=700)
    
    return grad_anim