from IPython.display import display, Markdown, HTML

def dfs_side_by_side(dfs, titles):
    """
    Displays two or more dataframes side by side with titles above each.
    """
    display(
        HTML(
            f"""
        <div style="display: flex; gap: 2rem;">
        {'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'.join(f'<div><h4>{titles[i]}</h4>{dfs[i].to_html()}</div>' for i in range(len(dfs)))}
        </div>
    """
        )
    )

def visualize_k_fold(data, k, shuffle=True, show_full=False):
    
    if shuffle:
        np.random.seed(23)
        data = data.sample(frac=1)
        
    if show_full:
        display(Markdown(f'### Full Dataset <small>({len(data)} rows)</small>'))
        display(data)
        display(Markdown('<hr>'))
    
    n = data.shape[0]

    fold_size = n // k

    for i in range(k):
        # Pick the ith set of fold_size rows to be the validation "slice".
        validation_rows = range(i * fold_size, (i + 1) * fold_size)

        # Pick the other (n - fold_size) rows to be the train "slice".
        # Note that there is no overlap, in a particular fold,
        # between train_rows and validation_rows.
        train_rows = list(set(range(n)).difference(set(validation_rows)))

        display(Markdown(f'### Fold {i + 1}'))
        dfs_side_by_side([data.iloc[train_rows], data.iloc[validation_rows]], 
                         [f'<span style="color:blue">Training</span> <small>({len(train_rows)} rows)</small>', 
                          f'<span style="color:green">Validation</span> <small>({len(validation_rows)} rows)</small>'])
        display(Markdown('<hr>'))
        
    visualize_k_fold(data, k=4, shuffle=True)
