import warnings
warnings.filterwarnings("ignore")

import matplotlib 
# matplotlib.use('agg')

import matplotlib.pyplot as plt

#import numpy as np
#import matplotlib.pyplot as plt
#plt.ioff()

def plot_graph(clf, X_train, y_train, X_test, y_test, x_label, y_label):
    pred = clf.predict(X_test)
    # clear current figure
    plt.clf()
    # plot graph
    plt.scatter(X_train, y_train, color="b", label="training data")
    plt.scatter(X_test, y_test, color="r", label="test data")
    plt.plot(X_test, pred, color="black")
    plt.legend(loc=2)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig("test.png")
    plt.show()
    
import base64
import json
import subprocess

def output_image(name, format, bytes):
    image_start = "BEGIN_IMAGE_f9825uweof8jw9fj4r8"
    image_end = "END_IMAGE_0238jfw08fjsiufhw8frs"
    data = {}
    data['name'] = name
    data['format'] = format
    data['bytes'] = base64.encodestring(bytes)
    print("image created")
    # print image_start+json.dumps(data)+image_end