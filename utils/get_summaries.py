from utils.models import Issue


def get_summaries_list(tasks: list) -> str:

  # handle input that might be the whole response dict
  if isinstance(tasks, dict) and "issues" in tasks:
    tasks = tasks["issues"] or []

  summaries = []
  for item in tasks:
    if isinstance(item, Issue):
      issue = item
    elif isinstance(item, dict):
      issue = Issue.from_dict(item)
    else:
      # skip unknown item types
      continue

    title = issue.key or issue.id or ""
    summary = issue.summary or ""
    summaries.append(f"{title} - {summary}")

  return "\n".join(summaries)
