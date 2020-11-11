// Autocomplete for address form

let placeSearch;
let autocomplete;

const componentForm = {
  street_number: "short_name",
  route: "long_name",
  locality: "long_name",
  administrative_area_level_2: "long_name",
  administrative_area_level_1: "long_name",
  country: "long_name",
  postal_code: "short_name"
};

function initAutocomplete() {
  // Create the autocomplete object, restricting the search predictions to
  // geographical location types.
  autocomplete = new google.maps.places.Autocomplete(
    document.getElementById("address_search"),
    { types: ["geocode"] }
  );
  // Avoid paying for data that you don't need by restricting the set of
  // place fields that are returned to just the address components.
  autocomplete.setFields(["address_component"]);
  // When the user selects an address from the drop-down, populate the
  // address fields in the form.
  autocomplete.addListener("place_changed", fillInAddress);
}

function fillInAddress() {
  // Get the place details from the autocomplete object.
  const place = autocomplete.getPlace();

  for (const component in componentForm) {
    document.getElementById(component).value = "";
    document.getElementById(component).disabled = false;
  }
  console.log(place.address_components)

  // Get each component of the address from the place details,
  // and then fill-in the corresponding field on the form.
  for (const component of place.address_components) {
    //console.log(component);
    const addressType = component.types[0];

    if (componentForm[addressType]) {
      const val = component[componentForm[addressType]];
      document.getElementById(addressType).value = val;
      
    }
  }
  if(document.getElementById('form-address-div')) {
    changeCSSClass("form-address-div", 'show');
  }
  //getLatLong();
}


const getLatLong = () => {
  const address = document.getElementById("address_search").value;
  console.log(address)
  const geocoder = new google.maps.Geocoder();
  geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      const latitude = results[0].geometry.location.lat();
      document.getElementById("lat").value=latitude;
      const longitude = results[0].geometry.location.lng();
      document.getElementById("lng").value=longitude;
    } 
  });
}

