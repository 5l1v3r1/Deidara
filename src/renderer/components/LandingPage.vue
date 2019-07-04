<template>
<!--
  <div id="wrapper">
    <img id="logo" src="~@/assets/logo.png" alt="electron-vue">
    <main>
      <div class="left-side">
        <span class="title">
          Welcome to your new project!
        </span>
        <system-information></system-information>
      </div>

      <div class="right-side">
        <div class="doc">
          <div class="title">Getting Started</div>
          <p>
            electron-vue comes packed with detailed documentation that covers everything from
            internal configurations, using the project structure, building your application,
            and so much more.
          </p>
          <button @click="open('https://simulatedgreg.gitbooks.io/electron-vue/content/')">Read the Docs</button><br><br>
        </div>
        <div class="doc">
          <div class="title alt">Other Documentation</div>
          <button class="alt" @click="open('https://electron.atom.io/docs/')">Electron</button>
          <button class="alt" @click="open('https://vuejs.org/v2/guide/')">Vue.js</button>
        </div>
      </div>
    </main>
  </div>
--><div>
  <el-container>
    <el-main>
      <div>
        <el-form label-position="right" size="mini" :inline="true">
          <el-form-item label-width="60px" label="目标：" >
            <el-input size="mini" id="target" type="text" style="width:150px"></el-input>
            <el-button size="mini">导入目标</el-button>
          </el-form-item>
          <el-form-item label-width="60px" label="并发：">
              <el-input-number v-model="concurrent" size="mini"></el-input-number>
          </el-form-item>
          <el-form-item label-width="60px" label="超时：">
              <el-input-number v-model="time_out" size="mini"></el-input-number>
          </el-form-item>
          <el-form-item label-width="60px" label="重试：">
              <el-input-number v-model="retry" size="mini"></el-input-number>
          </el-form-item>
        </el-form>
        <el-form :inline="true" label-position="right" size="mini">
          <el-form-item label-width="60px" label="用户：" >
            <el-input size="mini" id="target" type="text"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button size="mini">导入用户</el-button>
          </el-form-item>
          <el-form-item label-width="60px" label="密码：" >
            <el-input size="mini" id="target" type="text"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button size="mini">导入密码</el-button>
          </el-form-item>
          <el-form-item>
            <el-button size="mini">开始检测</el-button>
          </el-form-item>
          <el-form-item>
            <el-button size="mini">终止检测</el-button>
          </el-form-item>
          <el-form-item>
            <el-button size="mini">设置中心</el-button>
          </el-form-item>
        </el-form>
      </div>
      <div>
       <el-table
          :data="tableData"
          border
          style="width: 100%; height: 100%;">
        <el-table-column
          prop="date"
          label="日期"
          width="180">
        </el-table-column>
        <el-table-column
          prop="name"
          label="姓名"
          width="180">
        </el-table-column>
        <el-table-column
          prop="address"
          label="地址">
        </el-table-column>
        </el-table>
    </div>
  </el-main>
  <el-aside>
    <el-form style="margin-right:25px">
      <el-form-item label="Console Logs">
        <el-input type="textarea"
          v-model="logs"
          :autosize="{ minRows: 24, maxRows: 500}"
          ></el-input>
        </el-form-item>
      </el-form>
    </el-aside>
  </el-container>
  </div>
</template>

<script>
  import SystemInformation from './LandingPage/SystemInformation'

  export default {
    name: 'landing-page',
    components: { SystemInformation },
    data:function() {
      return {
        logs: '',
        concurrent: 10,
        time_out: 10,
        retry: 0,
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }]
      }
    },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      }
    }
  }
</script>

<style>
/*
  @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro');

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body { font-family: 'Source Sans Pro', sans-serif; }

  #wrapper {
    background:
      radial-gradient(
        ellipse at top left,
        rgba(255, 255, 255, 1) 40%,
        rgba(229, 229, 229, .9) 100%
      );
    height: 100vh;
    padding: 60px 80px;
    width: 100vw;
  }

  #logo {
    height: auto;
    margin-bottom: 20px;
    width: 420px;
  }

  main {
    display: flex;
    justify-content: space-between;
  }

  main > div { flex-basis: 50%; }

  .left-side {
    display: flex;
    flex-direction: column;
  }

  .welcome {
    color: #555;
    font-size: 23px;
    margin-bottom: 10px;
  }

  .title {
    color: #2c3e50;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 6px;
  }

  .title.alt {
    font-size: 18px;
    margin-bottom: 10px;
  }

  .doc p {
    color: black;
    margin-bottom: 10px;
  }

  .doc button {
    font-size: .8em;
    cursor: pointer;
    outline: none;
    padding: 0.75em 2em;
    border-radius: 2em;
    display: inline-block;
    color: #fff;
    background-color: #4fc08d;
    transition: all 0.15s ease;
    box-sizing: border-box;
    border: 1px solid #4fc08d;
  }

  .doc button.alt {
    color: #42b983;
    background-color: transparent;
  }
  */
</style>
