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
    Canada: 'red',
    France: 'red',
    England: 'red',
    Italy: 'red',
    Russia: 'red',
    Spain: 'red',
    Turkey: 'red',
    Germany: 'red',
  }
});

bubble_map.bubbles([
  {
    name: 'San Francisco',
    fillKey: 'USA',
    radius: 5,
    latitude: 37.782158,
    longitude: -122.434356
  },
  {
    name: 'Los Angeles',
    fillKey: 'USA',
    radius: 5,
    latitude: 34.069570,
    longitude: -118.444698
  },
  {
    name: 'Seattle',
    fillKey: 'USA',
    radius: 5,
    latitude: 47.656028,
    longitude: -122.309985
  },
  {
    name: 'Portland',
    fillKey: 'USA',
    radius: 5,
    latitude: 45.546765,
    longitude: -122.621463
  },
  {
    name: 'Houston',
    fillKey: 'USA',
    radius: 5,
    latitude: 29.726584,
    longitude: -95.380692
  },
  {
    name: 'NYC',
    fillKey: 'USA',
    radius: 5,
    latitude: 40.687695,
    longitude: -73.945349
  },
  {
    name: 'Chicago',
    fillKey: 'USA',
    radius: 5,
    latitude: 41.854194,
    longitude: -87.681344
  },
  {
    name: 'Boston',
    fillKey: 'USA',
    radius: 5,
    latitude: 42.362860,
    longitude: -71.095266
  },
  {
    name: 'Las Vegas',
    fillKey: 'USA',
    radius: 5,
    latitude: 36.216460,
    longitude: -115.269070
  },
  {
    name: 'Miami',
    fillKey: 'USA',
    radius: 5,
    latitude: 25.779232,
    longitude: -80.194345
  },
  {
    name: 'Toronto',
    fillKey: 'Canada',
    radius: 5,
    latitude: 43.676043,
    longitude: -79.401404
  },
  {
    name: 'Vancouver',
    fillKey: 'Canada',
    radius: 5,
    latitude: 49.277355,
    longitude: -123.121510
  },
  {
    name: 'Paris',
    fillKey: 'France',
    radius: 5,
    latitude: 48.861344,
    longitude: 2.346717
  },
  {
    name: 'London',
    fillKey: 'England',
    radius: 5,
    latitude: 51.510697,
    longitude: -0.135244
  },
  {
    name: 'Rome',
    fillKey: 'Italy',
    radius: 5,
    latitude: 41.897295,
    longitude: 12.491366
  },
  {
    name: 'Florence',
    fillKey: 'Italy',
    radius: 5,
    latitude: 43.775000,
    longitude: 11.253328
  },
  {
    name: 'Moscow',
    fillKey: 'Russia',
    radius: 5,
    latitude: 55.755975,
    longitude: 37.625628
  },
  {
    name: 'Madrid',
    fillKey: 'Spain',
    radius: 5,
    latitude: 40.417442,
    longitude: -3.700136
  },
  {
    name: 'Istanbul',
    fillKey: 'Turkey',
    radius: 5,
    latitude: 41.014648,
    longitude: 28.895450
  },
  {
    name: 'Munich',
    fillKey: 'Germany',
    radius: 5,
    latitude: 48.141625,
    longitude: 11.578915
  }
], {
  popupTemplate: function(geo, data) {
    return '<div class="hoverinfo">' + data.name + '</div>'
  }
});






