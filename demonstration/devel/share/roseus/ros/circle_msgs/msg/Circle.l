;; Auto-generated. Do not edit!


(when (boundp 'circle_msgs::Circle)
  (if (not (find-package "CIRCLE_MSGS"))
    (make-package "CIRCLE_MSGS"))
  (shadow 'Circle (find-package "CIRCLE_MSGS")))
(unless (find-package "CIRCLE_MSGS::CIRCLE")
  (make-package "CIRCLE_MSGS::CIRCLE"))

(in-package "ROS")
;;//! \htmlinclude Circle.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass circle_msgs::Circle
  :super ros::object
  :slots (_header _center _radius ))

(defmethod circle_msgs::Circle
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:center __center) (instance geometry_msgs::Point :init))
    ((:radius __radius) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _center __center)
   (setq _radius (float __radius))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:center
   (&rest __center)
   (if (keywordp (car __center))
       (send* _center __center)
     (progn
       (if __center (setq _center (car __center)))
       _center)))
  (:radius
   (&optional __radius)
   (if __radius (setq _radius __radius)) _radius)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; geometry_msgs/Point _center
    (send _center :serialization-length)
    ;; float64 _radius
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; geometry_msgs/Point _center
       (send _center :serialize s)
     ;; float64 _radius
       (sys::poke _radius (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; geometry_msgs/Point _center
     (send _center :deserialize buf ptr-) (incf ptr- (send _center :serialization-length))
   ;; float64 _radius
     (setq _radius (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get circle_msgs::Circle :md5sum-) "3ec3f1e4c9ed653d64f4a72bda22768b")
(setf (get circle_msgs::Circle :datatype-) "circle_msgs/Circle")
(setf (get circle_msgs::Circle :definition-)
      "Header header
geometry_msgs/Point center
float64 radius
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



(provide :circle_msgs/Circle "3ec3f1e4c9ed653d64f4a72bda22768b")


