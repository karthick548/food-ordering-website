$(function () {



  // Main Menu JS
  $(window).scroll(function () {
    if ($(this).scrollTop() < 50) {
      $("nav").removeClass("site-top-nav");
      $("#back-to-top").fadeOut();
    } else {
      $("nav").addClass("site-top-nav");
      $("#back-to-top").fadeIn();
    }
  });

  // Shopping Cart Toggle JS
  $("#shopping-cart").on("click", function () {
    $("#cart-content").toggle("blind", "", 500);
  });

  // Back-To-Top Button JS
  $("#back-to-top").click(function (event) {
    event.preventDefault();
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      1000
    );
  });

  // Delete Cart Item JS
  $(document).on("click", ".btn-delete", function (event) {
    event.preventDefault();
    $(this).closest("tr").remove();
    updateTotal();
  });

  // Update Total Price JS
  function updateTotal() {
    let total = 0;
    $("#cart-content tr").each(function () {
      const rowTotal = parseFloat($(this).find("td:nth-child(5)").text().replace("$", ""));
      if (!isNaN(rowTotal)) {
        total += rowTotal;
      }
    });
    $("#cart-content th:nth-child(5)").text("$" + total.toFixed(2));
    $(".tbl-full th:nth-child(6)").text("$" + total.toFixed(2));
  }
});









$(function () {

  // NAVBAR SCROLL EFFECT
  $(window).scroll(function () {
    if ($(this).scrollTop() < 50) {
      $("nav").removeClass("site-top-nav");
      $("#back-to-top").fadeOut();
    } else {
      $("nav").addClass("site-top-nav");
      $("#back-to-top").fadeIn();
    }
  });

 
  // SHOW / HIDE CART
$("#shopping-cart").on("click", function () {
      // ← FIXED
});




  // BACK TO TOP
  $("#back-to-top").click(function (event) {
    event.preventDefault();
    $("html, body").animate({ scrollTop: 0 }, 1000);
  });

  // ========= DYNAMIC CART SYSTEM =========

  let cart = [];

  // ADD TO CART
  $(".food-menu-box form").submit(function (e) {
    e.preventDefault();

    let name = $(this).find("h4").text();
    let price = parseFloat($(this).find(".food-price").text().replace("$", ""));
    let qty = parseInt($(this).find("input[type=number]").val());
    let img = $(this).find("img").attr("src");

    // Check if same item already in cart
    let exists = cart.find(item => item.name === name);

    if (exists) {
      exists.qty += qty;
      exists.total = exists.qty * exists.price;
    } else {
      cart.push({
        name: name,
        price: price,
        qty: qty,
        total: qty * price,
        img: img
      });
    }

    updateCart();
  });

  // DELETE ITEM
  $(document).on("click", ".btn-delete", function (e) {
    e.preventDefault();

    let name = $(this).data("name");
    cart = cart.filter(item => item.name !== name);

    updateCart();
  });

  // UPDATE CART TABLE
  function updateCart() {
    let html = `
      <tr>
        <th>Food</th>
        <th>Name</th>
        <th>Price</th>
        <th>Qty</th>
        <th>Total</th>
        <th>Action</th>
      </tr>
    `;

    let grandTotal = 0;

    cart.forEach(item => {
      grandTotal += item.total;

      html += `
        <tr>
          <td><img src="${item.img}" width="45"></td>
          <td>${item.name}</td>
          <td>$${item.price.toFixed(2)}</td>
          <td>${item.qty}</td>
          <td>$${item.total.toFixed(2)}</td>
          <td><a href="#" class="btn-delete" data-name="${item.name}">&times;</a></td>
        </tr>
      `;
    });

    html += `
      <tr>
        <th colspan="4">Total</th>
        <th>$${grandTotal.toFixed(2)}</th>
        <th></th>
      </tr>
    `;

    $(".cart-table").html(html);

    // Update badge count
    $(".badge").text(cart.length);
  }
  function updateCart() {

    let html = `
      <tr>
        <th>Food</th>
        <th>Name</th>
        <th>Price</th>
        <th>Qty</th>
        <th>Total</th>
        <th>Action</th>
      </tr>
    `;

    let grandTotal = 0;

    cart.forEach(item => {
        grandTotal += item.total;

        html += `
            <tr>
                <td><img src="${item.img}" width="45"></td>
                <td>${item.name}</td>
                <td>$${item.price}</td>
                <td>${item.qty}</td>
                <td>$${item.total}</td>
                <td><a href="#" class="btn-delete" data-name="${item.name}">&times;</a></td>
            </tr>
        `;
    });

    html += `
        <tr>
            <th colspan="4">Total</th>
            <th>$${grandTotal}</th>
            <th></th>
        </tr>
    `;

    $(".cart-table").html(html);
    $(".badge").text(cart.length);

    // ⭐ STEP 1 → THIS LINE (SAVE CART TO LOCAL STORAGE)
    localStorage.setItem("cartItems", JSON.stringify(cart));

}
$(".cart-table").html(html);
$(".badge").text(cart.length);

// ⭐ SAVE CART
localStorage.setItem("cartItems", JSON.stringify(cart));


});



