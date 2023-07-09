<template>
    <div>
      <h1>Users</h1>
      <ul>
        <li v-for="user in users" :key="user.id">
          {{ user.firstName }} {{ user.lastName }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        users: []
      }
    },
    async created() {
      try {
        this.users = await this.$axios.$get('/api/users')
      } catch (error) {
        console.error(error)
      }
    }
  }
  </script>
  