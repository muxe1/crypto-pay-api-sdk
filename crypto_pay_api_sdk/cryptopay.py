from requests import get, post

class Crypto:
    """
    First, you need to create your application and get an API token.
    Open [@CryptoBot](http://t.me/CryptoBot?start=pay) or [@CryptoTestnetBot](http://t.me/CryptoTestnetBot?start=pay) (for testnet),
    send a command `/pay` to create a new app and get API Token.
    
    Args:
        token {string} - Your API token
    """    
    def __init__(self, token, testnet = False):
        self.token = str(token)
        if testnet:
            self.url = 'https://testnet-pay.crypt.bot/api'
            
        else:
            self.url = 'https://pay.crypt.bot/api'   
        self.headers = {'Content-Type': 'application/json', 'Crypto-Pay-API-Token': self.token}  
        
    def getMe(self) -> (dict):
        """A simple method for testing your app's authentication token.
        
        Args:
            Requires no parameters.
            
        Returns:
            Basic information about the app.
        """             
        return get(f'{self.url}/getMe', headers=self.headers).json()
    
    def createInvoice(self, asset: str, amount: str, params= {}) -> (dict):
        """Use this method to create a new invoice.

        Args:
            asset {string} - Currency code. Supported assets: `BTC`, `TON`, `ETH` (only testnet), `USDT`, `USDC`, `BUSD`

            amount {string} - Amount of the invoice in float. For example: `125.50`
            
            description {string} - Optional. Description of invoice. Up to `1024 symbols`
            
            hidden_message {string} - Optional. The message will show when the user pays your invoice
            
            paid_btn_name {string} - Optional. Paid button name. This button will be shown when your invoice was paid
            Supported names: `viewItem` - View Item, `openChannel` - Open Channel, `openBot` - Open Bot, `callback` - Return
            
            paid_btn_url {string} - Optional. Paid button URL. You can set any payment success link (for example link on your bot)
            
            payload {string} - Optional. Some data. User ID, payment id, or any data you want to attach to the invoice; up to `4kb`
            
            allow_comments {boolean} - Optional. Allow adding comments when paying an invoice. `Default is true`
            
            allow_anonymous  {boolean} - Optional. Allow pay invoice as anonymous. `Default is true`
            
            expires_in {boolean} - Optional. You can set the expiration date of the invoice in seconds. Use this period: `1-2678400 seconds`
            
        Returns:
            Object of created invoice.
        """         
        return post(f'{self.url}/createInvoice',
                        headers = self.headers,
                        json = {'asset': asset,
                                'amount': amount,
                                **params}
                        ).json()     
        

    def transfer(self, user_id: int, asset: str, amount: str, spend_id: str, params = {}) -> (dict):
        """Use this method to send coins from your app to the user.

        Args:
            user_id {number} - Telegram User ID.
            
            asset {string} - Currency code. Supported assets: `BTC`, `TON`, `ETH` (only testnet), `USDT`, `USDC`, `BUSD`
            
            amount {string} - Amount of the transfer in float. For example: `125.50`
            
            spend_id {string} - Uniq ID to make your request idempotent. Up to `64 symbols`
            
            comment {string} - Optional. The comment of the invoice. Up to `1024 symbols`
            
            disable_send_notification {boolean} - Optional. Pass true if the user should not receive a notification about the transfer. `Default is false`
            
        Returns:
            Object of completed transfer.
        """        
        return post(f'{self.url}/transfer',
                        headers = self.headers,
                        json = {'user_id': user_id,
                                'asset': asset,
                                'amount': amount,
                                'spend_id': spend_id,
                                **params}
                        ).json()

    def getInvoices(self, params={}) -> (dict):
        """Use this method to get invoices of your app

        Args:
            asset -- Optional. Currency code.
            Supported assets: `BTC`, `TON`, `ETH` (only testnet), `USDT`, `USDC`, `BUSD`. Default: all assets

            invoice_ids {string} - Optional. Invoice `IDs` separated by comma

            status {string} - Optional. Status of invoices. Available statusses: active or paid. `Default: all statusses`

            offset {number} - Optional. Offset needed to return a specific subset of invoices. `Default 0`

            count {number} - Optional. Number of invoices to return. `Default 100, max 1000`

        Returns:
            Array of invoices
        """
        return get(f'{self.url}/getInvoices', headers=self.headers, json={**params}).json()

    def getBalance(self) -> (dict):
        """Use this method to get balance of your app

        Args:
            Requires no parameters.
            
        Returns:
            Array of assets
        """
        return get(f'{self.url}/getBalance', headers=self.headers).json()
        
    def getExchangeRates(self) -> (dict):
        """Use this method to get exchange rates of supported currencies

        Args:
            Requires no parameters.
            
        Returns:
            Array of currencies
        """
        return get(f'{self.url}/getExchangeRates', headers=self.headers).json()  
        
    def getCurrencies(self) -> (dict):
        """Use this method to supported currencies

        Args:
            Requires no parameters.
            
        Returns:
            Array of currencies
        """
        return get(f'{self.url}/getCurrencies', headers=self.headers).json() 
       
    
    