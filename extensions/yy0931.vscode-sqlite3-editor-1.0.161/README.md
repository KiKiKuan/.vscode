# SQLite3 Editor

[![Github Stars](https://img.shields.io/github/stars/yy0931/sqlite3-editor?style=social)](https://github.com/yy0931/sqlite3-editor)
[![GitHub issues](https://img.shields.io/github/issues/yy0931/sqlite3-editor)](https://github.com/yy0931/sqlite3-editor/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/yy0931/sqlite3-editor)](https://github.com/yy0931/sqlite3-editor/issues)

This extension allows you to edit [SQLite 3](https://www.sqlite.org/index.html) files without having to write SQL queries.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/demo.gif)

<!-- The database in the screenshot is the sample database in MySQL ported to SQLite, downloaded from https://github.com/fracpete/employees-db-sqlite. -->

## Feature Overview
This extension can be used to 📊 view and edit database contents, ⚙ view and edit table schema, and ▶️ execute SQL queries.

<img src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/three-parts-v2.png" width="650px">

Most of these features are not present in other VSCode extensions for SQLite, such as [alexcvzz/SQLite](https://github.com/AlexCovizzi/vscode-sqlite/) and [SQLite Viewer](https://github.com/qwtel/sqlite-viewer-vscode).

Here are some videos of the main features:

## 📊 Viewing Database Contents

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/view-database-contents.mp4" controls></video>

This extension uses [**scrolling**](https://en.wikipedia.org/wiki/Scrollbar) for browsing records, which should be more intuitive than [pagination](https://mui.com/material-ui/react-pagination/). At the same time, **only the data that is currently visible on the screen is retrieved** from the database, so it loads fast even on large databases. In addition, the data is **automatically reloaded** when the table is modified by another process. It also comes with conditional formatting, image BLOBs preview, foreign key hover, etc.

## 📊 Editing Database Contents

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/edit-database-contents.mp4" controls></video>

In addition to simple [UPDATE](https://www.sqlite.org/lang_update.html)s and [INSERT](https://www.sqlite.org/lang_insert.html)s shown in the recording above, you can bulk-set a value to a selection, delete multiple rows by dragging over row numbers, set a value to a cell in a foreign key column using a dropdown, edit a table via a view, etc.

## ⚙ Editing Table Schema

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/edit-table-schema.mp4" controls></video>

You can edit table schemas as shown in the video. In addition to [tables](https://www.sqlite.org/lang_createtable.html), you can also edit a [view](https://www.sqlite.org/lang_createview.html)'s name and definition.

## ▶️ Executing SQL Queries
![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/query-editor.gif)

You can run arbitrary queries in the query editor. The editor supports **context-aware auto-completion, syntax highlighting, hover documentation, signature help, and syntax validation**.


# Feature Documentation
The arrangement of the features listed in this section does not reflect any particular order. Feel free to explore each feature as per your interest.

Table of Contents
- [Creating a Database](#creating-a-database)
- [Editing Table Schema - Checking Table Schema](#editing-table-schema---checking-table-schema)
- [Editing Table Schema - Changing Column Definition](#editing-table-schema---changing-column-definition)
- [Editing Table Schema - Changing Column Order](#editing-table-schema---changing-column-order)
- [Editing Table Schema - Creating a Table](#editing-table-schema---creating-a-table)
- [Editing Table Schema - Creating an Index](#editing-table-schema---creating-an-index)
- [Editing Table Schema - Dropping a Table](#editing-table-schema---dropping-a-table)
- [Editing Table Schema - Renaming a Table](#editing-table-schema---renaming-a-table)
- [File Associations](#file-associations)
- [Importing and Exporting Data in CSV, JSON, or SQL](#importing-and-exporting-data-in-csv-json-or-sql)
- [In-Memory Databases](#in-memory-databases)
- [Opening the Database in a Command Line Shell](#opening-the-database-in-a-command-line-shell)
- [Query Editor - Overview](#query-editor---overview)
- [Query Editor - Document Formatting](#query-editor---document-formatting)
- [Query Editor - Executing a Part of Common Table Expression (CTE)](#query-editor---executing-a-part-of-common-table-expression-cte)
- [Query Editor - Syntax Validation](#query-editor---syntax-validation)
- [Table View - Auto Reloading](#table-view---auto-reloading)
- [Table View - Conditional Formatting](#table-view---conditional-formatting)
- [Table View - Displaying and Jumping to the Definition of Foreign Keys](#table-view---displaying-and-jumping-to-the-definition-of-foreign-keys)
- [Table View - Editing GENERATED Columns](#table-view---editing-generated-columns)
- [Table View - Entity-Relationship Diagram](#table-view---entity-relationship-diagram)
- [Table View - Filtering and Sorting Data](#table-view---filtering-and-sorting-data)
- [Table View - Git-Diff Support](#table-view---git-diff-support)
- [Table View - Group by Column](#table-view---group-by-column)
- [Table View - Inserting Data from CSV](#table-view---inserting-data-from-csv)
- [Table View - Jumping to a Table or a Row](#table-view---jumping-to-a-table-or-a-row)
- [Table View - Multi-Selection](#table-view---multi-selection)
- [Table View - Resizing Columns](#table-view---resizing-columns)
- [Table View - Resizing Rows](#table-view---resizing-rows)
- [Table View - Selecting a Table](#table-view---selecting-a-table)
- [Table View - Tabs](#table-view---tabs)
- [Using Non-Standard SQLite - Run-Time Loadable SQLite Extensions](#using-non-standard-sqlite---run-time-loadable-sqlite-extensions)
- [Using Non-Standard SQLite - User Compiled SQLite](#using-non-standard-sqlite---user-compiled-sqlite)

## Creating a Database
To create [a database file](https://www.sqlite.org/onefile.html), simply create a file with a supported file extension, such as .db, .sqlite, or .sqlite3. The extension will automatically initialize the file as a database if it is empty and has one of the supported extensions.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/new-database.gif)


## Editing Table Schema - Checking Table Schema
To view the schema of the active table, click on the "Schema" button located at the top of the editor. This will open a panel displaying the table schema, [indexes](https://www.sqlite.org/lang_createindex.html), and [triggers](https://www.sqlite.org/lang_createtrigger.html). This feature supports both [tables](https://www.sqlite.org/lang_createtable.html) and [views](https://www.sqlite.org/lang_createview.html).

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/table-schema-v2.png)

The "Index" section displays an array of blue and gray boxes for each index. They represent which column the index applies to, with numbers indicating the order. For example, if you have `CREATE TABLE table1(a, b, c); CREATE INDEX index1 ON table1 (c, a)`, then the coloring of the boxes would be `blue, gray, blue`, and the numbers would be `2, -, 1`.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/index-visualization.png)

When you hover your cursor over an index, it highlights the corresponding columns. Conversely, when you hover your cursor over the dotted text in the columns, it highlights the associated indexes in the "Schema" pane.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/index-hover.png)


## Editing Table Schema - Changing Column Definition
You can change the [type affinity](https://www.sqlite.org/datatype3.html#type_affinity) and the [constraints](https://www.sqlite.org/syntax/column-constraint.html) of a column with this feature.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/change-type.png)


## Editing Table Schema - Changing Column Order
You can change the order of table columns by dragging the table header.

We've tested this feature extensively, but we won't take any responsibility for possible data loss. Please ensure you check the generated query and/or create a backup before using this feature, especially if you're working with a critical database.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/reorder-columns.gif)


## Editing Table Schema - Creating a Table
You can access this feature by clicking on the statement at the bottom of the editor, then selecting "CREATE TABLE".

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/editors.png)

The tables that can be created by this feature are limited to simpler ones. To create a complex table, such as ones with [GENERATED columns](https://www.sqlite.org/gencol.html) or [COLLATE clauses](https://www.sqlite.org/lang_createtable.html#the_collate_clause), use the query editor.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/create-table.png)


## Editing Table Schema - Creating an Index
You can access this feature by either clicking the SQL statement at the bottom of the editor, right-clicking the table name in the SELECT statement, or clicking "Schema" then "Index > + Add".

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/editors.png)

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/table-selector-contextmenu.png)

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/table-schema-v2.png)


## Editing Table Schema - Dropping a Table
You can access this feature by either clicking on the SQL statement at the bottom of the editor, or by right-clicking the table name in the SELECT statement, and then selecting "DROP TABLE".

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/editors.png)

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/table-selector-contextmenu.png)


## Editing Table Schema - Renaming a Table
To rename a table, right-click the table name in the SELECT statement, and then select "Rename Table".

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/table-selector-contextmenu.png)


## File Associations
This extension recognizes `.db`, `.db3`, `.sdb`, `.s3db`, `.sqlitedb`, `.mddata`, `.sqlite`, `.sqlite3`, `.sl3`, `.vscdb`, and `.sq3` files as database files. To open other files, right-click the file in the explorer and select `Open with…` then `SQLite3 Editor`.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/open_with.gif)


## Importing and Exporting Data in CSV, JSON, or SQL
By clicking the "Other Tools..." button, you can access various features, including CSV, JSON, and SQL imports and exports.
These import and export features rely on a helper program bundled with this extension. You can check the available options by using `<command> import --help` or `<command> export --help`.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/other-tools.png)


## In-Memory Databases
You can connect to an in-memory database using `SQLite3 Editor: Connect to In-Memory Database` in the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette). Alternatively, you can connect by editing the first line in a query editor to `--database: :memory:` (for details, refer to the "Query Editor" section).
This feature should be useful to quickly test SQL statements.


## Opening the Database in a Command Line Shell
This feature opens an integrated terminal in VSCode, initialized with the command `sqlite3 <your-file>`. 
It is available only if you have the `sqlite3` command installed on your system. 
To use this feature, navigate to "Other Tools" then "Open in Command Line Shell".

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/open-in-command-line-shell.png)


## Query Editor - Overview
To access the query editor, click the "Query Editor" button.

The line comment at the first line of the query editor indicates the linked database. If it is deleted, the query editor will disconnect from the database.

Any files that start with `-- database: ...` will be recognized as a query editor. This allows you to save a query editor as a file for future use.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/query-editor-file.gif)

There are three ways to execute statements in the query editor:
- To run a single statement, use `Shift+Enter` or click the "Execute" button above the statement. The result will only be displayed if it is a SELECT statement. To display the result of PRAGMA statements, use the pragma functions (e.g. use `SELECT * FROM pragma_table_list();` instead of `PRAGMA table_list;`).
- To execute the entire file, use the ▷ button located in the top right corner of the editor.
- To execute a part of the file, select the text then click "Execute Selection" in the context menu.

The "Execute" button shown above a transaction (`BEGIN;` ... `END;` block) executes all the statements in the transaction. If the transaction is not successfully executed, the extension will perform a [ROLLBACK](https://www.sqlite.org/lang_transaction.html).

Due to the limitation of the current mechanism to reload the table, there may be a slight delay between the execution of a statement and the updates to the table.


## Query Editor - Document Formatting
You can format queries by selecting "Format Document" in the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) or by pressing Shift+Alt+F.

This feature employs [sql-formatter](https://github.com/sql-formatter-org/sql-formatter) to format queries.
You can adjust formatting options with the configurations under `sqlite3-editor.format`, and they are mostly compatible with [Prettier SQL VSCode](https://marketplace.visualstudio.com/items?itemName=inferrinizzard.prettier-sql-vscode).

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/format.gif)


## Query Editor - Executing a Part of Common Table Expression (CTE)
In the query editor, "Select" buttons are displayed for each CTE. This enhances the ease of creating complex queries involving CTEs.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/cte.gif)


## Query Editor - Syntax Validation
The query editor identifies syntax errors in SQL statements by [preparing](https://www.sqlite.org/c3ref/prepare.html) each statement in an isolated database connection and catching compilation errors.
However, due to the nature of this method, certain errors might not be detected, such as those within PRAGMA statements or references to non-existent tables.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/syntax-validator.png)


## Table View - Auto Reloading
When the 'Auto Reload' button is activated, the editor will automatically refresh the table whenever there are updates.

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/auto-reload.mp4" controls></video>


## Table View - Conditional Formatting
Conditional formatting colorizes table cells by their values. You can use this feature by right-clicking a table column then "Colorize (Conditional Formatting)".


## Table View - Displaying and Jumping to the Definition of Foreign Keys
You can view the source record of a cell in a column that is under a [foreign key constraint](https://www.sqlite.org/foreignkeys.html) by hovering the cursor over the cell.
If you want to jump to the source record, use the context menu item.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/hover-fk.gif)

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/goto-fk.gif)


## Table View - Editing GENERATED Columns
[GENERATED columns](https://www.sqlite.org/gencol.html) can be edited just like any other columns. Committing a change updates the table schema.

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/edit-generated-always-as.mp4" controls></video>


## Table View - Entity-Relationship Diagram
If the database contains [foreign keys](https://www.sqlite.org/foreignkeys.html) or [views](https://www.sqlite.org/lang_createview.html), the table selector will display the entity-relationship diagram alongside the list of tables. Clicking on an entity opens the corresponding table.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/erd.png)


## Table View - Filtering and Sorting Data
The find widget shown in the image below allows you to quickly filter records by searching for text matches across all columns, just like [the one in VSCode](https://code.visualstudio.com/docs/editor/codebasics#_find-and-replace). For more advanced usage, you can also use the regular expression, whole word, and case-sensitivity switches.
You can access this feature by pressing the "Find" button in the editor or pressing Ctrl+F.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/find_widget.png)

Column filters allow you to filter records based on a specific value in the chosen column. To use this, right-click on a table column header.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/column-filter.png)

Alternatively, you can also set a filter via the context menu on cells.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/set-filter.png)

To sort records by a specific column, simply click on the column name. You can also sort the table from the context menu on the column name.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/sorting.png)


## Table View - Git-Diff Support
When you open a database from [the source control view](https://code.visualstudio.com/docs/sourcecontrol/overview), you will see a side-by-side comparison of two versions of the database.

To display the differences between the two versions, click the "Compare with Local File" button. Depending on the size of the database, it may take several seconds or minutes for the differences to appear. If locking the databases is a problem for your use-case, you should avoid using this feature.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/diff.gif)


## Table View - Group by Column
You can group records by a column with this feature. To group a column, right-click on a column header then select "Group by Column". To cancel the grouping, click the icon on the column header.

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/group-by.mp4" controls></video>


## Table View - Inserting Data from CSV
You can insert CSV into an existing table by clicking the SQL statement at the bottom of the editor then selecting "Bulk Insert".

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/editors.png)

This feature inserts CSV data into the table. Each CSV column is encoded as TEXT, but if the table column has a data type (column affinity), SQLite will cast it to the appropriate type. For example, if a column is defined as "column1 INTEGER," then the CSV values in that column will be cast as an integer.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/bulk-insert.png)


## Table View - Jumping to a Table or a Row
When the extension's editor is active, you can use the Go to Table/Row command to navigate to a specific table and/or row. The Ctrl+G keybinding is assigned to this command.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/goto.gif)


## Table View - Multi-Selection
[UPDATE](https://www.sqlite.org/lang_update.html) and [DELETE](https://www.sqlite.org/lang_delete.html) statements support multi-selection. To select multiple cells, you can either drag over the cells, click a cell with the alt key pressed, or press the Shift + Arrow keys while a cell is selected.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/multi-select.gif)

> Dragging on row numbers is not currently supported, and you need to use the alt + click instead.

You can perform actions other than editing data by right-clicking on the selection.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/multi-select-contextmenu.png)


## Table View - Resizing Columns
You can resize columns by dragging the right edge of the column header. Alternatively, to adjust the width to the content, you can use the "Autofit Column Width" button in the context menu.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/autofit.gif)


## Table View - Resizing Rows
You can resize rows by dragging the lower edge of a row's number.

## Table View - Selecting a Table
You can switch between tables by clicking a table name in either the editor or the explorer.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/switch-table-2.gif)


## Table View - Tabs
Adding `"sqlite3-editor.ui.alwaysDisplayTabs": true` to VSCode's settings enables the table tab feature.
Its behavior resembles that of VSCode's tabs; in [the preview mode](https://code.visualstudio.com/docs/getstarted/userinterface#_preview-mode), the tab closes when you switch to another table, but after double-clicking the preview tab, the tab remains open until you click the close button.
Certain actions, such as selecting "Go to Source Record" on foreign key columns, activate the tab UI regardless of the value of the `sqlite3-editor.ui.alwaysDisplayTabs` setting.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/tabs.png)


## Using Non-Standard SQLite - Run-Time Loadable SQLite Extensions
The configuration setting "sqlite3-editor.runtimeLoadableExtensions.driver.sqlite3" allows you to specify [run-time loadable extensions](https://www.sqlite.org/loadext.html) that will be loaded with every SQLite connection opened by this extension.

For example, to load SpatiaLite, follow these instructions:

1. Install SpatiaLite:
   ```shell
   # Ubuntu/Debian
   sudo apt install libsqlite3-mod-spatialite
   
   # macOS
   brew install libspatialite
   ```
2. Configure the extension (`F1` or `Ctrl(Cmd) + Shift + P` -> `Preferences: Open User Settings (JSON)`):
   ```json
   "sqlite3-editor.runtimeLoadableExtensions.driver.sqlite3": {
       ".*": ["mod_spatialite"]
   }
   ```

   Run-time loadable extensions can be associated with specific files by matching them with a regex pattern. To match any file, use ".*".


## Using Non-Standard SQLite - User Compiled SQLite
Since this extension statically links SQLite to a component built with Rust, you need to rebuild the component to use a non-standard version of SQLite.

For example, if you want to add the compilation flag [SQLITE_OMIT_DEPRECATED](https://www.sqlite.org/compile.html#omit_deprecated) to SQLite to exclude deprecated features, follow these instructions:
1. First, you need to install [Rust](https://www.rust-lang.org/tools/install) and [Git](https://git-scm.com/).
2. Then, build the Rust component with the following commands. Note that this project uses the "bundled" [feature](https://doc.rust-lang.org/cargo/reference/features.html) of the [libsqlite3-sys](https://crates.io/crates/libsqlite3-sys) crate, and [libsqlite3-sys](https://crates.io/crates/libsqlite3-sys) uses the "LIBSQLITE3_FLAGS" environment variable when compiling the SQLite source.
   ```shell
   git clone https://github.com/yy0931/sqlite3-editor --single-branch --branch rust-backend
   cd sqlite3-editor
   cargo clean
   LIBSQLITE3_FLAGS='-DSQLITE_OMIT_DEPRECATED' cargo build --release --features sqlite
   ```
3. Finally, specify the absolute path to `./target/release/db-driver-rs` in the `sqlite3-editor.executablePath` setting of VSCode.

Please note that making changes like this could cause issues with future updates to the extension. Therefore, we recommend turning off automatic updates for this extension.

# Configurations
NOTE: This document does not cover all of the configuration options. Search "sqlite3-editor" in the VSCode's settings tab for other configurations.

## sqlite3-editor.connectionSetupQueries.debug
This configuration allows you to view which setup queries were used.
If enabled, the extension displays the URI matched against the regex patterns in connectionSetupQueries and the result of the match for each pattern when an editor is opened.


## sqlite3-editor.connectionSetupQueries.driver.sqlite
This configuration specifies the SQL statements that are executed immediately after connecting to a database.

The keys are case-sensitive regular expressions used to match the file URI (e.g. `file:///path/to/database.db`), and the values are corresponding SQL statements to be executed. If multiple item's patterns match the same URI, only the first item will be used.

This configuration is similar to the "sqlite.setupDatabase" configuration in [alexcvzz/sqlite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) but differs in that it uses regular expressions for path comparison.

Commands that are available in the SQLite's CLI, including `.load`, are not supported. Most [run-time loadable extensions](https://www.sqlite.org/loadext.html) can be loaded with `SELECT load_extension(...);`, but to load run-time loadable extensions that modify or delete existing functions, you need to use the `sqlite3-editor.runtimeLoadableExtensions.driver.sqlite3` configuration instead.

For example, to execute [`PRAGMA foreign_keys = ON;`](https://www.sqlite.org/pragma.html#pragma_foreign_keys), [`PRAGMA busy_timeout = 1000;`](https://www.sqlite.org/pragma.html#pragma_busy_timeout), and `SELECT load_extension('/home/user/sqlean/crypto.so');` on all SQLite 3 connections, use the following configuration:
```json
"sqlite3-editor.connectionSetupQueries.driver.sqlite3": {
    ".*": "PRAGMA foreign_keys = ON; PRAGMA busy_timeout = 1000; SELECT load_extension('/home/user/sqlean/crypto.so');"
}
```


## sqlite3-editor.maxHistoryEntries
With the default configuration, this extension stores the last 500 SQL queries executed in [ExtensionContext.globalState](https://code.visualstudio.com/api/references/vscode-api#ExtensionContext.globalState). You can view them using `SQLite3 Editor: Show History` and clear them using `SQLite3 Editor: Clear History` from [the command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette). This setting specifies the number of queries to save. If set to 0, history will not be saved.


## sqlite3-editor.runtimeLoadableExtensions.driver.sqlite3
This configuration loads [run-time loadable extensions](https://www.sqlite.org/loadext.html) immediately after connecting to a database, using the `sqlite3_load_extension` call in the SQLite C interface.

Most run-time loadable extensions can be loaded with `SELECT load_extension(...);`, but some run-time loadable extensions need the `sqlite3_load_extension` call, according to the documentation:

> load_extension(X), load_extension(X,Y)
> - The load_extension() function will fail if the extension attempts to modify or delete an SQL function or collating sequence. The extension can add new functions or collating sequences, but cannot modify or delete existing functions or collating sequences because those functions and/or collating sequences might be used elsewhere in the currently running SQL statement. To load an extension that changes or deletes functions or collating sequences, use the sqlite3_load_extension() C-language API.
>
> https://www.sqlite.org/lang_corefunc.html#load_extension

The keys are case-sensitive regular expressions used to match the file URI, and the values are the list of runtime-loadable extensions to be loaded. In case multiple patterns match the same URI, only the first item will be used. The runtime-loadable extensions are loaded before executing the setup queries specified in `sqlite3-editor.connectionSetupQueries.driver.sqlite3`.

For example, to load the `crypto` module in sqlean, download and extract a release of [sqlean](https://github.com/nalgeon/sqlean), and specify the extracted path as follows:

```json
"sqlite3-editor.runtimeLoadableExtensions.driver.sqlite3": {
  ".*": ["/home/user/sqlean/crypto.so"]
}
```


# Supported Environments
- Windows, x64, Windows 7+
- Windows, ia32, Windows 7+
- Windows, arm64
- Linux, x64, glibc 2.17+
- Linux, arm64, glibc 2.17+
- Linux, armhf, glibc 2.29+
- Linux, x64 *1
- Linux, arm64 *1
- Mac, x64, 10.7+, Lion+
- Mac, arm64, 11.0+, Big Sur+

*1 are fallbacks for when glibc is not available, such as on Alpine Linux, but they do not support [SQLite run-time loadable extensions](https://www.sqlite.org/loadext.html) because libc (musl) is statically linked.

# Monitoring and Reporting
## Error Reporting
This extension displays a "Send error report" button on error notifications. The button sends the error message and the stack trace to the extension's author using [Microsoft/vscode-extension-telemetry](https://github.com/Microsoft/vscode-extension-telemetry), or opens [a GitHub issue](https://github.com/yy0931/sqlite3-editor), depending on the user's telemetry settings. If vscode-extension-telemetry is used, the system information (i.e. the "common properties" of [Microsoft/vscode-extension-telemetry](https://github.com/microsoft/vscode-extension-telemetry/blob/04ff08da26bc437e87bfb398ac63be2685576066/README.md)) will also be included. If the webview threw an error, the webview’s browser information (User-Agent) would also be included.

Keep in mind that the bugs may not be fixed if the reports do not include enough information or the developer is busy, but your help in reporting errors is greatly appreciated.

## Opt-in Telemetry
This extension collects anonymous telemetry data using [Microsoft/vscode-extension-telemetry](https://github.com/Microsoft/vscode-extension-telemetry) if `telemetry.telemetryLevel` is `"all"` and `sqlite3-editor.telemetry` is `"allow"` in [VSCode's settings](https://code.visualstudio.com/docs/getstarted/settings). It is disabled by default. On the first use of the extension after installation, there is a small chance that a pop-up will appear, asking the user for consent to opt into the telemetry. Users can decline it by selecting the 'Deny' option in the pop-up.

The purpose of this telemetry is to:

- Determine whether the extension is being used and if continued development and releases are necessary.
- Improve the compatibility and performance of the extension based on frequently used environments.
- Improve the extension based on frequently used features.

The following is the list of data collected:

- The type of the editor tab (file, git-diff, or other).
- The startup time of the editor tab.
- Usage of internal commands that are registered with `vscode.commands.registerCommand`.
- Usage of each element on the UI.
- Usage of each keyboard shortcut.
- The type (such as table, view, etc.) and size of the active table (rounded to the nearest power of 2).
- The "common properties" of [Microsoft/vscode-extension-telemetry](https://github.com/Microsoft/vscode-extension-telemetry).

The data collected is encrypted and will be deleted after 90 days.

The data collected will only be used to improve the extension and will not be shared with any third parties.

Please note that the telemetry data collected by this extension may change in future releases.
