if (document.readyState == 'loading') {
	document.addEventListener('DOMContentLoaded', ready)
} else {
	ready()
}

// I replaced all the sessionStorage with sessionStorage because it's more convenient

function ready() {
	var removeCartItemButtons = document.getElementsByClassName('btn-danger')
	for (var i = 0; i < removeCartItemButtons.length; i++) {
		var button = removeCartItemButtons[i]
		button.addEventListener('click', removeCartItem)
	}

	var addToCartButtons = document.getElementsByClassName('shop-item-button')
	for (var i = 0; i < addToCartButtons.length; i++) {
		var button = addToCartButtons[i]
		button.addEventListener('click', addToCartClicked)
	}

    document.getElementsByClassName('btn-purchase')[0].addEventListener('click', purchaseClicked);
	displayCart();


	// this allows the cart number to display after refresh
	let productNumbers = sessionStorage.getItem('itemNumbers');
	if(productNumbers) {
		document.querySelector('.badge').textContent = productNumbers;
        document.querySelector('.badge-sidenav').textContent = productNumbers;
	}

	// this allows the total from the session storage to be accessed in the cart modal
    let total = sessionStorage.getItem('totalCost')
    if(total) {
        document.querySelector('.cart-total-price').textContent = 'Total: $' + total;
    } else {
        document.querySelector('.cart-total-price').textContent = 'Cart is Empty';
    }

}


function purchaseClicked() {
	// this clears the session storage when clear cart button is hit
	let result = window.confirm('You are about to clear your cart!')
	if(result == true) {
		alert('Cart Cleared.')
		var cartItems = document.getElementsByClassName('cart-items')[0]
		while (cartItems.hasChildNodes()) {
			cartItems.removeChild(cartItems.firstChild)
		}
		updateCartTotal()
		sessionStorage.clear();
		document.querySelector('.badge').textContent = 0;
		document.querySelector('.badge-sidenav').textContent = 0;
	} else {
		return
	}
}


function removeCartItem(event) {
	var buttonClicked = event.target
	buttonClicked.parentElement.parentElement.parentElement.remove()
	updateCartTotal()



	// this is what deletes items from session storage
	let sessionItem =  buttonClicked.parentElement.parentElement.parentElement.children[0].children[1].innerText
	let sessionItemCart = JSON.parse(sessionStorage.getItem('productInCart'))
	let product = {
		name: sessionItem,
	}
	let sessionKey = sessionItemCart[product.name].name
	if(sessionKey == sessionItem) {
		var sessionItemStorage = JSON.parse(sessionStorage.getItem('productInCart'))
		var key = sessionKey
		delete sessionItemStorage[key]
		//console.log(sessionItemStorage)
	}
	sessionStorage.setItem('productInCart', JSON.stringify(sessionItemStorage));





	// when you remove an item from the cart this takes it off the session storage
	let cartNumbers = sessionStorage.getItem('itemNumbers');
	sessionStorage.setItem('itemNumbers', cartNumbers - 1);
	document.querySelector('.badge').textContent = cartNumbers - 1;
	document.querySelector('.badge-sidenav').textContent = cartNumbers - 1;
}


function addToCartClicked(event) {
    var button = event.target
    var shopItem = button.parentElement.parentElement.parentElement
    var title = shopItem.getElementsByClassName('shop-item-title')[0].innerText
    var price = shopItem.getElementsByClassName('shop-item-price')[0].innerText
    var imageSrc = shopItem.getElementsByClassName('shop-item-image')[0].src
    var itemLink = shopItem.getElementsByClassName('link-title')[0].href


    /* i forgot what this is for so if theres a glitch uncomment this maybe itll fix it
    let productNumbers = sessionStorage.getItem('itemNumbers');
    if(productNumbers) {
        document.querySelector('.badge').textContent = productNumbers;
        document.querySelector('.badge-sidenav').textContent = productNumbers;
    }*/


    addItemToCart(title, price, imageSrc, itemLink)
    updateCartTotal()
}


