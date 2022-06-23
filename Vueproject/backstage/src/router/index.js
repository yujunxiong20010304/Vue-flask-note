import Vue from 'vue'
import VueRouter from 'vue-router'
import home from '@/views/home'
import login from '@/views/login'
import welcome from '@/views/welcome'
import datadisplay from '@/views/datadisplay'
Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    component: home,
    redirect: '/home/welcome',
    children: [
      { path: 'welcome', component: welcome },
      { path: 'datadisplay', component: datadisplay }
    ]
  },
  {
    path: '/login',
    component: login
  }
]

const router = new VueRouter({
  routes
})
router.beforeEach((to, from, next) => {
  const path = ['/home/welcome', '/home/datadisplay']
  if (path.indexOf(to.path) !== -1) {
    const token = window.sessionStorage.getItem('token')
    if (token) {
      next()
    } else {
      next('/login')
    }
  } else {
    next()
  }
})
export default router
