import random
import pandas as pd
import ipaddress

# DataFrames to store results
binary_to_decimal_df = pd.DataFrame(columns=["Generated Binary", "Correct Decimal", "User Answer", "Result"])
decimal_to_binary_df = pd.DataFrame(columns=["Generated Decimal", "Correct Binary", "User Answer", "Result"])
classful_results_df = pd.DataFrame(columns=["IP Address", "Class", "Result"])
subnet_results_df = pd.DataFrame(columns=["IP Address", "Subnet Mask", "Wildcard Mask", "User Answer", "Result"])

def binary_to_decimal_game(user_answer):
    random_binary = format(random.randint(0, 255), '08b')
    correct_decimal = int(random_binary, 2)

    result = "Correct" if user_answer.isdigit() and int(user_answer) == correct_decimal else "Wrong"
    binary_to_decimal_df.loc[len(binary_to_decimal_df)] = [random_binary, correct_decimal, user_answer, result]
    
    return f"Binary: {random_binary}, Decimal: {correct_decimal}, Your Answer: {user_answer} - {result}"

def decimal_to_binary_game(user_answer):
    random_decimal = random.randint(0, 255)
    correct_binary = format(random_decimal, '08b')

    result = "Correct" if user_answer == correct_binary else "Wrong"
    decimal_to_binary_df.loc[len(decimal_to_binary_df)] = [random_decimal, correct_binary, user_answer, result]
    
    return f"Decimal: {random_decimal}, Binary: {correct_binary}, Your Answer: {user_answer} - {result}"

def classful_address_analysis(ip):
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
        classful_results_df.loc[len(classful_results_df)] = [ip, ip_class, "Analyzed"]
        return f"IP Address: {ip}, Class: {ip_class}"
    except Exception as e:
        return f"Error: {e}"

def wildcard_mask_determination(user_answer):
    random_ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.0"
    random_cidr = random.randint(8, 30)
    ip_with_cidr = f"{random_ip}/{random_cidr}"

    try:
        network = ipaddress.ip_network(ip_with_cidr, strict=False)
        subnet_mask = network.netmask
        wildcard_mask = network.hostmask

        result = "Correct" if user_answer == str(wildcard_mask) else "Wrong"
        subnet_results_df.loc[len(subnet_results_df)] = [ip_with_cidr, str(subnet_mask), str(wildcard_mask), user_answer, result]
        return f"IP: {ip_with_cidr}, Subnet: {subnet_mask}, Wildcard: {wildcard_mask}, Your Answer: {user_answer} - {result}"
    except ValueError as e:
        return f"Invalid input: {e}"

def save_results():
    binary_to_decimal_df.to_csv("binary_to_decimal_results.csv", index=False)
    decimal_to_binary_df.to_csv("decimal_to_binary_results.csv", index=False)
    classful_results_df.to_csv("classful_analysis_results.csv", index=False)
    subnet_results_df.to_csv("wildcard_mask_results.csv", index=False)
