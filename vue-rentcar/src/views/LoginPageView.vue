<template>
  <div class="container">
    <div class="row justify-content-center mt-4">
      <div
        class="
          col-xl-3 col-lg-4 col-sm-6 col-md-5
          mb-4
          p-3
          text-center
          border
          rounded
        "
      >
        <h2>Вход</h2>

        <form @submit="userLogin">
          <input
            v-model="username"
            type="text"
            class="w-100 my-2 p-1"
            placeholder="Логин"
          />
          <input
            v-model="password"
            type="password"
            class="w-100 mb-2 p-1"
            placeholder="Пароль"
          />

          <button class="btn btn-rentcar w-100 py-2">Войти</button>
        </form>

        <p class="pt-4">Еще нет аккаунта?</p>
        <button
          @click="$router.push('/registration')"
          class="btn w-100 btn-outline-rentcar py-2"
        >
          Регистрация
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginPageView",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    b64DecodeUnicode(str) {
      return decodeURIComponent(
        atob(str)
          .split("")
          .map(function (c) {
            return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
          })
          .join("")
      );
    },
    setUserToLocal(token) {
      let payload = token.split(".")[1];
      let user_id = JSON.parse(this.b64DecodeUnicode(payload)).user_id;
      localStorage.setItem("user_id", user_id);
    },

    async redirectAuth(response, token) {
      if (response.status === 200) {
        await this.$store.dispatch("getUser");
        
        this.$router.push({
          path: "/myorders",
          name: "myorder",
        });
      }
    },

    async userLogin() {
      let data = {
        username: this.username,
        password: this.password,
      };
      const response = await fetch(`${this.$store.getters.getAuthUrl}/token/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      const token = await response.json();
      localStorage.setItem("access-token", token.access);
      localStorage.setItem("refresh-token", token.refresh);
      this.setUserToLocal(token.access);
      this.redirectAuth(response);
    },
  },
};
</script>