;; Auto-generated. Do not edit!


(when (boundp 'line_msgs::Line)
  (if (not (find-package "LINE_MSGS"))
    (make-package "LINE_MSGS"))
  (shadow 'Line (find-package "LINE_MSGS")))
(unless (find-package "LINE_MSGS::LINE")
  (make-package "LINE_MSGS::LINE"))

(in-package "ROS")
;;//! \htmlinclude Line.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass line_msgs::Line
  :super ros::object
  :slots (_header _first _second ))

(defmethod line_msgs::Line
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:first __first) (instance geometry_msgs::Point :init))
    ((:second __second) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _first __first)
   (setq _second __second)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:first
   (&rest __first)
   (if (keywordp (car __first))
       (send* _first __first)
     (progn
       (if __first (setq _first (car __first)))
       _first)))
  (:second
   (&rest __second)
   (if (keywordp (car __second))
       (send* _second __second)
     (progn
       (if __second (setq _second (car __second)))
       _second)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; geometry_msgs/Point _first
    (send _first :serialization-length)
    ;; geometry_msgs/Point _second
    (send _second :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; geometry_msgs/Point _first
       (send _first :serialize s)
     ;; geometry_msgs/Point _second
       (send _second :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; geometry_msgs/Point _first
     (send _first :deserialize buf ptr-) (incf ptr- (send _first :serialization-length))
   ;; geometry_msgs/Point _second
     (send _second :deserialize buf ptr-) (incf ptr- (send _second :serialization-length))
   ;;
   self)
  )

(setf (get line_msgs::Line :md5sum-) "311c7725c0a082e091be9312cb146234")
(setf (get line_msgs::Line :datatype-) "line_msgs/Line")
(setf (get line_msgs::Line :definition-)
      "Header header
geometry_msgs/Point first
geometry_msgs/Point second

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
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :line_msgs/Line "311c7725c0a082e091be9312cb146234")


