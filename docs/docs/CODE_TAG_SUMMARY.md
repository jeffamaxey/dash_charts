# Task Summary

Auto-Generated by `dash_charts`

- .dash_tutorials/08_px-charts.py
    - line   3    TODO: Migrate this sample code to ex_app_px.py

- .github/ISSUE_TEMPLATE/bug_report.md
    - line  12    TODO: Describe the bug -->
    - line  15    TODO: How can someone else replicate the issue -->
    - line  24    TODO: What did you expect? -->
    - line  28    TODO: Add any relevant versions -->
    - line  34    TODO: Add `pip freeze` or other version information that is relevant -->

- .github/ISSUE_TEMPLATE/feature_request.md
    - line  12    TODO: A description of what the problem is. Ex. I'm always frustrated when [...] -->
    - line  16    TODO: A description of what you want to happen -->
    - line  20    TODO: A description of any alternative solutions or features you've considered -->
    - line  24    TODO: Add any other context or screenshots about the feature request here -->

- .github/ISSUE_TEMPLATE/question.md
    - line  12    TODO: What is your question -->

- .github/PULL_REQUEST_TEMPLATE.md
    - line   8    TODO: Specify the issue number(s) associated with the changes here -->
    - line  14    TODO: Describe the purpose and high-level explanation of the changes -->
    - line  18    TODO: Check-off all items with an `x` (`[x]`) -->

- dash_charts/app_px.py
    - line  65 PLANNED: template should be able to be None
    - line  83 PLANNED: below items should be able to be None
    - line 187   FIXME: replace tabs-select with actual keyname (?)

- dash_charts/assets/09_user-styles.css
    - line  18   FIXME: Implement user-customizable styles

- dash_charts/coordinate_chart.py
    - line  19 PLANNED: subplots for multiple years of calendar charts (Subplot title is year)
    - line 335 PLANNED: make this configureable

- dash_charts/datatable.py
    - line   5    TODO: See pattern mathing callbacks for adding buttons (to show modal) to datatables
    - line   8 PLANNED: see conditional formatting: https://dash.plotly.com/datatable/conditional-formatting
    - line  10 PLANNED: These methods may be replaced in a future version of Dash
    - line  87 PLANNED: Maybe move parameters to attr.ib classes?

- dash_charts/modules_upload.py
    - line  76 PLANNED: Revisit. Should filename be a name or the full path?
    - line 371    TODO: Add delete button for each table - need pattern matching callback:
    - line 420   FIXME: Better handle NaN values...

- dash_charts/utils_app.py
    - line 156   FIXME: Need to decide if there is a better approach. Reading this code is confusing...

- dash_charts/utils_app_with_navigation.py
    - line  34    TODO: Try to see if I can resolve the interface differences or if I need make a subclass interface
    - line 154 PLANNED: Make the tabs and chart compact as well when the compact argument is set to True
    - line 361    TODO: Demo how pages could use parameters from pathname

- dash_charts/utils_data.py
    - line  24    TODO: what does this set?
    - line  84 PLANNED: Convert to FP and recursive calls?

- dash_charts/utils_json_cache.py
    - line  14   FIXME: Add versioning to the cache directory with semver logic: https://pypi.org/project/semantic-version/
    - line  32    TODO: Enable versioning of data and automatic deletion when the version changes

- dash_charts/utils_static_toc.py
    - line  43   FIXME: Figure out how to make the header links work (i.e. when clicked in TOC go to the respective header)

