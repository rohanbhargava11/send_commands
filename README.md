commands_actionlib.py -> It does a service call to drone_autopilot/autoInit and prints the state of the call.

issue_commands.py -> It does a service call to drone_autopilot/moveBy. It listens to topic /target and sends the target to parrot. It waits dor 45 seconds before returning false for the service call.


landing_pad.py -> It published values over target topic. It is used for debugging.


