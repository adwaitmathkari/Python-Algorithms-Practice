import asterisk as app


def test_app():
    input_values = [1, 3, "a*bc", "ab*c", "*"]

    f= open("testcase", "r")
    contents =f.read()
    input_values = contents.split()
    print(input_values)
 
    def mock_input():
        # output.append(s)
        return input_values.pop(0)
    app.input = mock_input
    
    
    # app.print = lambda s : output.append(s)


    app.a()
 
test_app()
