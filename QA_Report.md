## 🧾 QA_Report.md

---

### 🐞 Found Bugs & Issues

| # | Title                                      | Description                                         | Steps to Reproduce                                        | Expected Result                                | Actual Result                      |
|---|--------------------------------------------|-----------------------------------------------------|-----------------------------------------------------------|------------------------------------------------|------------------------------------|
| 1 | 🔁 Top 5 / Top 10 Toggle Not Working        | Toggling campaign views has no effect               | Go to any report → Click Top 5 / Top 10 buttons           | Chart and data should update                   | No change in chart or data         |
| 2 | 📅 "Last Month" in Date Filter Shows No Data| Date filter does not return any results             | Open date filter → Select “Last Month”                    | Should show last month's data                  | Displays “No data found”           |
| 3 | 🧩 Custom Date Filter Not Working           | Custom date selection fails                         | Select "Custom" → Pick any valid range                    | Data appears based on selected dates           | Still shows “No data found”        |
| 4 | 🧮 "A Year Ago" Missing in Compare Filter   | Missing comparative filter option                   | Click Compare dropdown                                    | "A Year Ago" should be listed                  | Option is missing                  |
| 5 | 💾 Reset Button Becomes Non-Functional      | Reset does not work after saving a report           | Create report → Make changes → Save → Click Reset         | Report resets to original state                | No change occurs                   |

---

### ✅ Regression Checklist

| Area           | Test Description                                 | Pass/Fail | Notes                                |
|----------------|--------------------------------------------------|-----------|--------------------------------------|
| Login          | QA credentials successfully log in               | ✅        |                                      |
| Dashboard      | Metric or chart appears on dashboard             | ✅        | "Spend", "Top", or "Advantage" seen  |
| Filters        | Date filter: "Last Month"                        | ❌        | Shows "No data found"                |
| Filters        | Custom date range (e.g., July 1 – July 30)       | ❌        | No data shown                        |
| Filters        | Compare filter: "A Year Ago"                     | ❌        | Option missing                       |
| Reports        | Reset button restores last saved version         | ❌        | Button does nothing                  |
| Boards         | Toggle Top 5 / Top 10 / Custom                   | ❌        | No change in data/chart              |
| Navigation     | Click saved report in sidebar                    | ✅        | Opens with correct filters           |
| Table ↔ Chart  | Chart and table values align                     | ✅        | Consistency confirmed                |
| Channel Filter | Filter (e.g., WhatsApp) updates table            | ✅        | Filtered data loads correctly        |

---

### 💡 Suggestions for Dashboard Usability & Test Coverage

#### 🎯 Usability Improvements
- **Graceful handling for empty states**: Display friendly message when no data is available after filter selection.
- **Improve toggle feedback**: Highlight the selected Top 5/10/Custom state clearly to indicate the active view.
- **Reset Button Confirmation**: Add a small tooltip or animation when reset occurs to confirm the action.

#### 🧪 Test Coverage Enhancements
- Add tests for:
  - ❌ Invalid or expired login sessions
  - ⏳ Filter performance under slow network
  - 📦 Export/download buttons for reports or tables
- Introduce **visual regression testing** (e.g., with Percy or Applitools) to ensure chart UI reflects changes.
- Add keyboard accessibility checks for dashboard elements.
- Include mobile responsiveness checks (e.g., viewport scaling, hover effects fallback).