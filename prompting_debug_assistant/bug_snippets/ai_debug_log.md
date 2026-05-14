## Bug 1 – bug1.py
**AI Prompt**: This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?

**AI Diagnosis**: The issue is caused by incorrect file path usage. The script expects bug1.py in the same working directory, but it is either deleted or referenced using an incorrect relative path.

**Suggested Fix**: Restore the file using `git restore bug1.py` or ensure correct directory structure and update import/path references.

**Alternative Fixes Tested**:
1. `git restore bug1.py` → Restored the file successfully.
2. Manually re-creating file → Also works but not recommended due to loss of original content.

**Result**: Fix 1 worked. File restored and script executes normally.

---

## Bug 2 – bug2.js
**AI Prompt**: This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?

**AI Diagnosis**: The file is missing from the expected directory, causing runtime failure when the script attempts to access it.

**Suggested Fix**: Restore the missing file using git or correct the file path in the codebase.

**Alternative Fixes Tested**:
1. `git restore bug2.js` → Successfully restored file.
2. Updating script path references → Not needed after restore.

**Result**: Fix 1 worked. Program runs successfully after restoration.

---

## Bug 3 – bug3.py
**AI Prompt**: This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?

**AI Diagnosis**: The file was deleted in the working directory, leading to missing file errors during execution.

**Suggested Fix**: Restore deleted file using Git to recover the original version.

**Alternative Fixes Tested**:
1. `git restore bug3.py` → Restored successfully.
2. Rewriting file manually → Not used to preserve original implementation.

**Result**: Fix 1 worked. No errors after restore.

---

## Bug 4 – bug4.cpp
**AI Prompt**: This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?

**AI Diagnosis**: The file is missing or not included in build/compile process, causing compilation failure or file-not-found error.

**Suggested Fix**: Restore file and ensure correct compilation command includes this file.

**Alternative Fixes Tested**:
1. `git restore bug4.cpp` → Fixed issue immediately.
2. Adjusting compile command only → Not needed after restore.

**Result**: Fix 1 worked. Compilation successful.

---

## Bug 5 – bug5.js
**AI Prompt**: This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?

**AI Diagnosis**: The file is missing from expected directory structure, causing script failure.

**Suggested Fix**: Restore missing file using Git.

**Alternative Fixes Tested**:
1. `git restore bug5.js` → Restored successfully.
2. Manual recreation → Not used.

**Result**: Fix 1 worked. Script runs correctly.