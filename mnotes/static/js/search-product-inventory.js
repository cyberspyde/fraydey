const searchFieldInventory = document.querySelector('#searchFieldInventory');
const tableOutputInventory = document.querySelector('.tableOutputInventory');
const appTableInventory = document.querySelector('.appTableInventory');
const tableOutputInventoryTable = document.querySelector('.tableOutputInventoryTable');

searchFieldInventory.addEventListener("keyup", (e) => {
	const searchValue = e.target.value;

	if(searchValue.trim().length > 0) {
		console.log("searchValue", searchValue);
		tableOutputInventory.innerHTML = "";
		tableOutputInventoryTable.innerHTML = `				<thead>
					    <tr>
					      <th scope="col">Nom</th>
					      <th scope="col" class="text-nowrap">Tan narx</th>
					      <th scope="col">Son</th>
					    </tr>
					  </thead>`;
		fetch("/search-product", {
			body: JSON.stringify({ searchText: searchValue }),
			method: "POST",
		})
			.then((res) => res.json())

			.then((data) => {
				console.log("data", data);
				if(data.length == 0){
					tableOutputInventory.innerHTML = "Mahsulot topilmadi!";
					tableOutputInventoryTable.innerHTML = "Mahsulot topilmadi!";

				}else{
					
				data.forEach((item) => {
				if( item.product_count > 0 ){
				tableOutputInventoryTable.innerHTML += `
					  	<tbody>
					  	
					    <tr>
					    	
					      <td><a href="../productview/${item.id}" class="link-primary">${item.product_name}</a></td>
					      <td>${item.product_price_initial}</td>
					      <td>${item.product_count}</td>     
					    	
					    </tr>
						
					    
					  </tbody>
				`;

				}else{
				tableOutputInventoryTable.innerHTML += `


					  	<tbody>
					  	
					    <tr>
					    	
					      <td><a href="../productview/${item.id}" class="link-primary">${item.product_name}</a></td>
					      <td>${item.product_price_initial}</td>
					      <td class="text-danger">Qolmagan</td>     
					    	
					    </tr>
						
					    
					  </tbody>
				`;
			}

				if( item.product_img.length > 0){
							tableOutputInventory.innerHTML += `

				<div class="row row-cols-2 d-flex justify-content-center text-center">
					
						<!-- Single Product -->
						<div class="">
								<div id="product-1" class="single-product" style="">
									<a href="../productview/${item.id}">
															    
									    <div class="part-1 border" style="background:  url('../../../media/${item.product_img}') no-repeat center; background-size: 100% auto;">
								</div>
										<div class="part-2" >
												<h3 class="product-title"><a href="{% url 'productview' product.id %}"><b class="text-uppercase text-dark"> ${item.product_name} </b> </a></h3>
												<h5 class="product-price"> Tan narx : ${item.product_price_initial} Sum</h5>
										</div>
								</div>
										</a>
						</div>
					
				</div>
				</div>
							`;
						} else {
							tableOutputInventory.innerHTML += `

				<div class="row row-cols-2 d-flex justify-content-center text-center">
					
						<!-- Single Product -->
						<div class="">
								<div id="product-1" class="single-product" style="">
									<a href="{% url 'productview' product.id %}">
															    
									 <div role="img" class="part-1 text-center my-auto row border"><span class="text-uppercase text-danger text-center align-self-center"> Rasm mavjud emas </span>
										</div>
										<div class="part-2" >
												<h3 class="product-title"><a href="{% url 'productview' product.id %}"><b class="text-uppercase text-dark"> ${item.product_name} </b> </a></h3>
												<h5 class="product-price"> Tan narx : ${item.product_price_initial} Sum</h5>
										</div>
										</div>
										</a>
										</div>
					
				</div>
				</div>
							`;
						}
						
						
					});
					
				}

			})

	}else{
		tableOutputInventory.innerHTML  = " <p> Mahsulotni boshidan qidiring yoki Mahsulotlar bo'limiga qayta yuklang. </p>";
		tableOutputInventoryTable.innerHTML = " <p> Mahsulotni boshidan qidiring yoki Mahsulotlar bo'limiga qayta yuklang. </p>";

	}
});
