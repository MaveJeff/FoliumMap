import folium

# Create a Folium map object
m = folium.Map(location=[-35.545058,139.389839], zoom_start=13)

# Define the bounds of the image, in latitude and longitude coordinates
# bounds = [[-35.9436997, 135.3596558], [-32.8148253, 141.4481992]]


# Create a Folium image overlay object

'''
image_overlay = folium.raster_layers.ImageOverlay(
    'output_962.png',
    bounds=bounds,
    opacity=1,
    name='Image Overlay',
    show=True,
    interactive=True,
    cross_origin=False,
    zindex=1
)
'''


# Add the image overlay to the map
image_overlay.add_to(m)

# Save the map as an HTML file
m.save('map.html')