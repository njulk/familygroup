# -*- coding: utf-8 -*-

import web
import json
import os

import sys
sys.path.append('..')

import utils

render=web.template.render('templates/')

class ImageController:

    def GET(self):
        '''获取图片上传测试页面'''
        return render.image()

    def POST(self):
        '''上传图片'''
        input=web.input(image={})

        if 'image' in input:
            if 'dir' in input:
                filedir='/static/'+input.dir
            else:
                filedir='/static'

            if os.path.isdir('.'+filedir):
                filepath=input.image.filename.replace('\\','/')
                filename=filepath.split('/')[-1]
                ext=filename.split('.',1)[1].lower()

                if ext=='jpg' or ext=='png' or ext=='gif':
                    url=filedir+'/'+filename

                    try:
                        fout=open('.'+url,'wb')
                        fout.write(input.image.file.read())
                        fout.close()
                        data={
                            'url': url
                        }
                        res=utils.createSuccess(data)
                    except:
                        res=utils.creatFailure(2)
                else:
                    res=utils.creatFailure(3)
            else:
                res=utils.creatFailure(4)
        else:
            res=utils.creatFailure(1)
        
        web.header('content-type', 'text/json')
        return json.dumps(res,cls=utils.JsonExtendEncoder)



