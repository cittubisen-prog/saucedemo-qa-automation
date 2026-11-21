# GitHub Setup & Submission Guide

This guide walks you through publishing this project to a public GitHub repository, filing the 3 required Bug Issues, and organizing them on a GitHub Project Kanban board.

---

## Step 1: Create a New Public Repository on GitHub
1. Log into your GitHub account at [https://github.com/](https://github.com/).
2. Click the **+** (plus icon) at the top-right corner and select **New repository**.
3. Repository name: `saucedemo-qa-automation`
4. Set visibility to **Public** (required by recruiter).
5. Leave "Add a README file" **unchecked** (we already have a complete README).
6. Click **Create repository**.

---

## Step 2: Push the Local Project to Your GitHub Repository
Open PowerShell or Command Prompt in the project folder:
```powershell
cd "c:\Users\Ranvijay\Downloads\saucedemo-qa-automation"

# Initialize git if not already done
git init
git add .
git commit -m "feat: complete QA automation suite, test plan, bug reports, and CI pipeline"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/saucedemo-qa-automation.git
git push -u origin main
```
*(If git is not installed on your command line, you can simply upload the project folder directly via the GitHub web UI using the "Upload files" button on your repo page!)*

---

## Step 3: Create the 3 Required Bug Issues on GitHub
In your GitHub repo, go to the **Issues** tab and click **New issue** for each of the 3 bugs:

### Issue 1:
* **Title:** `[BUG-01] Product catalog displays broken dog placeholder image for all products (problem_user)`
* **Labels:** `bug`, `high-priority`
* **Body:**
```markdown
### Summary
When authenticated as `problem_user`, all product images on `/inventory.html` fail to display and default to the generic dog 404 placeholder (`sl-404.168b1cce.jpg`).

### Steps to Reproduce
1. Navigate to https://www.saucedemo.com/
2. Log in with `problem_user` / `secret_sauce`
3. Inspect catalog product cards on `/inventory.html`

### Expected Result
Each product displays its correct, unique product image.

### Actual Result
All 6 products display identical broken dog placeholder images.

### Screenshot
Attached in `screenshots/BUG-01_problem_user_broken_images.png`.
```

### Issue 2:
* **Title:** `[BUG-02] Checkout Last Name field refuses input and blocks order completion (problem_user)`
* **Labels:** `bug`, `critical`
* **Body:**
```markdown
### Summary
On `/checkout-step-one.html`, the Last Name input field (`#last-name`) does not retain text or locks, triggering "Error: Last Name is required" and completely blocking order checkout.

### Steps to Reproduce
1. Log in with `problem_user` / `secret_sauce`
2. Add any item to cart and go to checkout
3. Fill First Name: John, Last Name: Doe, Zip: 12345
4. Click Continue

### Expected Result
User transitions to step two overview.

### Actual Result
Error displayed: "Error: Last Name is required". Checkout is permanently blocked.

### Screenshot
Attached in `screenshots/BUG-02_problem_user_checkout_lastname_broken.png`.
```

### Issue 3:
* **Title:** `[BUG-03] Suspended user account blocked at login with no recovery option (locked_out_user)`
* **Labels:** `bug`, `medium-priority`
* **Body:**
```markdown
### Summary
Logging in with `locked_out_user` displays "Epic sadface: Sorry, this user has been locked out." with no recovery, support, or reset options.

### Steps to Reproduce
1. Navigate to https://www.saucedemo.com/
2. Log in with `locked_out_user` / `secret_sauce`

### Expected Result
Helpful guidance or support contact link for account unlock.

### Actual Result
Generic error banner with no actionable recovery path.

### Screenshot
Attached in `screenshots/BUG-03_locked_out_user_error.png`.
```

---

## Step 4: Create the GitHub Project Kanban Board
1. In your GitHub repository, click the **Projects** tab.
2. Click **New project** (choose the **Board** template).
3. Project Name: `SauceDemo QA Bug Tracking Board`
4. Ensure three columns are present:
   * **To Do**
   * **In Progress**
   * **Done**
5. Click **+ Add item** or drag the 3 created issues into the board:
   * Move **BUG-01** to **To Do**
   * Move **BUG-02** to **In Progress**
   * Move **BUG-03** to **To Do**
6. Make sure the Project visibility is set to **Public** so the recruiters can view it!

---

## Step 5: Final Submission Link
Submit your public repo URL here:
👉 **[https://task.zeeshanali.org/submit/28649a4f-1ce9-4118-8c02-60c06fd162f4](https://task.zeeshanali.org/submit/28649a4f-1ce9-4118-8c02-60c06fd162f4)**
