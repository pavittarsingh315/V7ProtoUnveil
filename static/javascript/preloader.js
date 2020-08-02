if (document.readyState == 'loading') {
	document.addEventListener('DOMContentLoaded', ready)
} else {
	ready()
}

function ready() {
	document.querySelector('.mainsearchcontent').style.display='none';
    document.querySelector('.promos').style.display='block';
    document.querySelector('.preloaderheader').style.display='block';
    document.querySelector('.preloaderrightsnotice').style.display='block';
    document.querySelector('.prodiv').classList.add('progress');
    document.querySelector('.proind').classList.add('indeterminate');
    setTimeout(function(){ document.querySelector('.prodiv').classList.remove('progress');
    document.querySelector('.proind').classList.remove('indeterminate');
    document.querySelector('.mainsearchcontent').style.display='block';
    document.querySelector('.promos').style.display='none';
    document.querySelector('.preloaderrightsnotice').style.display='none';
    document.querySelector('.preloaderheader').style.display='none'; },10000);
}

function searchpreloader() {
    document.querySelector('.mainsearchcontent').style.display='none';
    document.querySelector('.prodiv').classList.add('progress');
    document.querySelector('.proind').classList.add('indeterminate');
    document.querySelector('.preloaderheader').style.display='block';
    document.querySelector('.preloaderrightsnotice').style.display='block';
    setTimeout(function(){ document.querySelector('.prodiv').classList.remove('progress');
    document.querySelector('.proind').classList.remove('indeterminate');
    document.querySelector('.mainsearchcontent').style.display='block';
    document.querySelector('.preloaderrightsnotice').style.display='none';
    document.querySelector('.preloaderheader').style.display='none';
    },30000);
}