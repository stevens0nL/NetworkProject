

import random
import pandas as pd
import ipaddress

# DataFrames to store results
binary_to_decimal_df = pd.DataFrame(columns=["Generated Binary", "Correct Decimal", "User Answer", "Result"])
decimal_to_binary_df = pd.DataFrame(columns=["Generated Decimal", "Correct Binary", "User Answer", "Result"])
classful_results_df = pd.DataFrame(columns=["IP Address", "Class", "Result"])
subnet_results_df = pd.DataFrame(columns=["IP Address", "Subnet Mask", "Wildcard Mask", "User Answer", "Result"])

def binary_to_decimal_game():
    """
    Binary to Decimal Conversion Game.
    Pseudocode:
    1. Generate a random 8-bit binary number.
    2. Convert it to decimal.
    3. Prompt the user to convert the binary to decimal.
    4. Check if the user's answer is correct.
    5. Save the result to a DataFrame.
    """
    random_binary = format(random.randint(0, 255), '08b')
    correct_decimal = int(random_binary, 2)
    print(f"\nConvert the following binary number to decimal: {random_binary}")
    print("Enter the decimal number as an integer (e.g., 42).")
    user_answer = input("Enter your decimal answer: ")

    result = "Correct" if user_answer.isdigit() and int(user_answer) == correct_decimal else "Wrong"
    if result == "Wrong":
        print(f"Incorrect! The correct decimal value is {correct_decimal}")
    else:
        print("Correct!")

    # Save result to DataFrame
    binary_to_decimal_df.loc[len(binary_to_decimal_df)] = [random_binary, correct_decimal, user_answer, result]

def decimal_to_binary_game():
    """
    Decimal to Binary Conversion Game.
    Pseudocode:
    1. Generate a random decimal number (0-255).
    2. Convert it to an 8-bit binary number.
    3. Prompt the user to convert the decimal to binary.
    4. Check if the user's answer is correct.
    5. Save the result to a DataFrame.
    """
    random_decimal = random.randint(0, 255)
    correct_binary = format(random_decimal, '08b')
    print(f"\nConvert the following decimal number to binary: {random_decimal}")
    print("Enter the binary number as an 8-bit string (e.g., 00101010).")
    user_answer = input("Enter your binary answer: ")

    result = "Correct" if user_answer == correct_binary else "Wrong"
    if result == "Wrong":
        print(f"Incorrect! The correct binary value is {correct_binary}")
    else:
        print("Correct!")

    # Save result to DataFrame
    decimal_to_binary_df.loc[len(decimal_to_binary_df)] = [random_decimal, correct_binary, user_answer, result]

def classful_address_analysis():
    """
    Classful Address Analysis.
    Pseudocode:
    1. Prompt the user to enter an IP address.
    2. Determine the class based on the first octet.
    3. Print the IP class.
    4. Save the result to a DataFrame.
    """
    ip = input("\nEnter an IP address (e.g., 192.168.1.1): ").strip()
    try:
        first_octet = int(ip.split('.')[0])
        if 0 <= first_octet <= 127:
            ip_class = "Class A"
        elif 128 <= first_octet <= 191:
            ip_class = "Class B"
        elif 192 <= first_octet <= 223:
            ip_class = "Class C"
        elif 224 <= first_octet <= 239:
            ip_class = "Class D (Multicast)"
        elif 240 <= first_octet <= 255:
            ip_class = "Class E (Experimental)"
        else:
            ip_class = "Invalid IP"
        print(f"The IP address belongs to: {ip_class}")
        classful_results_df.loc[len(classful_results_df)] = [ip, ip_class, "Analyzed"]
    except Exception as e:
        print(f"Error: {e}")


def wildcard_mask_determination():
    """
    Random Subnet Mask and Wildcard Mask Determination.
    Pseudocode:
    1. Generate a random IP address and subnet mask.
    2. Calculate the subnet mask and wildcard mask.
    3. Ask the user to compute the wildcard mask.
    4. Validate the user's response.
    5. Save the result to a DataFrame.
    """
    # Generate random IP and CIDR
    random_ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.0"
    random_cidr = random.randint(8, 30)
    ip_with_cidr = f"{random_ip}/{random_cidr}"

    try:
        # Calculate subnet and wildcard masks
        network = ipaddress.ip_network(ip_with_cidr, strict=False)
        subnet_mask = network.netmask
        wildcard_mask = network.hostmask

        # Display generated data
        print(f"\nIP Address with CIDR: {ip_with_cidr}")
        print(f"Subnet Mask: {subnet_mask}")
        print("Your task: Calculate the Wildcard Mask based on the given Subnet Mask.")

        # Prompt user for answer
        user_answer = input("Enter the Wildcard Mask (e.g., 0.0.0.255): ").strip()

        # Validate user's answer
        result = "Correct" if user_answer == str(wildcard_mask) else "Wrong"
        if result == "Wrong":
            print(f"Incorrect! The correct Wildcard Mask is {wildcard_mask}")
        else:
            print("Correct!")

        # Save results to DataFrame
        subnet_results_df.loc[len(subnet_results_df)] = [ip_with_cidr, str(subnet_mask), str(wildcard_mask), user_answer, result]

    except ValueError as e:
        print(f"Invalid input: {e}")

def save_results():
    """
    Save all results to CSV files.
    Pseudocode:
    1. Save binary-to-decimal results to `binary_to_decimal_results.csv`.
    2. Save decimal-to-binary results to `decimal_to_binary_results.csv`.
    3. Save classful analysis results to `classful_analysis_results.csv`.
    4. Save wildcard mask results to `wildcard_mask_results.csv`.
    """
    binary_to_decimal_df.to_csv("binary_to_decimal_results.csv", index=False)
    decimal_to_binary_df.to_csv("decimal_to_binary_results.csv", index=False)
    classful_results_df.to_csv("classful_analysis_results.csv", index=False)
    subnet_results_df.to_csv("wildcard_mask_results.csv", index=False)
    print("\nResults saved successfully!")


