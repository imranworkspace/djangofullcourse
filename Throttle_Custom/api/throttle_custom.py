from rest_framework.throttling import UserRateThrottle

class ImranUserThrottle(UserRateThrottle):
    scope='imran' # just pass user defind name and my created user name is 'test' so when I will hit after logged in in minute I can only hit 3 times not more than that