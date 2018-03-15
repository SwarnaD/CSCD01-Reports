import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.testing.decorators import image_comparison


@image_comparison(baseline_images=['simple_annotation'],
                  extensions=['png'])
def test_simple_annotation():
    # tests that a simple example graph with annotations
    # appear on the legend with their image and label
    x = np.arange(0.0, 15.0, 0.01)
    y = np.sin(0.3*np.pi*x)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, lw=2, label="sin(x)")
    ax.annotate("",
                xy=(1.6, 1.03), 
                xytext=(8.4, 1.03), 
                arrowprops={'arrowstyle':'<->'}, 
                label="wavelength")
    ax.annotate("",
                xy=(8.4, 0), 
                xytext=(8.35, 1.0), 
                arrowprops={'arrowstyle':'<->', 'ls':'dashed'}, 
                label="amplitude")
    ax.set_ylim(-1.5, 1.5)
    ax.legend()
    plt.show()


@image_comparison(baseline_images=['all_linestyles'],
                  extensions=['png'])
def test_all_linestyles():
    # tests that annotations with different linestyles
    # appear on the legend with their image and label
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 1.7)
    ax.annotate("",
                xy=(0.1, 0.1), 
                xytext=(0.1, 0.9), 
                arrowprops={'arrowstyle':'-', 'ls':'solid'}, 
                label="solid")
    ax.annotate("",
                xy=(0.3, 0.1), 
                xytext=(0.3, 0.9), 
                arrowprops={'arrowstyle':'-', 'ls':'dashed'}, 
                label="dashed")
    ax.annotate("",
                xy=(0.5, 0.1), 
                xytext=(0.5, 0.9), 
                arrowprops={'arrowstyle':'-', 'ls':'dashdot'}, 
                label="dashdot")
    ax.annotate("",
                xy=(0.7, 0.1), 
                xytext=(0.7, 0.9), 
                arrowprops={'arrowstyle':'-', 'ls':'dotted'}, 
                label="dotted")    
    ax.annotate("",
                xy=(0.9, 0.1), 
                xytext=(0.9, 0.9), 
                arrowprops={'arrowstyle':'-', 'ls':(0, (1,5))}, 
                label="offset, on-off-dash-seq")    
    ax.legend()
    plt.show()


@image_comparison(baseline_images=['all_arrowstyles'],
                  extensions=['png'])
def test_all_arrowstyles():
    # tests that annotations with different arrowstyles
    # appear on the legend with their image and label
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_ylim(0, 2.5)
    ax.annotate("",
                xy=(0.1, 0.1), 
                xytext=(0.5, 0.1), 
                arrowprops={'arrowstyle':'-'}, 
                label="-")
    ax.annotate("",
                xy=(0.1, 0.3), 
                xytext=(0.5, 0.3), 
                arrowprops={'arrowstyle':'->'}, 
                label="->")
    ax.annotate("",
                xy=(0.1, 0.5), 
                xytext=(0.5, 0.5), 
                arrowprops={'arrowstyle':'-['}, 
                label="-[") 
    ax.annotate("",
                xy=(0.1, 0.7), 
                xytext=(0.5, 0.7), 
                arrowprops={'arrowstyle':'|-|'}, 
                label="|-|")
    ax.annotate("",
                xy=(0.1, 0.9), 
                xytext=(0.5, 0.9), 
                arrowprops={'arrowstyle':'-|>'}, 
                label="-|>")
    ax.annotate("",
                xy=(0.1, 1.1), 
                xytext=(0.5, 1.1), 
                arrowprops={'arrowstyle':'<-'}, 
                label="<-")
    ax.annotate("",
                xy=(0.1, 1.3), 
                xytext=(0.5, 1.3), 
                arrowprops={'arrowstyle':'<->'}, 
                label="<->")
    ax.annotate("",
                xy=(0.1, 1.5), 
                xytext=(0.5, 1.5), 
                arrowprops={'arrowstyle':'<|-'}, 
                label="<|-")
    ax.annotate("",
                xy=(0.1, 1.7), 
                xytext=(0.5, 1.7), 
                arrowprops={'arrowstyle':'<|-|>'}, 
                label="<|-|>")
    ax.annotate("",
                xy=(0.1, 1.9), 
                xytext=(0.5, 1.9), 
                arrowprops={'arrowstyle':'fancy'}, 
                label="fancy")
    ax.annotate("",
                xy=(0.1, 2.1), 
                xytext=(0.5, 2.1), 
                arrowprops={'arrowstyle':'simple'}, 
                label="simple")
    ax.annotate("",
                xy=(0.1, 2.3), 
                xytext=(0.5, 2.3), 
                arrowprops={'arrowstyle':'wedge'}, 
                label="wedge")    
    ax.legend()
    plt.show()


@image_comparison(baseline_images=['annotation_colours'],
                  extensions=['png'])
def test_annotation_colours():
    # tests that annotations with different colors
    # appear on the legend with their image and label
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.annotate("",
                xy=(0.1, 0.1), 
                xytext=(0.1, 0.9), 
                arrowprops={'arrowstyle':'<|-|>', 
                            'ls':'solid', 
                            'color':'blue'}, 
                label="blue")
    ax.annotate("",
                xy=(0.2, 0.1), 
                xytext=(0.2, 0.9), 
                arrowprops={'arrowstyle':'-',
                            'ls':'dashed',
                            'color':'red'}, 
                label="red")
    ax.annotate("",
                xy=(0.3, 0.1), 
                xytext=(0.3, 0.9), 
                arrowprops={'arrowstyle':'|-|',
                            'ls':'dashdot',
                            'color':'yellow'},
                label="yellow")    
    ax.legend()
    plt.show()


@image_comparison(baseline_images=['annotation_text'],
                  extensions=['png'])
def test_annotation_text():
    # tests that annotations with different texts
    # appear on the legend with their image and label
    # note: the text itself does not appear on the legend,
    # only the arrow. The text itself is self-explanatory.
    # However, if only text is passed, the image will be
    # the text.
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.annotate("hello",
                xy=(0.1, 0.9), 
                xytext=(0.1, 0.1), 
                arrowprops={'arrowstyle':'-',
                            'ls':'dashed',
                            'color':'green'},
                label="hello") 
    ax.annotate("world",
                xy=(0.3, 0.9), 
                xytext=(0.3, 0.1), 
                arrowprops={'arrowstyle':'<->',
                            'ls':'dashdot',
                            'color':'purple'},
                label="world")
    ax.annotate("short text",
                xy=(0.5, 0.9), 
                xytext=(0.5, 0.1),
                label="short text")    
    ax.annotate("long text",
                xy=(0.7, 0.9), 
                xytext=(0.7, 0.1),
                label="long text")    
    
    ax.legend() 
    plt.show()


@image_comparison(baseline_images=['annotation_no_line_text'],
                  extensions=['png'])
def test_annotation_no_line_text():
    # tests that annotations with no line, text, or both
    # appear on the legend with their image and label
    # note: if no text, it will not appear in the legend
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.annotate("",
                xy=(0.1, 0.9), 
                xytext=(0.1, 0.1), 
                arrowprops={'arrowstyle':'-',
                            'ls':'dashed'},
                label="no text") 
    ax.annotate("no line",
                xy=(0.3, 0.1), 
                xytext=(0.3, 0.9),
                label="no line")
    ax.annotate("",
                xy=(0.5, 0.1), 
                xytext=(0.5, 0.9),
                label="no line or text")
    ax.legend() 
    plt.show()
    