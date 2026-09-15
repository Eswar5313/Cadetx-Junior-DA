# Contributing

1. Pick a task from `excel/HWI_Project_Control_Book.xlsx › 05_Task_Catalogue` or a GitHub Issue; assign yourself.
2. Branch from `main`: `git checkout -b week-04/abc-classification`.
3. Notebook naming `NN_task_name.ipynb`; import shared logic from `src/hwi`, don't copy-paste.
4. End every notebook with a **Results Summary** markdown cell (3–5 bullets: finding, number, so-what).
5. Export charts to `sprints/week-XX/outputs/` as PNG (1600×900, dpi 150).
6. Run `nbstripout` and `ruff check src/` before committing.
7. Commit message: `week-04: add ABC classification notebook (#23)`.
8. Open a PR using the template; one teammate reviews within 24 h.
9. Scrum Master updates `04_Sprint_Tracker`, writes `SPRINT_NOTES.md`, tags `vWeek-04`, submits link to CadetX portal on Friday.
