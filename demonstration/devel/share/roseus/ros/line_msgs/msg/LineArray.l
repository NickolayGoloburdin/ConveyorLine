;; Auto-generated. Do not edit!


(when (boundp 'line_msgs::LineArray)
  (if (not (find-package "LINE_MSGS"))
    (make-package "LINE_MSGS"))
  (shadow 'LineArray (find-package "LINE_MSGS")))
(unless (find-package "LINE_MSGS::LINEARRAY")
  (make-package "LINE_MSGS::LINEARRAY"))

(in-package "ROS")
;;//! \htmlinclude LineArray.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass line_msgs::LineArray
  :super ros::object
  :slots (_header _lines ))

(defmethod line_msgs::LineArray
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:lines __lines) ())
    )
   (send-super :init)
   (setq _header __header)
   (setq _lines __lines)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:lines
   (&rest __lines)
   (if (keywordp (car __lines))
       (send* _lines __lines)
     (progn
       (if __lines (setq _lines (car __lines)))
       _lines)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; line_msgs/Line[] _lines
    (apply #'+ (send-all _lines :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; line_msgs/Line[] _lines
     (write-long (length _lines) s)
     (dolist (elem _lines)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; line_msgs/Line[] _lines
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _lines (let (r) (dotimes (i n) (push (instance line_msgs::Line :init) r)) r))
     (dolist (elem- _lines)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get line_msgs::LineArray :md5sum-) "67b24130203bbd6fa25f7fed2d1b50b9")
(setf (get line_msgs::LineArray :datatype-) "line_msgs/LineArray")
(setf (get line_msgs::LineArray :definition-)
      "Header header
line_msgs/Line[] lines
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
MSG: line_msgs/Line
Header header
geometry_msgs/Point first
geometry_msgs/Point second

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :line_msgs/LineArray "67b24130203bbd6fa25f7fed2d1b50b9")


