<template>
  <!-- 增加页面 -->
  <div>
    <a-button type="primary" @click="showDrawer"> <a-icon type="plus" />添加</a-button>
    <a-drawer
      title="添加数据"
      :width="320"
      :visible="visible"
      :body-style="{ paddingBottom: '80px' }"
      @close="onClose"
    >
        <a-form-item label="商品名称">
          <a-input placeholder="请输入要录入的商品名称" v-model="title"/>
        </a-form-item>

        <a-form-item label="商品数量">
          <a-input-number v-model="value" :min="1" />
        </a-form-item>

        <a-form-item label="商品价格">
            <a-input-number
              v-model="price"
              :min="1"
              :default-value="0"
              :formatter="value => `$ ${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ',')"
              :parser="value => value.replace(/\$\s?|(,*)/g, '')"/>
        </a-form-item>

        <a-form-item label="上传图片">
          <div style="width: 100%;display: flex;">
            <label for="real">
              <div class="upload" @mouseenter="open" @mouseleave="close" ref="frame">
                <a-icon type="plus" style="font-size: 32px; color: #999;line-height: 100px;"/>
              </div>
            </label>
            <input id="real" type="file" style="display: none" @change="show_img" />
            <div class="demo-image" style="margin-left: 10px;">
              <div class="block">
                <el-image
                  v-if="img!=''"
                  style="width: 100px; height: 100px; border-radius: 5px;"
                  :src="img"
                  fit="cover"></el-image>
                <el-image
                  v-if="oldimg!=''&img==''"
                  style="width: 100px; height: 100px; border-radius: 5px;"
                  :src='require("../assets/"+oldimg)'
                  fit="cover"></el-image>
              </div>
            </div>
          </div>
        </a-form-item>

      <div
        :style="{
          position: 'absolute',
          right: 0,
          bottom: 0,
          width: '100%',
          borderTop: '1px solid #e9e9e9',
          padding: '10px 16px',
          background: '#fff',
          textAlign: 'right',
          zIndex: 1,
        }">
        <a-button :style="{ marginRight: '8px' }" @click="onClose">
          取消
        </a-button>
        <a-button type="primary" @click="deliver"
        :disabled="this.title === '' || this.img === ''"
        >
          提交
        </a-button>
        <a-button :style="{ marginLeft: '8px' }" type="dashed" @click="change"
        :disabled="this.title === '' || this.oldimg === ''"
        >
          更新
        </a-button>
      </div>
    </a-drawer>
  </div>
</template>
<script>
export default {
  name: 'addandmod',
  data () {
    return {
      visible: false, // 判断是否展开
      value: 1, // 数量
      price: 1, // 价格
      title: '', // 商品名称
      img: '',
      oldimg: '',
      id: ''
    }
  },
  methods: {
    // 修改后及时跟新
    async real_time () {
      const { data: res } = await this.$http.post(
        '/getdata'
      )
      console.log(res)
      this.$emit('valuechange', res)
    },
    async change () {
      this.visible = false // 关闭打开的菜单
      // 在此处进行axios请求
      const { data: res } = await this.$http.post(
        '/update', {
          value: this.value,
          price: this.price,
          title: this.title,
          img: this.img,
          id: this.id
        }
      )
      this.real_time()
      console.log(res)
      this.value = 1
      this.price = 1
      this.title = ''
      this.img = ''
      this.oldimg = ''
    },
    onClose () {
      this.visible = false // 关闭打开的菜单
      // 清空菜单
      this.value = 1
      this.price = 1
      this.title = ''
      this.img = ''
      this.oldimg = ''
    },
    // 拉开
    showDrawer () {
      this.visible = true
    },
    // 保存数据
    async deliver () {
      this.visible = false // 关闭打开的菜单
      // 在此处进行axios请求
      const { data: res } = await this.$http.post(
        '/add', {
          value: this.value,
          price: this.price,
          title: this.title,
          img: this.img
        }
      )
      this.real_time()
      console.log(res)
      this.value = 1
      this.price = 1
      this.title = ''
      this.img = ''
      this.oldimg = ''
    },
    open () {
      this.$refs.frame.style.border = '1px dashed #4CA7FF'
    },
    close () {
      this.$refs.frame.style.border = '1px dashed #d9d9d9'
    },
    show_img () {
      const file = document.querySelector('input[type=file]').files[0]
      const reader = new FileReader()
      reader.addEventListener(
        'load',
        () => {
          this.img = reader.result
          // 使用此处代码实现网页图片上传+下载
          /* var a = document.createElement('a')
          a.download = './aap.png'
          a.href = URL.createObjectURL(this.dataURLtoBlob(this.img))
          console.log(this.dataURLtoBlob(this.img))
          a.click() */
        },
        false
      )
      if (file) {
        reader.readAsDataURL(file)
      }
    },
    // data转blob，这段代码无用
    dataURLtoBlob (dataurl) {
      const arr = dataurl.split(',')
      const mime = arr[0].match(/:(.*?);/)[1]
      const bstr = atob(arr[1])
      let n = bstr.length
      const u8arr = new Uint8Array(n)
      while (n--) {
        u8arr[n] = bstr.charCodeAt(n)
      }
      return new Blob([u8arr], { type: mime })
    }
  }
}
</script>
<style>
.upload {
  width: 100px;
  height: 100px;
  border: 1px dashed #d9d9d9;
  text-align: center;
  background-color: #fafafa;
  border-radius: 5px;
}
</style>
