<template>
  <div class="home">
    <Login v-if="token===null" @setToken='setToken' />
    <Library v-if="token!==null" @setToken='setToken' :books="books" />
  </div>
</template>

<script>
import Login from '@/components/Login.vue';
import Library from '@/components/Library.vue';
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return{
      token: null,
      books: null,
    }
  },
  components: {
    Login,
    Library
  },
  methods: {
    setToken(token) {
      this.token = token;
      if (this.token !== null) {
      let config = {
        headers: {
          'Authorization': 'Token ' + this.token
        }
      }
      axios.get('http://127.0.0.1:8000/api/books', config)
      .then(async (res) => {
        const books = res.data.map(async (el) => {
          const promises = el.author.map(element => 
            axios.get(`http://127.0.0.1:8000/api/authors/${element}`)
            .then(res => res.data)
          );
          return {...el, author: await Promise.all(promises)};
        });
        this.books = await Promise.all(books);
        })
        .catch(err => console.log(err))
      }
    }
  }
}
</script>
