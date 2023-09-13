const updateBtn = document.querySelectorAll(".update-cart");


for (i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function () {
        const productId = this.dataset.product;
        const action = this.dataset.action


        if (user === "AnonymousUser") {
            console.log("not logged in")
        }
        else {
            updateUserOrder(productId, action)
        }
    })
}

const updateUserOrder = (productId, action) => {

    const url = "/update_item/"

    sendData(url, productId, action);


}

function getToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function sendData(url, productId, action) {
    const csrftoken = getToken('csrftoken');
    const response = await fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })

    const data = await response.json();
    location.reload();
}