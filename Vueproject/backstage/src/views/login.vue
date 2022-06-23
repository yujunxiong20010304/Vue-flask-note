<template>
<div>
  <div class="switch">
    <a-switch default-checked @change="onChange" />
  </div>
  <div class="sun" ref="dark"></div>
  <div class="moon"></div>
  <div class="sea"></div>
  <div class="login">
    <span class="heade">牛马后台管理登录</span>
    <a-form-model layout="inline" :model="formInline" @submit="handleSubmit" @submit.native.prevent>
      <a-form-model-item>
        <a-input v-model="formInline.user" placeholder="用户名">
          <a-icon slot="prefix" type="user" style="color:rgba(0,0,0,.25)" />
        </a-input>
      </a-form-model-item>

      <a-form-model-item>
        <a-input v-model="formInline.password" type="password" placeholder="密码">
          <a-icon slot="prefix" type="lock" style="color:rgba(0,0,0,.25)" />
        </a-input>
      </a-form-model-item>

      <a-form-model-item>
        <a-button
          @click="submit"
          type="primary"
          html-type="submit"
          :disabled="formInline.user === '' || formInline.password === ''">
          Log in
        </a-button>
      </a-form-model-item>

    </a-form-model>

  </div>
</div>
</template>

<script>
window.addEventListener('load', function () {
  const date = new Date()
  const sun = document.querySelector('.sun')
  if (date > 17 || date < 5) {
    sun.style.clipPath = 'inset(0px 100% 0px 0px)'
  } else {
    sun.style.clipPath = 'inset(0px 0% 0px 0px)'
  }
})
export default {
  name: 'login.vue',
  data () {
    return {
      checked: 'false',
      formInline: {
        user: '',
        password: ''
      }
    }
  },
  methods: {
    submit () {
      if (this.formInline.user === 'yujunxiong' && this.formInline.password === 'yjx20010304') {
        const value = this.formInline.user + this.password
        window.sessionStorage.setItem('token', value)
        window.location.href = 'http://localhost:8080/#/home/welcome'
      }
    },
    onChange (checked) {
      this.checked = checked
      if (checked) {
        this.$refs.dark.style.clipPath = 'inset(0px 100% 0px 0px)'
        this.$refs.dark.style.transition = 'all 2s'
      } else {
        this.$refs.dark.style.clipPath = 'inset(0px 0% 0px 0px)'
        this.$refs.dark.style.transition = 'all 2s'
      }
    },
    handleSubmit (e) {
      console.log(this.formInline)
    }
  }
}
</script>

<style scoped lang="less">
*{
  padding: 0;
  margin: 0;
}
.sun{
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: #FFEEA2;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  clip-path: inset(0px 100% 0px 0px);
}
.sun::after{
  content: '';
  display: block;
  width: 600px;
  height: 600px;
  border-radius: 50%;
  background-color: orange;
}
.sea {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 30%;
  backdrop-filter: blur(100px);
  -webkit-backdrop-filter: blur(100px);

  z-index: 20;
}
.moon {
  position: absolute;
  background-color: #040720;
  display: flex;
  width: 100%;
  height: 100%;
  justify-content: center;
  align-items: center;
}
.moon::after {
  content: '';
  display: block;
  width: 600px;
  height: 600px;
  box-shadow: 160px 180px 0px cyan;
  border-radius: 50%;
  transform: translate(-160px, -180px);
}
.switch {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 20;
}
.ant-switch-checked {
  background-color: cyan;
}
.ant-switch-loading-icon, .ant-switch::after {
  background-color: #040720;
}
.login {
  width: 300px;
  height: 200px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  z-index: 25;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.heade {
  font-size: 25px;
  color: white;
  font-weight: bold;
  line-height: 59px;
}
</style>
