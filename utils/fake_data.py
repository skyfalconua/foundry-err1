# Define a constant list of issues based on data from jira_get_project_issues.json

from .models import Issue, Status, Priority, Assignee, Reporter


ISSUES = [
    Issue(
        id="10013",
        key="KAN-4",
        summary="Epic 8888",
        status=Status(name="To Do", category="To Do", color="blue-gray"),
        priority=Priority(name="Medium"),
        assignee=Assignee(display_name="Unassigned"),
        reporter=Reporter(
            display_name="John Smith",
            name="John Smith",
            email="john.smith@example.com",
            avatar_url=(
                "https://secure.gravatar.com/avatar/"
                "5c7e21efd0bbd8e352b21bfc67dea735?d=https%3A%2F%2F"
                "avatar-management--avatars.us-west-2.prod.public."
                "atl-paas.net%2Finitials%2FAS-1.png"
            ),
        ),
        created="2025-12-09T22:43:32.744+0200",
        updated="2025-12-09T22:43:33.449+0200",
    ),
    Issue(
        id="10012",
        key="KAN-3",
        summary="Subtask 2.1",
        status=Status(name="To Do", category="To Do", color="blue-gray"),
        priority=None,
        assignee=Assignee(display_name="Unassigned"),
        reporter=Reporter(
            display_name="Sarah Johnson",
            name="Sarah Johnson",
            email="sarah.j@example.com",
            avatar_url=(
                "https://secure.gravatar.com/avatar/"
                "5c7e21efd0bbd8e352b21bfc67dea735?d=https%3A%2F%2F"
                "avatar-management--avatars.us-west-2.prod.public."
                "atl-paas.net%2Finitials%2FAS-1.png"
            ),
        ),
        created="2025-12-09T19:33:40.580+0200",
        updated="2025-12-09T19:33:41.059+0200",
    ),
    Issue(
        id="10011",
        key="KAN-2",
        summary="Task 2def",
        status=Status(
            name="In Progress", category="In Progress", color="yellow"
        ),
        priority=None,
        assignee=Assignee(display_name="Unassigned"),
        reporter=Reporter(
            display_name="Michael Brown",
            name="Michael Brown",
            email="mbrown@example.com",
            avatar_url=(
                "https://secure.gravatar.com/avatar/"
                "5c7e21efd0bbd8e352b21bfc67dea735?d=https%3A%2F%2F"
                "avatar-management--avatars.us-west-2.prod.public."
                "atl-paas.net%2Finitials%2FAS-1.png"
            ),
        ),
        created="2025-12-09T19:33:39.720+0200",
        updated="2025-12-09T22:44:14.590+0200",
    ),
    Issue(
        id="10010",
        key="KAN-1",
        summary="Task 1abc",
        status=Status(name="To Do", category="To Do", color="blue-gray"),
        priority=None,
        assignee=Assignee(display_name="Unassigned"),
        reporter=Reporter(
            display_name="Emily Davis",
            name="Emily Davis",
            email="emily.davis@example.com",
            avatar_url=(
                "https://secure.gravatar.com/avatar/"
                "5c7e21efd0bbd8e352b21bfc67dea735?d=https%3A%2F%2F"
                "avatar-management--avatars.us-west-2.prod.public."
                "atl-paas.net%2Finitials%2FAS-1.png"
            ),
        ),
        created="2025-12-09T19:33:39.399+0200",
        updated="2025-12-09T22:44:06.617+0200",
    ),
    Issue(
        id="10009",
        key="KAN-5",
        summary="Bug fix for login",
        status=Status(name="To Do", category="To Do", color="blue-gray"),
        priority=Priority(name="High"),
        assignee=Assignee(display_name="Unassigned"),
        reporter=Reporter(
            display_name="David Wilson",
            name="David Wilson",
            email="dwilson@example.com",
            avatar_url=(
                "https://secure.gravatar.com/avatar/"
                "5c7e21efd0bbd8e352b21bfc67dea735?d=https%3A%2F%2F"
                "avatar-management--avatars.us-west-2.prod.public."
                "atl-paas.net%2Finitials%2FAS-1.png"
            ),
        ),
        created="2025-12-08T14:20:15.123+0200",
        updated="2025-12-08T14:20:15.456+0200",
    ),
    Issue(
        id="10008",
        key="KAN-6",
        summary="Update documentation",
        status=Status(
            name="In Progress", category="In Progress", color="yellow"
        ),
        priority=Priority(name="Low"),
        assignee=Assignee(display_name="Unassigned"),
        reporter=Reporter(
            display_name="Jessica Martinez",
            name="Jessica Martinez",
            email="jmartinez@example.com",
            avatar_url=(
                "https://secure.gravatar.com/avatar/"
                "5c7e21efd0bbd8e352b21bfc67dea735?d=https%3A%2F%2F"
                "avatar-management--avatars.us-west-2.prod.public."
                "atl-paas.net%2Finitials%2FAS-1.png"
            ),
        ),
        created="2025-12-07T09:15:30.789+0200",
        updated="2025-12-09T16:22:45.123+0200",
    ),
    Issue(
        id="10007",
        key="KAN-7",
        summary="Performance optimization",
        status=Status(name="Done", category="Done", color="green"),
        priority=Priority(name="Medium"),
        assignee=Assignee(display_name="Unassigned"),
        reporter=Reporter(
            display_name="Robert Taylor",
            name="Robert Taylor",
            email="rtaylor@example.com",
            avatar_url=(
                "https://secure.gravatar.com/avatar/"
                "5c7e21efd0bbd8e352b21bfc67dea735?d=https%3A%2F%2F"
                "avatar-management--avatars.us-west-2.prod.public."
                "atl-paas.net%2Finitials%2FAS-1.png"
            ),
        ),
        created="2025-12-05T11:30:00.000+0200",
        updated="2025-12-09T10:15:20.555+0200",
    ),
    Issue(
        id="10006",
        key="KAN-8",
        summary="Add new feature X",
        status=Status(name="To Do", category="To Do", color="blue-gray"),
        priority=Priority(name="High"),
        assignee=Assignee(display_name="Unassigned"),
        reporter=Reporter(
            display_name="Linda Anderson",
            name="Linda Anderson",
            email="linda.a@example.com",
            avatar_url=(
                "https://secure.gravatar.com/avatar/"
                "5c7e21efd0bbd8e352b21bfc67dea735?d=https%3A%2F%2F"
                "avatar-management--avatars.us-west-2.prod.public."
                "atl-paas.net%2Finitials%2FAS-1.png"
            ),
        ),
        created="2025-12-04T08:00:00.000+0200",
        updated="2025-12-04T08:00:01.123+0200",
    ),
    Issue(
        id="10005",
        key="KAN-9",
        summary="Code review changes",
        status=Status(
            name="In Progress", category="In Progress", color="yellow"
        ),
        priority=Priority(name="Medium"),
        assignee=Assignee(display_name="Unassigned"),
        reporter=Reporter(
            display_name="James Thomas",
            name="James Thomas",
            email="jthomas@example.com",
            avatar_url=(
                "https://secure.gravatar.com/avatar/"
                "5c7e21efd0bbd8e352b21bfc67dea735?d=https%3A%2F%2F"
                "avatar-management--avatars.us-west-2.prod.public."
                "atl-paas.net%2Finitials%2FAS-1.png"
            ),
        ),
        created="2025-12-03T13:45:22.333+0200",
        updated="2025-12-09T12:30:10.222+0200",
    ),
    Issue(
        id="10004",
        key="KAN-10",
        summary="Setup CI/CD pipeline",
        status=Status(name="Done", category="Done", color="green"),
        priority=Priority(name="High"),
        assignee=Assignee(display_name="Unassigned"),
        reporter=Reporter(
            display_name="Patricia White",
            name="Patricia White",
            email="pwhite@example.com",
            avatar_url=(
                "https://secure.gravatar.com/avatar/"
                "5c7e21efd0bbd8e352b21bfc67dea735?d=https%3A%2F%2F"
                "avatar-management--avatars.us-west-2.prod.public."
                "atl-paas.net%2Finitials%2FAS-1.png"
            ),
        ),
        created="2025-12-01T10:00:00.000+0200",
        updated="2025-12-06T18:45:30.999+0200",
    ),
]
