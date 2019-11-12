
var http = require('http');
var https = require('https');
var dev_config = require('./config/development_config')
var fs = require('fs'), request = require('request');


function getImgResponsePromise() {
    return new Promise((resolve, reject) => {
        var options = {
            hostname: dev_config.url,
            path: dev_config.captcha_img_path
        };
        http.get(options, function(response) {
            console.log('Get img response.')
            console.log(response.statusCode);
            if (response.statusCode != '200') {
                reject(response.statusCode);
            } else {
                resolve(response);
            }
        });
    })
}


// console.log();
// res.pipe(fs.createWriteStream("2.png").on('close', function(){
//     console.log('done2');
// }));


getImgResponsePromise().then(response => {
        console.log(response.headers)
        cookie = response.headers['set-cookie'][0].split(";")[0];
        console.log('Cookie = ' + cookie)
        var options = {
            hostname: dev_config.url,
            path: dev_config.captcha_audio_path, 
            headers: {
                'Cookie': cookie
            }
        };
        http.get(options, function(response) {
            console.log('Get audio response.')
            console.log(response.statusCode);
            console.log(response.headers);
            if (response.statusCode == '200') {
                response.pipe(fs.createWriteStream("audio.mp3").on('close', function(){
                    console.log('Save mp3 finish.');
                }));
            }
        });
    }
);

