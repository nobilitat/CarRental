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
            type="text"
            class="w-100 mb-2 p-1"
            placeholder="Пароль"
          />

          <button class="btn btn-rentcar w-100 py-2">Войти</button>
        </form>

        <p class="pt-4">Еще нет аккаунта?</p>
        <button @click="$router.push('/registration')" class="btn w-100 btn-outline-rentcar py-2">Регистрация</button>
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
    async userLogin() {
      let data = {
        username: this.username,
        password: this.password,
      };
      await fetch(
        `http://127.0.0.1:8000/auth/jwt/create`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        }
      ).then(response=> response.data);
    },
  },
};
</script>