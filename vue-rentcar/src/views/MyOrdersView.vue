<template>
  <div class="container mt-2 mb-2 px-0">
    <NavAuthUser />
    <h2 class="mt-3 text-center">Мои заказы</h2>
    <div class="row mt-3 justify-content-center">
      <div class="col-lg-5 border border-secondary rounded-end pt-2">
        <p>Статус: state</p>
        <p>Заказ от date</p>
      </div>
    </div>
    <div class="row mt-3 justify-content-center">
      <div class="col-lg-5 border border-secondary rounded-end pt-2">
        <p>Статус: state</p>
        <p>Заказ от date</p>
      </div>
    </div>
    <div class="row mt-3 justify-content-center">
      <div class="col-lg-5 border border-secondary rounded-end pt-2">
        <p>Статус: state</p>
        <p>Заказ от date</p>
      </div>
    </div>
    <div class="row mt-3 justify-content-center">
      <div class="col-lg-5 border border-secondary rounded-end pt-2">
        <p>Статус: state</p>
        <p>Заказ от date</p>
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