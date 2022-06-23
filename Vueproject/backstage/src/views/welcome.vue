<template>
  <div id="welcome">
    <div id="left">
      <span style="color: #fff;">
        <span style="font-size: 30px;">欢 迎 来 到</span>
        <span style="font-size: 20px;">牛 马 后 台 管 理 系 统</span>
      </span>
      <br>
      <span style="color: #fff; padding-left: 20px;">
        你还可以点击牛马官方网站，关注更多信息
      </span>
      <br>
      <a-button type="danger" ghost icon="heat-map" style="border: 0;color: #fff;padding-left: 40px;">
        h t t p : / / w w w . b a i d u . c o m
      </a-button>
    </div>
    <div id="right" ref="zoom">
      <a-card style="width: 280px;background-color: aqua;border: 0;">
        <p style="color: #2c3e50;font-size: 20px;">后台管理</p>
        <p style="color: #45526b;"><a-icon type="sketch" /> 主管部门 <span style="padding-left: 20px;color: #8F969C;">余某，刘某</span></p>
        <p style="color: #45526b;"><a-icon type="slack" /> 技术支持 <span style="padding-left: 20px;color: #8F969C;">牛马技术</span></p>
        <p style="color: #45526b;"><a-icon type="ant-design" /> 版权所有 <span style="padding-left: 20px;color: #8F969C;">牛马官方</span></p>
      </a-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'welcome',
  props: ['action'],
  watch: {
    action (newVal, oldVal) {
      if (newVal) {
        this.$refs.zoom.style.width = '440px'
        this.$refs.zoom.style.transition = 'width .2s'
      } else {
        this.$refs.zoom.style.width = '320px'
      }
    },
    $route (to, from) {
      console.log(to.path)
    }
  }
}
</script>

<style scoped lang="less">
#welcome{
  width: 100%;
  height: 555px;
  overflow-y: scroll;
  display: flex;
  align-items: center;
  justify-content: space-between;
  #left {
    background-image: url("../assets/left.jpeg");
    background-repeat: no-repeat;
    background-position: center;
    width: 690px;
    height: 360px;
    margin-left: 25px;
    border-radius: 10px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    padding-left: 25px;
    padding-top: 25px;
  }
  #right {
    width: 320px;
    height: 360px;
    margin-right: 25px;
    background-color: aqua;
    border-radius: 10px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    padding-left: 25px;
    padding-top: 25px;
  }
}
</style>
