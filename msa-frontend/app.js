var express = require('express');
var path = require('path');
var port = 3000

var app = express();



app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/api', function (req, res){
  res.json({message: 'Hello, World!!'})
});

// 서버 시작
app.listen(port, () => {
  console.log(`frontend server on port ${port}`)
})