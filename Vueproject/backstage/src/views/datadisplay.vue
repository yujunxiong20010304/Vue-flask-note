<template>
  <div id="datadisplay">
    <!-- 顶部导航 -->
    <div id="navigation">
      <!-- 搜索 -->
      <div>
          <a-input
            placeholder="搜索"
            style="width: 205px"
            name="search"
            htmlType="text"
            v-model="value"
          />
          <a-button
            type="primary"
            style="width: 50px"
            name="btn"
            @click="lookup"
          >
            <a-icon type="search" />
          </a-button>
      </div>
      <!-- select -->
      <div>
        <a-select
          style="width: 150px"
          @change="handleChange"
          v-model="mode"
        >
          <a-select-option value=""> 选择排序方式 </a-select-option>
          <a-select-option value="default"> 默认排序 </a-select-option>
          <a-select-option value="number"> 数量排序 </a-select-option>
          <a-select-option value="price"> 价格排序 </a-select-option>
        </a-select>
      </div>
      <addandmod ref="control" @valuechange="getnew"></addandmod>
    </div>
    <ul id="list">
      <li
        v-for="(i, index) in data_list"
        :key="i.Id"
        class="sign"
        @mouseenter="card"
        @mouseleave="cardeth"
        @click="choice(index)"
      >
        <img :src='require("../assets/"+i.img)' alt="" style="width: 250px" />
        <span>{{ i.title }}</span>
        <br>
        <span>数量：{{ i.value }}</span>
        <br>
        <span>价格：{{ i.price }}</span>
        <span></span>
        <div class="behind_scenes">
          <div id="delete" @click="dele(i.Id)" >删除</div>
          <div id="modify" @click="change(i.Id)">修改</div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import addandmod from '@/components/addandmod'
import $ from 'jquery'
export default {
  name: 'datadisplay',
  props: ['action'],
  data () {
    return {
      data_list: '',
      value: '',
      mode: ''
    }
  },
  components: {
    addandmod
  },
  methods: {
    getnew (val) {
      this.data_list = val
    },
    async lookup () {
      const { data: res } = await this.$http.post(
        '/search', { value: this.value }
      )
      if (res !== '') {
        this.data_list = res
      }
    },
    // 数据更改
    async change (id) {
      const { data: res } = await this.$http.post(
        '/update', { id }
      )
      this.old = res
      console.log(res)
      this.$refs.control.showDrawer()
      this.$refs.control.value = res.value
      this.$refs.control.price = res.price
      this.$refs.control.title = res.title
      this.$refs.control.oldimg = res.img
      this.$refs.control.id = res.Id
    },
    // 删除
    async dele (id) {
      const { data: res } = await this.$http.post(
        '/delete', { id }
      )
      this.$refs.control.real_time()
      console.log(res, id)
    },
    // 全局数据获取
    async getData () {
      const { data: res } = await this.$http.post(
        '/getdata'
      )
      console.log(res)
      this.data_list = res
    },
    handleChange (value) {
      console.log(`selected ${value}`)
    },
    card (e) {
      e.target.style.boxShadow = '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)'
    },
    cardeth (e) {
      e.target.style.boxShadow = 'initial'
      const div = e.target.querySelector('div')
      div.style.bottom = '-60px'
      div.style.transition = 'all 0.2s'
    },
    choice (index) {
      const li = $('.sign')[index]
      li.querySelector('div').style.bottom = '-10px'
      li.querySelector('div').style.transition = 'all 0.2s'
    }
  },
  watch: {
    action (newVal, oldVal) {
      if (newVal) {
        $('.sign').css('margin-right', '32px')
        $('.sign').css('transition', 'all 0.2s')
      } else {
        $('.sign').css('margin-right', '5px')
        $('.sign').css('transition', 'all 0.2s')
      }
    },
    $route (to, from) {
      console.log(to.path)
    },
    mode: {
      async handler (newVal, oldVal) {
        const { data: res } = await this.$http.post(
          '/sort', { mode: this.mode }
        )
        this.data_list = res
      },
      immediate: true
    }
  },
  created () {
    this.getData()
  }
}
</script>

<style scoped lang="less">
#datadisplay {
  width: 100%;
  height: 555px;
  overflow-y: scroll;
  /*表单区域*/
  #formfield {
    width: 415px;
    height: 100%;
    background: #fff;
    margin: 0 auto;
  }
  /* 导航区域 */
  #navigation {
    width: 600px;
    height: 65px;
    display: flex;
    justify-content: space-between;
    position: relative;
    left: 25px;
  }
  #list {
    width: 100%;
    height: 100%;
    display: flex;

    flex-wrap: wrap;
    justify-content: flex-start;
    padding-left: 15px;
    padding-top: 15px;
    li {
      list-style: none;

      width: 205px;
      height: 210px;
      margin-right: 5px;
      margin-bottom: 25px;
      border-radius: 5px;
      position: relative;
      overflow: hidden;
      .behind_scenes {
        width: 100%;
        height: 60px;
        background: #fff;
        position: absolute;
        bottom: -60px;
        border-radius: 10px;
        display: flex;
        div {
          width: 100%;
          height: 60px;
          text-align: center;
          line-height: 50px;
        }
        #delete {
          background-color: red;
          border-top-left-radius: 10px;
          color: #fff;
        }
        #modify {
          background-color: deepskyblue;
          border-top-right-radius: 10px;
          color: #fff;
        }
      }
    }
  }
}
</style>
