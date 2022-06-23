<template>
  <div id="components-popover-demo-placement" class="ps">
    <div :style="{ marginLeft: `${buttonWidth}px`, clear: 'both', whiteSpace: 'nowrap' }">
      <a-popover placement="bottomRight">
        <template slot="content">
          <p><a-icon type="user" /> 个人中心</p>
          <p @click="close"><a-icon type="poweroff" />  退出登录</p>
        </template>
        <template slot="title">
          <span>管理员</span>
        </template>
        <a-button>admin</a-button>
      </a-popover>
    </div>
  </div>
</template>

<script>
export default {
  name: 'personal',
  data () {
    return {
      buttonWidth: 70
    }
  },
  methods: {
    close () {
      console.log('退出')
    }
  }
}
</script>
<style>
#components-popover-demo-placement .ant-btn {
  width: 70px;
  text-align: center;
  padding: 0;
  margin-right: 8px;
  margin-bottom: 8px;
}
.ps {
  margin-left: 200px;
}
</style>
