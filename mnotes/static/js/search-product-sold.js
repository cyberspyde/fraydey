const searchField = document.querySelector('#searchField');
const tableOutput = document.querySelector('.tableOutput');
const appTable = document.querySelector('.appTable');

tableOutput.style.display = "none";


searchField.addEventListener("keyup", (e) => {
	const searchValue = e.target.value;

	if(searchValue.trim().length > 0) {
		console.log("searchValue", searchValue);
		tableOutput.innerHTML = "";
		fetch("/search-product", {
			body: JSON.stringify({ searchText: searchValue }),
			method: "POST",
		})
			.then((res) => res.json())

			.then((data) => {
				console.log("data", data);
				if(data.length == 0){
					appTable.style.display = "none";
					tableOutput.style.display = "block";


					tableOutput.innerHTML = "Mahsulot topilmadi!";

				}else{
					appTable.style.display = "none";
					
					data.forEach((item) => {
						
						if( item.product_img.length > 0){
							tableOutput.innerHTML += `
								<div class="row row-cols-2 d-flex justify-content-center text-center">

				<!-- Single Product -->
				<div class="">
						<div id="product-1" class="single-product" style="">
							<a href="../productsold/${item.id}">
								

								

							    <div class="part-1 border" style="background:  url('../../../media/${item.product_img}') no-repeat center; background-size: 100% auto;">
								</div>

								
								 
								<div class="part-2">
										<h3 class="product-title"><a href="../productsold/${item.id}"><b class="text-uppercase text-dark"> ${item.product_name} </b> </a></h3>
										<h5 class="product-price"> Mahsulot tan narxi ${item.product_price_initial}</h5>
								</div>
								</div>
										</a>
									</div>

								</div>
					</div>
							`;
						} else {
							tableOutput.innerHTML += `
				<div class="row row-cols-2 d-flex justify-content-center text-center">

				<!-- Single Product -->
				<div class="">
						<div id="product-1" class="single-product" style="">
							<a href="../productsold/${item.id}">

							 
										<div role="img" class="part-1 text-center my-auto row border"><span class="text-uppercase text-danger text-center align-self-center"> Rasm mavjud emas </span></div>

								
								 
								<div class="part-2">
										<h3 class="product-title"><a href="../productsold/${item.id}"><b class="text-uppercase text-dark"> ${item.product_name} </b> </a></h3>
										<h5 class="product-price"> Mahsulot tan narxi ${item.product_price_initial}</h5>
								</div>
								</div>
							</a>
						</div>

					</div>
		</div>
							`;
						}
						
						tableOutput.style.display = "none";
					});
					tableOutput.style.display = "block";
				}

			})

	}else{
		tableOutput.style.display = "none";
		appTable.style.display = "block";
	}
});