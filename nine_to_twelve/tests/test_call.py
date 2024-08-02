from nine_to_twelve.api.ninetotwelve import ice_breaking, req

def test_ice_breaking():
    
    assert ice_breaking() == "ice_breaking"
    assert True

def test_data_check():
    df = req()
    
    assert len(df) > 1
    