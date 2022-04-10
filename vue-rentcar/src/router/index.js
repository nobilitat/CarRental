import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CarCatalogView from '../views/CarCatalogView.vue'
import ConditionsView from '../views/ConditionsView.vue'
import ContactView from "../views/ContactView"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/catalog',
    name: 'catalog',
    component: CarCatalogView
  },
  {
    path: '/conditions',
    name: 'conditions',
    component: ConditionsView
  },
  {
    path: '/contacts',
    name: 'contacts',
    component: ContactView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
