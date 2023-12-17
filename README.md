# Expert System for Fact and Rule Management

This is a simple expert system written in Python that allows you to manage facts and rules. The system interacts with the user to input new facts and rules, generate new facts based on existing rules, and provides options to delete facts, rules, or both.

## How to Use

1. **Running the Code:**
    - Make sure you have Python installed on your machine.
    - Save the provided code to a file, for example, `expert_system.py`.
    - Open a terminal or command prompt, navigate to the directory containing the file, and run the following command:

    ```bash
    python fc.py
    ```

2. **Options:**
    - The system presents several options to the user:
        - `1`: Enter a new fact.
        - `2`: Enter a new rule.
        - `3`: Generate new facts based on existing rules.
        - `4`: Delete all facts.
        - `5`: Delete all rules.
        - `6`: Delete all facts and rules.
        - Any other key: Exit.

3. **Inputting Facts and Rules:**
    - When prompted, you can input new facts or rules.
    - To stop entering, type a period (`.`) and press Enter.

4. **Generating New Facts:**
    - Option `3` allows the system to generate new facts based on existing rules.
    - It checks the conditions specified in the rules and adds the result as a new fact if the conditions are met.

5. **Deleting Facts and Rules:**
    - Options `4`, `5`, and `6` allow you to delete all facts, all rules, or both, respectively.
    - The corresponding database files (`facts_db.txt` and `rules_db.txt`) will be cleared.

6. **Exiting the Program:**
    - Pressing any other key will exit the program.

## Files
- `facts_db.txt`: Stores the facts entered by the user.
- `rules_db.txt`: Stores the rules entered by the user.

Feel free to experiment with entering different facts and rules and observe how the system generates new facts based on the existing rules.
