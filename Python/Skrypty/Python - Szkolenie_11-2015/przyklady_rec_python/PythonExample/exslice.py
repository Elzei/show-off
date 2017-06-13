class MyA(object):
    def __getitem__(self, *arg):
        print "len() -> %d" % len(arg)
        for i in arg:
            print "type: %s, val: %s" \
                % ( type(i), i )

a = MyA()
# Tradycyjnie, lista 1 elementowa
a[1:2:4]
# Tryb rozszerzony, lista 2 elementowa
a[1:2:,2:5:8]
# Z argumentem Ellipsis
a[..., 8:20:1]
