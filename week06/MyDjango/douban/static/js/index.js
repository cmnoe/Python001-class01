const columns = [
  {
    title: '用户名',
    dataIndex: 'user',
    key: 'user',
  },
  {
    title: '打分',
    dataIndex: 'star',
    key: 'star',
  },
  {
    title: '评论',
    dataIndex: 'content',
    key: 'content',
  }
]

let dataSource = null

let xmlHttp = new XMLHttpRequest()

function getShort(key) {
  xmlHttp.onreadystatechange =callback
  xmlHttp.open("get", `http://127.0.0.1:8000/douban/data/${key}`, true)

  xmlHttp.send()
}

function callback() {
  if (xmlHttp.readyState == 4)
      if (xmlHttp.status == 200) {
          //取得返回的数据
          let data = xmlHttp.responseText;
          //json字符串转为json格式
          dataSource = JSON.parse(eval(data));
          dataSource = dataSource.map(item => item.fields)
          ReactDOM.render(
            <div className="App">
              <h1>《霸王别姬》短评</h1>
              <antd.Input placeholder="输入搜索内容" style={{ width: 200, marginBottom: 10, marginLeft: 10 }} />
              <antd.Button type="primary" onClick={_ => getShort(document.getElementsByTagName('input')[1].value)} style={{ marginLeft: 8 }}>
                搜索
              </antd.Button>
              <antd.Table dataSource={dataSource}  columns={columns} rowKey='user' />
            </div>,
            document.getElementById("root")
          );    
      }
}

getShort('')
