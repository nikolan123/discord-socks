from flask import Flask, send_file, render_template, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import requests
import re
import io
import random

app = Flask(__name__)

def gibimage(titlehdv, disc, footr):
    image_width = 700
    image_height = 150
    image = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))

    draw = ImageDraw.Draw(image)

    # Load fonts
    big_font_size = 48
    small_font_size = 24
    footer_font_size = 20  # Define font size for footer text
    big_font = ImageFont.truetype("arial.ttf", size=big_font_size)
    small_font = ImageFont.truetype("arial.ttf", size=small_font_size)
    footer_font = ImageFont.truetype("arial.ttf", size=footer_font_size)

    big_text_x = 10
    big_text_y = 10
    draw.text((big_text_x, big_text_y), titlehdv, fill=(0, 0, 0), font=big_font)

    max_width = image_width - 20
    text_lines = []
    current_line = ''
    for word in disc.split():
        if draw.textlength(current_line + ' ' + word, font=small_font) <= max_width:
            current_line += ' ' + word
        else:
            text_lines.append(current_line.strip())
            current_line = word
    text_lines.append(current_line.strip())

    small_text_y = big_text_y + big_font_size + 10
    for line in text_lines:
        draw.text((big_text_x, small_text_y), line, fill=(0, 0, 0), font=small_font)
        small_text_y += small_font_size

    footer_text_x = 10
    footer_text_y = image_height - footer_font_size - 10
    draw.text((footer_text_x, footer_text_y), footr, fill=(0, 0, 0), font=footer_font)

    # Save image to a byte stream
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)

    return img_byte_array


@app.route("/")
def mainpagey():
    return "This is not affiliated with Discord."

# s/o/ck
@app.route('/channels/')
@app.route('/channels/<path:subpath>')
def catch_channels(subpath=''):
    filename = "images/socknew.png"
    return send_file(filename, mimetype='image/gif')

# s/o/ck -> s/e/x
@app.route('/channxls/')
@app.route('/channxls/<path:subpath>')
def catch_chdfannels(subpath=''):
    filename = "images/sockfetish.png"
    return send_file(filename, mimetype='image/gif')

# s/o/ck -> s/el/ect
@app.route('/channects/')
@app.route('/channects/<path:subpath>')
def catch_chfffannels(subpath=''):
    filename = "images/ok.png"
    return send_file(filename, mimetype='image/gif')

# s/o/ck -> s/chan/mc
@app.route('/mcnels/')
@app.route('/mcnels/<path:subpath>')
def catch_chfsdsdfsdffannels(subpath=''):
    filename = "images/mc.png"
    return send_file(filename, mimetype='image/gif')

# s/o/ck -> s/chan/mc -> s/nels//hi
@app.route('/mc/')
@app.route('/mc/<path:subpath>')
def catch_asdchfsdsdfsdffannels(subpath=''):
    try:
        splitsb = subpath.split('/')
        server = splitsb[0]
        url = f"https://ping.cornbread2100.com/ping/?ip={server}&port=25565"
        response = requests.get(url)

        if response.status_code == 200:
            jsons = response.json()
            titleh = f"{server} is up!"
            motd = jsons['description']['text']
            cleanmotd = re.sub(r'§[a-f0-9klr]', ' ', motd)
            cleanmotd = re.sub(r'\s+', ' ', cleanmotd)
            cleanmotd = re.sub(r'[^\x00-\x7F]+', '', cleanmotd)
        else:
            return send_file(gibimage("Error Aww what a shamey ):", response.text, "Thanks to Cornbread 2100 for letting me use his API <3"), mimetype='image/png')
        return send_file(gibimage(titleh, cleanmotd, "Thanks to Cornbread 2100 for letting me use his API <3"), mimetype='image/png')
    except Exception as e:
        return send_file(gibimage("ok", "ok", "Thanks to Cornbread 2100 for letting me use his API <3"), mimetype='image/png')

# s/o/ck -> s/ls/f
@app.route('/channef')
@app.route('/channef/<path:subpath>')
def catch_awedfsdchfsdsdfsdffannels(subpath=''):
    while True:
        try:
            responsee = requests.get("https://api.cornbread2100.com/count?query={}")
            randnum = int(responsee.text)
            randnum = random.randint(1, randnum-1)

            qq = "&query={}"
            furl = f"https://api.cornbread2100.com/servers?limit=1&skip={randnum}"
            url = furl
            url += qq
            response = requests.get(url)

            if response.status_code == 200:
                jsons = response.json()
                jsons = jsons[0]
                titleh = f"{jsons['ip']}:{jsons['port']}"
                try:
                    motd = jsons['description']['text']
                except:
                    motd = "MOTD failed to load ): what a shamey"
                cleanmotd = re.sub(r'§[a-f0-9klr]', ' ', motd)
                cleanmotd = re.sub(r'\s+', ' ', cleanmotd)
                cleanmotd = re.sub(r'[^\x00-\x7F]+', '', cleanmotd)
            else:
                return send_file(gibimage("Error Aww what a shamey ):", response.text, "s/ef/$&/h for next page, Thanks to Cornbread 2100 for letting me use his API <3"), mimetype='image/png')
            return send_file(gibimage(titleh, cleanmotd, "s/ef/$&/h for next page, Thanks to Cornbread 2100 for letting me use his API <3"), mimetype='image/png')
        except Exception as e:
            print(e)

@app.route('/invite/')
@app.route('/invite/<path:subpath>')
def catch_chffffsfannels(subpath=''):
    return render_template("invite.html", title="ok")



@app.route('/generate_image', methods=['GET'])
def generatjle_image():
    big_text = request.args.get('big_text')
    small_text = request.args.get('small_text')
    footer_text = request.args.get('footer_text')
    if big_text is None or small_text is None or footer_text is None:
        return jsonify({'error': 'big_text, small_text, and footer_text parameters are required'}), 400



    return send_file(gibimage(big_text, small_text, footer_text), mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
