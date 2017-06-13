try:
	raise SyntaxError("Komunikat")
except Exception as e:
	print "Exception.args value: %s\nException.args type: %s" \
		% (e.args, type(e.args) )
	print "Exception value: %s\nException type: %s" \
		% (e, type(e))
	import sys
	print "sys.exc_type value: %s\nsys.exc_type type: %s" \
		% (sys.exc_type, type(sys.exc_type))
	print "sys.exc_value value: %s\nsys.exc_value type: %s" \
		% (sys.exc_value, type(sys.exc_value))
	print "sys.exc_traceback value: %s\nsys.exc_traceback type: %s" \
		% (sys.exc_traceback, type(sys.exc_traceback))

	print dir(sys.exc_traceback)
	print dir(e)

