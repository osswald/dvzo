import 'tinymce'

//Themes
import 'tinymce/themes/silver'

//Icons
import 'tinymce/icons/default'

//Plugins
import 'tinymce/plugins/advlist'
import 'tinymce/plugins/charmap'
import 'tinymce/plugins/lists'
import 'tinymce/plugins/table'
import 'tinymce/plugins/template'

tinymce.init({
    height: '600px',
    selector: '.tinymce-textarea',
    content_css: '/static/main.min.css',
    skin_url: '/static/tinymce/skins/ui/oxide',
    plugins: 'advlist lists charmap template table',
    menubar: 'edit insert format tools table',
    toolbar: 'undo redo | bold italic underline strikethrough | styleselect| alignleft aligncenter ' +
        'alignright alignjustify | outdent indent | table | numlist bullist checklist | forecolor backcolor removeformat' +
        ' | charmap | template',
    custom_undo_redo_levels: 10,
    templates: [
        {
            title: 'Abstellplanung',
            description: 'Fügt eine Tabelle für die Abstellplanung ein.',
            url: '/static/tinymce/templates/parking.html'
        },
        {
            title: 'Tourenplan vorhanden',
            description: 'Verwenden, wenn der Tourenplan vorhanden ist und mit dem Briefing mitgeschickt werden kann.',
            url: '/static/tinymce/templates/shifts_plan.html'
        },
        {
            title: 'Tourenplan nicht vorhanden',
            description: 'Verwenden, wenn der Tourenplan noch nicht vorhanden ist und nachgereicht wird.',
            url: '/static/tinymce/templates/shifts_no_plan.html'
        }],
    style_formats: [
        {
            title: 'Fahrzeuge', items: [
                {title: 'Lok', inline: 'span', classes: 'badge bg-primary'},
                {title: 'Sitzplatzwagen', inline: 'span', classes: 'badge bg-success'},
                {title: 'Gastro', inline: 'span', classes: 'badge bg-danger'},
                {title: 'Amor-Express', inline: 'span', classes: 'badge bg-warning'},
                {title: 'Gepäckwagen', inline: 'span', classes: 'badge bg-secondary'},
                {title: 'Andere', inline: 'span', classes: 'badge bg-dark'},
            ]
        },
    ]
});
