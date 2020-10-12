<template>
    <div class="main">
        <div class="container">
            <div class="main__columns">
                <form @submit.prevent="register_method">
                    <div class="main__block">
                        <div class="main__block title">
                            <p>Login</p>
                        </div>
                        <div class="main__block inputfield">
                            <input type="text" id="username" v-model="username" name="username">
                        </div>
                    </div>
                    <div class="main__block">
                        <div class="main__block title">
                            <p>Pass</p>
                        </div>
                        <div class="main__block inputfield">
                            <input type="password" id="password" v-model="password" name="password">
                        </div>
                    </div>
                    <div class="main__block">
                        <button type="submit">REGISTER</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Register',
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        register_method() {
            console.log(this.username)
            axios.post('http://127.0.0.1:8000/api/users/', {
                username: this.username,
                password: this.password,
            })
            .then(res => console.log(res))
            .catch(err => console.log(err));
            this.$router.push('/')
        }
    }
}
</script>

<style scoped>
    .main {
        font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
    }
    .container {
        margin: 0 auto;
        width: 350px;
        border: 1px solid #000;
        border-radius: 3px;
    }
    .main__columns {
        display: flex;
        flex-direction: column;
        font-size: 20px;
        text-align: 20px;
        margin: 5px;
    }
    .main__rows:nth-child(1) {
        margin: 30px 0 0 0;
    }
    .main__block {
        display: flex;
    }
    .main__block input{
        height: 30px;
        width: 95%;
    }
    .inputfield {
        width: 80%;
        align-items: center;
        margin: 0 10px 0 10px;
    }
    .title {
        width: 20%;
        margin: 0 10px 0 10px;
    }
    .main__block button{
        margin: 0 10px;
    }
</style>