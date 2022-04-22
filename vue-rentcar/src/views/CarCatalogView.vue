<template>
  <div>
    <br />
    <div class="container-md bg-lightblue rounded">
      <h2 class="pt-4 ms-5">Каталог авто</h2>

      <div class="row pt-1 pb-5 justify-content-center me-3">
        <div
          v-for="car in carList"
          :key="car.id"
          class="col-lg-5 col-md-10 col-sm-10 selectcar pt-4 ms-4">
          <span class="text-on-pic text-uppercase bg-translucent fs-4" style="postiton: absolute; width: 100%; text-align: center;">{{ car.title }}</span>
          <img
            src="../assets/img/pic-not-find.png"
            alt="picture not find"
            class="img-fluid"
          />
          <span class="price">Стоимость <br>
            {{car.car_price}} руб/сутки
          </span>
          <button type="button" class="btn-lg btn-primary btn-select-style">
            Заказать
          </button>
        </div>
      </div>
    </div>
    <br />
  </div>
</template>

<style scoped>
.price{
  position: absolute;
  bottom: 0%;
  left: 0;
}
.selectcar {
  position: relative;
  padding: 0;
}
.selectcar:hover > .btn-select-style {
  background-color: rgb(13, 110, 253);
  border-color: rgb(13, 110, 253);
}
.btn-select-style {
  position: absolute;
  bottom: 0%;
  right: 0;
  width: 50%;
  background-color: rgb(13, 110, 253, 0.3);
  border-color: rgb(13, 110, 253, 0.1);
  border-bottom-right-radius: 0%;
}
.text-on-pic {
  position: absolute;
}
</style>

<script>
export default {
  name: "CarCatalogView",
  components: {},
  data() {
    return {
      carList: [],
    };
  },
  created() {
    this.loadCarList();
  },
  methods: {
    async loadCarList() {
      this.carList = await fetch(
        `${this.$store.getters.getServerUrl}/cars/car/list`
      ).then((response) => response.json());
    },
  },
};
</script>