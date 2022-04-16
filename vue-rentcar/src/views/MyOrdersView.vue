<template>
  <div class="container mt-2 mb-2 px-0">
    <NavAuthUser />
    <h2 class="mt-3">Мои заказы</h2>
    <div class="container-md">
      <div class="row border border-secondary mt-3 pt-2">
        <p>Статус: state</p>
        <p>Заказ от date</p>
      </div>
    </div>
    <div class="container-md">
      <div class="row border border-secondary mt-3 pt-2">
        <p>Статус: {{ state }}</p>
        <p>Заказ от {{ date }}</p>
      </div>
    </div>
    <div class="container-md">
      <div class="row border border-secondary mt-3 pt-2">
        <p>Статус: {{ state }}</p>
        <p>Заказ от {{ date }}</p>
      </div>
    </div>
    <div class="container-md">
      <div class="row border border-secondary mt-2 pt-2">
        <p>Статус: {{ state }}</p>
        <p>Заказ от {{ date }}</p>
      </div>
    </div>
    
  </div>
</template>

<script>
import NavAuthUser from "../components/NavAuthUser.vue";

export default {
  name: "MyOrdersView",
  components: {
    NavAuthUser,
  },
};
</script>