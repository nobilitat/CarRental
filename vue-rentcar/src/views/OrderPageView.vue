<template>
  <div class="container mt-2 mb-2 px-0">
    <NavAuthUser />
    <h2 class="mt-3 text-center">Заказ № {{ orderDetails.id }}</h2>
    <div class="row justify-content-center">
      <div class="col-lg-5">
        <p v-if="orderDetails.active_state">СТАТУС: ОТКРЫТ</p>
        <p v-else>СТАТУС: ЗАКРЫТ</p>
        <p>Пользователь: {{ orderDetails.customer.user.username }}</p>
        <p>Автомобиль: {{ orderDetails.car.title }}</p>
        <p>Дата получения: {{ orderDetails.date_getting }}</p>
        <p>
          Адрес доставки:
          {{ orderDetails.delivery.delivery_zone.area_name }} район,
          {{ orderDetails.delivery.address }}
        </p>
        <p>Время доставки:  {{ orderDetails.delivery.delivery_time }}</p>
        <p>Срок аренды: {{ orderDetails.period }} дн</p>
        <p>Стоимость: {{ orderDetails.order_price }} руб</p>
      </div>
    </div>
  </div>
</template>

<script>
import NavAuthUser from "../components/NavAuthUser.vue";
import {numberFormatter, dateTimeFormatter, dateFormatter} from "../assets/js/additional-functions.js"

export default {
  name: "OrderPageView",
  components: {
    NavAuthUser,
  },
  data() {
    return {
      orderDetails: {},
    };
  },
  // Не получилось вытащить order (undefined)
  // props: {
  //   order: Object
  // },
  created() {
    this.getDataAboutOrder();
  },
  methods: {
    async getDataAboutOrder() {
      const idOrder = this.$route.params.id;
      const resposne = await fetch(
        `${this.$store.getters.getServerUrl}/cars/order/detail/${idOrder}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("access-token")}`,
          },
        }
      );

      this.orderDetails = await resposne.json();
      this.orderDetails.order_price = numberFormatter(this.orderDetails.order_price);
      this.orderDetails.date_getting = dateFormatter(this.orderDetails.date_getting);
      this.orderDetails.delivery.delivery_time = dateTimeFormatter(this.orderDetails.delivery.delivery_time)
      
    },
  },
};
</script>