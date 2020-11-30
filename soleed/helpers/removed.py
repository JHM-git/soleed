#from edit_school(add language)

'''
if language_form.validate_on_submit():
    
    if language_form.language.data in languages:
      flash('Idioma ya está en la oferta del colegio. Puedes editarlo abajo')
      return redirect(url_for('main.edit_school'))
    language = Languages.query.filter_by(language=language_form.language.data).first()
    language_to_db = Language(language_id=language.id, 
starting_age=language_form.starting_age.data, weekly_hours=language_form.weekly_hours.data, 
description=language_form.description.data, school_id=school.id)
    if language_form.is_obligatory.data == '1':
      language_to_db.is_obligatory = True
    elif language_form.is_obligatory.data == '0':
      language_to_db.is_obligatory = False
    db.session.add(language_to_db)
    db.session.commit()
    
    flash('idioma añadido')
    return redirect(url_for('main.edit_school'))
    
'''
#from edit-language-form.html
'''
<script>
  $(document).ready(function() {
    $('.edit-language-form').submit(function (e) {
      if($('#edit_description').val().length === 0 || $('#edit_weekly_hours').val().length === 0) {
        alert('Por favor, rellena todos los datos');
        e.preventDefault();
      } else if(!document.getElementById('edit_is_obligatory-0').checked && !document.getElementById('edit_is_obligatory-1').checked) {
        alert('Por favor, elige si el idioma es obligatorio');
        e.preventDefault();
      } else {
        const url = "{{ url_for('main.edit_language') }}"; // send the form data here.
        const data = $('.edit-language-form').serialize(); // serializes the form's elements.
        $.ajax({
            type: "POST",
            url: url,
            datatype: "json",
            data: data, 
        })
        .done(function(json) {
          alert('Hemos registrado los cambios.');
          console.log(json);
          $("#languages").load(window.location.href + " #languages");
          document.getElementById('edit-language-form').reset();
          document.getElementById('edit-language-bt').click();
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
                xhr.setRequestHeader("X-CSRFToken", "{{ edit_language_form.csrf_token._value() }}")
            }
          }
        })
      }
    })
  });
</script>
'''
