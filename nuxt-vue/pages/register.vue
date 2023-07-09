<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="register">
      <input v-model="firstName" placeholder="First name" required>
      <input v-model="lastName" placeholder="Last name" required>
      <input v-model="email" type="email" placeholder="Email" required>
      <input v-model="username" placeholder="Username" required>
      <input v-model="password" type="password" placeholder="Password" required>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      username: '',
      password: ''
    }
  },
  methods: {
    async register() {
      try {
        const response = await this.$axios.$post('/api/register', {
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          username: this.username,
          password: this.password
        })
        this.$router.push('/users')
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
