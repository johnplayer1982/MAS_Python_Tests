from flask import Flask, request, render_template
import os
import urllib2
import re

app = Flask(__name__)
@app.route('/')

def my_form():

    return render_template('my-form.html')

@app.route('/', methods=['POST'])

def my_form_post():

    url = request.form['url']

    site_url = urllib2.urlopen(url)
    html = site_url.read()

    links = re.findall('"((http|ftp)s?://.*?)"', html)

    link_count = len(links)
    success_count = 0
    ignore_count = 0
    no_path_count = 0
    error_count = 0
    not_found_count = 0
    image_count = 0

    results = []
    error_results = []
    not_found_results = []
    image_results = []

    for link in links:

        link_path = link[0]
        extension = os.path.splitext(link_path)
        print extension[1]

        if '.jpg' in extension[1] or '.png' in extension[1]:
            image_count += 1
            image_results.append(link)

        elif link_path == 'http://www.w3.org/1999/xhtml':
            print 'Not a visitable URL:', link_path
            ignore_count += 1

        elif link_path == 'https://':
            print 'No full path given:', link_path
            no_path_count += 1

        else:
            link_string = link_path
            open_link = urllib2.urlopen(link_string)
            status = open_link.getcode()

            print 'Checking', link_path

            if status == 200:
                success_count += 1
            elif status == 400:
                error_count += 1
                error_results.append(link)
            elif status == 404:
                not_found_count += 1
                not_found_results.append(link)

        this_result = '<li>Testing: %s | <span>status %s returned</span></li>' % (link_path, status)
        results.append(this_result)

        result_string = str(results)
        result_string = result_string.replace('[', '')
        result_string = result_string.replace(']', '')
        result_string = result_string.replace("'", "")
        result_string = result_string.replace(',', '')

        error_string = str(error_results)
        error_string = error_string.replace('[', '')
        error_string = error_string.replace(']', '')
        error_string = error_string.replace("'", "")
        error_string = error_string.replace(',', '')

        image_string = str(image_results)
        image_string = image_string.replace('[', '')
        image_string = image_string.replace(']', '')
        image_string = image_string.replace("'", "")
        image_string = image_string.replace("(", "")
        image_string = image_string.replace(")", "")
        image_string = image_string.replace(',', '<br />')

        summary_string = 'All Done! I found a total of <span>{link_count}</span> links on <a href="{link_url}" target="_blank">{link_url}</a>, Of these, <span>{success_count}</span> completed with a status code of 200 (success). <span>{no_path_count}</span> links contained incomplete paths, <span>{error_count}</span> links resulted in an error, <span>{not_found_count}</span> links resulted in a 404 (file not found), <span>{image_count}</span> links were actually images'.format(link_count=link_count,link_url=url,success_count=success_count,no_path_count=no_path_count,error_count=error_count,not_found_count=not_found_count,image_count=image_count)

    return render_template('my-form.html',
                           summary=summary_string,
                           output=result_string,
                           errors=error_string,
                           images=image_string
                           )
