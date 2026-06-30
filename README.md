# Matrix_CEAGENTS

> BM25 Self-Learning Orchestrator This orchestrator uses the BM25 algorithm to retrieve successful task patterns from the memory ledger/database, allowing the system to "self-learn" and adapt its prompts based on historically successful agent runs.

*Auto-generated 2026-06-30 15:57 from source — branch `master`, 27 Python modules, 12 other files.*

## Architecture

```
  README.md
  nx_engine_mapper.py
  swarm_registry.json
  core/
    build_manifest.json
    cegcc/
      README.md
  db/
    project.db
  memory/
    chat_memory.json
    learnings.jsonl
    viper_code_vault.db
  system/
    __init__.py
    agentic_sync_daemon.py
    bm25_orchestrator.py
    ce_simulator.py
    chat_harvester.py
    datacenter_sync.sh
    enex_importer.py
    evernote_manager.py
    fault_injector.py
    flow_orchestrator.py
    google_bridge.py
    gui_bridge.py
    backup/
      desktop_LEGACY.html
      gui_bridge_LEGACY.py
    evernote-gw-py/
      evernote-gw
      evernote_gw.py
    static/
      icons/
        placeholder.txt
    templates/
      desktop.html
```

## Dependencies

External packages imported by this project:

`PocketMatrix`, `bs4`, `dotenv`, `email`, `evernote`, `flask`, `gkeepapi`, `markdown`, `mimetypes`, `rank_bm25`, `requests`, `smtplib`, `xml`, `zipfile`

## How to run

Executable entry points (have a `__main__` block):

- `python nx_engine_mapper.py`
- `python system/agentic_sync_daemon.py`
- `python system/backup/gui_bridge_LEGACY.py`
- `python system/bm25_orchestrator.py`
- `python system/ce_simulator.py`
- `python system/chat_harvester.py`
- `python system/enex_importer.py`
- `python system/evernote-gw-py/evernote_gw.py`
- `python system/evernote_manager.py`
- `python system/fault_injector.py`
- `python system/flow_orchestrator.py`
- `python system/google_bridge.py`

## Modules

### `system/agentic_sync_daemon.py`

- `log(msg)`
- `run_sync_cycle()`
- `main()`

### `system/backup/gui_bridge_LEGACY.py`

- `list_models()`
- `active_model()`
- `list_knowledge()`
- `search_knowledge()`
- `knowledge_stats()`
- `desktop()`
- `manifest()`
- `omni_chat()`
- `list_projects()`
- `list_databases()`
- `query_database()`
- `update_database()`
- `handle_notes()`
- `handle_todo()`
- `sync_todo_google()`

### `system/bm25_orchestrator.py`

BM25 Self-Learning Orchestrator
This orchestrator uses the BM25 algorithm to retrieve successful task patterns
from the memory ledger/database, allowing the system to "self-learn" and adapt
its prompts based on historically successful agent runs.

- **class `BM25Orchestrator`**
  - methods: `load_memory`, `_add_document`, `_compute_idf`, `get_scores`, `retrieve_best_context`, `orchestrate`

### `system/ce_simulator.py`

- **class `CESubstrateSimulator`** — Simulates a remote Windows CE device for local testing and pedagogy.
  - methods: `get_status`, `simulate_shell`

### `system/chat_harvester.py`

- `extract_todos()`

### `system/enex_importer.py`

- `import_enex(enex_file_path)`

### `system/evernote-gw-py/evernote_gw.py`

- `load_tokens()`
- `save_tokens(tok)`
- `enml_wrap(html_body)`
- `md_to_enml(md)`
- `md5_hex(b)`
- `get_client(token)`
- `cmd_auth(_args)`
- `cmd_create_note(args)`
- `cmd_import_jsonl(args)`
- `main()`

### `system/evernote_manager.py`

- `init_db()`
- `upsert_note(note_id, title, content, tags, updated_at)`
- `search_notes(query)`

