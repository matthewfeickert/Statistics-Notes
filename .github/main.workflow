workflow "Test Python 3.6.8" {
  on = "push"
  resolves = ["Python 3.6.8 Debian"]
}

action "Python 3.6.8 Debian" {
  uses = "docker://python:3.6.8"
  runs = "./.github/actions/tests/entrypoint.sh"
}


workflow "Test Python 3.7.3" {
  on = "push"
  resolves = ["Python 3.7.3 Debian"]
}

action "Python 3.7.3 Debian" {
  uses = "docker://python:3.7.3"
  runs = "./.github/actions/tests/entrypoint.sh"
}
