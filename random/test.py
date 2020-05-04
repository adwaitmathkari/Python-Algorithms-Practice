import app
 
def test_app():
    input_values = [2, 3]
    output = []
 
    def mock_input(s):
        output.append(s)
        return input_values.pop(0)
    app.input = mock_input
    app.print = print
 
    app.main()

    # print(output)

test_app()

