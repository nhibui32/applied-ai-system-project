from logic_utils import check_guess
import logging

logging.basicConfig(
    filename="logs/reliability_test_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_reliability_tests():
    test_cases = [
        {"guess": 5, "secret": 5, "expected": "Correct!"},
        {"guess": 3, "secret": 5, "expected": "Too low!"},
        {"guess": 8, "secret": 5, "expected": "Too high!"},
        {"guess": 1, "secret": 10, "expected": "Too low!"},
        {"guess": 10, "secret": 1, "expected": "Too high!"},
        {"guess": 7, "secret": 7, "expected": "Correct!"},
    ]

    passed = 0

    for i, test in enumerate(test_cases, start=1):
        try:
            result = check_guess(test["guess"], test["secret"])

            if result == test["expected"]:
                passed += 1
                print(f"Test {i}: PASS")
                logging.info(f"Test {i} passed: {test}")
            else:
                print(f"Test {i}: FAIL")
                print(f"Expected: {test['expected']}, Got: {result}")
                logging.error(
                    f"Test {i} failed: expected {test['expected']}, got {result}"
                )

        except Exception as error:
            print(f"Test {i}: ERROR - {error}")
            logging.error(f"Test {i} crashed: {error}")

    total = len(test_cases)
    reliability_score = passed / total

    print("\nReliability Summary")
    print(f"{passed} out of {total} tests passed.")
    print(f"Reliability Score: {reliability_score:.2f}")

    logging.info(f"Final reliability score: {reliability_score:.2f}")


if __name__ == "__main__":
    run_reliability_tests()