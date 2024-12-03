from lec_utils import *
from ipywidgets import interact

x = np.array([1, 2, 3, 4, 8, 9, 10, 9, 10])
y = np.array([7, 10, 6, 8, 3, 5, 4, 9.5, 10])

# Run this cell.
def show_ratings():
    fig = px.scatter(x=x, y=y, size_max=20, size=[10] * 9)
    fig.update_xaxes(title='Rating for Modern Family')
    fig.update_yaxes(title='Rating for Stranger Things')
    fig.update_layout(width=400, height=400)
    return fig

def visualize_centroids(centroids, show_color=True, assignments=None, lines=False, title=None):
    """
    Visualize k-means clustering with centroids and colored data points.
    
    Parameters:
    x (np.array): X-coordinates of data points
    y (np.array): Y-coordinates of data points
    centroids (list): List of (x, y) centroid coordinates
    
    Returns:
    plotly.graph_objs.Figure: Interactive scatter plot with centroids and clustered points
    """
    # Color palette for centroids and clusters
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan']
    
    # Create a scatter plot of original points
    fig = go.Figure()
    
    # Assign each point to the nearest centroid
    data_points = np.column_stack((x, y))
    centroid_colors = {}
    point_assignments = []
    
    if not assignments:
        for point in data_points:
            # Find closest centroid
            distances = [np.linalg.norm(point - cent) for cent in centroids]
            closest_cent_index = np.argmin(distances)
            point_assignments.append(closest_cent_index)
        
    else:
        point_assignments = assignments
    
    # Plot data points with centroid colors
    for i, (cent_x, cent_y) in enumerate(centroids):
        # Filter points assigned to this centroid
        mask = np.array(point_assignments) == i
        cluster_x = x[mask]
        cluster_y = y[mask]
        
        # Use a lighter version of the centroid color
        color = colors[i % len(colors)]
        light_color = f"light{color}"
        
        # Add cluster points with light color and transparency
        fig.add_trace(go.Scatter(
            x=cluster_x, 
            y=cluster_y, 
            mode='markers',
            marker=dict(color=(color if show_color else 'black'), size=25, opacity=0.5),
            name=f'Cluster {i+1} Points'
        ))

        if lines:
            # Add lines from centroid to each point in the cluster
            for point_x, point_y in zip(cluster_x, cluster_y):
                # Calculate distances
                dist = np.linalg.norm(np.array([point_x, point_y]) - np.array([cent_x, cent_y]))
                dist_squared = dist ** 2

                dist_squared = (int(dist_squared) if np.isclose(int(dist_squared), dist_squared) else round(dist_squared, 2))
                
                # Line from centroid to point
                fig.add_trace(go.Scatter(
                    x=[cent_x, point_x], 
                    y=[cent_y, point_y], 
                    mode='lines',
                    line=dict(color=color, width=1, dash='dot'),
                    showlegend=False
                ))
                
                # Annotate midpoint with distance
                # mid_x = (cent_x + point_x) / 2
                # mid_y = (cent_y + point_y) / 2
                # fig.add_trace(go.Scatter(
                #     x=[mid_x], 
                #     y=[mid_y], 
                #     mode='text',
                #     text=[f'Dist² = {round(dist_squared, 2)}'],
                #     textfont=dict(size=15, color=color),
                #     showlegend=False
                # ))

                # Annotation at 0.6 position along line with angle
                mid_x = cent_x + 0.6 * (point_x - cent_x)
                mid_y = cent_y + 0.6 * (point_y - cent_y)
    
                fig.add_annotation(
                    x=mid_x+0.2,
                    y=mid_y,
                    text=f'Dist² = <b>{dist_squared}</b>',
                    showarrow=False,
                    font=dict(size=12, color=color),
                    textangle=np.degrees(np.arctan2(np.abs(point_y - cent_y), np.abs(point_x - cent_x)))
                )
                
                # fig.add_trace(go.Scatter(
                #     x=[mid_x], 
                #     y=[mid_y], 
                #     mode='text',
                #     text=[f'{dist_squared}'],
                #     textfont=dict(size=10, color=color),
                #     # angle=np.degrees(np.arctan2(point_y - cent_y, point_x - cent_x)),
                #     showlegend=False
                # ))
    
    # Plot centroids with full color and larger size
    for i, (cent_x, cent_y) in enumerate(centroids):
        color = colors[i % len(colors)]
        fig.add_trace(go.Scatter(
            x=[cent_x], 
            y=[cent_y], 
            mode='markers',
            marker=dict(color=color, size=30, symbol='star'),
            name=f'Centroid {i+1}'
        ))

    k = len(centroids)
    if title is None:
        title = f'Clusters for {k} centroids:<br>{", ".join([str(cent) for cent in centroids])}'
    
    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title='Rating for Modern Family',
        yaxis_title='Rating for Stranger Things',
        width=800,
        height=600,
        showlegend=False
    )
    
    return fig

