<template>
  <div>
    <header id="header" class="header">
      <nav class="navbar navbar-expand-md navbar-dark bg-main">
        <div class="container">
          <a class="navbar-brand" href="/">RentCar</a>
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
                <a class="nav-link active" aria-current="page" href="/"
                  >Главная</a
                >
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#/catalog">Каталог авто</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#/conditions" tabindex="-1" aria-disabled="true"
                  >Условия</a
                >
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#/contacts" tabindex="-1" aria-disabled="true"
                  >Контакты</a
                >
              </li>
              <li v-if="getCurrentUser" class="nav-item">
                <a class="nav-link" href="#/myorders" tabindex="-1" aria-disabled="true"
                  >Личный кабинет</a
                >
              </li>
              <li v-if="getCurrentUser" class="nav-item">
                <a class="nav-link" href="#/logout/" tabindex="-1" aria-disabled="true"
                  >Выйти</a
                >
              </li>
              <li class="nav-item" v-else>
                <a class="nav-link" href="#/login" tabindex="-1" aria-disabled="true"
                  >Вход</a
                >
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
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
