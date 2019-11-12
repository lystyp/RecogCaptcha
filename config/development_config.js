require('dotenv').config();

module.exports = {
    url: process.env.URL, 
    captcha_img_path: process.env.CAPTCHA_IMG_PATH, 
    captcha_audio_path: process.env.CAPTCHA_AUDIO_PATH
}