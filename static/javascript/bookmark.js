if (document.readyState == 'loading') {
	document.addEventListener('DOMContentLoaded', ready)
} else {
	ready()
}

function ready() {
	var bookmarkItem = document.getElementsByClassName('bookmark-btn')
	for (var i = 0; i < bookmarkItem.length; i++) {
		var button = bookmarkItem[i]
		button.addEventListener('click', bookmarkClicked)
	}
}

function bookmarkClicked() {
    if (user === 'AnonymousUser'){
        alert('Please Login or Register to access this feature')
    } else {
        var button = event.target
        var list = button.parentElement
        var productId= this.dataset.product
        var action = this.dataset.action
        if (action == 'remove') {
            M.toast({html: 'Mark Removed!', classes: 'rounded'})
            button.innerHTML = 'bookmark_outline'
            list.setAttribute('data-action', 'add')
            list.setAttribute('title', 'Add Bookmark')
            updateBookmarkList(productId, action)
        } else if (action == 'add') {
            M.toast({html: 'Bookmarked!', classes: 'rounded'})
            button.innerHTML = 'bookmark'
            list.setAttribute('data-action', 'remove')
            list.setAttribute('title', 'Remove Bookmark')
            updateBookmarkList(productId, action)
        }
    }

}

function updateBookmarkList(productId, action) {

    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })
}