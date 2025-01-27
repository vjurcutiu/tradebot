from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import web3, get_coin_data  # Import the global web3 instance

app = Flask(__name__)
CORS(app)

@app.route('/api/block-number', methods=['GET'])
def get_block_number():
    """
    Endpoint to fetch the latest Ethereum block number.
    """
    try:
        if web3 is None:
            raise Exception("Web3 is not connected to the Ethereum node")
        
        if request.args.get('force_error') == 'true':
            # Simulate an error by raising an exception
            raise Exception("Forced error for testing purposes")
        
        block_number = web3.eth.block_number
        return jsonify({"block_number": block_number})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/coin-data', methods=['GET'])
def get_coin_data_route():
    """
    Endpoint to fetch cryptocurrency data.
    """
    coin_id = request.args.get('coin_id', 'bitcoin')  # Default to 'bitcoin' if no coin_id is provided
    try:
        coin_data = get_coin_data(coin_id)
        return jsonify(coin_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
