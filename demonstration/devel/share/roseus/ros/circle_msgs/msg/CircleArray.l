;; Auto-generated. Do not edit!


(when (boundp 'circle_msgs::CircleArray)
  (if (not (find-package "CIRCLE_MSGS"))
    (make-package "CIRCLE_MSGS"))
  (shadow 'CircleArray (find-package "CIRCLE_MSGS")))
(unless (find-package "CIRCLE_MSGS::CIRCLEARRAY")
  (make-package "CIRCLE_MSGS::CIRCLEARRAY"))

(in-package "ROS")
;;//! \htmlinclude CircleArray.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass circle_msgs::CircleArray
  :super ros::object
  :slots (_header _circles ))

(defmethod circle_msgs::CircleArray
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:circles __circles) ())
    )
   (send-super :init)
   (setq _header __header)
   (setq _circles __circles)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:circles
   (&rest __circles)
   (if (keywordp (car __circles))
       (send* _circles __circles)
     (progn
       (if __circles (setq _circles (car __circles)))
       _circles)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; circle_msgs/Circle[] _circles
    (apply #'+ (send-all _circles :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; circle_msgs/Circle[] _circles
     (write-long (length _circles) s)
     (dolist (elem _circles)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; circle_msgs/Circle[] _circles
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _circles (let (r) (dotimes (i n) (push (instance circle_msgs::Circle :init) r)) r))
     (dolist (elem- _circles)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get circle_msgs::CircleArray :md5sum-) "3f6edfcd6124c497c196e136cc24f493")
(setf (get circle_msgs::CircleArray :datatype-) "circle_msgs/CircleArray")
(setf (get circle_msgs::CircleArray :definition-)
      "Header header
circle_msgs/Circle[] circles
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: circle_msgs/Circle
Header header
geometry_msgs/Point center
float64 radius
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :circle_msgs/CircleArray "3f6edfcd6124c497c196e136cc24f493")


