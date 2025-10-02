from linechart import app

def test_radio(dash_duo):
   dash_duo.start_server(app)
   dash_duo.wait_for_element("#region_selector", timeout=10)

def test_header(dash_duo):
   dash_duo.start_server(app)
   dash_duo.wait_for_element("#header", timeout=10)


def test_graph(dash_duo):
   dash_duo.start_server(app)
   dash_duo.wait_for_element("#px-line", timeout=10)
