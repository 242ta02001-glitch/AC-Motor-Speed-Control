# AC Motor Speed Control System
# EEE Student GitHub Project
# VFD-Based Speed Control Simulation

import time

# Motor specifications
MOTOR_POLES = 4
MAX_FREQUENCY = 50       # Hz
MIN_FREQUENCY = 0        # Hz


def calculate_synchronous_speed(frequency):
    """
    Calculate synchronous speed of an AC motor.

    Formula:
    Ns = (120 * f) / P
    """

    if frequency == 0:
        return 0

    speed = (120 * frequency) / MOTOR_POLES
    return speed


def motor_status(frequency):

    if frequency == 0:
        return "STOPPED"
    elif frequency < 20:
        return "LOW SPEED"
    elif frequency < 40:
        return "MEDIUM SPEED"
    else:
        return "HIGH SPEED"


def display_motor_data(frequency, voltage):

    speed = calculate_synchronous_speed(frequency)
    status = motor_status(frequency)

    print("\n" + "=" * 45)
    print("          AC MOTOR SPEED CONTROL")
    print("=" * 45)

    print(f"Supply Frequency : {frequency:.2f} Hz")
    print(f"Supply Voltage   : {voltage:.2f} V")
    print(f"Motor Poles      : {MOTOR_POLES}")
    print(f"Motor Speed      : {speed:.0f} RPM")
    print(f"Motor Status     : {status}")

    print("=" * 45)


def main():

    print("AC Motor Speed Control System")
    print("VFD-Based Speed Control")
    print("--------------------------------")

    while True:

        try:

            frequency = float(
                input("\nEnter frequency (0-50 Hz): ")
            )

            if frequency < MIN_FREQUENCY or frequency > MAX_FREQUENCY:
                print("Please enter frequency between 0 and 50 Hz.")
                continue

            # V/f control
            voltage = (frequency / MAX_FREQUENCY) * 230

            display_motor_data(frequency, voltage)

            choice = input(
                "\nDo you want to change speed? (y/n): "
            ).lower()

            if choice != "y":

                print("\nAC Motor Control System stopped.")
                break

        except ValueError:

            print("Invalid input!")
            print("Please enter a numerical value.")


if __name__ == "__main__":
    main()
