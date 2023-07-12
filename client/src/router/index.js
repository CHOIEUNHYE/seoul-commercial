import { createRouter, createWebHistory } from 'vue-router'
import Search from '../components/Search.vue'
import Chart from '../components/Chart.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/search',
      name: 'search',
      component: Search
    },
    {
      path: '/chart',
      name: 'chart',
      component: Chart
    },
  ]
})

export default router
