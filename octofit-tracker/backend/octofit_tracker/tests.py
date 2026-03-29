from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Marvel", description="Marvel Team")
        self.user = User.objects.create(name="Iron Man", email="ironman@marvel.com", team=self.team)

    def test_user_creation(self):
        self.assertEqual(self.user.name, "Iron Man")
        self.assertEqual(self.user.team.name, "Marvel")

class ActivityModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="DC", description="DC Team")
        self.user = User.objects.create(name="Batman", email="batman@dc.com", team=self.team)
        self.activity = Activity.objects.create(user=self.user, activity_type="Running", duration=30, date=timezone.now().date())

    def test_activity_creation(self):
        self.assertEqual(self.activity.user.name, "Batman")
        self.assertEqual(self.activity.activity_type, "Running")

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(name="Pushups", description="Upper body workout")

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "Pushups")

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Avengers", description="Earth's Mightiest Heroes")
        self.leaderboard = Leaderboard.objects.create(team=self.team, score=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.team.name, "Avengers")
        self.assertEqual(self.leaderboard.score, 100)
