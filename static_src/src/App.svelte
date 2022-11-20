<script>
	// export let name;
	let flights;
  async function getData(){
	var url = '/api/v1/flight/'
	await fetch(url)
  .then((res)=>res.json())
  .then(function(data){
	console.log(data)
	flights=data })
return flights
  }
  let promise = getData()
</script>

<main class="d-flex flex-nowrap">
	<div class="d-flex flex-column flex-shrink-0 p-3 text-bg-dark" style="width: 230px;">
		<a href="/" class="d-flex align-items-center mb-4 mb-md-0 me-md-auto text-white text-decoration-none">
		  <svg class="bi pe-none me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
		  <span class="fs-4">Домашняя</span>
		</a>
		<hr>
		<ul class="nav nav-pills flex-column mb-auto">
		  <li>
			<a href="/flight/" class="nav-link text-white">
			  <svg class="bi pe-none me-2" width="16" height="16"><use xlink:href="#speedometer2"/></svg>
			  Рейсы
			</a>
		  </li>
		  <li>
			<a href="/warehouses/" class="nav-link text-white">
			  <svg class="bi pe-none me-2" width="16" height="16"><use xlink:href="#table"/></svg>
			  Склады
			</a>
		  </li>
		  <li>
			<a href="/careers/" class="nav-link text-white">
			  <svg class="bi pe-none me-2" width="16" height="16"><use xlink:href="#grid"/></svg>
			  Карьеры
			</a>
		  </li>
		  <li>
			<a href="/tracks/" class="nav-link text-white">
			  <svg class="bi pe-none me-2" width="16" height="16"><use xlink:href="#people-circle"/></svg>
			  Самосвалы
			</a>
		  </li>
		</ul>
		<hr>
		<ul>
	</ul>
</div>
<div class="d-flex flex-column align-items-stretch flex-shrink-1" style="width: 100%;">
  <a href="/" class="d-flex align-items-center flex-shrink-0 p-3 link-dark text-decoration-none border-bottom">
	<svg class="bi pe-none me-2" width="30" height="24"><use xlink:href="#bootstrap"/></svg>
	<span class="fs-5 fw-semibold">Список рейсов</span>
  </a>
  {#await promise}
  <p>...подождите</p>
  {:then data}
  <div class="list-group list-group-flush border-bottom scrollarea">
{#each data as flight}
	<a href="/flight/{flight.id}" class="list-group-item list-group-item-action py-3 lh-sm" aria-current="true">
	  <div class="d-flex w-100 align-items-center justify-content-between">
		<strong class="mb-1">Номер рейса: {flight.id}</strong>
	  </div>
	  <div class="col-10 mb-1 small">Дата: {flight.date}</div>
	  <div class="col-10 mb-1 small">Координаты: {flight.coordinates}</div>
	  <hr>
	  <div class="col-10 mb-1 small"><a href="/warehouses/{flight.warehouse_id}">Склад №: {flight.warehouse_id}</a>
	 <a href="/careers/{flight.career_id}">Карьер №: {flight.career_id}</a>
	<a href="/trucks/{flight.truck_id}">Самосвал №: {flight.truck_id}</a></div>
	</a>
{/each}
  </div>
  {:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
</main>

<style>
</style>