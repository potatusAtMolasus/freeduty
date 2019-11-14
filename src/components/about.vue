<template>
  <h2>О нас</h2>
</template>

<script>
export default {
  name: "About",
  computed: {
    username() {
      return this.$route.params.username
    }
  },
  methods: {
    goBack() {
      window.history.length > 1 ? this.$router.go(-1) : this.$router.push('/')
    }
  }
};
</script>


