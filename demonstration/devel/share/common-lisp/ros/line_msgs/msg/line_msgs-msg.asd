
(cl:in-package :asdf)

(defsystem "line_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Line" :depends-on ("_package_Line"))
    (:file "_package_Line" :depends-on ("_package"))
    (:file "LineArray" :depends-on ("_package_LineArray"))
    (:file "_package_LineArray" :depends-on ("_package"))
  ))