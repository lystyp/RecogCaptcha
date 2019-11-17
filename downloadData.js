
var http = require('http');
var https = require('https');
var dev_config = require('./config/development_config')
var fs = require('fs');


function getImgResponsePromise(name) {
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
                var cookie = response.headers['set-cookie'][0].split(";")[0];
                response.pipe(fs.createWriteStream(name).on('close', function(){
                    console.log('Save image finish.');
                }));
                resolve(cookie);
            }
        });
    })
}


function getAudioResponsePromise(name, cookie) {
    return new Promise((resolve, reject) => {
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
                response.pipe(fs.createWriteStream(name).on('close', function(){
                    console.log('Save mp3 finish.');
                    resolve("Success");
                }));
            } else {
                reject("Download audio error.");
            }
        });
    })
}

async function asyncDownloadData(image_path, audio_path, number){
    for (var i = 0;i < number; i++) {
        image_name = image_path + i + ".png"
        audio_name = audio_path + i + ".mp3"
        let cookie = await getImgResponsePromise(image_name);
        await getAudioResponsePromise(audio_name, cookie);
    }
}

asyncDownloadData("./test_data/image/", "./test_data/audio/", 10000).catch( err => {
    console.log(err);
});
