import os

facts = []
rules = []

# function to read facts and rules from the file and populate the facts array
def load_facts_and_rules():
    with open("facts_db.txt", "r") as fact_db_content:
        file_contents = fact_db_content.read()
        if file_contents:
            content0 = file_contents.strip()
            facts.extend(content0.split('|'))
    with open("rules_db.txt", "r") as rule_db_content:
        file_contents = rule_db_content.read()
        if file_contents:
            content1 = file_contents.strip()
            rules.extend(content1.split('|'))

# load initial facts and rules from the files
load_facts_and_rules()

def print_facts_and_rules():
    print("\nFacts: ")
    for f in facts:
        print(f)
    print("\nRules: ")
    for r in rules:
        print(r)

def add_fact(fact):
    fact = fact.lower()
    if fact and fact not in facts:
        facts.append(fact)
        print(f"\nFact '{fact}' has been added to facts.\n")
        print_facts_and_rules()

        # Add the new fact to the facts database (txt file)
        with open("facts_db.txt", "a") as file:
            file.write(fact + "|")
    else:
        print("Constraints! Fact input must not already exist in facts list, must not be empty, and must be in lowercase.")
        print_facts_and_rules()

def add_rule(rule):
    rule = rule.lower()
    if rule and rule not in rules and "if " in rule and ", then " in rule:
        rules.append(rule)
        print(f"\nRule '{rule}' has been added to rules.\n")
        print_facts_and_rules()
        # Add the new rule to the rules database (txt file)
        with open("rules_db.txt", "a") as file:
            file.write(rule + "|")
    else:
        print("Constraints! Rule input must not already exist in rules list, must not be empty, and must be in the right format and lowercase.")
        print_facts_and_rules()

def generate_new_created_fact(count = 0):
    new = False
    print(f"ITERATION {count}:")
    for r in rules:
        if " then " in r:
            # conditions == antecedents
            # result == consequent
            conditions, result = r.split(", then ")
            condition_facts = conditions.replace("if ", "").split(" and ")

            # check if the conditions in a particular string rule are present in facts database
            # and the result is not a duplicate fact
            print("FACTS: ", facts)
            print(f"CHECKING RULE: '{r}'")
            print(f"CONDITION(s): {condition_facts}")
            print(f"CONSEQUENT: '{result}'")
            print(f"PROCESSING: Checking if all conditions is a present fact in facts and the result is not in facts...")

            if all(condition in facts for condition in condition_facts) and result not in facts:
                print(f"FINDINGS: Rule is true. So '{result}' will now be a new fact.")
                print(f"NEW GENERATED FACT: {result}\n")
                new = True
                facts.append(result)
                with open("facts_db.txt", "a") as file:
                    file.write(result + "|")

            elif result in facts:
                print(f"Consequent '{result}' is already in facts.\n")

            else:
                print("FINDINGS: Rule is not true. The result can't be added as a new fact.\n")
    if new:
        generate_new_created_fact(count + 1)
    else:
        print("Done.")

# main loop
while True:
    print_facts_and_rules()
    print("\nOptions:")
    print("[1] Enter a new fact")
    print("[2] Enter a new rule")
    print("[3] Generate new facts")
    print("[4] Delete all facts")
    print("[5] Delete all rules")
    print("[6] Delete all facts and rules")
    print("[else] Exit")

    choice = input("\nSelect an Option: ")

    if choice == "1":
        while True:
            new_fact = input("\nEnter a fact (enter '.' to stop): ")
            os.system('cls')
            if new_fact == ".":
                break
            add_fact(new_fact)

    elif choice == "2":
        while True:
            new_rule = input("\nEnter a rule (e.g., 'if condition(s) and condition(s) then result') (enter '.' to stop): ")
            os.system('cls')    
            if new_rule == ".":
                break
            add_rule(new_rule)

    elif choice == "3":
        os.system('cls')
        generate_new_created_fact()

    elif choice == "4":
        os.system('cls')
        facts = []
        with open("facts_db.txt", "w") as file:
            file.truncate(0)  # clear the facts_db.txt file
        print("\nAll facts have been deleted.")

    elif choice == "5":
        os.system('cls')
        rules = []
        with open("rules_db.txt", "w") as file:
            file.truncate(0)  # clear the rules_db.txt file
        print("\nAll rules have been deleted.")

    elif choice == "6":
        os.system('cls')
        facts = []
        rules = []
        with open("facts_db.txt", "w") as facts_file:
            facts_file.truncate(0)  # clear the facts_db.txt file
        with open("rules_db.txt", "w") as rules_file:
            rules_file.truncate(0)  # clear the rules_db.txt file
        print("\nAll facts and rules have been deleted.")

    else:
        break