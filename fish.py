# coding: utf-8

from flask import Flask, request, url_for, redirect, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons

app = Flask(__name__, template_folder="templates")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4"

# you can also pass key here
GoogleMaps(app, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")


@app.route('/middle', methods=['POST'])
def middle():
    uid = request.form['ucode']
    # if uid=="b123":
    return redirect(url_for('person'))
    # else:
        # return redirect(url_for('gov'))

@app.route("/person")
def person():

    polyline = {
        'stroke_color': '#0AB0DE',
        'stroke_opacity': 1.0,
        'stroke_weight': 3,
        'path': [{'lat': -8.831329, 'lng': 116.514596},
                 {'lat': -8.824975, 'lng': 116.514190},
                 {'lat': -8.819457, 'lng': 116.515542},
                 {'lat': -8.815350, 'lng': 116.510754},
                 {'lat': -8.819703, 'lng': 116.502612},
                 {'lat': -8.827473, 'lng': 116.511321},
                 {'lat': -8.831329, 'lng': 116.514596}]

    }

    path1 = [(33.665, -116.235), (33.666, -116.256),
             (33.667, -116.250), (33.668, -116.229)]

    plinemap = Map(
        identifier="plinemap",
        varname="plinemap",
        lat=-8.831329,
        lng=116.514596,
        style=(
            "height:80%;"
            "width:50%;"
            "top:100;"
            "left:10;"
            "position:absolute;"
            "z-index:200;"  
        ),
        markers=[
              {
                 'icon': 'https://files.slack.com/files-pri/T02MNHHJA-F971R9ZFD/ship.png',             
                 'lat': -8.831329,
                 'lng': 116.514596,
                 'infobox': "<b>Budi julaeha<br/>pangandaran</b>"
              }
          ],
        polylines=[polyline, path1]
    )

    return render_template(
        'fish.html',
        plinemap=plinemap
    )

@app.route("/gov")
def gov():

    polyline = {
    'stroke_color': '#0AB0DE',
    'stroke_opacity': 1.0,
    'stroke_weight': 3,
    'path': [{'lat': -8.831329, 'lng': 116.514596},
             {'lat': -8.824975, 'lng': 116.514190},
             {'lat': -8.819457, 'lng': 116.515542},
             {'lat': -8.815350, 'lng': 116.510754},
             {'lat': -8.819703, 'lng': 116.502612},
             {'lat': -8.827473, 'lng': 116.511321},
             {'lat': -8.831329, 'lng': 116.514596},
             {'lat': -8.831877, 'lng': 116.514790}
             ]
    }
    
    polyline2 = {
        'stroke_color': '#08004b',
        'stroke_opacity': 1.0,
        'stroke_weight': 3,
        'path': [{'lat': -8.835159, 'lng': 116.512373},
                 {'lat': -8.837067, 'lng': 116.510331},
                 {'lat': -8.835720, 'lng': 116.507836},
                 {'lat': -8.831951, 'lng': 116.500989},
                 {'lat': -8.828103, 'lng': 116.509538},
                 {'lat': -8.832939, 'lng': 116.510830},
                 {'lat': -8.835159, 'lng': 116.512373}]

    }


    polyline3 = {
        'stroke_color': '#008080',
        'stroke_opacity': 1.0,
        'stroke_weight': 3,
        'path': [{'lat': -8.831322, 'lng': 116.514715},
                 {'lat': -8.829985, 'lng': 116.510761},
                 {'lat': -8.829985, 'lng': 116.510761},
                 {'lat': -8.824851, 'lng': 116.504635},
                 {'lat': -8.825290, 'lng': 116.509613},
                 {'lat': -8.825290, 'lng': 116.509613},
                 {'lat': -8.831322, 'lng': 116.514715},
                 {'lat': -8.831739, 'lng': 116.515015}
                 ]
    }

    polyline5 = {
        'stroke_color': '#06c253',
        'stroke_opacity': 1.0,
        'stroke_weight': 3,
        'path': [{'lat': -8.830843, 'lng': 116.498367},
                 {'lat': -8.825618, 'lng': 116.502234},
                 {'lat': -8.832493, 'lng': 116.504636},
                 {'lat': -8.833660, 'lng': 116.500929},
                 {'lat': -8.832515, 'lng': 116.499212},
                 {'lat': -8.830843, 'lng': 116.498367}
                 ]
    }
    polyline_fill = {
    'stroke_color': '#008080',
    'stroke_opacity': 1.0,
    'fill_color': '#ABC321',
    'stroke_weight': 3,
    'path': [{'lat': -8.822147, 'lng': 116.506429},
             {'lat': -8.823437, 'lng': 116.505405},
             {'lat': -8.824077, 'lng': 116.505870},
             {'lat': -8.823157, 'lng': 116.507651},
             {'lat': -8.822147, 'lng': 116.506429},

             ]
    }
    polyline_fill2 = {
    'stroke_color': '#f1554d',
    'stroke_opacity': 1.0,
    'fill_color': '#ff9b9b',
    'stroke_weight': 3,
    'path': [{'lat': -8.828370, 'lng': 116.503255},
             {'lat': -8.828644, 'lng': 116.504512},
             {'lat': -8.829190, 'lng': 116.504287},
             {'lat': -8.829291, 'lng': 116.503773},
             {'lat': -8.829015, 'lng': 116.503451},
             {'lat': -8.828370, 'lng': 116.503255}
             ]
    }


    polyline_fill22 = {
    'stroke_color': '#f1554d',
    'stroke_opacity': 1.0,
    'fill_color': '#ff9b9b',
    'stroke_weight': 3,
    'path': [{'lat': -8.824897, 'lng': 116.502240},
             {'lat': -8.825215, 'lng': 116.503055},
             {'lat': -8.825480, 'lng': 116.502658},
             {'lat': -8.825618, 'lng': 116.502234},
             {'lat': -8.824897, 'lng': 116.502240}
             ]
    }


    plinemap = Map(
        identifier="plinemap",
        varname="plinemap",
        lat=-8.831329,
        lng=116.514596,
        style=(
            "height:100%;"
            "width:100%;"
            "top:100;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        markers=[
              {
                 'icon': 'https://files.slack.com/files-pri/T02MNHHJA-F971R9ZFD/ship.png',             
                 'lat': -8.831877,
                 'lng': 116.514790,
                 'infobox': "<img src='/static/images/budi_anduk.JPG' width='70%' height='80%'/> \
                            <div> \
                            <font size='20'> \
                            Budi zunaidi </br> \
                            Domisili : Kerupukan </br> \
                            Tangkapan bulan ini : 5 ton \
                            Jenis ikan : 4 jenis \
                            Tanggal lapor terakhir : Senin 23 Oktober 2017 \
                            </font></div>"
              },
              {
                 'icon': 'https://files.slack.com/files-pri/T02MNHHJA-F971R9ZFD/ship.png',             
                 'lat': -8.831951,
                 'lng': 116.500989,
                 'infobox': "<img src='/static/images/budi2.jpg' width='70%' height='80%'/> \
                            <div> \
                            <font size='20'> \
                            Ahmad supandi </br> \
                            Domisili : Jeneng agung </br> \
                            Tangkapan bulan ini : 1 ton \
                            Jenis ikan : 2 jenis \
                            Tanggal lapor terakhir : Sabtu 10 Oktober 2017 \
                            </font></div>"
              },
            {
                 'icon': 'https://files.slack.com/files-pri/T02MNHHJA-F971R9ZFD/ship.png',             
                 'lat': -8.831739,
                 'lng': 116.515015,
                                'infobox': "<img src='/static/images/bambang3.jpeg' width='70%' height='80%'/> \
                            <div> \
                            <font size='20'> \
                            Bambang </br> \
                            Domisili : Semangkit agung </br> \
                            Tangkapan bulan ini : 0.5 ton \
                            Jenis ikan : 1 jenis \
                            Tanggal lapor terakhir : Selasa 13 Oktober 2017 \
                            </font></div>"
             },
              {
                 'icon': 'https://files.slack.com/files-pri/T02MNHHJA-F971R9ZFD/ship.png',             
                 'lat': -8.830843,
                 'lng': 116.498367,
                 'infobox': "<img src='/static/images/budi_anduk.JPG' width='70%' height='80%'/> \
                            <div> \
                            <font size='20'> \
                            Budi zunaidi </br> \
                            Domisili : Kerupukan </br> \
                            Tangkapan bulan ini : 5 ton \
                            Jenis ikan : 4 jenis \
                            Tanggal lapor terakhir : Senin 23 Oktober 2017 \
                            </font></div>"
              },
                  {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat':  -8.823247,
                'lng':  116.506267,
                'infobox': "<img src='/static/images/googly.jpg' width='70%' height='80%'/> \
                            <div> \
                            <font size='20'> \
                            Ikan tongkol </br> \
                            musim : 10 Januari - 23 Maret </br> \
                            kapasitas : 20 ton \
                            </font></div>"
            },
              {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat':  -8.828748,
                'lng':  116.504108,
                'infobox': "<img src='/static/images/kembong.jpg' width='70%' height='80%'/> \
                            <div> \
                            <font size='20'> \
                            Ikan kembung </br> \
                            musim : 23 Maret - 5 Agustus </br> \
                            kapasitas : 50 ton \
                            </font></div>"
            },
          ],
        polylines=[polyline,polyline2,polyline3,polyline5],
        polygons=[polyline_fill,polyline_fill2,polyline_fill22]
    )


    return render_template(
        'gov.html',
        plinemap=plinemap
    )
@app.route('/')
@app.route('/home')
def home():
    return render_template(
        "home.html"
        )

@app.route('/fullmap')
def fullmap():
    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:100%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "Hello I am <b style='color:green;'>GREEN</b>!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "Hello I am <b style='color:blue;'>BLUE</b>!"
            },
            {
                'icon': icons.dots.yellow,
                'title': 'Click Here',
                'lat': 37.4500,
                'lng': -122.1350,
                'infobox': (
                    "Hello I am <b style='color:#ffcc00;'>YELLOW</b>!"
                    "<h2>It is HTML title</h2>"
                    "<img src='//placehold.it/50'>"
                    "<br>Images allowed!"
                )
            }
        ],
        # maptype = "TERRAIN",
        # zoom="5"
    )
    return render_template('example_fullmap.html', fullmap=fullmap)


