from rest_framework.throttling import UserRateThrottle


class CreateFeedbackThrottle(UserRateThrottle):
    scope = 'createFeedback'
