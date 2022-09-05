import functools
import sys
import traceback


def wrap_response(func):
    @functools.wraps(func)
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as err:
            print(type(err), file=sys.stderr)
            print(str(err), file=sys.stderr)
            print(err.__class__.__name__, file=sys.stderr)
            traceback.print_exc()
            print("-" * 60)
        # finally:
        #     return json.dumps(
        #         response,
        #         default=json_default,
        #     ).encode("utf-8")

    return inner_function