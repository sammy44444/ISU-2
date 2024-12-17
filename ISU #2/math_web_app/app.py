from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import os
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for saving plots

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = 'static/images'
# Get the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Set the upload folder to an absolute path
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static/images')

def calculate_statistics(data):
    """Calculates mean, median, and mode for the given data."""
    mean = np.mean(data)
    median = np.median(data)
    mode_data = Counter(data)
    mode = [key for key, val in mode_data.items() if val == max(mode_data.values())]
    return mean, median, mode

def create_box_and_whisker_plot(data, filename):
    """Creates and saves a box-and-whisker plot for the data."""
    plt.figure(figsize=(6, 4))
    plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
    plt.title("Box-and-Whisker Plot")
    plt.xlabel("Values")
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    plt.savefig(filepath)
    plt.close()
    return filepath

def create_histogram(data, filename):
    """Creates and saves a histogram for the data."""
    plt.figure(figsize=(6, 4))
    plt.hist(data, bins=10, color='skyblue', edgecolor='black')
    plt.title("Histogram")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    plt.savefig(filepath)
    plt.close()
    return filepath

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from form
        data = request.form['data']
        try:
            data = list(map(float, data.split(',')))
        except ValueError:
            return render_template('index.html', error="Please enter valid numeric data separated by commas.")

        # Calculate statistics
        mean, median, mode = calculate_statistics(data)

        # Generate plots
        boxplot_path = create_box_and_whisker_plot(data, 'boxplot.png')
        histogram_path = create_histogram(data, 'histogram.png')

        return render_template(
            'index.html',
            mean=mean,
            median=median,
            mode=mode,
            boxplot_url=boxplot_path,
            histogram_url=histogram_path,
        )
    return render_template('index.html')

if __name__ == '__main__':
    # Ensure the images directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
 



