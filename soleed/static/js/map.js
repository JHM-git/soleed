// Google maps for school page 

const initMap = function(locationObj) {
  const location = locationObj;
  const map = new google.maps.Map(document.getElementById('map'), {zoom: 17, center: location});
  const marker = new google.maps.Marker({position: location, map: map});
}

latLngNum = {
  lat: parseFloat(latLng.lat),
  lng: parseFloat(latLng.lng)
}

google.maps.event.addDomListener(window, 'load', initMap(latLngNum));


//const testFunction = function() {
//  console.log('This is working');
//}