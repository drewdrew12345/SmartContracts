from program import compile_app
from deployment import deploy
from akita_inu_asa_utils import *


def main():
    developer_config = load_developer_config()

    algod_address = developer_config['algodAddress']
    algod_token = developer_config['algodToken']
    algod_client = get_algod_client(algod_token, algod_address)

    compile_app(algod_client)
    print("Program Compiled")

    asset_id = 44887300  # ASSET ID
    end_time = 1636903860  # UTC TIMESTAMP
    algod_address = developer_config['algodAddress']
    algod_token = developer_config['algodToken']
    creator_mnemonic = developer_config['creatorMnemonic']
    creator_public_key = developer_config['creatorAddress']

    deploy(algod_address, algod_token, creator_public_key, creator_mnemonic, asset_id, end_time)
    print("Program Deployed")

main()
