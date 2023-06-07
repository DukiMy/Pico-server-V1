class WebPage:
    
    def firstPage(temperature, pico_led_state, formatted_uptime_info, cpu_freq):
        
        # TODO: Fix the white-space: pre-wrap so that the program doesnt need to rely on tabs in the code editor.
        #		Preferably another approach.
        css_styling = """
            <style>
                body {
                    background-color: lightgrey;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 20px;
                    width: 80%;
                }
                form {
                    display: inline-block;
                    margin-right: 10px;
                }
                input[type="submit"] {
                    padding: 20px 40px;
                    font-size: 20px;
                    border-radius: 5px;
                    transition: background-color 0.3s;
                }
                input[type="submit"]:hover {
                    background-color: #ddd;
                }
                .code-block {
                    display: flex;
                    flex-direction: column;
                    align-items: flex-start;
                    font-size: 20px;
                    font-family: 'Courier New', monospace;
                    padding: 10px;
                    border-radius: 5px;
                    background-color: #2c2a2a;
                    color: #f8f8f8;
                    width: 75%;
                    border: 1px solid #ccc;
                    box-shadow: 2px 2px 6px 0px rgba(0,0,0,0.2);
                    white-space: pre-wrap;
                    line-height: 2;

                }
                .expand {
                    display: inline-block;
                    transition: transform 0.3s;
                    transform-origin: left;
                    margin: 0;
                    text-align: left;
                }
                .expand label {
                    min-width: 150px;
                    display: inline-block;
                }
                .expand:hover {
                    transform: scale(1.5);
                }
            </style>
        """

        # The purpose of the indentation should not be changed if you do not want the code-block contents to change place.
        html = f"""
    <!DOCTYPE html>
    <html>
    <head>

        {css_styling}

    </head>
    <body>
        <div class="container">
        
            <!-- Buttons -->
            <div>
                <form action="./lighton">    <!-- Sends the request type './lighton' when the button is pressed -->
                    <input type="submit" value="Light on" />
                </form>
                
                <form action="./lightoff">
                    <input type="submit" value="Light off" />
                </form>

                <form action="./blink">
                    <input type="submit" value="Blink" />
                </form>    
            </div>
            
            <!-- Code block -->
            <div class="code-block">
                <span class="expand"><label>LED status:</label> {pico_led_state}</span>
                <span class="expand"><label>Temperature:</label> {temperature} C</span>
                <span class="expand"><label>Uptime:</label> {formatted_uptime_info}</span>
                <span class="expand"><label>CPU frequency:</label> {cpu_freq} MHz</span>
            </div>
            
        </div>
    </body>
    </html>
                """
        return str(html)