### `system/fault_injector.py`

- **class `DynamicFaultInjector`**
  - methods: `inject_fault`, `tutor_student`

### `system/flow_orchestrator.py`

- `get_system_flow()`

### `system/google_bridge.py`

- `load_credentials()` — Loads Google credentials (Email and App Password) from config.
- `send_gmail(to_addr, subject, body, retries)` — Sends an email via Gmail SMTP using an App Password with exponential backoff.
- `sync_keep(tasks, retries)` — Syncs the local PocketMatrix ToDo database with Google Keep with backoff.

### `system/gui_bridge.py`

- `get_matrix_config()`
- `save_email_config()`
- `save_oauth_config()`
- `save_node_config()`
- `generate_node_id_api()`
- `get_axioms()`
- `list_models()`
- `fetch_models_api()`
- `get_swarm_status()` — Calculates Happiness and Health for all agents (MSN/Sims Mode).
- `get_ops_manual()`
- `get_nx_nodes()`
- `get_nx_edges()`
- `add_nx_node()`
- `brute_force_control()`
- `trigger_sync()`

### `system/harvest_evernote.py`

- `harvest_notes()`

### `system/harvest_logs.py`

- `harvest_logs()`

### `system/headless_bridge.py`

- **class `HeadlessBridge`**
  - methods: `translate_and_execute`

### `system/ingestion_engine.py`

- **class `IngestionEngine`**
  - methods: `clean_text`, `fetch_and_parse`, `format_for_danube`

### `system/knowledge_hub.py`

- `init_hub()`
- `search_knowledge_bm25(query)`

### `system/onedrive_scanner.py`

- `scan_and_ingest(scan_path)`

### `system/orchestrator.py`

- `get_active_todos()`
- `get_blueprints()`
- `run_orchestration()`

### `system/positive_ping.py`

- `generate_ping()`

### `system/project_to_evernote.py`

- `summarize_and_store()`

### `system/quarantine_filter.py`

- `isolate_anomalies()`

### `system/telemetry_parser.py`

- **class `TelemetryParser`**
  - methods: `generate_mock_telemetry`, `analyze_telemetry`

### `system/viper_pedagogy.py`

- `process_viper_notes(notes_dir)`

## Public API index

