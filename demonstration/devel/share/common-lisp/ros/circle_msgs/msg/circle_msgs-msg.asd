
(cl:in-package :asdf)

(defsystem "circle_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Circle" :depends-on ("_package_Circle"))
    (:file "_package_Circle" :depends-on ("_package"))
    (:file "CircleArray" :depends-on ("_package_CircleArray"))
    (:file "_package_CircleArray" :depends-on ("_package"))
  ))