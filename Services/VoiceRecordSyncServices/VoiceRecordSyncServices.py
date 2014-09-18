__author__ = 'rui'
#-*- coding: utf-8 -*-

import tornado
from tornado import ioloop
import VoiceRecordEnum
import FileParing
from tornado import web, wsgi
import Messager
from tornado import escape
from tornado import httpserver
import jsonpickle
from ResAudio import resAudioList


class VoiceRecordsResource(web.RequestHandler):
    def initialize(self):
        pass

    def post(self):
        consumer = Messager.MessageConsumer()
        producer = Messager.MessageProducer()
        resAudio = tornado.escape.json_decode(self.request.body)
        if len(resAudio):
            consumer.Listen('')
        for res in resAudioList.GenerateResAudio(resAudio):
            producer.ParallelSend('')


class FilesResource(web.RequestHandler):
    def post(self):
        print self.request.body
        filePath = tornado.escape.json_decode(self.request.body)
        fileParsing = FileParing.FileParsing()
        fileParsing.getFiles(filePath["filePath"].encode("utf-8"))
        self.write({
            "files": jsonpickle.encode(fileParsing.files, unpicklable = False)})


if __name__ == "__main__":
    try:
        print "Services Start"
        app = wsgi.WSGIApplication([(r"/files/path", FilesResource)])
        server = httpserver.HTTPServer(app)
        app.listen(9090)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print "Service Error"


