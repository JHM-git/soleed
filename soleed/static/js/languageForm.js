

const sendData = (e, form, ids, urlToSend, bt, reload) => {
  e = e || window.Event; 
  if($(ids[0]).val().length === 0 || $(ids[1]).val().length === 0) {
    alert('Por favor, rellena todos los datos');
    e.preventDefault();
  } else if(!document.getElementById(ids[2]).checked && !document.getElementById(ids[3]).checked) {
    alert('Por favor, elige si el idioma es obligatorio');
    e.preventDefault();
  } else {
    const data = $('.' + form).serialize(); // serializes the form's elements.
    $.ajax({
        type: "POST",
        url: urlToSend, // send the form data here.
        datatype: "json",
        data: data, 
    })
    .done(function(json) {
      if(json.data.error) {
        alert('Idioma ya está en la oferta del colegio. Puedes editarlo abajo');
        console.log(json);
      } else {
        alert('Hemos registrado los cambios.');
        console.log(json);
        $(reload).load(window.location.href + " " + reload);
        document.getElementById(form).reset();
        document.getElementById(bt).click();
      }
    })
    .fail(function(xhr, status, errorThrown) {
      alert('Lo siento, ha ocurrido un problema');
      console.log('Error: ' + errorThrown);
      console.log('Status: ' + status);
      console.dir(xhr) 
    });
    e.preventDefault(); // block the traditional submission of the form.
    // Inject our CSRF token into our AJAX request.
    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", "{{ language_form.csrf_token._value() }}")
        }
      }
    })
  } 
};

const removeData = (e, form, urlToSend, bt, reload, reload2) => {
  e = e || window.Event;
  const data = $('.' + form).serialize(); // serializes the form's elements.
  $.ajax({
    type: "POST",
    url: urlToSend, // send the form data here.
    datatype: "json",
    data: data, 
  })
  .done(function(json) {
    alert('Hemos registrado los cambios.');
    console.log(json);
    $(reload).load(window.location.href + " " + reload);
    document.getElementById(bt).click();
  })
  .fail(function(xhr, status, errorThrown) {
    alert('Lo siento, ha ocurrido un problema');
    console.log('Error: ' + errorThrown);
    console.log('Status: ' + status);
    console.dir(xhr) 
  });
  e.preventDefault(); // block the traditional submission of the form.
  // Inject our CSRF token into our AJAX request.
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", "{{ remove_language_form.csrf_token._value() }}")
      }
    }
  })
};

async function removeLang(e, form, urlToSend, bt, reload, reloadls) {
  await removeData(e, form, urlToSend, bt, reload);
  setTimeout(function(){
    $(reloadls[0]).load(window.location.href + " " + reloadls[0]);
    $(reloadls[1]).load(window.location.href + " " + reloadls[1]);
  }, 500);
};

async function addLang(e, form, ids, urlToSend, bt, reload, reloadls) {
  await sendData(e, form, ids, urlToSend, bt, reload);
  setTimeout(function(){
    $(reloadls[0]).load(window.location.href + " " + reloadls[0]);
    $(reloadls[1]).load(window.location.href + " " + reloadls[1]);
  }, 500);
}
