

def test_wordpress_is_working(host):
    cmd = host.run("curl -L http://localhost | grep 'WordPress'")
    assert cmd.rc == 0
