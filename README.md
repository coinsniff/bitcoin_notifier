bitcoin_notifier
================

Notifier for bitcoin based on prices. Text/email

### Currently ONLY tested with Python 2.7 on ubuntu (linux)

To email:<br/>
First, create a file called UsernameAndPassword.py and place in same directory as main.py<br/>
Note, this uses Gmail SMTP servers so input your gmail username and password (I promise I won't steal it!)<br/>

Include the code:
```python
gmailUsername = "insert email@here.com"
gmailPassword = "insert real passowrd here"
```
Make sure to keep the quotes. Replace the text in between quotes

Script usage is
```python
python main.py [comparison operator] [price] [email address] [interval (hours) in between notifications] [exchange]
```
Note that the only exchange supported right now is coinbase so put 'coinbase' for exchange.<br/>
Also, the comparison operator must be put in single quotes i.e. '<' <br/>
Price can be any float (decimal) number i.e. 340.11 or 660<br/>
email address is obviously any valid email address<br/>
Interval in HOURS between each notifcation. Accepts decimals (i.e for every 10 minutes, input 0.16666).<br/>
If you put 1 (hour), when it hits your price threshold, it will send you an email and then "sleep" for an hour
and won't start checking or sending you notifications until an hour later.<br/>

##### Note that the comparison operator only accepts two inputs currently, '>' or '<'

Current supported exchanges: Coinbase, Coinbase Exchange, Bitstamp, Bitfinex, Btc-e

### Example usage
```python
python main.py '<' 350.52 test@gmail.com 6 coinbase
```
Sends a notification once every 6 hours ONLY IF coinbase exchange price is < $350.52

```python
python main.py '>' 500 ilikebitcoin@gmail.com 0.5 coinbase
```
Sends a notifcation once every half an hour (0.5 hours) ONLY IF coinbase exchange price is > $500


## Disclaimer: I do not take any responsibility for any resulting action (good or bad) from using this code. Use at your own risk<br/>
## I am not accountable for any money you lose using this program