def show_elbow():
    x = np.array([1, 2, 3, 4, 8, 9, 10, 9, 10])
    y = np.array([7, 10, 6, 8, 3, 5, 4, 9.5, 10])

    # By default, it uses k = 8!
    from sklearn.cluster import KMeans

    inertias = []
    for k in range(1, 10):
        model = KMeans(n_clusters=k)
        model.fit(np.vstack([x, y]).T)
        inertias.append(model.inertia_)

    fig = px.line(x=range(1, 10), y=inertias, title='Inertia vs. k in<br>k-means clustering of ratings data', markers=True)
    fig.update_layout(xaxis_title='k (number of clusters)', yaxis_title='Inertia', width=800, height=500)

    return fig

def show_elbow_world_bank(world_bank):

    from sklearn.cluster import KMeans

    inertias = []
    for k in range(1, 21):
        model = KMeans(n_clusters=k, random_state=23)
        model.fit(world_bank)
        inertias.append(model.inertia_)

    fig = px.line(x=range(1, 21), y=inertias, title='Inertia vs. k in<br>k-means clustering of World Bank data', markers=True)
    fig.update_layout(xaxis_title='k (number of clusters)', yaxis_title='Inertia', width=800, height=500)
    return fig
        
def list_countries_by_cluster(clusters):

    df = clusters.to_frame().reset_index()
    df.columns = ['country', 'cluster']

    for c in np.sort(df['cluster'].unique()):
        print(f'Cluster {c}: ' + ', '.join(df.loc[df['cluster'] == c, 'country']) + '\n')

def country_choropleth(clusters):

    clusters = clusters.reset_index().rename(columns={0: 'cluster'})
    clusters['cluster'] = clusters['cluster'].astype(str)

    fig = px.choropleth(clusters,
              locations='country',
              locationmode='country names',
              color='cluster',
              hover_name='country',
              title='Country Clusters',
              category_orders={'cluster': ['0', '1', '2', '3', '4', '5']},
              width=1000,
              height=800)
    
    return fig

# x = np.array([1, 2, 3, 4, 8, 9, 10, 9, 10])
# y = np.array([7, 10, 6, 8, 3, 5, 4, 9.5, 10])

