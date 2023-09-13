const order_btn = document.getElementById("place-order");
const user_name = document.getElementById('user_name').value;
const email = document.getElementById('email').value;
const billing_address = document.getElementById('billing-address').value;
const phone = document.getElementById('phone').value;
const total = document.getElementById('total').dataset.total;

order_btn.addEventListener("click", function (e) {
    processOrder(user_name, email, billing_address, phone, subtotal, shipping, total)
})


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

async function processOrder(name, email, billing_address, phone, subtotal, shipping, total) {
    const url = "/process_order/";
    const csrftoken = getToken('csrftoken');
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'name': name,
            'email': email,
            'address': billing_address,
            'phone': phone,
            'total': total
        })
    })
    const data = await response.json();

    window.location.href = "http://127.0.0.1:8000/shop/"
}

