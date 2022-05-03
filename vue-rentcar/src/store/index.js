import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        backendUrl: "http://127.0.0.1:8000/api/v1",
        authUrl: "http://127.0.0.1:8000/auth"
    },
    mutations: {},
    actions: {},
    modules: {},
    getters: {
        getServerUrl: state => {
            return state.backendUrl
        },
        getAuthUrl: state => {
            return state.authUrl
        }
    }
})

export default store