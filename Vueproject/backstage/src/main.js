import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8' // 编码
axios.defaults.baseURL = 'http://127.0.0.1:5000'
Vue.prototype.$http = axios
Vue.use(ElementUI)
Vue.config.productionTip = false
Vue.use(Antd)
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
