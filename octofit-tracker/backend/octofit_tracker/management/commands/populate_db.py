
from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data for users
        users = [
            {"email": "alice@example.com", "name": "Alice", "team": "Red Rockets", "age": 16},
            {"email": "bob@example.com", "name": "Bob", "team": "Blue Blazers", "age": 17},
            {"email": "carol@example.com", "name": "Carol", "team": "Red Rockets", "age": 15}
        ]
        db.users.delete_many({})
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Red Rockets", "members": ["alice@example.com", "carol@example.com"]},
            {"name": "Blue Blazers", "members": ["bob@example.com"]}
        ]
        db.teams.delete_many({})
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"activity_id": 1, "user": "alice@example.com", "type": "run", "duration": 30, "distance": 5},
            {"activity_id": 2, "user": "bob@example.com", "type": "bike", "duration": 45, "distance": 15},
            {"activity_id": 3, "user": "carol@example.com", "type": "swim", "duration": 20, "distance": 1}
        ]
        db.activity.delete_many({})
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"leaderboard_id": 1, "team": "Red Rockets", "points": 120},
            {"leaderboard_id": 2, "team": "Blue Blazers", "points": 90}
        ]
        db.leaderboard.delete_many({})
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"workout_id": 1, "user": "alice@example.com", "workout": "5k run", "date": "2025-05-20"},
            {"workout_id": 2, "user": "bob@example.com", "workout": "15k bike", "date": "2025-05-21"},
            {"workout_id": 3, "user": "carol@example.com", "workout": "1k swim", "date": "2025-05-22"}
        ]
        db.workouts.delete_many({})
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully in octofit_db.'))
