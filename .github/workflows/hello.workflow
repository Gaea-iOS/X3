workflow "Dangerfile JS Eval" {
  on = "pull_request"
  resolves = "Danger JS"
}
action "Danger JS" {
  uses = "./run-danger/"
  secrets = ["GITHUB_TOKEN"]
}