<script>
export default {
  name: "UserLogout",
  created() {
    this.logoutUser();
    localStorage.setItem("access-token", "error");
    this.redirectUser();
  },
  methods: {
    async logoutUser() {
      const data = {
        "refresh_token": localStorage.getItem("refresh-token")
      };

      const response = await fetch(
        `${this.$store.getters.getServerUrl}/cars/logout`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("access-token")}`,
          },
          body: JSON.stringify(data),
        }
      );

      if (response.status === 205) {
        return response
      }
    },
    redirectUser() {
      this.$router.push({
        path: "/login",
        name: "login",
      });
    },
  },
};
</script>