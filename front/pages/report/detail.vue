<template>
  <div class="container">
    <el-row>
      <div class="report">
        {{ data.name || 'Clover测试报告' }}
      </div>
    </el-row>
    <el-row>
      <div class="title">
        Summary
      </div>
    </el-row>
    <el-row>
      <el-table
        :data="headers"
        :show-header="false"
        style="width: 100%"
        border
      >
        <el-table-column
          prop="hc1"
          min-width="16.66%"
        />
        <el-table-column
          prop="hc2"
          min-width="16.66%"
        />
        <el-table-column
          prop="hc3"
          min-width="16.66%"
        />
        <el-table-column
          prop="hc4"
          min-width="16.66%"
        />
        <el-table-column
          prop="hc5"
          min-width="16.66%"
        />
        <el-table-column
          prop="hc6"
          min-width="16.66%"
        />
      </el-table>
    </el-row>
    <el-row>
      <div class="title">
        Detail
      </div>
    </el-row>
    <el-row>
      <el-table
        :data="results"
        :row-class-name="tableRowClassName"
        style="width: 100%"
        border
      >
        <el-table-column
          prop="name"
          label="用例名"
          width="200"
        />
        <el-table-column
          prop="start"
          label="开始时间"
          width="180"
        />
        <el-table-column
          prop="end"
          label="结束时间"
          width="180"
        />
        <el-table-column
          prop="elapsed"
          label="请求时间(ms)"
          width="120"
        />
        <el-table-column
          prop="operate"
          label="比较操作"
          width="180"
        />
        <el-table-column
          prop="expect"
          label="期盼结果"
          width="180"
        />
        <el-table-column
          prop="actual"
          label="实际结果"
          width="180"
        />
        <el-table-column
          prop="status"
          label="状态"
        >
          <template slot-scope="scope">
            <el-tag
              :type="scope.row.status === 'passed' ? 'success' : 'error'"
              disable-transitions
            >
              {{ scope.row.status }}
            </el-tag>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      data: {
        platform: {
        },
        detail: {}
      },
      headers: [],
      results: [],
      total: 0,
      success: 0,
      failed: 0,
      error: 0,
      skip: 0,
      percent: 0.0,
      fail_or_error: false
    }
  },
  mounted () {
    this.refresh()
  },
  methods: {
    handleFormat (data) {
      // python返回的None数据通过json转换成js的null。
      if (data === null) {
        return 'None'
      }
      return data
    },
    refresh () {
      this.$axios
        .post('/api/v1/report/search', { id: this.$route.query.id })
        .then((res) => {
          if (res.data.status === 0) {
            this.data = res.data.data
            console.log(res.data.data)
            this.total = this.data.interface.total
            this.success = this.data.interface.passed
            this.failed = this.data.interface.failed
            this.error = this.data.interface.error
            this.skiped = this.data.interface.skiped
            this.percent = this.data.interface.percent.toFixed(0) + '%'
            // 这里是报告的详细数据。
            for (const name in this.data.detail) {
              for (const index in this.data.detail[name].result) {
                let elapsed = 0
                elapsed = this.handleFormat(this.data.detail[name].elapsed)
                let actual = '-'
                actual = this.handleFormat(this.data.detail[name].result[index].actual)
                let expect = '-'
                expect = this.handleFormat(this.data.detail[name].result[index].expect)
                this.results.push({
                  name,
                  start: this.data.detail[name].start,
                  end: this.data.detail[name].end,
                  elapsed,
                  status: this.data.detail[name].result[index].status,
                  actual,
                  expect,
                  operate: this.data.detail[name].result[index].operate
                })
              }
            }
            // 这里是报告的表头数据。
            this.headers.push({
              hc1: '部门',
              hc2: this.data.team,
              hc3: '项目',
              hc4: this.data.project,
              hc5: '类型',
              hc6: this.data.type
            })
            this.headers.push({
              hc1: 'Clover平台',
              hc2: this.data.platform.clover,
              hc3: 'Python',
              hc4: this.data.platform.python,
              hc5: '操作系统',
              hc6: this.data.platform.platform
            })
            this.headers.push({
              hc1: '开始时间',
              hc2: this.data.start,
              hc3: '结束时间',
              hc4: this.data.end,
              hc5: '持续时间(ms)',
              hc6: this.data.duration
            })
            this.headers.push({
              hc1: '全部',
              hc2: '成功',
              hc3: '失败',
              hc4: '错误',
              hc5: '跳过',
              hc6: '通过率'
            })
            this.headers.push({
              hc1: this.total,
              hc2: this.success,
              hc3: this.failed,
              hc4: this.error,
              hc5: this.skip,
              hc6: this.percent
            })
            if (this.fail_or_error) {
              this.$message({
                type: 'error',
                message: '测试报告中检测到断言失败或错误，请关注！',
                center: true,
                offset: 160
              })
            }
          } else {
            this.$message({
              type: 'warning',
              message: res.data.message,
              center: true
            })
          }
        })
        .catch(() => {
          this.$message({
            type: 'error',
            message: '服务出错，请联系管理员',
            center: true
          })
        })
    },
    tableRowClassName ({ row, rowIndex }) {
      if (row.status === 'passed') {
        return 'success'
      } else if (row.status === 'error') {
        return 'danger'
      } else if (row.status === 'failed') {
        return 'warning'
      } else if (row.status === 'skip') {
        return 'info'
      } else {
        return 'primary'
      }
    }
  }
}
</script>

<style scoped>
.container {
  padding-left: 36px;
  padding-right: 36px;
}

.report {
  padding-top: 20px;
  padding-bottom: 20px;
  font-size: 36px;
  text-align: center;
}

.title {
  padding-top: 20px;
  padding-bottom: 20px;
  font-size: 20px;
}
</style>
