import should_dingus
from dingus import Dingus
from should_dsl import should, should_not, ShouldNotSatisfied


class TestCall:
    def setup(self):
        self.dinges = Dingus('callable')

    def test_simple_call(self):
        (lambda: self.dinges()) |should| call(self.dinges)

    def test_nothing_called(self):
        (lambda: None) |should_not| call(self.dinges)

    def test_unexpected_call(self):
        def wrapper():
            (lambda: self.dinges()) |should_not| call(self.dinges)
        msg = '<Dingus callable> was unexpectedly called'
        wrapper |should| throw(ShouldNotSatisfied, msg)

    def test_expected_call_not_happened(self):
        def wrapper():
            (lambda: None) |should| call(self.dinges)
        msg = '<Dingus callable> has not been called'
        wrapper |should| throw(ShouldNotSatisfied, msg)

    def test_call_once(self):
        (lambda: self.dinges()) |should| call(self.dinges).once

    def test_too_many_calls(self):
        def wrapper():
            def actions():
                self.dinges()
                self.dinges()
            actions |should| call(self.dinges).once
        msg = '<Dingus callable> was called 2 times, expected 1'
        wrapper |should| throw(ShouldNotSatisfied, msg)

    def test_call_with_positional_param(self):
        def wrapper():
            self.dinges(1)
        wrapper |should| call(self.dinges).with_params(1)

    def test_call_with_wrong_positional_param(self):
        def wrapper():
            def actions():
                self.dinges(2)
            actions |should| call(self.dinges).with_params(1)
        msg = '<Dingus callable> has not been called with params (1,) {}'
        wrapper |should| throw(ShouldNotSatisfied, msg)

    def test_call_with_keyword_param(self):
        def wrapper():
            self.dinges(one=1)
        wrapper |should| call(self.dinges).with_params(one=1)

    def test_call_with_wrong_keyword_param(self):
        def wrapper():
            def actions():
                self.dinges(one=2)
            actions |should| call(self.dinges).with_params(one=1)
        msg = ("<Dingus callable> has not been called "
                "with params () {'one': 1}")
        wrapper |should| throw(ShouldNotSatisfied, msg)

    def test_the_lot(self):
        def wrapper():
            def actions():
                self.dinges(1, one=1)
                self.dinges(1, one=1)
            actions |should| call(self.dinges).once.with_params(1, one=1)
        msg = ("<Dingus callable> was called 2 times "
                "with params (1,) {'one': 1}, expected 1")
        wrapper |should| throw(ShouldNotSatisfied, msg)

    def test_call_should_not_reset(self):
        def wrapper():
            def actions():
                self.dinges()
            actions |should| call(self.dinges).once

        self.dinges()
        self.dinges()
        msg = '<Dingus callable> was called 3 times, expected 1'
        wrapper |should| throw(ShouldNotSatisfied, msg)
