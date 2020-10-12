<template>
    <div>
        <div v-bind:key="book.id" v-for="book in books">
            <p>Книга: {{book.name}}</p>
            <p>Дата публикации: {{book.publication_date}}</p>
            <p>Жанр: {{book.genre}}</p>
            <p>ISBN код: {{book.ISBN_code}}</p>
            <p>Автор: </p>
                <ul>
                    <li :key="au.id" v-for="au in book.author">{{au.name}} {{au.surname}}</li>
                </ul>
            <p>==================</p>
        </div>
        <button @click="logout">LOGOUT</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Library',
    components: {
    },
    data() {
        return{
            token: null,
        }
    },
    props: ['books'],
    methods: {
        logout() {
            localStorage.removeItem('user-token')
            this.$emit('setToken', this.token)
        }
    }
}
</script>