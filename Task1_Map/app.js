// Fetch the polygon data from the JSON file
fetch('polygon.json')
  .then(response => response.json())
  .then(data => {
    const polygonCoordinates = data.polygon.map(coord => ol.proj.fromLonLat(coord));

    // Create a polygon feature
    const polygonFeature = new ol.Feature({
      geometry: new ol.geom.Polygon([polygonCoordinates])
    });

    // Create a vector source and add the polygon feature
    const vectorSource = new ol.source.Vector({
      features: [polygonFeature]
    });

    // Create a vector layer using the vector source
    const vectorLayer = new ol.layer.Vector({
      source: vectorSource
    });

    // Initialize the map
    const map = new ol.Map({
      target: 'map', // The id of the div where the map will be rendered
      layers: [
        new ol.layer.Tile({
          source: new ol.source.OSM() // Using OpenStreetMap tile layer
        }),
        vectorLayer // Add the vector layer containing the polygon
      ],
      view: new ol.View({
        center: ol.proj.fromLonLat([17.385044, 46.055556]), // Center the map (use a central point of your polygon coordinates)
        zoom: 10 // Adjust zoom level as needed
      })
    });

    // Fit the map view to the extent of the polygon
    map.getView().fit(vectorSource.getExtent(), { padding: [100, 100, 100, 100] });
  })
  .catch(error => console.error('Error fetching the polygon data:', error));
