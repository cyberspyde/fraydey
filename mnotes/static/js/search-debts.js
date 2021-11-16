const searchFieldSellOnDebt = document.querySelector('#searchFieldSellOnDebt');


const tableOutputSellOnDebt = document.querySelector('.tableOutputSellOnDebt');
const appTableSellOnDebt = document.querySelector('.appTableSellOnDebt');

tableOutputSellOnDebt.style.display = "none";


searchFieldSellOnDebt.addEventListener("keyup", (e) => {
	const searchValue = e.target.value;

	if(searchValue.trim().length > 0) {
		console.log("searchValue", searchValue);
		tableOutputSellOnDebt.innerHTML = "";
		fetch("/search-product-sellondebt", {
			body: JSON.stringify({ searchText: searchValue }),
			method: "POST",
		})
			.then((res) => res.json())

			.then((sellondebt_data) => {
				console.log("sellondebt_data", sellondebt_data);
				if(sellondebt_data.length == 0){
					appTableSellOnDebt.style.display = "none";
					tableOutputSellOnDebt.style.display = "block";


					tableOutputSellOnDebt.innerHTML = "Mahsulot topilmadi!";

				}else{
					appTableSellOnDebt.style.display = "none";
					tableOutputSellOnDebt.style.display = "block";
					fullypaid_count = 0;
					partlypaid_count = 0;
					notpaid_count = 0;

					sellondebt_data.forEach((item) => {

						if (item.isfullypaid) {
							fullypaid_count += 1;

							if( fullypaid_count >= 0 && notpaid_count >= 0 && partlypaid_count >= 0){
								tableOutputSellOnDebt.innerHTML += ` 

								    <thead>
								    <tr>
								      <th scope="col">Qarzdor ismi</th>
								      <th scope="col">Mahsulot nomi</th>
								      <th scope="col">Aloqa</th>
								    </tr>
								  </thead>

								  <tbody class="bg-success">
								    <tr>
								      <td>${item.customer_name}</td>
								      <td>${item.product_name}</td>
								      <td>${item.customer_phone} <button type="button" class="link-primary" data-toggle="modal" data-target="#{{selldebt.id}}"> (batafsil) </button></td>
								    </tr>
								  </tbody>
								  `;
							}else {

							}
							
						} else if (item.ispartlypaid) {
							partlypaid_count += 1;
							if(partlypaid_count >= 1 && fullypaid_count == 0 && notpaid_count == 0){
								tableOutputSellOnDebt.innerHTML += `
								    <thead>
								    <tr>
								      <th scope="col">Qarzdor ismi</th>
								      <th scope="col">Mahsulot nomi</th>
								      <th scope="col">Aloqa</th>
								    </tr>
								  </thead>
								  <tbody class="bg-warning">
								    <tr>
								      <td>${item.customer_name}</td>
								      <td>${item.product_name}</td>
								      <td>${item.customer_phone} <button type="button" class="link-primary" data-toggle="modal" data-target="#{{selldebt.id}}"> (batafsil) </button></td>
								    </tr>
								  </tbody>

								 `;
							} else {
								tableOutputSellOnDebt.innerHTML += `
								  <tbody class="bg-warning">
								    <tr>
								      <td>${item.customer_name}</td>
								      <td>${item.product_name}</td>
								      <td>${item.customer_phone} <button type="button" class="link-primary" data-toggle="modal" data-target="#{{selldebt.id}}"> (batafsil) </button></td>
								    </tr>
								  </tbody>

								 `;
							}
							

						} else {
							notpaid_count += 1;
							if (notpaid_count >= 1 && fullypaid_count == 0 && partlypaid_count == 0) {
						tableOutputSellOnDebt.innerHTML += ` 

						    <thead>
						    <tr>
						      <th scope="col">Qarzdor ismi</th>
						      <th scope="col">Mahsulot nomi</th>
						      <th scope="col">Aloqa</th>
						    </tr>
						  </thead>
						  <tbody class="bg-danger">
						    <tr>
						      <td>${item.customer_name}</td>
						      <td>${item.product_name}</td>
						      <td>${item.customer_phone} <button type="button" class="link-primary" data-toggle="modal" data-target="#{{selldebt.id}}"> (batafsil) </button></td>
						    </tr>
						  </tbody>

												`;
							} else {
							tableOutputSellOnDebt.innerHTML += ` 

						  <tbody class="bg-danger">
						    <tr>
						      <td>${item.customer_name}</td>
						      <td>${item.product_name}</td>
						      <td>${item.customer_phone} <button type="button" class="link-primary" data-toggle="modal" data-target="#{{selldebt.id}}"> (batafsil) </button></td>
						    </tr>
						  </tbody>

												`;
							}
							
						}

						

						appTableSellOnDebt.style.display = "none";
						tableOutputSellOnDebt.style.display = "none";
					});
					tableOutputSellOnDebt.style.display = "block";
				}

			})

	}else{
		tableOutputSellOnDebt.style.display = "none";
		appTableSellOnDebt.style.display = "block";
	}
});