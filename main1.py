import folium
from folium import plugins
from shapely.geometry import Polygon
from pyproj import Proj, transform


# Provided data
zone_data = {
    "city": "Trivandrum",
    "zones": [
        {
            "id": 36,
            "name": "Nettayam",
            "uber_h3_index_3km": 605173827105718271,
            "boundary": [
                {
                    "lat": 8.533370921169928,
                    "lng": 77.03668035980067
                },
                {
                    "lat": 8.568190763768051,
                    "lng": 77.03719358474507
                },
                {
                    "lat": 8.586383078037594,
                    "lng": 77.00856704412529
                },
                {
                    "lat": 8.569757779643906,
                    "lng": 76.97944027307273
                },
                {
                    "lat": 8.534949644028803,
                    "lng": 76.97893384112379
                },
                {
                    "lat": 8.516755099245186,
                    "lng": 77.00754738921243
                }
            ],
            "center_point": {
                "longitude": 77.00806041534666,
                "latitude": 8.551567880982246
            },
            "shifts": [
                "Shift1"
            ]
        },
        {
            "id": 35,
            "name": "Thumba",
            "uber_h3_index_3km": 605173820126396415,
            "boundary": [
                {
                    "lat": 8.538078284352393,
                    "lng": 76.8635571917395
                },
                {
                    "lat": 8.572862922497226,
                    "lng": 76.8640500616582
                },
                {
                    "lat": 8.5910231760842,
                    "lng": 76.83547160230239
                },
                {
                    "lat": 8.574401077205996,
                    "lng": 76.80641331741958
                },
                {
                    "lat": 8.539628229347482,
                    "lng": 76.80592721647628
                },
                {
                    "lat": 8.521465689557461,
                    "lng": 76.83449263344357
                }
            ],
            "center_point": {
                "longitude": 76.83498533717325,
                "latitude": 8.556243229840794
            },
            "shifts": [
                "Shift1"
            ]
        },
        {
            "id": 37,
            "name": "Nedumangad",
            "uber_h3_index_3km": 605173826568847359,
            "boundary": [
                {
                    "lat": 8.586383078037594,
                    "lng": 77.00856704412529
                },
                {
                    "lat": 8.621199474191043,
                    "lng": 77.00907704700322
                },
                {
                    "lat": 8.639378849172475,
                    "lng": 76.98045348545196
                },
                {
                    "lat": 8.622744086798868,
                    "lng": 76.95133292806224
                },
                {
                    "lat": 8.587939413992059,
                    "lng": 76.95082971657575
                },
                {
                    "lat": 8.569757779643906,
                    "lng": 76.97944027307273
                }
            ],
            "center_point": {
                "longitude": 76.97995008238186,
                "latitude": 8.604567113639325
            },
            "shifts": [
                "Shift1"
            ]
        },
        {
            "id": 1,
            "name": "Vazhuthakadu",
            "uber_h3_index_3km": 605173824689799167,
            "boundary": [
                {
                    "lat": 8.48194356780951,
                    "lng": 77.0070377370972
                },
                {
                    "lat": 8.516755099245186,
                    "lng": 77.00754738921243
                },
                {
                    "lat": 8.534949644028803,
                    "lng": 76.97893384112379
                },
                {
                    "lat": 8.518334877052531,
                    "lng": 76.94982363968448
                },
                {
                    "lat": 8.483535064071123,
                    "lng": 76.94932077420053
                },
                {
                    "lat": 8.465338299040226,
                    "lng": 76.977921325508
                }
            ],
            "center_point": {
                "longitude": 76.97843078447107,
                "latitude": 8.50014275854123
            },
            "shifts": [
                "Shift1"
            ]
        },
        {
            "id": 3,
            "name": "Peroorkada",
            "uber_h3_index_3km": 605173820797485055,
            "boundary": [
                {
                    "lat": 8.534949644028803,
                    "lng": 76.97893384112379
                },
                {
                    "lat": 8.569757779643906,
                    "lng": 76.97944027307273
                },
                {
                    "lat": 8.587939413992059,
                    "lng": 76.95082971657575
                },
                {
                    "lat": 8.571315161274914,
                    "lng": 76.92172573938984
                },
                {
                    "lat": 8.536518760511054,
                    "lng": 76.92122609245942
                },
                {
                    "lat": 8.518334877052531,
                    "lng": 76.94982363968448
                }
            ],
            "center_point": {
                "longitude": 76.95032988371767,
                "latitude": 8.553135939417212
            },
            "shifts": [
                "Shift1"
            ]
        },
        {
            "id": 4,
            "name": "Technopark",
            "uber_h3_index_3km": 605173819992178687,
            "boundary": [
                {
                    "lat": 8.536518760511054,
                    "lng": 76.92122609245942
                },
                {
                    "lat": 8.571315161274914,
                    "lng": 76.92172573938984
                },
                {
                    "lat": 8.589486108702282,
                    "lng": 76.89313121004591
                },
                {
                    "lat": 8.572862922497226,
                    "lng": 76.8640500616582
                },
                {
                    "lat": 8.538078284352393,
                    "lng": 76.8635571917395
                },
                {
                    "lat": 8.51990506925161,
                    "lng": 76.89213869519246
                }
            ],
            "center_point": {
                "longitude": 76.8926381650809,
                "latitude": 8.55469438443158
            },
            "shifts": [
                "Shift1",
                "Morning"
            ]
        },
        {
            "id": 2,
            "name": "Thampanoor",
            "uber_h3_index_3km": 605173820529049599,
            "boundary": [
                {
                    "lat": 8.483535064071123,
                    "lng": 76.94932077420053
                },
                {
                    "lat": 8.518334877052531,
                    "lng": 76.94982363968448
                },
                {
                    "lat": 8.536518760511054,
                    "lng": 76.92122609245942
                },
                {
                    "lat": 8.51990506925161,
                    "lng": 76.89213869519246
                },
                {
                    "lat": 8.485117002538091,
                    "lng": 76.89164260835148
                },
                {
                    "lat": 8.466930880263218,
                    "lng": 76.92022714212546
                }
            ],
            "center_point": {
                "longitude": 76.92072982533564,
                "latitude": 8.50172360894794
            },
            "shifts": [
                "Shift1"
            ]
        },
        {
            "id": 9,
            "name": "Kaniyapuram",
            "uber_h3_index_3km": 605173820394831871,
            "boundary": [
                {
                    "lat": 8.589486108702282,
                    "lng": 76.89313121004591
                },
                {
                    "lat": 8.624279030340166,
                    "lng": 76.89362763813648
                },
                {
                    "lat": 8.642436987413335,
                    "lng": 76.86503614046833
                },
                {
                    "lat": 8.625804318831333,
                    "lng": 76.8359612550223
                },
                {
                    "lat": 8.5910231760842,
                    "lng": 76.83547160230239
                },
                {
                    "lat": 8.572862922497226,
                    "lng": 76.8640500616582
                }
            ],
            "center_point": {
                "longitude": 76.86454631793895,
                "latitude": 8.607648757311424
            },
            "shifts": [
                "Shift1"
            ]
        },
        {
            "id": 10,
            "name": "Manacaud",
            "uber_h3_index_3km": 605173824421363711,
            "boundary": [
                {
                    "lat": 8.43053514082228,
                    "lng": 76.97741524176146
                },
                {
                    "lat": 8.465338299040226,
                    "lng": 76.977921325508
                },
                {
                    "lat": 8.483535064071123,
                    "lng": 76.94932077420053
                },
                {
                    "lat": 8.466930880263218,
                    "lng": 76.92022714212546
                },
                {
                    "lat": 8.432139451882794,
                    "lng": 76.91972783864335
                },
                {
                    "lat": 8.413940476908886,
                    "lng": 76.94831538895816
                }
            ],
            "center_point": {
                "longitude": 76.94882128519949,
                "latitude": 8.448736552164755
            },
            "shifts": [
                "Shift1"
            ]
        },
        {
            "id": 38,
            "name": "Vattapara",
            "uber_h3_index_3km": 605173820260614143,
            "boundary": [
                {
                    "lat": 8.587939413992059,
                    "lng": 76.95082971657575
                },
                {
                    "lat": 8.622744086798868,
                    "lng": 76.95133292806224
                },
                {
                    "lat": 8.64091275626931,
                    "lng": 76.92272537697411
                },
                {
                    "lat": 8.624279030340166,
                    "lng": 76.89362763813648
                },
                {
                    "lat": 8.589486108702282,
                    "lng": 76.89313121004591
                },
                {
                    "lat": 8.571315161274914,
                    "lng": 76.92172573938984
                }
            ],
            "center_point": {
                "longitude": 76.92222876819739,
                "latitude": 8.606112759562933
            },
            "shifts": [
                "Shift1"
            ]
        },
        {
            "id": 39,
            "name": "Thonnakkal",
            "uber_h3_index_3km": 605173824018710527,
            "boundary": [
                {
                    "lat": 8.642436987413335,
                    "lng": 76.86503614046833
                },
                {
                    "lat": 8.677226363090208,
                    "lng": 76.86552934943735
                },
                {
                    "lat": 8.695371275622472,
                    "lng": 76.83694089723554
                },
                {
                    "lat": 8.678729137294782,
                    "lng": 76.80787228878482
                },
                {
                    "lat": 8.643951556700745,
                    "lng": 76.80738585353562
                },
                {
                    "lat": 8.625804318831333,
                    "lng": 76.8359612550223
                }
            ],
            "center_point": {
                "longitude": 76.836454297414,
                "latitude": 8.660586606492146
            },
            "shifts": [
                "Shift1"
            ]
        },
        {
            "id": 40,
            "name": "Attingal",
            "uber_h3_index_3km": 605173823481839615,
            "boundary": [
                {
                    "lat": 8.695371275622472,
                    "lng": 76.83694089723554
                },
                {
                    "lat": 8.73015703857749,
                    "lng": 76.83743088680598
                },
                {
                    "lat": 8.748288852519144,
                    "lng": 76.80884549385691
                },
                {
                    "lat": 8.731637257139358,
                    "lng": 76.77978317644637
                },
                {
                    "lat": 8.696863305379427,
                    "lng": 76.7792999589351
                },
                {
                    "lat": 8.678729137294782,
                    "lng": 76.80787228878482
                }
            ],
            "center_point": {
                "longitude": 76.80836211701079,
                "latitude": 8.71350781108878
            },
            "shifts": [
                "Shift1"
            ]
        },
        {
            "id": 57,
            "name": "Chirayinkeezhu",
            "uber_h3_index_3km": 605173823213404159,
            "boundary": [
                {
                    "lat": 8.643951556700745,
                    "lng": 76.80738585353562
                },
                {
                    "lat": 8.678729137294782,
                    "lng": 76.80787228878482
                },
                {
                    "lat": 8.696863305379427,
                    "lng": 76.7792999589351
                },
                {
                    "lat": 8.680222236222498,
                    "lng": 76.75025426295936
                },
                {
                    "lat": 8.64545647828641,
                    "lng": 76.74977459335685
                },
                {
                    "lat": 8.627319966347699,
                    "lng": 76.77833385609583
                }
            ],
            "center_point": {
                "longitude": 76.77882013561127,
                "latitude": 8.66209044670526
            },
            "shifts": [
                "Shift1"
            ]
        },
        {
            "id": 58,
            "name": "Kilimanoor",
            "uber_h3_index_3km": 605173822542315519,
            "boundary": [
                {
                    "lat": 8.745320748776876,
                    "lng": 76.92422569324934
                },
                {
                    "lat": 8.780126403928973,
                    "lng": 76.92472602813827
                },
                {
                    "lat": 8.798266635040104,
                    "lng": 76.89611148679063
                },
                {
                    "lat": 8.7816035562855,
                    "lng": 76.86700965506606
                },
                {
                    "lat": 8.746809673093926,
                    "lng": 76.86651610669738
                },
                {
                    "lat": 8.728667096160564,
                    "lng": 76.89511760553229
                }
            ],
            "center_point": {
                "longitude": 76.895617762579,
                "latitude": 8.763465685547658
            },
            "shifts": []
        },
        {
            "id": 59,
            "name": "Melvetoor",
            "uber_h3_index_3km": 605173823616057343,
            "boundary": [
                {
                    "lat": 8.696863305379427,
                    "lng": 76.7792999589351
                },
                {
                    "lat": 8.731637257139358,
                    "lng": 76.77978317644637
                },
                {
                    "lat": 8.7497583015092,
                    "lng": 76.75121393199716
                },
                {
                    "lat": 8.73310776628172,
                    "lng": 76.72217455149767
                },
                {
                    "lat": 8.698345653245733,
                    "lng": 76.72169809795406
                },
                {
                    "lat": 8.680222236222498,
                    "lng": 76.75025426295936
                }
            ],
            "center_point": {
                "longitude": 76.75073732996496,
                "latitude": 8.714989086629656
            },
            "shifts": []
        },
        {
            "id": 60,
            "name": "Kallambalam",
            "uber_h3_index_3km": 605173575850131455,
            "boundary": [
                {
                    "lat": 8.748288852519144,
                    "lng": 76.80884549385691
                },
                {
                    "lat": 8.783070936066471,
                    "lng": 76.80933226375636
                },
                {
                    "lat": 8.801189597505312,
                    "lng": 76.7807499438423
                },
                {
                    "lat": 8.7845285578292,
                    "lng": 76.75169393150792
                },
                {
                    "lat": 8.7497583015092,
                    "lng": 76.75121393199716
                },
                {
                    "lat": 8.731637257139358,
                    "lng": 76.77978317644637
                }
            ],
            "center_point": {
                "longitude": 76.7802697902345,
                "latitude": 8.766412250428113
            },
            "shifts": []
        },
        {
            "id": 61,
            "name": "Kadinamkulam",
            "uber_h3_index_3km": 605173823750275071,
            "boundary": [
                {
                    "lat": 8.5910231760842,
                    "lng": 76.83547160230239
                },
                {
                    "lat": 8.625804318831333,
                    "lng": 76.8359612550223
                },
                {
                    "lat": 8.643951556700745,
                    "lng": 76.80738585353562
                },
                {
                    "lat": 8.627319966347699,
                    "lng": 76.77833385609583
                },
                {
                    "lat": 8.592550630112568,
                    "lng": 76.77785097069187
                },
                {
                    "lat": 8.574401077205996,
                    "lng": 76.80641331741958
                }
            ],
            "center_point": {
                "longitude": 76.80690280917793,
                "latitude": 8.609175120880424
            },
            "shifts": []
        },
        {
            "id": 62,
            "name": "Venjaramoodu",
            "uber_h3_index_3km": 605173822810750975,
            "boundary": [
                {
                    "lat": 8.64091275626931,
                    "lng": 76.92272537697411
                },
                {
                    "lat": 8.67571389935331,
                    "lng": 76.92322536770665
                },
                {
                    "lat": 8.693869549639892,
                    "lng": 76.89462083584058
                },
                {
                    "lat": 8.677226363090208,
                    "lng": 76.86552934943735
                },
                {
                    "lat": 8.642436987413335,
                    "lng": 76.86503614046833
                },
                {
                    "lat": 8.624279030340166,
                    "lng": 76.89362763813648
                }
            ],
            "center_point": {
                "longitude": 76.89412745142725,
                "latitude": 8.65907309768437
            },
            "shifts": []
        },
        {
            "id": 63,
            "name": "Nagaroor",
            "uber_h3_index_3km": 605173822273880063,
            "boundary": [
                {
                    "lat": 8.693869549639892,
                    "lng": 76.89462083584058
                },
                {
                    "lat": 8.728667096160564,
                    "lng": 76.89511760553229
                },
                {
                    "lat": 8.746809673093926,
                    "lng": 76.86651610669738
                },
                {
                    "lat": 8.73015703857749,
                    "lng": 76.83743088680598
                },
                {
                    "lat": 8.695371275622472,
                    "lng": 76.83694089723554
                },
                {
                    "lat": 8.677226363090208,
                    "lng": 76.86552934943735
                }
            ],
            "center_point": {
                "longitude": 76.86602594692485,
                "latitude": 8.712016832697424
            },
            "shifts": []
        },
        {
            "id": 64,
            "name": "Varkala",
            "uber_h3_index_3km": 605173577058091007,
            "boundary": [
                {
                    "lat": 8.7497583015092,
                    "lng": 76.75121393199716
                },
                {
                    "lat": 8.7845285578292,
                    "lng": 76.75169393150792
                },
                {
                    "lat": 8.802636424691983,
                    "lng": 76.72312778621856
                },
                {
                    "lat": 8.785976436189433,
                    "lng": 76.69409473519853
                },
                {
                    "lat": 8.75121803457919,
                    "lng": 76.69362149796667
                },
                {
                    "lat": 8.73310776628172,
                    "lng": 76.72217455149767
                }
            ],
            "center_point": {
                "longitude": 76.72265440573109,
                "latitude": 8.76787092018012
            },
            "shifts": []
        },
        {
            "id": 65,
            "name": "Pongumoodu",
            "uber_h3_index_3km": 605173575715913727,
            "boundary": [
                {
                    "lat": 8.746809673093926,
                    "lng": 76.86651610669738
                },
                {
                    "lat": 8.7816035562855,
                    "lng": 76.86700965506606
                },
                {
                    "lat": 8.799733005833655,
                    "lng": 76.83841120306731
                },
                {
                    "lat": 8.783070936066471,
                    "lng": 76.80933226375636
                },
                {
                    "lat": 8.748288852519144,
                    "lng": 76.80884549385691
                },
                {
                    "lat": 8.73015703857749,
                    "lng": 76.83743088680598
                }
            ],
            "center_point": {
                "longitude": 76.83792426820833,
                "latitude": 8.764943843729364
            },
            "shifts": []
        }
    ],
    "number_of_zones": 21
}




# Define the projection systems
h3_projection = Proj(proj='latlong', datum='WGS84')
osm_projection = Proj(proj='latlong', datum='WGS84')

# Create a Folium map centered around the first zone
map_center = [zone_data["zones"][0]["boundary"][0]["lat"], zone_data["zones"][0]["boundary"][0]["lng"]]
mymap = folium.Map(location=map_center, zoom_start=12)
# Project and add zone boundaries to the map
for zone in zone_data["zones"]:
    boundary_coords = [(point["lat"], point["lng"]) for point in zone["boundary"]]
    osm_boundary_coords = [transform(h3_projection, osm_projection, lat, lng) for lat, lng in boundary_coords]
    polygon = Polygon(osm_boundary_coords)

    folium.Polygon(
        locations=polygon.exterior.coords[:],
        popup=zone["name"],
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.3,
    ).add_to(mymap)
# Save the map to an HTML file
mymap.save('index.html')