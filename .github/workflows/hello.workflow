workflow "Dangerfile JS Eval" {
  on = "push"
  resolves = "Danger JS"
}
action "Danger JS" {
  uses = "./run-danger/"
  secrets = ["GITHUB_TOKEN"]
}