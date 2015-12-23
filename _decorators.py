# coding=utf-8


def transact(method):
    def transacted_call(slf, *args, **kwargs):
        try:
            transaction = self.start_transaction()
            r = method(slf, *args, **kwargs)
            transaction.commit()
            return r
        except:
            transaction.rollback()
            raise
    return transacted_call

class C:
    @transact
    def update(self, what):
        return x