function addItemToCart(title, price, imageSrc, itemLink){
	var cartRow = document.createElement('div')
	cartRow.classList.add('collection-item')
	cartRow.classList.add('avatar')
	cartRow.classList.add('cart-row')
	var cartItems = document.getElementsByClassName('cart-items')[0]
	var cartItemNames = cartItems.getElementsByClassName('cart-item-title')
	for (var i = 0; i < cartItemNames.length; i++) {
		if (cartItemNames[i].innerText == title) {
			alert('This item is already in your cart.')
			return
		}
	}


	// this actually adds the session storage amount to the cart button display
	let productNumbers = sessionStorage.getItem('itemNumbers');
	productNumbers = parseInt(productNumbers);
	if(productNumbers) {
		sessionStorage.setItem('itemNumbers', productNumbers + 1);
		document.querySelector('.badge').textContent = productNumbers + 1;
        document.querySelector('.badge-sidenav').textContent = productNumbers + 1;
	} else {
		sessionStorage.setItem('itemNumbers', 1);
		document.querySelector('.badge').textContent = 1;
        document.querySelector('.badge-sidenav').textContent = 1;
	}




// this takes the name price and image of item added to cart and puts it into the session storage
	let product = {
			name: title,
			imageurl: imageSrc,
			price: price,
			itemLink: itemLink,
		}
	setItems(product);
	function setItems(product) {
		let cartItems = sessionStorage.getItem('productInCart');
		cartItems = JSON.parse(cartItems);
		if(cartItems != null) {
			if (cartItems[product.name] == undefined) {
				cartItems = {
					...cartItems,
					[product.name]: product
				}
			}
		} else {
			cartItems = {
				[product.name] : product
			};
		};
		sessionStorage.setItem('productInCart', JSON.stringify(cartItems));
	};





	M.toast({html: 'Item Added!', classes: 'rounded'})
	var cartRowContents = `
		<div>
		    <img src="${imageSrc}" alt="" class="circle">
		    <span class="title cart-item-title">${title}</span>
		</div>
		<div class="cart-price">${price}</div>
		<a title="Go to the product page." class="btn btn-small waves-effect waves-light" style="background-color: #FE1520;" href="${itemLink}" target="_blank"><i class="large material-icons white-text">input</i></a>
		<div class="btn-danger">
			<button class="secondary-content waves-effect waves-light btn-floating backcolor-secondary-scheme"><i class="small material-icons" title="Delete Item">delete</i></button>
		</div>`
	cartRow.innerHTML = cartRowContents
	cartItems.append(cartRow)
	cartRow.getElementsByClassName('btn-danger')[0].addEventListener('click', removeCartItem)
}


function updateCartTotal() {
	var cartItemContainer = document.getElementsByClassName('cart-items')[0]
	var cartRows = cartItemContainer.getElementsByClassName('cart-row')
	var total = 0
	for (var i = 0; i < cartRows.length; i++) {
		var cartRow = cartRows[i]
		var priceElement = cartRow.getElementsByClassName('cart-price')[0]
		var price = parseFloat(priceElement.innerText.replace('$', ''))
		total = total + price
	}
	total = Math.round(total * 100) / 100

	//this makes the total of the cart in the session storage
	sessionStorage.setItem('totalCost', total);
	// this allows all the prices to get added
	document.getElementsByClassName('cart-total-price')[0].innerText = 'Total: $' + total
}



function displayCart() {
	let cartItems = sessionStorage.getItem('productInCart');
	cartItems = JSON.parse(cartItems);
	let cartContainer = document.querySelector('.cart-items');
    if ( cartItems && cartContainer ) {
        cartContainer.innerHTML = ``;
        Object.values(cartItems).map(item => {
            cartContainer.innerHTML += `
            <div class='collection-item avatar cart-row'>
                <div>
                    <img src="${item.imageurl}" alt="" class="circle">
                    <span class="title cart-item-title">${item.name}</span>
                </div>
				<div class="cart-price">${item.price}</div>
				<a title="Go to the product page." class="btn btn-small waves-effect waves-light" style="background-color: #FE1520;" href="${item.itemLink}" target="_blank"><i class="material-icons white-text">input</i></a>
                <div class="btn-danger">
					<button onclick="reloadDelete(event)" class="secondary-content waves-effect waves-light btn-floating backcolor-secondary-scheme"><i class="small material-icons" title="Delete Item">delete</i></button>
                </div>
            </div>`
        });
        total = sessionStorage.getItem('totalCost')
        document.getElementsByClassName('cart-total-price')[0].innerText = 'Total: $' + total
    }
}


// this is what deletes items from session storage after a page is reloaded
function reloadDelete(event) {
    var buttonClicked = event.target
    buttonClicked.parentElement.parentElement.parentElement.remove()
    updateCartTotal()
    // this is what deletes items from session storage
    let sessionItem =  buttonClicked.parentElement.parentElement.parentElement.children[0].children[1].innerText
    let sessionItemCart = JSON.parse(sessionStorage.getItem('productInCart'))
    let product = {
        name: sessionItem,
    }
    let sessionKey = sessionItemCart[product.name].name
    if(sessionKey == sessionItem) {
        var sessionItemStorage = JSON.parse(sessionStorage.getItem('productInCart'))
        var key = sessionKey
        delete sessionItemStorage[key]
        //console.log(sessionItemStorage)
    }
    sessionStorage.setItem('productInCart', JSON.stringify(sessionItemStorage));
    // when you remove an item from the cart this takes it off the session storage
    let cartNumbers = sessionStorage.getItem('itemNumbers');
    sessionStorage.setItem('itemNumbers', cartNumbers - 1);
    document.querySelector('.badge').textContent = cartNumbers - 1;
    document.querySelector('.badge-sidenav').textContent = cartNumbers - 1;
}
