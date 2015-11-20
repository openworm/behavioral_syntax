import numpy as np

from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d

from scipy import io
from sklearn import manifold
from sklearn.metrics import euclidean_distances

#this allows us to view the tangent angle distance between postures which 
#helps to develop an intuition of which postures are close and which
#are far apart. 

g = io.loadmat('/Users/cyrilrocke/Documents/c_elegans/data/postures')
postures = g.get('postures')


seed = np.random.RandomState(seed=3)

similarities = euclidean_distances(postures.T)

mds = manifold.MDS(n_components=2, max_iter=5000, eps=1e-9, random_state=seed,
                   dissimilarity="precomputed", n_jobs=1)
                   
pos = mds.fit(similarities).embedding_

def mtext(p, x, y, textstr):
    p.text(x, y, text=[textstr],
         text_color='steelblue', text_align="center", text_font_size="10pt")


output_file("color_scatter.html", title="postures MDS")
TOOLS="resize,crosshair,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select"

# create a new plot with a range set with a tuple
p = figure(plot_width=400, plot_height=400, x_range=(-8, 10),y_range=(-8,8),tools=TOOLS)


p.scatter(pos[:,0],pos[:,1],radius=0.2,fill_color='#FFDAB9', fill_alpha=0.6)

for i in range(90):
    mtext(p, [pos[:,0][i]], [pos[:,1][i]-0.15], str(i))

show(p)
