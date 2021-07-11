// External resources
import 'popper.js';
import 'jquery';
import 'bootstrap';
import 'bootstrap-table';
import '@fortawesome/fontawesome-free/js/all.js';

import $ from 'jquery';
import Choices from "choices.js";
import Sortable from "sortablejs";
import Chart from 'chart.js/auto';
import tippy from 'tippy.js';

// Ugly assign stuff on window to use in templates
// Please remove me!
window.$ = $;
window.Choices = Choices;
window.Sortable = Sortable;
window.Chart = Chart;
window.tippy = tippy;

// Custom resources
import './javascript/resource-calendar';
import './javascript/reservation-calendar'
import dateSorter from "./javascript/date-sorter";
import './javascript/tinymce'

window.dateSorter = (a, b) => dateSorter(a, b);
