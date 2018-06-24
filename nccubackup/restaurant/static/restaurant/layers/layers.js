var lyr_OpenStreetMap = new ol.layer.Tile({
                        source: new ol.source.TileWMS(({
                          url: "http://wmsproxy.appspot.com/CloudMaps.jsp",
                          params: {"LAYERS": "OpenStreetMap", "TILED": "true"},
                        })),
                        title: "OpenStreetMap",
                        
                        
                      });var format_ = new ol.format.GeoJSON();
var features_ = format_.readFeatures(geojson_, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_ = new ol.source.Vector();
jsonSource_.addFeatures(features_);var lyr_ = new ol.layer.Vector({
                source:jsonSource_, 
                style: style_,
                title: "校園建築"
            });

lyr_OpenStreetMap.setVisible(true);lyr_.setVisible(true);
var layersList = [lyr_OpenStreetMap,lyr_];
lyr_.set('fieldAliases', {'name': 'name', 'website': 'website', 'imformatio': 'imformatio', 'image': 'image', });
lyr_.set('fieldImages', {'name': 'TextEdit', 'website': 'TextEdit', 'imformatio': 'TextEdit', 'image': 'TextEdit', });
lyr_.set('fieldLabels', {'name': 'no label', 'website': 'no label', 'imformatio': 'no label', 'image': 'no label', });
lyr_.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});