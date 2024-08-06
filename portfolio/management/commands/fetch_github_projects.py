# portfolio/management/commands/fetch_github_projects.py

import requests
from django.core.management.base import BaseCommand
from portfolio.models import Project

class Command(BaseCommand):
    help = 'Fetch projects from GitHub'

    def handle(self, *args, **kwargs):
        # Url to retrieve my github repo. 
        url = 'https://api.github.com/users/asandilenkala/repos'
        response = requests.get(url)

        if response.status_code == 200:
            repos = response.json()

            for repo in repos:
                project, created = Project.objects.update_or_create(
                    github_url=repo['html_url'],
                    defaults={
                        'title': repo['name'],
                        'description': repo['description'] or ''
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created project: {repo["name"]}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated project: {repo["name"]}'))
        else:
            self.stderr.write(self.style.ERROR('Failed to fetch projects from GitHub'))
