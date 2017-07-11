def remove_url_anchor(url):
    anchor_pos = url.find('#')
    return url if anchor_pos < 0 else url[:anchor_pos]
