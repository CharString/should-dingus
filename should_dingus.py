from should_dsl import matcher

__version__ = '0.3'

class Call(object):
    
    name = 'call'

    def __call__(self, called_dingus):
        self._called_dingus = called_dingus
        self._times = None
        self._args = []
        self._kwargs = {}
        return self

    def __getattr__(self, rterm):
        if rterm == 'once':
            self._times = 1
        return self

    def with_params(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        return self

    def match(self, function):
        function()
        self._calls = self._called_dingus.calls('()',
                *self._args, **self._kwargs)
        if self._times:
            return len(self._calls) == self._times
        else:
            return len(self._calls) > 0

    def message_for_failed_should(self):
        msg = repr(self._called_dingus)
        if not self._calls:
            msg += " has not been called"
        else:
            msg += (" was called %d times" % len(self._calls))

        if self._args or self._kwargs:
            msg += " with params %r %r" % (self._args, self._kwargs)

        if self._times:
            msg += ", expected %d" % self._times
        return msg

    def message_for_failed_should_not(self):
        return "%s was unexpectedly called" % repr(self._called_dingus)

matcher(Call)
