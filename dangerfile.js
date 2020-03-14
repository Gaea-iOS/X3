import {message, warn, markdown, danger} from "danger"

message("ha ha ha")

danger.git.modified_files.length

// Encourage smaller PRs
var bigPRThreshold = 30;
if (danger.github.pr.additions + danger.github.pr.deletions > bigPRThreshold) {
  warn(':exclamation: Big PR (' + ++errorCount + ')');
  markdown('> (' + errorCount + ') : Pull Request size seems relatively large. If Pull Request contains multiple changes, split each into separate PR will helps faster, easier review.');
}