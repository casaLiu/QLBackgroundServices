__author__ = 'rui'
#-*- coding: utf-8 -*-

import tornado
from tornado import ioloop
import VoiceRecordEnum
import FileParing
import pyrestful
from pyrestful import mediatypes
from pyrestful.rest import get, post, put, delete
import Messager
from tornado import escape
import jsonpickle
from ResAudio import resAudioList


class VoiceRecordsResource(pyrestful.rest.RestHandler):
    @post(_path = "/voicerecordSync", _types = [str], _produces = mediatypes.APPLICATION_JSON)
    def createVoiceRecord(data):
        consumer = Messager.MessageConsumer()
        producer = Messager.MessageProducer()
        resAudio = tornado.escape.json_decode(data.request.body)
        if len(resAudio):
            consumer.Listen('')
        for res in resAudioList.GenerateResAudio(resAudio):
            producer.ParallelSend('')


class FilesResource(pyrestful.rest.RestHandler):
    @post(_path = "/files/path", _type = [str], _produces = mediatypes.APPLICATION_JSON)
    def ProcessFile(data):
        filePath = tornado.escape.json_decode(data.request.body)
        fileParsing = FileParing.FileParsing()
        fileParsing.getFiles(filePath["filePath"].encode("utf-8"))
        return {
            "files": jsonpickle.encode(fileParsing.files, unpicklable = False)}


if __name__ == "__main__":
    try:
        print "Services Start"
        app = pyrestful.rest.RestService([FilesResource, VoiceRecordsResource])
        app.listen(9090)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print "Service Error"