- docs/CODE_TAG_SUMMARY.md
    - line   6 PLANNED: template should be able to be None
    - line   7 PLANNED: below items should be able to be None
    - line   8   FIXME: replace tabs-select with actual keyname (?)
    - line  11 PLANNED: subplots for multiple years of calendar charts (Subplot title is year)
    - line  12 PLANNED: make this configureable
    - line  15    TODO: See pattern mathing callbacks for adding buttons (to show modal) to datatables
    - line  16 PLANNED: see conditional formatting: https://dash.plotly.com/datatable/conditional-formatting
    - line  17 PLANNED: These methods may be replaced in a future version of Dash
    - line  18 PLANNED: Maybe move parameters to attr.ib classes?
    - line  21 PLANNED: Revisit. Should filename be a name or the full path?
    - line  22    TODO: Add delete button for each table - need pattern matching callback:
    - line  23   FIXME: Better handle NaN values...
    - line  29   FIXME: Need to decide if there is a better approach. Reading this code is confusing...
    - line  32    TODO: Try to see if I can resolve the interface differences or if I need make a subclass interface
    - line  33 PLANNED: Make the tabs and chart compact as well when the compact argument is set to True
    - line  34    TODO: Demo how pages could use parameters from pathname
    - line  37    TODO: what does this set?
    - line  38 PLANNED: Convert to FP and recursive calls?
    - line  41   FIXME: Add versioning to the cache directory with semver logic: https://pypi.org/project/semantic-version/
    - line  42    TODO: Enable versioning of data and automatic deletion when the version changes
    - line  45   FIXME: Figure out how to make the header links work (i.e. when clicked in TOC go to the respective header)
    - line  48    TODO: Currently not online )
    - line  49   FIXME: Keep updates up to date! -->
    - line  50   FIXME: the change to use Box/_ID needs to be implemented in the examples. This is causing failures in the test cases
    - line  51    TODO: See https://github.com/KyleKing/calcipy/issues/38 -->
    - line  52    TODO: Show an example (screenshots, terminal recording, etc.) -->
    - line  55 PLANNED: Move all of this into a function! (and/or task?)
    - line  56    TODO: pypi package wasn't working. Used local version
    - line  57 PLANNED: needs to be a bit more efficient...
    - line  60    TODO: CLICKABLE POPUPS
    - line  61    TODO: See: https://dash.plot.ly/datatable/interactivity
    - line  62    TODO: Formatting (Typing): https://dash.plot.ly/datatable/typing
    - line  65 PLANNED: Move all of this into a function! (and/or task?) {Duplicate of dodo.py}
    - line  66 PLANNED: Output the test name and other information to the test.log file. Currently only used in `no_log_errors`
    - line  67 PLANNED: move to dash_dev
    - line  68    HACK: get_logs always return None with webdrivers other than Chrome
    - line  69   FIXME: Handle path to the executable. Example with Firefox when the Gecko Drive is installed and on path
    - line  72    TODO: Also set marker size based on value?
    - line  73    TODO: Re-align alignment charts into line and update screenshot
    - line  74    TODO: Maybe green heat map like Github? For one year?
    - line  77   FIXME: AttributeError: 'DataTableDemo' object has no attribute 'ids'
    - line  78    TODO: CLICKABLE POPUPS
    - line  79    TODO: See: https://dash.plot.ly/datatable/interactivity
    - line  80    TODO: Formatting (Typing): https://dash.plot.ly/datatable/typing
    - line  83    TODO: Decide which styles from Bulma should be compared here

- docs/README.md
    - line   5    TODO: Currently not online )
    - line  48   FIXME: Keep updates up to date! -->
    - line  98   FIXME: the change to use Box/_ID needs to be implemented in the examples. This is causing failures in the test cases
    - line 172   FIXME: Document use of the `calcipy_template` instead of manual configuration -->
    - line 423    TODO: See https://github.com/KyleKing/calcipy/issues/38 -->
    - line 438    TODO: Show an example (screenshots, terminal recording, etc.) -->

- dodo.py
    - line  31 PLANNED: Move all of this into a function! (and/or task?)
    - line  53    TODO: pypi package wasn't working. Used local version
    - line  56 PLANNED: needs to be a bit more efficient...

- pyproject.toml
    - line  71   FIXME: In-progress testing of a better dash table

- scripts/jsonl_viewer.py
    - line  79    TODO: CLICKABLE POPUPS
    - line  87    TODO: See: https://dash.plot.ly/datatable/interactivity
    - line  93    TODO: Formatting (Typing): https://dash.plot.ly/datatable/typing

- tests/configuration.py
    - line  15 PLANNED: Move all of this into a function! (and/or task?) {Duplicate of dodo.py}
    - line  29 PLANNED: Output the test name and other information to the test.log file. Currently only used in `no_log_errors`
    - line  30 PLANNED: move to a lazy import within dash_charts?
    - line  47    HACK: get_logs always return None with webdrivers other than Chrome
    - line  48   FIXME: Handle path to the executable. Example with Firefox when the Gecko Drive is installed and on path

- tests/examples/ex_coordinate_chart.py
    - line  17    TODO: Also set marker size based on value?
    - line  18    TODO: Re-align alignment charts into line and update screenshot
    - line  19    TODO: Maybe green heat map like Github? For one year?

- tests/examples/ex_datatable.py
    - line  18   FIXME: AttributeError: 'DataTableDemo' object has no attribute 'ids'
    - line  80    TODO: CLICKABLE POPUPS
    - line  88    TODO: See: https://dash.plot.ly/datatable/interactivity
    - line  94    TODO: Formatting (Typing): https://dash.plot.ly/datatable/typing

- tests/examples/ex_style_bootstrap.py
    - line  92    TODO: Decide which styles from Bulma should be compared here

- tests/test_examples_ex_datatable.py
    - line  14   FIXME: Fix the "ids" error

Found code tags for FIXME (22), TODO (54), PLANNED (30), HACK (2)

<!-- calcipy:skip_tags -->