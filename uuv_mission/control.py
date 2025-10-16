class Control:
    def __init__(self):
        self.kp = 0.15
        self.kd = 0.6
        self.previous_error = 0.0

    def compute_action(self, reference: float, observation: float) -> float:
        error = reference - observation
        derivative_error = (error - self.previous_error)

        action = (self.kp * error +
                  self.kd * derivative_error)

        self.previous_error = error
        return action