import decimal

# conta methods ## procedural fashion ##

def create(number: int, owner: str, balance: decimal, limit: decimal) -> dict:
    """_summary_

    Args:
        number (int): account number;
        owner (string): owner name;
        balance (decimal): account balance;
        limit (decimal): account limit;

    Returns:
        dict: dict of account
    """
    account = {
        "number": number,
        "owner": owner,
        "balance": balance,
        "limit": limit
          }    
    return account


def deposit(account: dict, value: decimal) -> dict:
    """_summary_

    Args:
        account (dict): receives a account object and update it's 'balance';
        value (decimal): the value to update account's 'balance';

    Returns:
        dict: account updated;
    """
    account["balance"] += value
    return account


def withdraw(account: dict, value: decimal) -> dict:
    """_summary_

    Args:
        account (dict): account to withdraw
        value (decimal): value of withdraw

    Returns:
        dict: account updated
    """
    account["balance"] -= value
    return account


def statement(conta: dict) -> decimal:
    """_summary_

    Args:
        account (dict): account to see the statement

    Returns:
        dict: account's balance
    """
    return f"Balance: {conta.get('balance')}"