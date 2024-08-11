import click
import secrets
import string

# ====================

@click.group(help="A group of commands for password generator.")
def gen_pass():
    """
    A group of commands for the password generator.
    This function serves as the entry point for the Click group.
    """
    pass

# ====================

@click.command("gen")
@click.option("-l", "--length", type=int, required=True, help="Length of password (minimum: 8).")
@click.option("-c", "--include-cap", is_flag=True, help="Include uppercase letters in the password.")
@click.option("-n", "--include-num", is_flag=True, help="Include numbers in the password.")
@click.option("-s", "--include-sp", is_flag=True, help="Include special characters in the password.")
def generate_pass(length, include_cap, include_num, include_sp):
    """
    Generate a random password based on specified criteria.

    Parameters:
    - length (int): The length of the password to be generated. Must be at least 8.
    - include_cap (bool): Flag to include uppercase letters in the password.
    - include_num (bool): Flag to include numbers in the password.
    - include_sp (bool): Flag to include special characters in the password.

    Raises:
    - click.BadParameter: If the password length is less than 8 or no character types are included.
    """
    
    # check if the length is less than the minimum required
    if length < 8:
        raise click.BadParameter("Password length must be at least 8.")

    # initialize the alphabet with lowercase letters
    alphabet = string.ascii_lowercase
    
    # include uppercase letters if the flag is set
    if include_cap:
        alphabet += string.ascii_uppercase  # Append uppercase letters
    
    # include numbers if the flag is set
    if include_num:
        alphabet += string.digits  # Append digits
    
    # include special characters if the flag is set
    if include_sp:
        alphabet += string.punctuation  # Append special characters

    # ensure at least one character type is included
    if len(alphabet) == 0:
        raise click.BadParameter("At least one character type must be included.")

    # generate the password by selecting random characters from the alphabet
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    
    # output the generated password
    click.echo(f"\nGenerated Password:\n{password}\n")

# ====================

# Add the generate_pass command to the gen_pass group
gen_pass.add_command(generate_pass)

# ====================

if __name__ == "__main__":
    gen_pass()
