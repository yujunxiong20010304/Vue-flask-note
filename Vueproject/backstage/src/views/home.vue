<template>
  <a-layout id="components-layout-demo-side" style="min-height: 100vh">
    <!-- 侧边栏 -->
    <a-layout-sider v-model="collapsed" collapsible :theme="theme">
      <div class="logo">
        <a-switch
          default-checked
          checked-children="dark"
          un-checked-children="light"
          @change="changeTheme"
        />
      </div>
      <a-menu :theme=theme :default-selected-keys="[addre]" mode="inline" :trigger="null">

        <a-menu-item key="welcome">
          <a-icon type="smile" />
          <span>欢迎</span>
          <router-link to="/home/welcome">
          </router-link>
        </a-menu-item>

        <a-sub-menu key="2">
          <span slot="title"><a-icon type="profile" /><span>商品管理</span></span>
          <a-menu-item key="datadisplay">
            <a-icon type="cloud-upload" />数据录入
            <router-link to="/home/datadisplay">
            </router-link>
          </a-menu-item>
          <a-menu-item key="4">
            <a-icon type="monitor" />数据分析
          </a-menu-item>
        </a-sub-menu>

        <a-menu-item key="5">
          <a-icon type="fire" />
          <span>个人主页</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>

    <!-- content -->
    <a-layout>

      <a-layout-header style="background: #fff; padding: 0" >
        <!-- 展示路由 -->

        <a-row>
          <a-col :span="8">
            <a-breadcrumb>
              <a-breadcrumb-separator style="line-height: 64px;margin-left: 25px;">
                {{ address }}
              </a-breadcrumb-separator>
            </a-breadcrumb>
          </a-col>
          <a-col :span="8" :offset="8">
            <personal></personal>
          </a-col>
        </a-row>

      </a-layout-header>

      <!-- 路由切换内容区域 -->
      <a-layout-content>
        <div class="content">
          <router-view :action="collapsed"></router-view>
        </div>
      </a-layout-content>

    </a-layout>

  </a-layout>
</template>
<script>
import personal from '@/components/personal'
export default {
  name: 'home',
  components: {
    personal
  },
  data () {
    return {
      collapsed: false,
      theme: 'dark',
      addre: '' // 是最后一位路由
    }
  },
  methods: {
    handleClick (e) {
      console.log('click ', e)
      this.current = e.key
    },
    changeTheme (checked) {
      this.theme = checked ? 'dark' : 'light'
    }
  },
  computed: {
    // 计算属性，更新当前的路由地址
    address () {
      const list = this.$route.path.split('/')
      list.splice(0, 2)
      const dict = {
        welcome: '欢迎',
        datadisplay: '商品管理 / 数据录入'
      }
      return dict[list[0]]
    }
  },
  watch: {
    $route: {
      handler (to, from) {
        this.addre = to.path.split('/').splice(2, 3)[0]
      },
      immediate: true
    }
  }
}
</script>

<style>
#components-layout-demo-side .logo {
  height: 32px;
  margin: 16px;
}
</style>
