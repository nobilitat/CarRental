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
        <h2>Регистрация</h2>

        <form @submit="userRegistration">
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
          <input
            v-model="re_password"
            type="password"
            class="w-100 mb-2 p-1"
            placeholder="Повторите пароль"
          />

          <button class="btn btn-rentcar w-100 py-2">Регистрация</button>
        </form>

        <p class="pt-4">Уже есть аккаунт?</p>
        <button @click="$router.push('/login')" class="btn w-100 btn-outline-rentcar py-2">Войти</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegistrationPageView",
  data() {
    return {
      username: "",
      password: "",
      re_password: ""
    };
  },
  methods: {
    async userRegistration() {
      let data = {
        username: this.username,
        password: this.password,
        re_password: this.re_password
      };
      await fetch(
        `http://127.0.0.1:8000/auth/users/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        }
      ).then(response=> {this.$router.push('/login')})
      .catch(error=> console.log(error));
    },
  },
};
</script>