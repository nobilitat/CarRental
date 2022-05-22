<template>
  <div class="container mt-2 mb-2 px-0">
    <NavAuthUser />
    <h2 class="mt-3 text-center">Мои заказы</h2>
    <div v-for="order in orderList" :key="order.id">
      <div
        @click="goToOrder(order)"
        class="row justify-content-center text-center"
      >
        <p class="col-lg-6 order-section bg-lightblue border border-secondary rounded-end p-2 mt-2">
          <span v-if="order.active_state">Статус: Открыт</span>
          <span v-else>Статус: Закрыт</span> <br />
          <br />
          <span>Заказ № {{ order.id }}</span> <br />
          <span>Дата: {{ order.date_getting }}</span> <br />
          <span>Сумма заказа: {{ order.order_price }} руб</span> <br />
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.order-section:hover {
  cursor:pointer;
}
</style>

<script>
import NavAuthUser from "../components/NavAuthUser.vue";

export default {
  name: "MyOrdersView",
  data() {
    return {
      orderList: [],
    };
  },
  components: {
    NavAuthUser,
  },
  created() {
    this.getOrders();
  },
  methods: {
    async getOrders() {
      const response = await fetch(
        `${this.$store.getters.getServerUrl}/cars/order/list`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("access-token")}`,
          },
        }
      );
      this.orderList = await response.json();
    },
    goToOrder(order) {
      this.$router.push({
        path: `/order/${order.id}`,
        params: {
          order: order,
        },
      });
    },
  },
};
</script>