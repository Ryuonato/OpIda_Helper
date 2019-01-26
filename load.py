def plugin_start(plugin_dir):
	"""
	Load this plugin into EDMC
	"""
	print "I am loaded! My plugin folder is {}".format(plugin_dir.encode("utf-8"))
	return "Test"

def plugin_stop():
	"""
	EDMC is closing
	"""
	print "Farwell cruel world!"

	