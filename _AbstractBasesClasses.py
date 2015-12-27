# coding=utf-8

import abc # Abstract Base Classes

class AbstractTalker(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def format(self, message):
        return message

    def say(self, message):
        print self.format(message)

class LoudTalker(AbstractTalker):
    def format(self, message):
        return "%s!" % message

class Screamer(LoudTalker):
    def format(self, message):
        return super(Screamer, self).format(message).upper()



class ShoutFormatterMixin(object):
    def format(self, message):
      return "%s!" % message

class PublicAddressSystem(ShoutFormatterMixin, AbstractTalker):
    def play_music(self, song):
        super(PublicAddressSystem, self).say(song.tablature)




if __name__ == '__main__':
    b = LoudTalker()
    b.say('b talking')
    print(b.__class__.__base__)
    print(b.__class__.__base__.__base__)
    c = Screamer()
    c.say('c talking')
    print(c.__class__.__base__)
    print(c.__class__.__base__.__base__)
    print(c.__class__.__base__.__base__.__base__)

    f = PublicAddressSystem()
    f.say('f1')
    print(f.__class__.__base__)
    print(f.__class__.__base__.__base__)
    print(f.__class__.__base__.__base__.__base__)


    d = ShoutFormatterMixin()
    print(d.format('d'))