@app.route("/trial")
def mapview():
    mymap = Map(
        identifier="view-side",  # for DOM element
        varname="mymap",  # for JS object name
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        varname="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers={
            icons.dots.green: [(37.4419, -122.1419), (37.4500, -122.1350)],
            icons.dots.blue: [(37.4300, -122.1400, "Hello World")]
        }
    )

    trdmap = Map(
        identifier="trdmap",
        varname="trdmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': icons.alpha.B,
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "Hello I am <b style='color:green;'>GREEN</b>!"
            },
            {
                'icon': icons.dots.blue,
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "Hello I am <b style='color:blue;'>BLUE</b>!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                'lat': 37.4500,
                'lng': -122.1350,
                'infobox': (
                    "Hello I am <b style='color:#ffcc00;'>YELLOW</b>!"
                    "<h2>It is HTML title</h2>"
                    "<img src='//placehold.it/50'>"
                    "<br>Images allowed!"
                )
            }
        ]
    )

    clustermap = Map(
        identifier="clustermap",
        varname="clustermap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'lat': 37.4500,
                'lng': -122.1350
            },
            {
                'lat': 37.4400,
                'lng': -122.1350
            },
            {
                'lat': 37.4300,
                'lng': -122.1350
            },
            {
                'lat': 36.4200,
                'lng': -122.1350
            },
            {
                'lat': 36.4100,
                'lng': -121.1350
            }
        ],
        zoom=12,
        cluster=True
    )

    movingmap = Map(
        identifier="movingmap",
        varname="movingmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'lat': 37.4500,
                'lng': -122.1350
            }
        ],
        zoom=12
    )

    movingmarkers = [
        {
            'lat': 37.4400,
            'lng': -122.1350
        },
        {
            'lat': 37.4430,
            'lng': -122.1350
        },
        {
            'lat': 37.4450,
            'lng': -122.1350
        },
        {
            'lat': 37.4490,
            'lng': -122.1350
        }
    ]

    rectangle = {
        'stroke_color': '#0000FF',
        'stroke_opacity': .8,
        'stroke_weight': 5,
        'fill_color': '#FFFFFF',
        'fill_opacity': .1,
        'bounds': {
            'north': 33.685,
            'south': 33.671,
            'east': -116.234,
            'west': -116.251
        }
    }

    rectmap = Map(
        identifier="rectmap",
        varname="rectmap",
        lat=33.678,
        lng=-116.243,
        rectangles=[
            rectangle,
            [33.678, -116.243, 33.671, -116.234],
            (33.685, -116.251, 33.678, -116.243),
            [(33.679, -116.254), (33.678, -116.243)],
            ([33.689, -116.260], [33.685, -116.250]),
        ]
    )

    circle = {
        'stroke_color': '#FF00FF',
        'stroke_opacity': 1.0,
        'stroke_weight': 7,
        'fill_color': '#FFFFFF',
        'fill_opacity': .8,
        'center': {
                  'lat': 33.685,
                  'lng': -116.251
        },
        'radius': 2000,
    }

    circlemap = Map(
        identifier="circlemap",
        varname="circlemap",
        lat=33.678,
        lng=-116.243,
        circles=[
            circle,
            [33.685, -116.251, 1000],
            (33.685, -116.251, 1500),
        ]
    )

    polyline = {
        'stroke_color': '#0AB0DE',
        'stroke_opacity': 1.0,
        'stroke_weight': 3,
        'path': [{'lat': 33.678, 'lng': -116.243},
                 {'lat': 33.679, 'lng': -116.244},
                 {'lat': 33.680, 'lng': -116.250},
                 {'lat': 33.681, 'lng': -116.239},
                 {'lat': 33.678, 'lng': -116.243}]
    }

    path1 = [(33.665, -116.235), (33.666, -116.256),
             (33.667, -116.250), (33.668, -116.229)]

    path2 = ((33.659, -116.243), (33.660, -116.244),
             (33.649, -116.250), (33.644, -116.239))

    path3 = ([33.688, -116.243], [33.680, -116.244],
             [33.682, -116.250], [33.690, -116.239])

    path4 = [[33.690, -116.243], [33.691, -116.244],
             [33.692, -116.250], [33.693, -116.239]]

    plinemap = Map(
        identifier="plinemap",
        varname="plinemap",
        lat=33.678,
        lng=-116.243,
        polylines=[polyline, path1, path2, path3, path4]
    )

    polygon = {
        'stroke_color': '#0AB0DE',
        'stroke_opacity': 1.0,
        'stroke_weight': 3,
        'fill_color': '#ABC321',
        'fill_opacity': .5,
        'path': [{'lat': 33.678, 'lng': -116.243},
                 {'lat': 33.679, 'lng': -116.244},
                 {'lat': 33.680, 'lng': -116.250},
                 {'lat': 33.681, 'lng': -116.239},
                 {'lat': 33.678, 'lng': -116.243}]
    }

    pgonmap = Map(
        identifier="pgonmap",
        varname="pgonmap",
        lat=33.678,
        lng=-116.243,
        polygons=[polygon, path1, path2, path3, path4]
    )

    collapsible = Map(
        identifier="collapsible",
        varname="collapsible",
        lat=60.000025,
        lng=30.288809,
        zoom=13,
        collapsible=True
    )

    infoboxmap = Map(
        identifier="infoboxmap",
        zoom=12,
        lat=59.939012,
        lng=30.315707,
        markers=[{
            'lat': 59.939,
            'lng': 30.315,
            'infobox': 'This is a marker'
        }],
        circles=[{
            'stroke_color': '#FF00FF',
            'stroke_opacity': 1.0,
            'stroke_weight': 7,
            'fill_color': '#FF00FF',
            'fill_opacity': 0.2,
            'center': {
                'lat': 59.939,
                'lng': 30.3
            },
            'radius': 200,
            'infobox': "This is a circle"
        }],
        rectangles=[{
            'stroke_color': '#0000FF',
            'stroke_opacity': .8,
            'stroke_weight': 5,
            'fill_color': '#FFFFFF',
            'fill_opacity': .1,
            'bounds': {
                'north': 59.935,
                'south': 59.93,
                'east': 30.325,
                'west': 30.3,
            },
            'infobox': "This is a rectangle"
        }],
        polygons=[{
            'stroke_color': '#0AB0DE',
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': [
                [59.94, 30.318],
                [59.946, 30.325],
                [59.946, 30.34],
                [59.941, 30.35],
                [59.938, 30.33]
            ],
            'infobox': 'This is a polygon'
        }],
        polylines=[{
            'stroke_color': '#0AB0DE',
            'stroke_opacity': 1.0,
            'stroke_weight': 10,
            'path': [
                (59.941, 30.285),
                (59.951, 30.31),
                (59.95, 30.36),
                (59.938, 30.358)
            ],
            'infobox': 'This is a polyline'
        }]
    )

    return render_template(
        'example.html',
        mymap=mymap,
        sndmap=sndmap,
        trdmap=trdmap,
        rectmap=rectmap,
        circlemap=circlemap,
        plinemap=plinemap,
        pgonmap=pgonmap,
        clustermap=clustermap,
        movingmap=movingmap,
        movingmarkers=movingmarkers,
        collapsible=collapsible,
        infoboxmap=infoboxmap
    )




if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
