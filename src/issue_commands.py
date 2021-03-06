#!/usr/bin/env python
import roslib
roslib.load_manifest('tum_ardrone')
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Point
import actionlib
from std_srvs.srv import Empty
from tum_ardrone.msg import *
def issue_commands(data):
    rospy.loginfo("waypoints: Got the target!!!")
    client = actionlib.SimpleActionClient('drone_autopilot/moveBy',MoveAction)
    client.wait_for_server()
    goal=MoveGoal()
    goal.x=data.x
    goal.y=data.y
    goal.z=data.z
    rospy.loginfo("waypoints: Sending goal")
    client.send_goal(goal)
    state=client.wait_for_result(rospy.Duration.from_sec(45.0))
    print state
    if state==True:
	count=0
	rospy.loginfo("issue_commands-: Reached the target, Toggle cam")
	rospy.wait_for_service('ardrone/togglecam')
        toggle_cam=rospy.ServiceProxy('ardrone/togglecam',Empty)
	
          #toggle_cam.wait_for_server()
        try:

	          state=toggle_cam()
		  print state
                  rospy.loginfo("color_tracker-: toogled the cam")
        except rospy.ServiceException as exc:
		rospy.loginfo("Service didn't process request"+str(exc))
    else:
	if count<3:

		count=count+1
		rospy.loginfo("issue_commands-: Didn't reach the target")
		rospy.loginfo("issue_commands-: Trying"+str(count))
		issue_commands(goal)
        else:
		rospy.loginfo("can't reach")
    #rospy.set_param('check',state)
    
   

  
	   
	   	
	  

if __name__ == '__main__':
    rospy.init_node('waypoints',anonymous=True)
    target=rospy.get_param("target","target")
    rospy.Subscriber(target,Point,issue_commands)
    rospy.spin()
    
    
    
        
