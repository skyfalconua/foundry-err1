from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional
import json

@dataclass
class Status:
  name: Optional[str] = None
  category: Optional[str] = None
  color: Optional[str] = None

  @classmethod
  def from_dict(cls, d: Optional[dict]) -> Optional["Status"]:
    if not d:
      return None
    return cls(
      name=d.get("name"),
      category=d.get("category"),
      color=d.get("color"),
    )


@dataclass
class Priority:
  name: Optional[str] = None

  @classmethod
  def from_dict(cls, d: Optional[dict]) -> Optional["Priority"]:
    if not d:
      return None
    return cls(name=d.get("name"))


@dataclass
class Assignee:
  display_name: Optional[str] = None

  @classmethod
  def from_dict(cls, d: Optional[dict]) -> Optional["Assignee"]:
    if not d:
      return None
    return cls(display_name=d.get("display_name"))


@dataclass
class Reporter:
  display_name: Optional[str] = None
  name: Optional[str] = None
  email: Optional[str] = None
  avatar_url: Optional[str] = None

  @classmethod
  def from_dict(cls, d: Optional[dict]) -> Optional["Reporter"]:
    if not d:
      return None
    return cls(
      display_name=d.get("display_name"),
      name=d.get("name"),
      email=d.get("email"),
      avatar_url=d.get("avatar_url"),
    )


@dataclass
class Issue:
  id: Optional[str] = None
  key: Optional[str] = None
  summary: Optional[str] = None
  status: Optional[Status] = None
  priority: Optional[Priority] = None
  assignee: Optional[Assignee] = None
  reporter: Optional[Reporter] = None
  created: Optional[str] = None
  updated: Optional[str] = None

  @classmethod
  def from_dict(cls, d: dict) -> "Issue":
    return cls(
      id=d.get("id"),
      key=d.get("key"),
      summary=d.get("summary"),
      status=Status.from_dict(d.get("status")),
      priority=Priority.from_dict(d.get("priority")),
      assignee=Assignee.from_dict(d.get("assignee")),
      reporter=Reporter.from_dict(d.get("reporter")),
      created=d.get("created"),
      updated=d.get("updated"),
    )


@dataclass
class ProjectIssuesResponse:
  total: Optional[int] = None
  start_at: Optional[int] = None
  max_results: Optional[int] = None
  issues: List[Issue] = ()

  @classmethod
  def from_dict(cls, d: dict) -> "ProjectIssuesResponse":
    issues_data = d.get("issues") or []
    issues = [Issue.from_dict(i) for i in issues_data]
    return cls(
      total=d.get("total"),
      start_at=d.get("start_at"),
      max_results=d.get("max_results"),
      issues=issues,
    )

  @classmethod
  def from_json(cls, s: str) -> "ProjectIssuesResponse":
    return cls.from_dict(json.loads(s))