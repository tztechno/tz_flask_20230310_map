
import IPython
from folium import plugins
import folium
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            lat = float(request.form['lat'])
            lon = float(request.form['lon'])
            zoom = int(request.form['zoom'])
            eq_map = folium.Map(location=[lat, lon],tiles='Stamen Terrain',zoom_start=zoom,min_zoom=2.0)
            eq_map.add_child(plugins.HeatMap([[lat, lon]]))
            eq_map.save("static/2023.html")
            graph_html= "<iframe width='600' height='400' src='static/2023.html' frameborder='0'></iframe>"
            
            return render_template('index.html', graph_html=graph_html)

        except ValueError:
            result = "Error: Please enter a valid number."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



