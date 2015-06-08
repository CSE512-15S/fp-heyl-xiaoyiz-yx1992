var bubble_map = new Datamap({
  element: document.getElementById("container"),
  scope: 'usa',
  projection: 'mercator',
  geographyConfig: {
    popupOnHover: true,
    highlightOnHover: true
  },
  fills: {
    defaultFill: '#ABDDA4',
    USA: 'blue',
    high: 'red'
  },
  data: {
    'TX': { fillKey: 'high' },
    'FL': { fillKey: 'high' },
    'NC': { fillKey: 'high' },
    'CA': { fillKey: 'high' },
    'NY': { fillKey: 'high' },
    'CO': { fillKey: 'high' }
  }
});

bubble_map.bubbles([
  {
    name: 'Birmingham',
    fillKey: 'USA',
    radius: 5,
    latitude: 33.653333,
    longitude: -86.808889
  },
  {
    name: 'Anchorage',
    fillKey: 'USA',
    radius: 5,
    latitude: 61.216667,
    longitude: -149.900000
  },
  {
    name: 'Phoenix',
    fillKey: 'USA',
    radius: 5,
    latitude: 33.450000,
    longitude: -112.066667
  },
  {
    name: 'Little Rock',
    fillKey: 'USA',
    radius: 5,
    latitude: 34.736111,
    longitude: -92.331111
  },
  {
    name: 'Los Angeles',
    fillKey: 'USA',
    radius: 5,
    latitude: 34.05,
    longitude: -118.25
  },
  {
    name: 'Denver',
    fillKey: 'USA',
    radius: 5,
    latitude: 39.761850,
    longitude: -104.881105
  },
  {
    name: 'Bridgeport',
    fillKey: 'USA',
    radius: 5,
    latitude: 41.186389,
    longitude: -73.195556
  },
  {
    name: 'Wilmington',
    fillKey: 'USA',
    radius: 5,
    latitude: 39.745833,
    longitude: -75.546667
  },
  {
    name: 'Jacksonville',
    fillKey: 'USA',
    radius: 5,
    latitude: 30.336944,
    longitude: -81.661389
  },
  {
    name: 'Atlanta',
    fillKey: 'USA',
    radius: 5,
    latitude: 33.755,
    longitude: -84.39
  },
  {
    name: 'Honolulu',
    fillKey: 'USA',
    radius: 5,
    latitude: 21.3,
    longitude: -157.816667
  },
  {
    name: 'Boise',
    fillKey: 'USA',
    radius: 5,
    latitude: 43.616667,
    longitude: -116.2
  },
  {
    name: 'Chicago',
    fillKey: 'USA',
    radius: 5,
    latitude: 41.836944,
    longitude: -87.684722
  },
  {
    name: 'Indianapolis',
    fillKey: 'USA',
    radius: 5,
    latitude: 39.73,
    longitude: -86.27
  },
  {
    name: 'Des Moines',
    fillKey: 'USA',
    radius: 5,
    latitude: 41.53,
    longitude: -93.65
  },
  {
    name: 'Wichita',
    fillKey: 'USA',
    radius: 5,
    latitude: 37.65,
    longitude: -97.43
  },
  {
    name: 'Louisville',
    fillKey: 'USA',
    radius: 5,
    latitude: 38.18,
    longitude: -85.73
  },
  {
    name: 'New Orleans',
    fillKey: 'USA',
    radius: 5,
    latitude: 30.03,
    longitude: -90.03
  },
  {
    name: 'Portland_Maine',
    fillKey: 'USA',
    radius: 5,
    latitude: 43.65,
    longitude: -70.32
  },
  {
    name: 'Baltimore',
    fillKey: 'USA',
    radius: 5,
    latitude: 39.33,
    longitude: -76.42
  },
  {
    name: 'Boston',
    fillKey: 'USA',
    radius: 5,
    latitude: 42.37,
    longitude: -71.03
  },
  {
    name: 'Detroit',
    fillKey: 'USA',
    radius: 5,
    latitude: 42.42,
    longitude: -83.02
  },
  {
    name: 'Minneapolis',
    fillKey: 'USA',
    radius: 5,
    latitude: 44.88,
    longitude: -93.22
  },
  {
    name: 'Jackson',
    fillKey: 'USA',
    radius: 5,
    latitude: 32.32,
    longitude: -90.08
  },
  {
    name: 'Kansas City',
    fillKey: 'USA',
    radius: 5,
    latitude: 39.12,
    longitude: -94.60
  },
  {
    name: 'Billings',
    fillKey: 'USA',
    radius: 5,
    latitude: 45.80,
    longitude: -108.53
  },
  {
    name: 'Omaha',
    fillKey: 'USA',
    radius: 5,
    latitude: 41.30,
    longitude: -95.90
  },
  {
    name: 'Las Vegas',
    fillKey: 'USA',
    radius: 5,
    latitude: 36.08,
    longitude: -115.17
  },
  {
    name: 'Manchester',
    fillKey: 'USA',
    radius: 5,
    latitude: 42.93,
    longitude: -71.43
  },
  {
    name: 'Newark',
    fillKey: 'USA',
    radius: 5,
    latitude: 40.70,
    longitude: -74.17
  },
  {
    name: 'Albuquerque',
    fillKey: 'USA',
    radius: 5,
    latitude: 35.05,
    longitude: -106.60
  },
  {
    name: 'New York',
    fillKey: 'USA',
    radius: 5,
    latitude: 40.77,
    longitude: -73.98
  },
  {
    name: 'Charlotte',
    fillKey: 'USA',
    radius: 5,
    latitude: 35.22,
    longitude: -80.93
  },
  {
    name: 'Fargo',
    fillKey: 'USA',
    radius: 5,
    latitude: 46.90,
    longitude: -96.80
  },
  {
    name: 'Columbus',
    fillKey: 'USA',
    radius: 5,
    latitude: 40.00,
    longitude: -82.88
  },
  {
    name: 'Oklahoma City',
    fillKey: 'USA',
    radius: 5,
    latitude: 35.40,
    longitude: -97.60
  },
  {
    name: 'Portland_Oregon',
    fillKey: 'USA',
    radius: 5,
    latitude: 45.60,
    longitude: -122.60
  },
  {
    name: 'Philadelphia',
    fillKey: 'USA',
    radius: 5,
    latitude: 39.88,
    longitude: -75.25
  },
  {
    name: 'Providence',
    fillKey: 'USA',
    radius: 5,
    latitude: 41.73,
    longitude: -71.43
  },
  {
    name: 'Columbia',
    fillKey: 'USA',
    radius: 5,
    latitude: 33.95,
    longitude: -81.12
  },
  {
    name: 'Sioux Falls',
    fillKey: 'USA',
    radius: 5,
    latitude: 43.58,
    longitude: -96.73
  },
  {
    name: 'Memphis',
    fillKey: 'USA',
    radius: 5,
    latitude: 35.05,
    longitude: -90.00
  },
  {
    name: 'Houston',
    fillKey: 'USA',
    radius: 5,
    latitude: 29.97,
    longitude: -95.35
  },
  {
    name: 'Salt Lake City',
    fillKey: 'USA',
    radius: 5,
    latitude: 40.78,
    longitude: -111.97
  },
  {
    name: 'Burlington',
    fillKey: 'USA',
    radius: 5,
    latitude: 44.47,
    longitude: -73.15
  },
  {
    name: 'Virginia Beach',
    fillKey: 'USA',
    radius: 5,
    latitude: 36.85,
    longitude: -75.98
  },
  {
    name: 'Seattle',
    fillKey: 'USA',
    radius: 5,
    latitude: 47.45,
    longitude: -122.30
  },
  {
    name: 'Charleston',
    fillKey: 'USA',
    radius: 5,
    latitude: 38.37,
    longitude: -81.60
  },
  {
    name: 'Milwaukee',
    fillKey: 'USA',
    radius: 5,
    latitude: 42.95,
    longitude: -87.90
  },
  {
    name: 'Cheyenne',
    fillKey: 'USA',
    radius: 5,
    latitude: 41.15,
    longitude: -104.82
  }
], {
  popupTemplate: function(geo, data) {
    return '<div class="hoverinfo">' + data.name + '</div>' + ""
  }
});
