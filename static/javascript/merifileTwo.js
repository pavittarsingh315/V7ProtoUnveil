/* Slides */
const slider = document.querySelector('.slider');
M.Slider.init(slider, {
	indicators: false,
	height: 600,
	interval: 7000,
	transition: 500
});

M.AutoInit();


/* Autocomplete */
const ac =document.querySelector
('.autocomplete');
M.Autocomplete.init(ac, {
    data: {
//        'Google': null,
//        'Macbook Air': null,
//        'Macbook Pro': null,
//        'iMac': null,
//        'iPad': null,
//        'iPhone': null,
//        'Airpods': null,
//        'Graphics card': null,
//        'AMD Ryzen': null,
//        'Intel i3': null,
//        'Intel i5': null,
//        'Intel i7': null,
//        'Intel i9': null,
    },
    limit:10,
    minLength:1,
});