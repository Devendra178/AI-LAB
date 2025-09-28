(defun move (n source target auxiliary)
  (if (= n 1)
      (format t "Move disk 1 from ~A → ~A~%" source target)
      (progn
        (move (- n 1) source auxiliary target)
        (format t "Move disk ~A from ~A → ~A~%" n source target)
        (move (- n 1) auxiliary target source))))

(defun tower-of-hanoi ()
  (format t "🏰 Tower of Hanoi in Lisp 🧠~%")
  (format t "Enter number of disks (minimum 3): ")
  (let ((n (read)))
    (if (< n 3)
        (format t "Please enter at least 3 disks.~%")
        (progn
          (format t "~%Number of disks: ~A~%" n)
          (format t "Minimum moves required: ~A~%~%" (- (expt 2 n) 1))
          (move n 'A 'C 'B)
          (format t "~%🎯 Puzzle solved!~%")))))

;; Automatically start when file is loaded
(tower-of-hanoi)
