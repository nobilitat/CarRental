<template>
  <div class="container mt-2 mb-2 px-0">
    <NavAuthUser />
    <h2 class="mt-3">Новый заказ</h2>
   
    
  </div>
</template>

<script>
import NavAuthUser from "../components/NavAuthUser.vue";

export default {
  name: "NewOrder",
  components: {
    NavAuthUser,
  },
};
</script>