if (document.readyState == 'loading') {
	document.addEventListener('DOMContentLoaded', ready)
} else {
	ready()
}

function ready() {
// place the donation request here when some searches a redirect to donates shows up do the thing below
	document.getElementById('donations').style.display='none';
	console.log('Hello World')
}

function homepreloader() {
    document.getElementById("homepreloaderid").innerHTML =
    `<div class="row">
        <div class="col s12 m3 l2"></div>
        <div class="col s12 m6 l8">
            <h6 class="center container preloaderheader">Please wait while we gather your results</h6>
            <h6 class="center container preloaderrightsnotice">
                All rights of the product belong to the redirected seller.
            </h6>
            <div class="prodiv">
                <div class="proind"></div>
            </div>
        </div>
        <div class="col s12 m3 l2"></div>
    </div>`;



    document.querySelector('.mainhomecontent').style.display='none';
    document.querySelector('.prodiv').classList.add('progress');
    document.querySelector('.proind').classList.add('indeterminate');
    document.querySelector('.preloaderheader').style.display='block';
    document.getElementById('donations').style.display='block';
    document.querySelector('.preloaderrightsnotice').style.display='block';
    setTimeout(function(){ document.querySelector('.prodiv').classList.remove('progress');
    document.querySelector('.proind').classList.remove('indeterminate');
    document.querySelector('.mainhomecontent').style.display='block';
    document.querySelector('.preloaderrightsnotice').style.display='none';
    document.querySelector('.preloaderheader').style.display='none';
    },100000);
}


