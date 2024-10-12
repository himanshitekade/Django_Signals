# Assignment Submission

## Topic: Django Signals

### Question 1: By default are Django signals executed synchronously or asynchronously?
Explanation: Django signals are executed synchronously. This means that the signal receiver function is executed immediately after the signal is sent, and the code execution will wait until the receiver has finished executing before continuing.

Code: See application/signals.py for code.

### Question 2: Do Django signals run in the same thread as the caller?
Explanation: Yes, Django signals run in the same thread as the caller by default. When a signal is sent, the code that handles the signal (receiver) is executed within the same thread, meaning no new thread is created for handling the signal.

Code: See application/signals.py for code.

### Question 3: Do Django signals run in the same database transaction as the caller?
Explanation: Yes, by default, Django signals run in the same database transaction as the caller. If an exception is raised during the signal processing, it will roll back the entire database transaction, including the changes made by the caller.

Code: See application/signals.py for code.

---

## Topic: Custom Classes in Python

Task: Implement a 'Rectangle' class that allows iteration over the instance to return its length and width.
Code: See custom_classes/rectangle.py for code.

---

## Resume
Link to my resume:(https://drive.google.com/file/d/1hlhtwUH745-y1y-MV7oqyvOBY4PCTTLd/view?usp=sharing)
