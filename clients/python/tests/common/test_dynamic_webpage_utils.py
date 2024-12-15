from common.dynamic_webpage_utils import dynamic_query_url_with_chrome_driver_and_save

def test_google_dot_com():
    google_dot_com_url = "http://www.google.com/"
    dynamic_query_url_with_chrome_driver_and_save(google_dot_com_url, '/tmp/chrome_driver_test_google_dot_com.html')
