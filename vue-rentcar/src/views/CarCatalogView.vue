<template>
  <div>
    <br />
    <div class="container-md bg-main rounded">
      <h2 class="pt-3 ms-4 ps-2 text-white">Каталог авто</h2>
      <div class="row pt-1 px-5">
        <div class="col-md selectcar me-3 pt-3">
          <img src="../assets/img/pic-not-find.png" alt="picture not find" class="img-fluid">
          <button type="button" class="btn-lg btn-primary btn-select-style">Заказать</button>
        </div>
        <div class="col-md selectcar pt-3">
          <img src="../assets/img/pic-not-find.png" alt="picture not find" class="img-fluid">
          <button type="button" class="btn-lg btn-primary btn-select-style">Заказать</button>
        </div>
      </div>
      <div class="row px-5">
        <div class="col-md selectcar me-3 pt-3">
          <img src="../assets/img/pic-not-find.png" alt="picture not find" class="img-fluid">
          <button type="button" class="btn-lg btn-primary btn-select-style">Заказать</button>
        </div>
        <div class="col-md selectcar pt-3">
          <img src="../assets/img/pic-not-find.png" alt="picture not find" class="img-fluid">
          <button type="button" class="btn-lg btn-primary btn-select-style">Заказать</button>
        </div>
      </div>
      <div class="row px-5 pb-3">
        <div class="col-md selectcar me-3 pt-3">
          <img src="../assets/img/pic-not-find.png" alt="picture not find" class="img-fluid">
          <button type="button" class="btn-lg btn-primary btn-select-style">Заказать</button>
        </div>
        <div class="col-md selectcar pt-3">
          <img src="../assets/img/pic-not-find.png" alt="picture not find" class="img-fluid">
          <button type="button" class="btn-lg btn-primary btn-select-style">Заказать</button>
        </div>
      </div>
    </div>
    <br>
  </div>
</template>

<style scoped>
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
</style>

<script>
export default {
  name: "CarCatalogView",
  components: {},
};
</script>