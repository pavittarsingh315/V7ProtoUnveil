//if (document.readyState == 'loading') {
//	document.addEventListener('DOMContentLoaded', ready)
//} else {
//	ready()
//}
//
//function ready() {
//    document.getElementById("searchpreloaderid").innerHTML =
//    `<div class="row container">
//        <div class="col s12 m3 l2"></div>
//        <div class="col s12 m6 l8">
//            <h6 class="center container preloaderheader">Please wait while we gather your results</h6>
//            <h6 class="center container preloaderrightsnotice">
//                All rights of the product belong to the redirected seller.
//            </h6>
//            <div class="prodiv">
//                <div class="proind"></div>
//            </div>
//        </div>
//        <div class="col s12 m3 l2"></div>
//    </div>`;
//
//	document.querySelector('.mainsearchcontent').style.display='none';
//    document.querySelector('.promos').style.display='block';
//    document.querySelector('.preloaderheader').style.display='block';
//    document.querySelector('.preloaderrightsnotice').style.display='block';
//    document.querySelector('.prodiv').classList.add('progress');
//    document.querySelector('.proind').classList.add('indeterminate');
//    setTimeout(function(){ document.querySelector('.prodiv').classList.remove('progress');
//    document.querySelector('.proind').classList.remove('indeterminate');
//    document.querySelector('.mainsearchcontent').style.display='block';
//    document.querySelector('.promos').style.display='none';
//    document.querySelector('.preloaderrightsnotice').style.display='none';
//    document.querySelector('.preloaderheader').style.display='none'; },10000);
//}