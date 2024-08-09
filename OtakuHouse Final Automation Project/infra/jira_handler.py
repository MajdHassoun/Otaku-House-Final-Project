from jira import JIRA

from infra.config_provider import ConfigProvider


class JiraHandler:
    def __init__(self):
        self.config = ConfigProvider().load_config_json()
        self.secret_json = ConfigProvider.load_secret_json()
        self._jira_url = self.config["jira_url"]
        self._auth_jira = JIRA(
            basic_auth=(self.config["jira_email"], self.secret_json["jira_api_token"]),
            options={'server': self._jira_url}
        )

    def create_issue(self, project_key, summary, description, issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }

        return self._auth_jira.create_issue(fields=issue_dict)
