import argparse
import json

if __name__ == "__main__":
    # Args set up
    parser = argparse.ArgumentParser(description = "Say Hello to Your Fellow Cohort-Members", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--message-file", type=str, default="./messages/factory_hello.json", help="Message File - a JSON-formatted file with keys name, message, and sign_off")
    args = parser.parse_args()

    # Read the file and verify its contents
    message_dict = json.load(open(args.message_file, "r"))
    required_keys = ["name", "message", "sign_off"]
    assert all(key in message_dict for key in required_keys), "Missing one or more required keys"

    # Print a message
    print("Hello UCB Cohort, my name is %s. " % message_dict["name"], end="")
    print("%s." % message_dict["message"])
    print("Until next time,\n\t%s" % message_dict["sign_off"])

