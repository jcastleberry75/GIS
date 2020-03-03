from flask import Flask, request
from custom_logger import cus_logger


logger = cus_logger("zoom_tests.log")

def error_handler(error):
    error_msg = str(error)
    logger.critical("The Flask Server has generated the following error")
    logger.debug(error_msg)


def main():
    logger.info('#################### FLASK SERVER STARTED  ####################')
    app = Flask(__name__)

    @app.route("/testing", methods=['POST'])
    def test():
        try:
            if request.method == 'POST':
                incoming_msg = request.args.get('msg')
                if incoming_msg:
                    logger.info(incoming_msg)
                    rsp = f"""Message Received: {incoming_msg}"""
                    logger.info(rsp)
                    return(rsp)
                else:
                    logger.warning(f"""Bad POST: {request}""")
                    return ("Go Away")
            else:
                logger.warning(f"""Bad POST: {request}""")
                return("Go Away")

        except (OSError, SystemError, ConnectionError, Exception) as err:
            error_handler(err)

    while True:
        app.run(host='0.0.0.0', debug=True, port=10001)


if __name__ == "__main__":
    main()