def color_ratings(title='', labels=None, show_distances=None, width=800, height=600):
    """
    Create a scatter plot with points colored by unique labels and annotated with label values.
    
    Parameters:
    x (array-like): X-coordinates of points
    y (array-like): Y-coordinates of points
    labels (array-like, optional): Labels for each point. If None, uses point indices.
    
    Returns:
    plotly.graph_objs.Figure: Interactive scatter plot with colored and labeled points
    """
    # If no labels provided, use point indices
    if labels is None:
        labels = list(range(len(x)))
    
    # Get unique labels and assign colors
    unique_labels = list(set(labels))
    color_map = {label: f'hsl({i*360/len(unique_labels)}, 80%, 50%)' for i, label in enumerate(unique_labels)}
    color_map = ['red', 'blue', 'green', 'purple', 'orange', 'cyan', 'magenta', 'brown', 'navy']
    
    # Create figure
    fig = go.Figure()

    # show_distances is an array of tuples
    # and shows the distances between all points in those pairs of labels
    # e.g.
    # show_distances = [(0, 2), (2, 3), (4, 5)]

    if show_distances:
        for pair_of_clusters in show_distances:
            cluster_1, cluster_2 = pair_of_clusters
            mask_1 = [l == cluster_1 for l in labels]
            mask_2 = [l == cluster_2 for l in labels]

            x_clust1 = x[mask_1]
            x_clust2 = x[mask_2]
            y_clust1 = y[mask_1]
            y_clust2 = y[mask_2]

            for i in range(len(x_clust1)):
                for j in range(len(x_clust2)):
                    dist_squared = (x_clust1[i] - x_clust2[j])**2 + (y_clust1[i] - y_clust2[j])**2
                    dist_squared = (int(dist_squared) if np.isclose(int(dist_squared), dist_squared) else round(dist_squared, 2))

                    # Line between points
                    fig.add_trace(go.Scatter(
                        x=[x_clust1[i], x_clust2[j]], 
                        y=[y_clust1[i], y_clust2[j]], 
                        mode='lines',
                        line=dict(color='gray', width=1, dash='dot'),
                        showlegend=False
                    ))
        
                    # textangle= np.degrees(np.arctan2(np.abs(y_clust2[j] - y_clust1[i]), np.abs(x_clust2[j] - x_clust1[i])))
                    
                    # Midpoint annotation
                    mid_x = (x_clust1[i] + x_clust2[j]) / 2
                    mid_y = (y_clust1[i] + y_clust2[j]) / 2
                    fig.add_annotation(
                        x=mid_x - 0.05,
                        y=mid_y + 0.1,
                        text=f'<b>{round(np.sqrt(dist_squared), 2)}</b>',
                        showarrow=False,
                        # textangle=textangle,
                        font=dict(size=12, color='gray')
                    )

    # Add points for each unique label
    for label in unique_labels:
        # Find indices of points with this label
        mask = [l == label for l in labels]
        
        # Add scatter trace for this label group
        fig.add_trace(go.Scatter(
            x=[x[i] for i in range(len(x)) if mask[i]],
            y=[y[i] for i in range(len(y)) if mask[i]],
            mode='markers+text',
            marker=dict(
                color=color_map[label],
                size=50,
                opacity=0.7
            ),
            text=[str(label) for i in range(len(x)) if mask[i]],
            textposition='middle center',
            textfont=dict(size=25, color='white'),
            name=f'Label {label}'
        ))
    
    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title='Rating for Modern Family',
        yaxis_title='Rating for Stranger Things',
        showlegend=False,
        width=width,
        height=height
    )
    
    return fig

def show_scatter_comp():

    clustering_comp = np.load('data/clustering-comparison.npy')

    fig = px.scatter(x=clustering_comp[:, 0], y=clustering_comp[:, 1], size_max=10, size=[10] * clustering_comp.shape[0])
    fig.update_layout(width=800, height=600, xaxis_title='Feature 1', yaxis_title='Feature 2')
    return fig

def show_scatter_comp_k_means(k):

    clustering_comp = np.load('data/clustering-comparison.npy')

    from sklearn.cluster import KMeans

    model = KMeans(n_clusters=k, random_state=98)
    model.fit(clustering_comp)

    colors = model.labels_.astype(str)

    fig = px.scatter(x=clustering_comp[:, 0], y=clustering_comp[:, 1], size_max=10, size=[10] * clustering_comp.shape[0], color=colors)
    fig.update_layout(width=800, height=600, xaxis_title='Feature 1', yaxis_title='Feature 2', title=f'k-Means Clustering when k = {k}')
    return fig

def show_scatter_comp_agg(k):

    clustering_comp = np.load('data/clustering-comparison.npy')

    from sklearn.cluster import AgglomerativeClustering

    model = AgglomerativeClustering(n_clusters=k)
    model.fit(clustering_comp)

    colors = model.labels_.astype(str)

    fig = px.scatter(x=clustering_comp[:, 0], y=clustering_comp[:, 1], size_max=10, size=[10] * clustering_comp.shape[0], color=colors)
    fig.update_layout(width=800, height=600, xaxis_title='Feature 1', yaxis_title='Feature 2', title=f'Agglomerative Clustering when k = {k}')
    return fig