| Module | Function | Signature |
|--------|----------|-----------|
| `agentic_sync_daemon` | `log` | `log(msg)` |
| `agentic_sync_daemon` | `main` | `main()` |
| `agentic_sync_daemon` | `run_sync_cycle` | `run_sync_cycle()` |
| `chat_harvester` | `extract_todos` | `extract_todos()` |
| `enex_importer` | `import_enex` | `import_enex(enex_file_path)` |
| `evernote_gw` | `cmd_auth` | `cmd_auth(_args)` |
| `evernote_gw` | `cmd_create_note` | `cmd_create_note(args)` |
| `evernote_gw` | `cmd_import_jsonl` | `cmd_import_jsonl(args)` |
| `evernote_gw` | `enml_wrap` | `enml_wrap(html_body)` |
| `evernote_gw` | `get_client` | `get_client(token)` |
| `evernote_gw` | `load_tokens` | `load_tokens()` |
| `evernote_gw` | `main` | `main()` |
| `evernote_gw` | `md5_hex` | `md5_hex(b)` |
| `evernote_gw` | `md_to_enml` | `md_to_enml(md)` |
| `evernote_gw` | `save_tokens` | `save_tokens(tok)` |
| `evernote_manager` | `init_db` | `init_db()` |
| `evernote_manager` | `search_notes` | `search_notes(query)` |
| `evernote_manager` | `upsert_note` | `upsert_note(note_id, title, content, tags, updated_at)` |
| `flow_orchestrator` | `get_system_flow` | `get_system_flow()` |
| `google_bridge` | `load_credentials` | `load_credentials()` |
| `google_bridge` | `send_gmail` | `send_gmail(to_addr, subject, body, retries)` |
| `google_bridge` | `sync_keep` | `sync_keep(tasks, retries)` |
| `gui_bridge` | `active_model` | `active_model()` |
| `gui_bridge` | `add_nx_node` | `add_nx_node()` |
| `gui_bridge` | `add_scheduled_task` | `add_scheduled_task()` |
| `gui_bridge` | `audio_evolve` | `audio_evolve()` |
| `gui_bridge` | `brute_force_control` | `brute_force_control()` |
| `gui_bridge` | `check_readiness` | `check_readiness()` |
| `gui_bridge` | `clippy_learn` | `clippy_learn()` |
| `gui_bridge` | `clippy_recall` | `clippy_recall()` |
| `gui_bridge` | `config_qwen` | `config_qwen()` |
| `gui_bridge` | `db_schema` | `db_schema()` |
| `gui_bridge` | `delete_file` | `delete_file()` |
| `gui_bridge` | `desktop` | `desktop()` |
| `gui_bridge` | `evernote_search` | `evernote_search()` |
| `gui_bridge` | `fetch_models_api` | `fetch_models_api()` |
| `gui_bridge` | `generate_node_id_api` | `generate_node_id_api()` |
| `gui_bridge` | `get_axioms` | `get_axioms()` |
| `gui_bridge` | `get_flow` | `get_flow()` |
| `gui_bridge` | `get_help` | `get_help()` |
| `gui_bridge` | `get_mail` | `get_mail()` |
| `gui_bridge` | `get_matrix_config` | `get_matrix_config()` |
| `gui_bridge` | `get_nx_edges` | `get_nx_edges()` |
| `gui_bridge` | `get_nx_nodes` | `get_nx_nodes()` |
| `gui_bridge` | `get_ops_manual` | `get_ops_manual()` |
| `gui_bridge` | `get_proposals` | `get_proposals()` |
| `gui_bridge` | `get_scheduled_tasks` | `get_scheduled_tasks()` |
| `gui_bridge` | `get_swarm_status` | `get_swarm_status()` |
| `gui_bridge` | `get_tasks` | `get_tasks()` |
| `gui_bridge` | `git_commit` | `git_commit()` |
| `gui_bridge` | `git_status` | `git_status()` |
| `gui_bridge` | `handle_chat` | `handle_chat()` |
| `gui_bridge` | `handle_notes` | `handle_notes()` |
| `gui_bridge` | `handle_todo` | `handle_todo()` |
| `gui_bridge` | `knowledge_stats` | `knowledge_stats()` |
| `gui_bridge` | `list_databases` | `list_databases()` |
| `gui_bridge` | `list_files` | `list_files()` |
| `gui_bridge` | `list_keys` | `list_keys()` |
| `gui_bridge` | `list_knowledge` | `list_knowledge()` |
| `gui_bridge` | `list_models` | `list_models()` |

## Status

- Branch: `master`
- Last commit: 2026-06-29 03:23:27 -0600
- File types: .json ×3, .md ×2, .db ×2, .html ×2, .jsonl ×1, .sh ×1, .txt ×1

### Recent commits
```
68d6665 [Moe autonomous] Matrix_CEAGENTS 2026-06-29 03:23
c0bb6e0 [Moe autonomous] Matrix_CEAGENTS 2026-06-27 12:43
625ddf6 [Moe autonomous] Matrix_CEAGENTS 2026-06-26 17:32
872c15a [Moe autonomous] Matrix_CEAGENTS 2026-06-19 23:11
ab8c97d [Moe autonomous] Matrix_CEAGENTS 2026-06-19 22:33
ce59320 [Moe autonomous] Matrix_CEAGENTS 2026-06-19 22:03
a7ec715 feat: Link NXEngine mapper to Genetic Techno Engine
6d69583 feat: Add NXEngine Mind Palace Mapper
```

---
*README generated by `readme_generator.py` (Viper). Deterministic — derived from source, not LLM prose.*