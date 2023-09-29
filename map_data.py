# building maps with dots


def dots_on_a_map(df, target_inspection, year, depth):
    import folium
    import folium.plugins
    import branca.colormap as cm
    import os

    # builds map structure
    cali_map = folium.Map(location=[38.78666543, -124.0731082])

    # builds color scale
    s_min, s_max = df[target_inspection].agg(['min', 'max'])
    # adjust scale to add slight buffer either end
    s_max = s_max + 1
    s_min = s_min - 1

    colormap = cm.linear.YlOrBr_09.scale(s_min, s_max)
    colormap.caption = target_inspection + ' for  ' + year + ' at ' + str(depth) + ' meters'

    for i, r in df.iterrows():
        # setting for the popup
        lat = r['lat']
        long = r['long']
        to_be_inspected = r[target_inspection]

        # make sure "lat" then "long"
        # silly mistake
        folium.Circle((lat, long),
                      radius=1,
                      fill=True,
                      color=colormap(to_be_inspected)
                      ).add_to(cali_map)

    # does not work inside of function but will work in notebook
    cali_map.add_child(colormap)

    # saving output as html
    # saving map as png, has issues with zoom
    fn = target_inspection + '_ ' + year + '_ ' + str(depth) + '.html'
    cali_map.save(fn)


# example call
#

dots_on_a_map(result_50_100, 'Salnty','1949',depth_2)