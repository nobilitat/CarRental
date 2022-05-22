<template>
  <div>
   
    <nav class="navbar navbar-expand-md navbar-dark bg-main rounded-bottom">
      <div class="container">
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarScroll"
          aria-controls="navbarScroll"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div
          class="collapse navbar-collapse justify-content-end"
          id="navbarScroll"
        >
          <ul class="navbar-nav" style="--bs-scroll-height: 100px">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#/neworder"
                >Новый заказ</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#/myorders">Мои заказы</a>
            </li>
            <!-- <li class="nav-item">
              <a
                class="nav-link"
                href="#/contacts"
                tabindex="-1"
                aria-disabled="true"
                >Поддержка</a
              >
            </li> -->
            <li v-if="getCurrentUser" class="nav-item">
               <span
                class="nav-link text-white border"
                >{{getCurrentUser}}</span>
            </li>

          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'


export default {
  name: "NavAuthUser",
  computed: {
    ...mapGetters([
      "getCurrentUser"
    ])
  },
  created() {
  }
}
</script>