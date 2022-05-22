import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        backendUrl: "http://127.0.0.1:8000/api/v1",
        authUrl: "http://127.0.0.1:8000/auth",
        username: false,
    },
    plugins: [
        createPersistedState(
            // {
            //     key: 'vuex',
            //     reducer(val) {
            //         let accesstoken = localStorage.getItem("access-token");
            //         if (accesstoken === "error") {
            //             return {}
            //         }
            //         return val
            //     }
            // }
        )
    ],
    mutations: {
        setUser(state, json) {
            state.username = json[0].username
        },
        cleanUser(state) {
            state.username = false
        }

    },
    actions: {
        async getUser({ commit }) {
            let data = {
                user_id: localStorage.getItem('user_id'),
            };

            const response = await fetch(
                `http://127.0.0.1:8000/api/v1/cars/user`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${localStorage.getItem('access-token')}`
                    },
                    body: JSON.stringify(data),
                }
            );
            const json = await response.json();
            console.log(json);
            // localStorage.setItem("username", json[0].username);
            commit('setUser', json)
        }
    },
    modules: {},
    getters: {
        getServerUrl: state => {
            return state.backendUrl
        },
        getAuthUrl: state => {
            return state.authUrl
        },
        getCurrentUser: state => {
            return state.username
        },
    }
})

export default store