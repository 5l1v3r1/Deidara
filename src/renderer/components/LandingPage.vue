<template>
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
            <el-input size="mini" id="target" type="text" style="width:150px"></el-input>
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
          style="width: 100%; height: 100%;"
          size="mini">
          <el-table-column type="index" label="ID" align="center" width="50px"></el-table-column>
          <el-table-column prop="host" label="HOST" align="center" width="120px">
            <template slot-scope="scope">
              <el-tag size="mini">{{ scope.row.host }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column align="center" prop="type" label="数据库类型" filter-placement="bottom-end" width="120px">
            <template slot-scope="scope">
              <el-tag size="mini">{{ scope.row.type }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="version" label="版本号" align="center" width="120px">
            <template slot-scope="scope">
              <el-tag size="mini">{{ scope.row.version }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="version" label="用户名" align="center" width="120px">
            <template slot-scope="scope">
              <el-tag size="mini">{{ scope.row.user_name }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="version" label="密码" align="center" width="120px">
            <template slot-scope="scope">
              <el-tag size="mini">{{ scope.row.password }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="操作" align="center">
            <template slot-scope="scope">
              <el-button
                size="mini"
                @click="handleEdit(scope.$index, scope.row)" type="primary">连接</el-button>
              <el-button
                size="mini"
                @click="handleDelete(scope.$index, scope.row)" type="primary">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-pagination
          @size-change="handleSizeChange1"
          @current-change="handleCurrentChange1" :current-page="current_page"
          :page-sizes="[10, 20, 50, 100]"
          :page-size="page_size" layout="total, sizes, prev, pager, next, jumper"
          :total="tableData.length">
          </el-pagination>
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
        current_page: 1,
        page_size: 10,
        tableData: [{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        },{
          host: '127.0.0.1:3306',
          type: 'MySQL',
          version: '5.7',
          user_name: 'root',
          password: '123456'
        }]
      }
    },
    methods: {
       handleSizeChange1: function(page_size) { // 每页条数切换
        this.page_size = page_size
        this.handleCurrentChange1(this.current_page);
    },
    handleCurrentChange1: function(current_page) {//页码切换
        this.current_page = current_page
        this.currentChangePage(this.tableData,current_page) 
    },
    //分页方法（重点）
   currentChangePage(list,current_page) { 
      let from = (current_page - 1) * this.page_size;
      let to = current_page * this.page_size;
      this.tempList = [];
      for (; from < to; from++) {
        if (list[from]) {
          this.tempList.push(list[from]);
        }
      }
    },
    }
  }
</script>
<style>

</style>
