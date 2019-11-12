
var http = require('http');
var dev_config = require('./config/development_config')
var fs = require('fs'), request = require('request');

// Send cookie 方法參考這篇
// https://codeday.me/bug/20180923/262269.html
// 記得網址跟path要分開填，不然他就會去找 (url + path) : 80 ，哪有port接在path後面的!!

// ---------------------------------------------------------------------------------------------
// 抓圖片法1
// url = dev_config.url
// var options = {
//     hostname: url,
//     path: dev_config.captcha_img_path, 
//     method: 'GET'
// };

// http.request(options, function (resp) {
//     resp.pipe(fs.createWriteStream("3.png").on('close', function(){
//         console.log('done1');
//     }));
// }).end();

// ---------------------------------------------------------------------------------------------
// 抓圖片法2
var cookie = ""
var res_img = undefined;
var options2 = {
    hostname: url,
    path: dev_config.captcha_img_path
};
http.get(options2, function(res) {
    console.log(res.headers['set-cookie'][0].split(";")[0]);
    res.pipe(fs.createWriteStream("2.png").on('close', function(){
        console.log('done2');
    }));
});
// ---------------------------------------------------------------------------------------------
