__author__ = 'rui'
#-*- coding: utf-8 -*-

from richenum import EnumConstructionException
from richenum import EnumLookupError
from richenum import RichEnum
from richenum import RichEnumValue


class EncodingEnumValue(RichEnumValue):
    def __init__(self, flavor, *args):
        super(EncodingEnumValue, self).__init__(*args)
        self.flavor = flavor


class AudioFormatEnumValue(RichEnum):
    def __init__(self, flavor, *args):
        super(AudioFormatEnumValue, self).__init__(*args)
        self.flavor = flavor


class ChannelEnumValue(RichEnum):
    def __init__(self, flavor, *args):
        super(ChannelEnumValue, self).__init__(*args)
        self.flavor = flavor





