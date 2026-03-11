# CODEBASE.md: System Architecture Map

## 1. Architecture Overview
Generated on: 2026-03-11 16:27

### 1.1 System Map (Mermaid)
```mermaid
graph TD
    "src/ol_superset/ol_superset/cli.py" --> "sys"
    "src/ol_superset/ol_superset/cli.py" --> "cyclopts"
    "src/ol_superset/ol_superset/cli.py" --> "ol_superset.commands.apply_rls"
    "src/ol_superset/ol_superset/cli.py" --> "ol_superset.commands.dedupe"
    "src/ol_superset/ol_superset/cli.py" --> "ol_superset.commands.export"
    "src/ol_superset/ol_superset/cli.py" --> "ol_superset.commands.lock"
    "src/ol_superset/ol_superset/cli.py" --> "ol_superset.commands.promote"
    "src/ol_superset/ol_superset/cli.py" --> "ol_superset.commands.refresh"
    "src/ol_superset/ol_superset/cli.py" --> "ol_superset.commands.sync"
    "src/ol_superset/ol_superset/cli.py" --> "ol_superset.commands.validate"
    "src/ol_superset/ol_superset/commands/refresh.py" --> "sys"
    "src/ol_superset/ol_superset/commands/refresh.py" --> "pathlib"
    "src/ol_superset/ol_superset/commands/refresh.py" --> "typing"
    "src/ol_superset/ol_superset/commands/refresh.py" --> "cyclopts"
    "src/ol_superset/ol_superset/commands/refresh.py" --> "rich.console"
    "src/ol_superset/ol_superset/commands/refresh.py" --> "rich.table"
    "src/ol_superset/ol_superset/commands/refresh.py" --> "ol_superset.lib.superset_api"
    "src/ol_superset/ol_superset/commands/refresh.py" --> "ol_superset.lib.utils"
    "src/ol_superset/ol_superset/commands/lock.py" --> "sys"
    "src/ol_superset/ol_superset/commands/lock.py" --> "pathlib"
    "src/ol_superset/ol_superset/commands/lock.py" --> "typing"
    "src/ol_superset/ol_superset/commands/lock.py" --> "cyclopts"
    "src/ol_superset/ol_superset/commands/lock.py" --> "rich.console"
    "src/ol_superset/ol_superset/commands/lock.py" --> "rich.table"
    "src/ol_superset/ol_superset/commands/lock.py" --> "ol_superset.lib.superset_api"
    "src/ol_superset/ol_superset/commands/lock.py" --> "ol_superset.lib.utils"
    "src/ol_superset/ol_superset/commands/dedupe.py" --> "re"
    "src/ol_superset/ol_superset/commands/dedupe.py" --> "pathlib"
    "src/ol_superset/ol_superset/commands/dedupe.py" --> "cyclopts"
    "src/ol_superset/ol_superset/commands/dedupe.py" --> "yaml"
    "src/ol_superset/ol_superset/commands/dedupe.py" --> "rich.console"
    "src/ol_superset/ol_superset/commands/dedupe.py" --> "rich.table"
    "src/ol_superset/ol_superset/commands/apply_rls.py" --> "json"
    "src/ol_superset/ol_superset/commands/apply_rls.py" --> "sys"
    "src/ol_superset/ol_superset/commands/apply_rls.py" --> "pathlib"
    "src/ol_superset/ol_superset/commands/apply_rls.py" --> "typing"
    "src/ol_superset/ol_superset/commands/apply_rls.py" --> "cyclopts"
    "src/ol_superset/ol_superset/commands/apply_rls.py" --> "rich.console"
    "src/ol_superset/ol_superset/commands/apply_rls.py" --> "rich.table"
    "src/ol_superset/ol_superset/commands/apply_rls.py" --> "ol_superset.lib.superset_api"
    "src/ol_superset/ol_superset/commands/apply_rls.py" --> "ol_superset.lib.utils"
    "src/ol_superset/ol_superset/commands/sync.py" --> "sys"
    "src/ol_superset/ol_superset/commands/sync.py" --> "typing"
    "src/ol_superset/ol_superset/commands/sync.py" --> "cyclopts"
    "src/ol_superset/ol_superset/commands/sync.py" --> "ol_superset.lib.database_mapping"
    "src/ol_superset/ol_superset/commands/sync.py" --> "ol_superset.lib.superset_api"
    "src/ol_superset/ol_superset/commands/sync.py" --> "ol_superset.lib.utils"
    "src/ol_superset/ol_superset/commands/validate.py" --> "sys"
    "src/ol_superset/ol_superset/commands/validate.py" --> "typing"
    "src/ol_superset/ol_superset/commands/validate.py" --> "yaml"
    "src/ol_superset/ol_superset/commands/validate.py" --> "cyclopts"
    "src/ol_superset/ol_superset/commands/validate.py" --> "ol_superset.lib.utils"
    "src/ol_superset/ol_superset/commands/export.py" --> "typing"
    "src/ol_superset/ol_superset/commands/export.py" --> "cyclopts"
    "src/ol_superset/ol_superset/commands/export.py" --> "ol_superset.commands.dedupe"
    "src/ol_superset/ol_superset/commands/export.py" --> "ol_superset.lib.utils"
    "src/ol_superset/ol_superset/commands/promote.py" --> "subprocess"
    "src/ol_superset/ol_superset/commands/promote.py" --> "sys"
    "src/ol_superset/ol_superset/commands/promote.py" --> "typing"
    "src/ol_superset/ol_superset/commands/promote.py" --> "cyclopts"
    "src/ol_superset/ol_superset/commands/promote.py" --> "ol_superset.lib.database_mapping"
    "src/ol_superset/ol_superset/commands/promote.py" --> "ol_superset.lib.utils"
    "src/ol_superset/ol_superset/commands/promote.py" --> "yaml"
    "src/ol_superset/ol_superset/lib/utils.py" --> "subprocess"
    "src/ol_superset/ol_superset/lib/utils.py" --> "sys"
    "src/ol_superset/ol_superset/lib/utils.py" --> "pathlib"
    "src/ol_superset/ol_superset/lib/database_mapping.py" --> "json"
    "src/ol_superset/ol_superset/lib/database_mapping.py" --> "re"
    "src/ol_superset/ol_superset/lib/database_mapping.py" --> "subprocess"
    "src/ol_superset/ol_superset/lib/database_mapping.py" --> "sys"
    "src/ol_superset/ol_superset/lib/database_mapping.py" --> "pathlib"
    "src/ol_superset/ol_superset/lib/database_mapping.py" --> "yaml"
    "src/ol_superset/ol_superset/lib/superset_api.py" --> "hashlib"
    "src/ol_superset/ol_superset/lib/superset_api.py" --> "json"
    "src/ol_superset/ol_superset/lib/superset_api.py" --> "secrets"
    "src/ol_superset/ol_superset/lib/superset_api.py" --> "sys"
    "src/ol_superset/ol_superset/lib/superset_api.py" --> "webbrowser"
    "src/ol_superset/ol_superset/lib/superset_api.py" --> "base64"
    "src/ol_superset/ol_superset/lib/superset_api.py" --> "http.server"
    "src/ol_superset/ol_superset/lib/superset_api.py" --> "pathlib"
    "src/ol_superset/ol_superset/lib/superset_api.py" --> "threading"
    "src/ol_superset/ol_superset/lib/superset_api.py" --> "urllib.parse"
    "src/ol_superset/ol_superset/lib/superset_api.py" --> "requests"
    "src/ol_superset/ol_superset/lib/superset_api.py" --> "yaml"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/sensors/object_storage.py" --> "json"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/sensors/object_storage.py" --> "collections.abc"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/sensors/object_storage.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/sensors/object_storage.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/sensors/object_storage.py" --> "dagster_aws.s3"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/sensors/object_storage.py" --> "ol_orchestrate.resources.gcp_gcs"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/yaml_config_helper.py" --> "pathlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/yaml_config_helper.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/yaml_config_helper.py" --> "yaml"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/glue_helper.py" --> "types"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/glue_helper.py" --> "boto3"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/glue_helper.py" --> "pyiceberg.catalog.glue"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/openedx.py" --> "hashlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/openedx.py" --> "json"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/openedx.py" --> "tarfile"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/openedx.py" --> "datetime"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/openedx.py" --> "pathlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/openedx.py" --> "tempfile"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/openedx.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/openedx.py" --> "xml.etree.ElementTree"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/automation_policies.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/hooks.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/utils.py" --> "hashlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/utils.py" --> "os"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/utils.py" --> "zipfile"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/utils.py" --> "pathlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/utils.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/utils.py" --> "ol_orchestrate.resources.secrets.vault"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/constants.py" --> "os"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/constants.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/file_rendering.py" --> "csv"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/file_rendering.py" --> "pathlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_helpers.py" --> "os"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_helpers.py" --> "re"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_helpers.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_helpers.py" --> "dagster._core.definitions.partitions.utils.base"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_helpers.py" --> "dagster_aws.s3"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_helpers.py" --> "ol_orchestrate.io_managers.filepath"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/arrow_helper.py" --> "pyarrow"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/event_log.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/event_log.py" --> "dagster._config"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/event_log.py" --> "dagster._config.config_schema"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/event_log.py" --> "dagster._core.storage.config"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/event_log.py" --> "dagster._core.storage.event_log"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/event_log.py" --> "dagster._core.storage.event_log.polling_event_watcher"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/event_log.py" --> "dagster._core.storage.sql"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/event_log.py" --> "dagster._serdes"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/event_log.py" --> "dagster_postgres.event_log"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/event_log.py" --> "dagster_postgres.utils"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/event_log.py" --> "sqlalchemy"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/schedule_storage.py" --> "dagster._config"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/schedule_storage.py" --> "dagster._config.config_schema"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/schedule_storage.py" --> "dagster._core.storage.config"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/schedule_storage.py" --> "dagster._core.storage.schedules"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/schedule_storage.py" --> "dagster._core.storage.sql"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/schedule_storage.py" --> "dagster._serdes"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/schedule_storage.py" --> "dagster_postgres.schedule_storage"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/schedule_storage.py" --> "dagster_postgres.utils"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/schedule_storage.py" --> "sqlalchemy"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/run_storage.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/run_storage.py" --> "dagster._config"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/run_storage.py" --> "dagster._config.config_schema"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/run_storage.py" --> "dagster._core.storage.config"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/run_storage.py" --> "dagster._core.storage.runs"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/run_storage.py" --> "dagster._core.storage.sql"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/run_storage.py" --> "dagster._serdes"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/run_storage.py" --> "dagster_postgres.run_storage"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/run_storage.py" --> "dagster_postgres.utils"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/run_storage.py" --> "sqlalchemy"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/__init__.py" --> "ol_orchestrate.lib.postgres.event_log"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/__init__.py" --> "ol_orchestrate.lib.postgres.run_storage"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/__init__.py" --> "ol_orchestrate.lib.postgres.schedule_storage"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_types/files.py" --> "pathlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_types/files.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_types/google.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_types/google.py" --> "google.cloud.bigquery.dataset"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/io_managers/filepath.py" --> "pathlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/io_managers/filepath.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/io_managers/filepath.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/io_managers/filepath.py" --> "fsspec.implementations.local"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/io_managers/filepath.py" --> "gcsfs"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/io_managers/filepath.py" --> "pydantic"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/io_managers/filepath.py" --> "s3fs"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/io_managers/filepath.py" --> "upath"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/io_managers/filepath.py" --> "ol_orchestrate.resources.secrets.vault"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/partitions/edxorg.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/outputs.py" --> "shutil"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/outputs.py" --> "datetime"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/outputs.py" --> "pathlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/outputs.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/outputs.py" --> "pydantic"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/athena_db.py" --> "pyathena"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/athena_db.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/athena_db.py" --> "pyathena.cursor"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/gcp_gcs.py" --> "contextlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/gcp_gcs.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/gcp_gcs.py" --> "google.cloud"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/gcp_gcs.py" --> "google.oauth2"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/gcp_gcs.py" --> "pydantic"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/oauth.py" --> "time"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/oauth.py" --> "collections.abc"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/oauth.py" --> "contextlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/oauth.py" --> "datetime"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/oauth.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/oauth.py" --> "httpx"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/oauth.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/oauth.py" --> "pydantic"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/oauth.py" --> "ol_orchestrate.resources.secrets.vault"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client_factory.py" --> "collections.abc"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client_factory.py" --> "contextlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client_factory.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client_factory.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client_factory.py" --> "pydantic"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client_factory.py" --> "ol_orchestrate.resources.api_client"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client_factory.py" --> "ol_orchestrate.resources.canvas_api"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client_factory.py" --> "ol_orchestrate.resources.learn_api"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client_factory.py" --> "ol_orchestrate.resources.secrets.vault"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/openedx.py" --> "collections.abc"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/openedx.py" --> "contextlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/openedx.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/openedx.py" --> "urllib.parse"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/openedx.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/openedx.py" --> "httpx"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/openedx.py" --> "pydantic"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/openedx.py" --> "ol_orchestrate.resources.oauth"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/openedx.py" --> "ol_orchestrate.resources.secrets.vault"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/bigquery_db.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/bigquery_db.py" --> "google.cloud"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/bigquery_db.py" --> "google.oauth2"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client.py" --> "httpx"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client.py" --> "pydantic"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/github.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/github.py" --> "github"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/github.py" --> "pydantic"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/github.py" --> "ol_orchestrate.resources.secrets.vault"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/learn_api.py" --> "hashlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/learn_api.py" --> "hmac"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/learn_api.py" --> "json"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/learn_api.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/learn_api.py" --> "pydantic"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/learn_api.py" --> "ol_orchestrate.resources.api_client"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/canvas_api.py" --> "collections.abc"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/canvas_api.py" --> "pathlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/canvas_api.py" --> "typing"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/canvas_api.py" --> "pydantic"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/canvas_api.py" --> "ol_orchestrate.resources.api_client"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/postgres_db.py" --> "pandas"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/postgres_db.py" --> "psycopg2"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/postgres_db.py" --> "pyarrow"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/postgres_db.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/secrets/vault.py" --> "json"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/secrets/vault.py" --> "os"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/secrets/vault.py" --> "pathlib"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/secrets/vault.py" --> "boto3"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/secrets/vault.py" --> "hvac"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/secrets/vault.py" --> "dagster"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/secrets/vault.py" --> "pydantic"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/secrets/vault.py" --> "urllib.parse"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/secrets/vault.py" --> "webbrowser"
    "packages/ol-orchestrate-lib/src/ol_orchestrate/resources/secrets/vault.py" --> "http.server"
    "dg_projects/canvas/canvas/definitions.py" --> "typing"
    "dg_projects/canvas/canvas/definitions.py" --> "dagster"
    "dg_projects/canvas/canvas/definitions.py" --> "dagster_aws.s3"
    "dg_projects/canvas/canvas/definitions.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/canvas/canvas/definitions.py" --> "ol_orchestrate.lib.dagster_helpers"
    "dg_projects/canvas/canvas/definitions.py" --> "ol_orchestrate.lib.utils"
    "dg_projects/canvas/canvas/definitions.py" --> "ol_orchestrate.resources.api_client_factory"
    "dg_projects/canvas/canvas/definitions.py" --> "canvas.assets.canvas"
    "dg_projects/canvas/canvas/definitions.py" --> "canvas.sensors.canvas"
    "dg_projects/canvas/canvas/definitions.py" --> "warnings"
    "dg_projects/canvas/canvas/definitions.py" --> "ol_orchestrate.resources.secrets.vault"
    "dg_projects/canvas/canvas/sensors/canvas.py" --> "json"
    "dg_projects/canvas/canvas/sensors/canvas.py" --> "dagster"
    "dg_projects/canvas/canvas/sensors/canvas.py" --> "canvas.lib.canvas"
    "dg_projects/canvas/canvas/lib/canvas.py" --> "json"
    "dg_projects/canvas/canvas/lib/canvas.py" --> "pygsheets"
    "dg_projects/canvas/canvas/lib/canvas.py" --> "dagster"
    "dg_projects/canvas/canvas/lib/canvas.py" --> "google.oauth2"
    "dg_projects/canvas/canvas/assets/canvas.py" --> "json"
    "dg_projects/canvas/canvas/assets/canvas.py" --> "time"
    "dg_projects/canvas/canvas/assets/canvas.py" --> "pathlib"
    "dg_projects/canvas/canvas/assets/canvas.py" --> "httpx"
    "dg_projects/canvas/canvas/assets/canvas.py" --> "dagster"
    "dg_projects/canvas/canvas/assets/canvas.py" --> "ol_orchestrate.lib.automation_policies"
    "dg_projects/canvas/canvas/assets/canvas.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/canvas/canvas/assets/canvas.py" --> "ol_orchestrate.lib.utils"
    "dg_projects/canvas/canvas/resources/api_client_factory.py" --> "collections.abc"
    "dg_projects/canvas/canvas/resources/api_client_factory.py" --> "contextlib"
    "dg_projects/canvas/canvas/resources/api_client_factory.py" --> "typing"
    "dg_projects/canvas/canvas/resources/api_client_factory.py" --> "dagster"
    "dg_projects/canvas/canvas/resources/api_client_factory.py" --> "ol_orchestrate.resources.api_client"
    "dg_projects/canvas/canvas/resources/api_client_factory.py" --> "ol_orchestrate.resources.canvas_api"
    "dg_projects/canvas/canvas/resources/api_client_factory.py" --> "ol_orchestrate.resources.learn_api"
    "dg_projects/canvas/canvas/resources/api_client_factory.py" --> "ol_orchestrate.resources.secrets.vault"
    "dg_projects/canvas/canvas/resources/api_client_factory.py" --> "pydantic"
    "dg_projects/openedx/openedx/definitions.py" --> "os"
    "dg_projects/openedx/openedx/definitions.py" --> "datetime"
    "dg_projects/openedx/openedx/definitions.py" --> "functools"
    "dg_projects/openedx/openedx/definitions.py" --> "typing"
    "dg_projects/openedx/openedx/definitions.py" --> "dagster"
    "dg_projects/openedx/openedx/definitions.py" --> "dagster._core.definitions.definitions_class"
    "dg_projects/openedx/openedx/definitions.py" --> "dagster_aws.s3"
    "dg_projects/openedx/openedx/definitions.py" --> "dagster_duckdb"
    "dg_projects/openedx/openedx/definitions.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/openedx/openedx/definitions.py" --> "ol_orchestrate.lib.dagster_helpers"
    "dg_projects/openedx/openedx/definitions.py" --> "ol_orchestrate.lib.utils"
    "dg_projects/openedx/openedx/definitions.py" --> "ol_orchestrate.resources.api_client_factory"
    "dg_projects/openedx/openedx/definitions.py" --> "ol_orchestrate.resources.secrets.vault"
    "dg_projects/openedx/openedx/definitions.py" --> "openedx.components"
    "dg_projects/openedx/openedx/definitions.py" --> "openedx.jobs.normalize_logs"
    "dg_projects/openedx/openedx/definitions.py" --> "warnings"
    "dg_projects/openedx/openedx/jobs/normalize_logs.py" --> "dagster"
    "dg_projects/openedx/openedx/jobs/normalize_logs.py" --> "openedx.ops.normalize_logs"
    "dg_projects/openedx/openedx/sensors/openedx.py" --> "json"
    "dg_projects/openedx/openedx/sensors/openedx.py" --> "datetime"
    "dg_projects/openedx/openedx/sensors/openedx.py" --> "httpx"
    "dg_projects/openedx/openedx/sensors/openedx.py" --> "dagster"
    "dg_projects/openedx/openedx/sensors/openedx.py" --> "ol_orchestrate.lib.dagster_helpers"
    "dg_projects/openedx/openedx/sensors/openedx.py" --> "ol_orchestrate.resources.openedx"
    "dg_projects/openedx/openedx/sensors/openedx.py" --> "pydantic"
    "dg_projects/openedx/openedx/sensors/openedx.py" --> "openedx.lib.magic_numbers"
    "dg_projects/openedx/openedx/sensors/openedx.py" --> "openedx.partitions.openedx"
    "dg_projects/openedx/openedx/components/__init__.py" --> "openedx.components.openedx_deployment"
    "dg_projects/openedx/openedx/components/openedx_deployment.py" --> "typing"
    "dg_projects/openedx/openedx/components/openedx_deployment.py" --> "dagster"
    "dg_projects/openedx/openedx/components/openedx_deployment.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/openedx/openedx/components/openedx_deployment.py" --> "ol_orchestrate.resources.openedx"
    "dg_projects/openedx/openedx/components/openedx_deployment.py" --> "ol_orchestrate.resources.secrets.vault"
    "dg_projects/openedx/openedx/components/openedx_deployment.py" --> "openedx.assets.openedx"
    "dg_projects/openedx/openedx/components/openedx_deployment.py" --> "openedx.lib.assets_helper"
    "dg_projects/openedx/openedx/components/openedx_deployment.py" --> "openedx.partitions.openedx"
    "dg_projects/openedx/openedx/components/openedx_deployment.py" --> "openedx.sensors.openedx"
    "dg_projects/openedx/openedx/ops/normalize_logs.py" --> "collections.abc"
    "dg_projects/openedx/openedx/ops/normalize_logs.py" --> "pathlib"
    "dg_projects/openedx/openedx/ops/normalize_logs.py" --> "dagster"
    "dg_projects/openedx/openedx/ops/normalize_logs.py" --> "dagster.core.definitions.input"
    "dg_projects/openedx/openedx/ops/normalize_logs.py" --> "pydantic"
    "dg_projects/openedx/openedx/lib/assets_helper.py" --> "functools"
    "dg_projects/openedx/openedx/lib/assets_helper.py" --> "dagster"
    "dg_projects/openedx/openedx/schedules/open_edx.py" --> "dagster"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "hashlib"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "json"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "time"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "datetime"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "pathlib"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "tempfile"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "urllib.parse"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "httpx"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "jsonlines"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "dagster"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "flatten_dict"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "flatten_dict.reducers"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "ol_orchestrate.lib.automation_policies"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "ol_orchestrate.lib.openedx"
    "dg_projects/openedx/openedx/assets/openedx.py" --> "upath"
    "dg_projects/openedx/openedx/partitions/openedx.py" --> "dagster"
    "dg_projects/openedx/openedx/partitions/openedx.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "os"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "typing"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "dagster"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "dagster_aws.s3"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "dagster_aws.s3.resources"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "ol_orchestrate.lib.utils"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "ol_orchestrate.resources.gcp_gcs"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "ol_orchestrate.resources.openedx"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "ol_orchestrate.resources.outputs"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "ol_orchestrate.resources.secrets.vault"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "legacy_openedx.jobs.open_edx"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "legacy_openedx.resources.healthchecks"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "legacy_openedx.resources.mysql_db"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "legacy_openedx.resources.sqlite_db"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "legacy_openedx.schedules.open_edx"
    "dg_projects/legacy_openedx/legacy_openedx/definitions.py" --> "warnings"
    "dg_projects/legacy_openedx/legacy_openedx/jobs/open_edx.py" --> "dagster"
    "dg_projects/legacy_openedx/legacy_openedx/jobs/open_edx.py" --> "ol_orchestrate.lib.hooks"
    "dg_projects/legacy_openedx/legacy_openedx/jobs/open_edx.py" --> "legacy_openedx.ops.open_edx"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "hashlib"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "json"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "subprocess"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "time"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "collections.abc"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "datetime"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "pathlib"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "httpx"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "jsonlines"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "dagster"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "dagster.core.definitions.input"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "flatten_dict"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "flatten_dict.reducers"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "ol_orchestrate.lib.file_rendering"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "ol_orchestrate.lib.openedx"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "pydantic"
    "dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py" --> "pypika"
    "dg_projects/legacy_openedx/legacy_openedx/schedules/open_edx.py" --> "dagster"
    "dg_projects/legacy_openedx/legacy_openedx/resources/mysql_db.py" --> "typing"
    "dg_projects/legacy_openedx/legacy_openedx/resources/mysql_db.py" --> "pymysql"
    "dg_projects/legacy_openedx/legacy_openedx/resources/mysql_db.py" --> "dagster"
    "dg_projects/legacy_openedx/legacy_openedx/resources/mysql_db.py" --> "pymysql.cursors"
    "dg_projects/legacy_openedx/legacy_openedx/resources/sqlite_db.py" --> "sqlite3"
    "dg_projects/legacy_openedx/legacy_openedx/resources/sqlite_db.py" --> "typing"
    "dg_projects/legacy_openedx/legacy_openedx/resources/sqlite_db.py" --> "dagster"
    "dg_projects/legacy_openedx/legacy_openedx/resources/healthchecks.py" --> "urllib.parse"
    "dg_projects/legacy_openedx/legacy_openedx/resources/healthchecks.py" --> "typing"
    "dg_projects/legacy_openedx/legacy_openedx/resources/healthchecks.py" --> "httpx"
    "dg_projects/legacy_openedx/legacy_openedx/resources/healthchecks.py" --> "dagster"
    "dg_projects/legacy_openedx/legacy_openedx/resources/healthchecks.py" --> "pydantic"
    "dg_projects/data_platform/data_platform/definitions.py" --> "typing"
    "dg_projects/data_platform/data_platform/definitions.py" --> "dagster"
    "dg_projects/data_platform/data_platform/definitions.py" --> "dagster_slack"
    "dg_projects/data_platform/data_platform/definitions.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/data_platform/data_platform/definitions.py" --> "ol_orchestrate.lib.utils"
    "dg_projects/data_platform/data_platform/definitions.py" --> "ol_orchestrate.resources.secrets.vault"
    "dg_projects/data_platform/data_platform/definitions.py" --> "warnings"
    "dg_projects/data_platform/data_platform/assets/metadata/databases.py" --> "metadata.ingestion.source.database.trino.metadata"
    "dg_projects/data_platform/data_platform/assets/metadata/databases.py" --> "metadata.workflow.ingestion"
    "dg_projects/data_platform/data_platform/assets/metadata/databases.py" --> "metadata.workflow.metadata"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "os"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "typing"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "dagster"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "dagster_aws.s3"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "ol_orchestrate.io_managers.filepath"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "ol_orchestrate.lib.dagster_helpers"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "ol_orchestrate.lib.utils"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "ol_orchestrate.resources.api_client_factory"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "ol_orchestrate.resources.oauth"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "learning_resources.assets.sloan_api"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "learning_resources.assets.video_shorts"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "learning_resources.sensors.video_shorts"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "warnings"
    "dg_projects/learning_resources/learning_resources/definitions.py" --> "ol_orchestrate.resources.secrets.vault"
    "dg_projects/learning_resources/learning_resources/sensors/video_shorts.py" --> "dagster"
    "dg_projects/learning_resources/learning_resources/sensors/video_shorts.py" --> "learning_resources.assets.video_shorts"
    "dg_projects/learning_resources/learning_resources/lib/video_processing.py" --> "os"
    "dg_projects/learning_resources/learning_resources/lib/video_processing.py" --> "pathlib"
    "dg_projects/learning_resources/learning_resources/lib/video_processing.py" --> "ffmpeg"
    "dg_projects/learning_resources/learning_resources/lib/video_processing.py" --> "dagster"
    "dg_projects/learning_resources/learning_resources/lib/google_sheets.py" --> "hashlib"
    "dg_projects/learning_resources/learning_resources/lib/google_sheets.py" --> "json"
    "dg_projects/learning_resources/learning_resources/lib/google_sheets.py" --> "re"
    "dg_projects/learning_resources/learning_resources/lib/google_sheets.py" --> "datetime"
    "dg_projects/learning_resources/learning_resources/lib/google_sheets.py" --> "typing"
    "dg_projects/learning_resources/learning_resources/lib/google_sheets.py" --> "urllib.parse"
    "dg_projects/learning_resources/learning_resources/lib/google_sheets.py" --> "pygsheets"
    "dg_projects/learning_resources/learning_resources/lib/google_sheets.py" --> "dagster"
    "dg_projects/learning_resources/learning_resources/lib/google_sheets.py" --> "dateutil"
    "dg_projects/learning_resources/learning_resources/lib/google_sheets.py" --> "google.oauth2"
    "dg_projects/learning_resources/learning_resources/assets/sloan_api.py" --> "hashlib"
    "dg_projects/learning_resources/learning_resources/assets/sloan_api.py" --> "json"
    "dg_projects/learning_resources/learning_resources/assets/sloan_api.py" --> "datetime"
    "dg_projects/learning_resources/learning_resources/assets/sloan_api.py" --> "pathlib"
    "dg_projects/learning_resources/learning_resources/assets/sloan_api.py" --> "jsonlines"
    "dg_projects/learning_resources/learning_resources/assets/sloan_api.py" --> "dagster"
    "dg_projects/learning_resources/learning_resources/assets/sloan_api.py" --> "ol_orchestrate.resources.oauth"
    "dg_projects/learning_resources/learning_resources/assets/open_learning_library.py" --> "dagster"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "hashlib"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "json"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "os"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "shutil"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "tempfile"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "collections.abc"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "pathlib"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "typing"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "httpx"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "dagster"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "ol_orchestrate.lib.automation_policies"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "ol_orchestrate.resources.api_client_factory"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "upath"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "learning_resources.lib.contants"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "learning_resources.lib.google_sheets"
    "dg_projects/learning_resources/learning_resources/assets/video_shorts.py" --> "learning_resources.lib.video_processing"
    "dg_projects/b2b_organization/b2b_organization/definitions.py" --> "b2b_organization.assets.data_export"
    "dg_projects/b2b_organization/b2b_organization/definitions.py" --> "b2b_organization.sensors.b2b_organization"
    "dg_projects/b2b_organization/b2b_organization/definitions.py" --> "dagster"
    "dg_projects/b2b_organization/b2b_organization/definitions.py" --> "dagster_aws.s3"
    "dg_projects/b2b_organization/b2b_organization/definitions.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/b2b_organization/b2b_organization/definitions.py" --> "ol_orchestrate.lib.dagster_helpers"
    "dg_projects/b2b_organization/b2b_organization/definitions.py" --> "ol_orchestrate.lib.utils"
    "dg_projects/b2b_organization/b2b_organization/definitions.py" --> "warnings"
    "dg_projects/b2b_organization/b2b_organization/definitions.py" --> "ol_orchestrate.resources.secrets.vault"
    "dg_projects/b2b_organization/b2b_organization/sensors/b2b_organization.py" --> "json"
    "dg_projects/b2b_organization/b2b_organization/sensors/b2b_organization.py" --> "dagster"
    "dg_projects/b2b_organization/b2b_organization/sensors/b2b_organization.py" --> "ol_orchestrate.lib.glue_helper"
    "dg_projects/b2b_organization/b2b_organization/assets/data_export.py" --> "hashlib"
    "dg_projects/b2b_organization/b2b_organization/assets/data_export.py" --> "datetime"
    "dg_projects/b2b_organization/b2b_organization/assets/data_export.py" --> "pathlib"
    "dg_projects/b2b_organization/b2b_organization/assets/data_export.py" --> "b2b_organization.partitions.b2b_organization"
    "dg_projects/b2b_organization/b2b_organization/assets/data_export.py" --> "dagster"
    "dg_projects/b2b_organization/b2b_organization/assets/data_export.py" --> "ol_orchestrate.lib.glue_helper"
    "dg_projects/b2b_organization/b2b_organization/partitions/b2b_organization.py" --> "dagster"
    "dg_projects/student_risk_probability/student_risk_probability/definitions.py" --> "os"
    "dg_projects/student_risk_probability/student_risk_probability/definitions.py" --> "dagster"
    "dg_projects/student_risk_probability/student_risk_probability/definitions.py" --> "dagster_aws.s3"
    "dg_projects/student_risk_probability/student_risk_probability/definitions.py" --> "dagster_iceberg.config"
    "dg_projects/student_risk_probability/student_risk_probability/definitions.py" --> "dagster_iceberg.io_manager.polars"
    "dg_projects/student_risk_probability/student_risk_probability/definitions.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/student_risk_probability/student_risk_probability/definitions.py" --> "ol_orchestrate.lib.dagster_helpers"
    "dg_projects/student_risk_probability/student_risk_probability/definitions.py" --> "ol_orchestrate.lib.utils"
    "dg_projects/student_risk_probability/student_risk_probability/definitions.py" --> "student_risk_probability.assets.risk_probability"
    "dg_projects/student_risk_probability/student_risk_probability/definitions.py" --> "warnings"
    "dg_projects/student_risk_probability/student_risk_probability/definitions.py" --> "ol_orchestrate.resources.secrets.vault"
    "dg_projects/student_risk_probability/student_risk_probability/lib/helper.py" --> "json"
    "dg_projects/student_risk_probability/student_risk_probability/lib/helper.py" --> "pathlib"
    "dg_projects/student_risk_probability/student_risk_probability/lib/helper.py" --> "sklearn.preprocessing"
    "dg_projects/student_risk_probability/student_risk_probability/assets/risk_probability.py" --> "datetime"
    "dg_projects/student_risk_probability/student_risk_probability/assets/risk_probability.py" --> "dagster"
    "dg_projects/student_risk_probability/student_risk_probability/assets/risk_probability.py" --> "ol_orchestrate.lib.automation_policies"
    "dg_projects/student_risk_probability/student_risk_probability/assets/risk_probability.py" --> "ol_orchestrate.lib.glue_helper"
    "dg_projects/student_risk_probability/student_risk_probability/assets/risk_probability.py" --> "student_risk_probability.lib.helper"
    "dg_projects/data_loading/data_loading/definitions.py" --> "pathlib"
    "dg_projects/data_loading/data_loading/definitions.py" --> "dagster"
    "dg_projects/data_loading/data_loading/definitions.py" --> "dagster_dlt"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/defs.py" --> "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/dagster_assets.py"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/dagster_assets.py" --> "dagster"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/dagster_assets.py" --> "dagster_dlt"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/dagster_assets.py" --> "dagster_dlt.translator"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/dagster_assets.py" --> "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/loads.py"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/loads.py" --> "logging"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/loads.py" --> "os"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/loads.py" --> "pathlib"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/loads.py" --> "dlt"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/loads.py" --> "dlt.extract"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/loads.py" --> "dlt.sources"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/loads.py" --> "dlt.sources.filesystem"
    "dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/loads.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/edxorg/edxorg_tests/test_edxorg_lib.py" --> "pytest"
    "dg_projects/edxorg/edxorg_tests/test_edxorg_lib.py" --> "edxorg.lib.edxorg"
    "dg_projects/edxorg/edxorg/definitions.py" --> "os"
    "dg_projects/edxorg/edxorg/definitions.py" --> "functools"
    "dg_projects/edxorg/edxorg/definitions.py" --> "typing"
    "dg_projects/edxorg/edxorg/definitions.py" --> "dagster"
    "dg_projects/edxorg/edxorg/definitions.py" --> "dagster_aws.s3"
    "dg_projects/edxorg/edxorg/definitions.py" --> "ol_orchestrate.io_managers.filepath"
    "dg_projects/edxorg/edxorg/definitions.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/edxorg/edxorg/definitions.py" --> "ol_orchestrate.lib.dagster_helpers"
    "dg_projects/edxorg/edxorg/definitions.py" --> "ol_orchestrate.lib.utils"
    "dg_projects/edxorg/edxorg/definitions.py" --> "ol_orchestrate.resources.api_client_factory"
    "dg_projects/edxorg/edxorg/definitions.py" --> "ol_orchestrate.resources.gcp_gcs"
    "dg_projects/edxorg/edxorg/definitions.py" --> "ol_orchestrate.resources.openedx"
    "dg_projects/edxorg/edxorg/definitions.py" --> "ol_orchestrate.resources.outputs"
    "dg_projects/edxorg/edxorg/definitions.py" --> "ol_orchestrate.resources.secrets.vault"
    "dg_projects/edxorg/edxorg/definitions.py" --> "ol_orchestrate.sensors.object_storage"
    "dg_projects/edxorg/edxorg/definitions.py" --> "edxorg.assets.edxorg_api"
    "dg_projects/edxorg/edxorg/definitions.py" --> "edxorg.assets.edxorg_archive"
    "dg_projects/edxorg/edxorg/definitions.py" --> "edxorg.assets.edxorg_db_table_specs"
    "dg_projects/edxorg/edxorg/definitions.py" --> "edxorg.assets.openedx_course_archives"
    "dg_projects/edxorg/edxorg/definitions.py" --> "edxorg.io_managers.gcs"
    "dg_projects/edxorg/edxorg/definitions.py" --> "edxorg.jobs.edx_gcs_courses"
    "dg_projects/edxorg/edxorg/definitions.py" --> "edxorg.jobs.retrieve_edx_exports"
    "dg_projects/edxorg/edxorg/definitions.py" --> "edxorg.ops.object_storage"
    "dg_projects/edxorg/edxorg/definitions.py" --> "warnings"
    "dg_projects/edxorg/edxorg/jobs/edx_gcs_courses.py" --> "dagster"
    "dg_projects/edxorg/edxorg/jobs/edx_gcs_courses.py" --> "edxorg.ops.edx_gcs_courses"
    "dg_projects/edxorg/edxorg/jobs/retrieve_edx_exports.py" --> "dagster"
    "dg_projects/edxorg/edxorg/jobs/retrieve_edx_exports.py" --> "edxorg.assets.edxorg_archive"
    "dg_projects/edxorg/edxorg/ops/edx_gcs_courses.py" --> "os"
    "dg_projects/edxorg/edxorg/ops/edx_gcs_courses.py" --> "pathlib"
    "dg_projects/edxorg/edxorg/ops/edx_gcs_courses.py" --> "dagster"
    "dg_projects/edxorg/edxorg/ops/edx_gcs_courses.py" --> "dagster.core.definitions.input"
    "dg_projects/edxorg/edxorg/ops/edx_gcs_courses.py" --> "pydantic"
    "dg_projects/edxorg/edxorg/ops/object_storage.py" --> "pathlib"
    "dg_projects/edxorg/edxorg/ops/object_storage.py" --> "dagster"
    "dg_projects/edxorg/edxorg/ops/object_storage.py" --> "pydantic"
    "dg_projects/edxorg/edxorg/lib/edxorg.py" --> "re"
    "dg_projects/edxorg/edxorg/lib/edxorg.py" --> "collections.abc"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "hashlib"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "json"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "re"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "tarfile"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "tempfile"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "datetime"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "pathlib"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "duckdb"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "jsonlines"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "dagster"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "dagster._core.definitions.data_version"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "flatten_dict"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "flatten_dict.reducers"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "google.cloud"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "ol_orchestrate.lib.dagster_helpers"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "ol_orchestrate.lib.openedx"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "ol_orchestrate.partitions.edxorg"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "pydantic"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "upath"
    "dg_projects/edxorg/edxorg/assets/edxorg_archive.py" --> "edxorg.lib.edxorg"
    "dg_projects/edxorg/edxorg/assets/openedx_course_archives.py" --> "hashlib"
    "dg_projects/edxorg/edxorg/assets/openedx_course_archives.py" --> "json"
    "dg_projects/edxorg/edxorg/assets/openedx_course_archives.py" --> "pathlib"
    "dg_projects/edxorg/edxorg/assets/openedx_course_archives.py" --> "tempfile"
    "dg_projects/edxorg/edxorg/assets/openedx_course_archives.py" --> "httpx"
    "dg_projects/edxorg/edxorg/assets/openedx_course_archives.py" --> "jsonlines"
    "dg_projects/edxorg/edxorg/assets/openedx_course_archives.py" --> "dagster"
    "dg_projects/edxorg/edxorg/assets/openedx_course_archives.py" --> "dagster._core.definitions.partitions.utils.multi"
    "dg_projects/edxorg/edxorg/assets/openedx_course_archives.py" --> "ol_orchestrate.lib.automation_policies"
    "dg_projects/edxorg/edxorg/assets/openedx_course_archives.py" --> "ol_orchestrate.lib.openedx"
    "dg_projects/edxorg/edxorg/assets/openedx_course_archives.py" --> "ol_orchestrate.partitions.edxorg"
    "dg_projects/edxorg/edxorg/assets/openedx_course_archives.py" --> "upath"
    "dg_projects/edxorg/edxorg/assets/edxorg_api.py" --> "hashlib"
    "dg_projects/edxorg/edxorg/assets/edxorg_api.py" --> "json"
    "dg_projects/edxorg/edxorg/assets/edxorg_api.py" --> "datetime"
    "dg_projects/edxorg/edxorg/assets/edxorg_api.py" --> "pathlib"
    "dg_projects/edxorg/edxorg/assets/edxorg_api.py" --> "jsonlines"
    "dg_projects/edxorg/edxorg/assets/edxorg_api.py" --> "dagster"
    "dg_projects/edxorg/edxorg/assets/edxorg_api.py" --> "ol_orchestrate.resources.openedx"
    "dg_projects/edxorg/edxorg/assets/edxorg_db_table_specs.py" --> "dagster"
    "dg_projects/edxorg/edxorg/assets/edxorg_db_table_specs.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/edxorg/edxorg/assets/edxorg_db_table_specs.py" --> "ol_orchestrate.partitions.edxorg"
    "dg_projects/edxorg/edxorg/assets/edxorg_db_table_specs.py" --> "edxorg.assets.edxorg_archive"
    "dg_projects/edxorg/edxorg/io_managers/gcs.py" --> "pathlib"
    "dg_projects/edxorg/edxorg/io_managers/gcs.py" --> "dagster"
    "dg_projects/edxorg/edxorg/io_managers/gcs.py" --> "ol_orchestrate.resources.gcp_gcs"
    "dg_projects/edxorg/edxorg/io_managers/gcs.py" --> "upath"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "os"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "re"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "pathlib"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "dagster"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "dagster_airbyte"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "dagster_dbt"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "ol_orchestrate.lib.utils"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "ol_orchestrate.resources.github"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "ol_orchestrate.resources.secrets.vault"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "lakehouse.assets.instructor_onboarding"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "lakehouse.assets.lakehouse.dbt"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "lakehouse.assets.superset"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "lakehouse.resources.airbyte"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "lakehouse.resources.superset_api"
    "dg_projects/lakehouse/lakehouse/definitions.py" --> "warnings"
    "dg_projects/lakehouse/lakehouse/assets/instructor_onboarding.py" --> "datetime"
    "dg_projects/lakehouse/lakehouse/assets/instructor_onboarding.py" --> "io"
    "dg_projects/lakehouse/lakehouse/assets/instructor_onboarding.py" --> "typing"
    "dg_projects/lakehouse/lakehouse/assets/instructor_onboarding.py" --> "dagster"
    "dg_projects/lakehouse/lakehouse/assets/instructor_onboarding.py" --> "dagster_dbt.asset_utils"
    "dg_projects/lakehouse/lakehouse/assets/instructor_onboarding.py" --> "ol_orchestrate.lib.glue_helper"
    "dg_projects/lakehouse/lakehouse/assets/instructor_onboarding.py" --> "ol_orchestrate.resources.github"
    "dg_projects/lakehouse/lakehouse/assets/instructor_onboarding.py" --> "lakehouse.assets.lakehouse.dbt"
    "dg_projects/lakehouse/lakehouse/assets/superset.py" --> "datetime"
    "dg_projects/lakehouse/lakehouse/assets/superset.py" --> "httpx"
    "dg_projects/lakehouse/lakehouse/assets/superset.py" --> "dagster"
    "dg_projects/lakehouse/lakehouse/assets/superset.py" --> "dagster_dbt"
    "dg_projects/lakehouse/lakehouse/assets/superset.py" --> "ol_orchestrate.lib.automation_policies"
    "dg_projects/lakehouse/lakehouse/assets/superset.py" --> "lakehouse.assets.lakehouse.dbt"
    "dg_projects/lakehouse/lakehouse/assets/superset.py" --> "lakehouse.resources.superset_api"
    "dg_projects/lakehouse/lakehouse/assets/lakehouse/dbt.py" --> "os"
    "dg_projects/lakehouse/lakehouse/assets/lakehouse/dbt.py" --> "collections.abc"
    "dg_projects/lakehouse/lakehouse/assets/lakehouse/dbt.py" --> "pathlib"
    "dg_projects/lakehouse/lakehouse/assets/lakehouse/dbt.py" --> "typing"
    "dg_projects/lakehouse/lakehouse/assets/lakehouse/dbt.py" --> "dagster"
    "dg_projects/lakehouse/lakehouse/assets/lakehouse/dbt.py" --> "dagster_dbt"
    "dg_projects/lakehouse/lakehouse/assets/lakehouse/dbt.py" --> "ol_orchestrate.lib.automation_policies"
    "dg_projects/lakehouse/lakehouse/assets/lakehouse/dbt.py" --> "ol_orchestrate.lib.constants"
    "dg_projects/lakehouse/lakehouse/resources/airbyte.py" --> "collections.abc"
    "dg_projects/lakehouse/lakehouse/resources/airbyte.py" --> "typing"
    "dg_projects/lakehouse/lakehouse/resources/airbyte.py" --> "urllib.parse"
    "dg_projects/lakehouse/lakehouse/resources/airbyte.py" --> "dagster._annotations"
    "dg_projects/lakehouse/lakehouse/resources/airbyte.py" --> "dagster_airbyte.resources"
    "dg_projects/lakehouse/lakehouse/resources/airbyte.py" --> "dagster_shared.utils.cached_method"
    "dg_projects/lakehouse/lakehouse/resources/airbyte.py" --> "pydantic.fields"
    "dg_projects/lakehouse/lakehouse/resources/airbyte.py" --> "pydantic.functional_validators"
    "dg_projects/lakehouse/lakehouse/resources/superset_api.py" --> "collections.abc"
    "dg_projects/lakehouse/lakehouse/resources/superset_api.py" --> "contextlib"
    "dg_projects/lakehouse/lakehouse/resources/superset_api.py" --> "datetime"
    "dg_projects/lakehouse/lakehouse/resources/superset_api.py" --> "typing"
    "dg_projects/lakehouse/lakehouse/resources/superset_api.py" --> "dagster"
    "dg_projects/lakehouse/lakehouse/resources/superset_api.py" --> "ol_orchestrate.resources.oauth"
    "dg_projects/lakehouse/lakehouse/resources/superset_api.py" --> "ol_orchestrate.resources.secrets.vault"
    "dg_projects/lakehouse/lakehouse/resources/superset_api.py" --> "pydantic"
    "dg_deployments/reconcile_edxorg_partitions.py" --> "argparse"
    "dg_deployments/reconcile_edxorg_partitions.py" --> "logging"
    "dg_deployments/reconcile_edxorg_partitions.py" --> "re"
    "dg_deployments/reconcile_edxorg_partitions.py" --> "sys"
    "dg_deployments/reconcile_edxorg_partitions.py" --> "urllib.parse"
    "dg_deployments/reconcile_edxorg_partitions.py" --> "boto3"
    "dg_deployments/reconcile_edxorg_partitions.py" --> "dagster"
    "dg_deployments/reconcile_edxorg_partitions.py" --> "dagster._core.events"
    "dg_deployments/reconcile_edxorg_partitions.py" --> "dagster._core.storage.event_log.base"
    "bin/dbt-create-staging-models.py" --> "json"
    "bin/dbt-create-staging-models.py" --> "re"
    "bin/dbt-create-staging-models.py" --> "subprocess"
    "bin/dbt-create-staging-models.py" --> "pathlib"
    "bin/dbt-create-staging-models.py" --> "typing"
    "bin/dbt-create-staging-models.py" --> "yaml"
    "bin/dbt-create-staging-models.py" --> "cyclopts"
    "bin/dbt-local-dev.py" --> "os"
    "bin/dbt-local-dev.py" --> "sys"
    "bin/dbt-local-dev.py" --> "concurrent.futures"
    "bin/dbt-local-dev.py" --> "pathlib"
    "bin/dbt-local-dev.py" --> "threading"
    "bin/dbt-local-dev.py" --> "typing"
    "bin/dbt-local-dev.py" --> "boto3"
    "bin/dbt-local-dev.py" --> "cyclopts"
    "bin/dbt-local-dev.py" --> "duckdb"
    "bin/dbt-local-dev.py" --> "trino"
    "bin/dbt-local-dev.py" --> "trino.auth"
    "bin/dbt-local-dev.py" --> "traceback"
    "bin/dbt-local-dev.py" --> "shutil"
    "bin/dbt-local-dev.py" --> "subprocess"
    "bin/dbt-local-dev.py" --> "json"
    "bin/uv-operations.py" --> "subprocess"
    "bin/uv-operations.py" --> "sys"
    "bin/uv-operations.py" --> "pathlib"
    "bin/uv-operations.py" --> "typing"
    "bin/uv-operations.py" --> "cyclopts"
    "bin/utils/chunk_tracking_logs_by_day.py" --> "sys"
    "bin/utils/chunk_tracking_logs_by_day.py" --> "datetime"
    "bin/utils/chunk_tracking_logs_by_day.py" --> "typing"
    "bin/utils/chunk_tracking_logs_by_day.py" --> "typer"
    "bin/utils/chunk_tracking_logs_by_day.py" --> "boto3"
```

## 2. Module Purpose Index
### `build.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `.pre-commit-config.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 4 changes/30d

### `docker-compose.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_dbt/package-lock.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/packages.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/dbt_project.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/profiles.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/macros/starburst_trino_grant_sql.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/macros/date_parse.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/macros/generate_hash_id.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/macros/cast_date_to_iso8601.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/macros/override_ref.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/macros/json_extract_scalar.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/macros/translate_course_id_to_platform.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/macros/json_query_string.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/macros/generate_base_model_enhanced.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/macros/generate_program_readable_id.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/macros/override_source.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/macros/generate_model_yaml_enhanced.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/macros/transform_code_to_readable_values.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/macros/transform_studentmodule_data.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/macros/apply_deduplication_query.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/macros/date_diff.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/macros/check_cross_column_duplicates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/macros/cast_timestamp_to_iso8601.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/macros/apply_grants_macro_override.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/macros/duckdb_glue_integration.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/macros/extract_course_id.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/macros/cross_db_functions.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_dbt/seeds/_seed_doc.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/dimensional/afact_problem_engagement.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/dimensional/dim_problem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/dimensional/afact_discussion_engagement.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/dimensional/dim_course_content.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/dimensional/tfact_chatbot_events.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/dimensional/afact_course_page_engagement.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/dimensional/dim_discussion_topic.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_dbt/models/dimensional/tfact_video_events.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/dimensional/dim_platform.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/dimensional/tfact_problem_events.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/dimensional/tfact_discussion_events.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/dimensional/afact_video_engagement.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/dimensional/tfact_studentmodule_problems.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/dimensional/dim_video.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/dimensional/_dim__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/dimensional/tfact_course_navigation_events.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/dimensional/dim_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/reporting/mitxonline_video_engagements_w_video_counts.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/reporting/student_risk_probability_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/reporting/_reporting__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 8 changes/30d

### `src/ol_dbt/models/reporting/instructor_module_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/reporting/cheating_detection_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/reporting/chatbot_usage_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/reporting/program_enrollment_with_user_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/reporting/learner_demographics_and_cert_info.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/reporting/combined_enrollments_with_gender_and_date.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/reporting/page_engagement_views_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/reporting/video_engagement_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/reporting/organization_administration_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/reporting/Enrollment_Activity_Counts_Dataset.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/reporting/engagement_problem_completion_raw.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/reporting/problem_engagement_detail_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/reporting/program_summary_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/reporting/_reporting__sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/reporting/mitxonline_course_engagements_daily_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/reporting/combined_video_engagements_counts_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/reporting/learner_engagement_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/reporting/enrollment_detail_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/reporting/engagement_problem_completion_summary.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/learn-ai/stg__learn_ai__app__postgres__chatbots_djangocheckpoint.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/learn-ai/_stg_learn_ai__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/learn-ai/_learn_ai__sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/learn-ai/stg__learn_ai__app__postgres__chatbots_tutorbotoutput.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/learn-ai/stg__learn_ai__app__postgres__chatbots_chatresponserating.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/learn-ai/stg__learn_ai__app__postgres__users_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/learn-ai/stg__learn_ai__app__postgres__chatbots_userchatsession.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/ovs/stg__ovs__studio__postgres__ui_video.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/ovs/_stg_ovs__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/ovs/_ovs__sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/ovs/stg__ovs__studio__postgres__ui_edxendpoint.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/ovs/stg__ovs__studio__postgres__ui_collection.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/ovs/stg__ovs__studio__postgres__ui_collectionedxendpoint.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/ovs/stg__ovs__studio__postgres__ui_encodejob.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/zendesk/stg__zendesk__organization.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/zendesk/stg__zendesk__brand.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/zendesk/stg__zendesk__group.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/zendesk/stg__zendesk__user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/zendesk/stg__zendesk__ticket_comment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/zendesk/stg__zendesk__ticket_field.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/zendesk/_zendesk__sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/zendesk/stg__zendesk__ticket.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/zendesk/_stg_zendesk_models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__courses_course.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__applications_courserun_applicationstep.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__ecommerce_orderaudit.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__applications_applicationstep_submission.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__auth_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__applications_applicationstep.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__ecommerce_wiretransferreceipt.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__django_contenttype.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/_stg_bootcamps__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__profiles_legaladdress.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__courses_courserun.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__ecommerce_order.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__courses_personalprice.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__courses_courseruncertificate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__applications_courserun_application.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/_bootcamps__sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__courses_installment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__profiles_profile.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__ecommerce_line.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__ecommerce_receipt.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/bootcamps/stg__bootcamps__app__postgres__courserunenrollment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__mysql__grades_visibleblocks.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__ecommerce_basket.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__flexiblepricing_flexiblepriceapplication.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__users_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__django_contenttype.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__reversion_revision.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_programrequirement.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__ecommerce_order.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__mysql__grades_subsectiongradeoverride.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_program.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__ecommerce_userdiscount.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__cms_signatorypage.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_courserun.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__ecommerce_basketdiscount.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__mysql__auth_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__cms_wagtail_page.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__openedx_openedxuser.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_courserunenrollment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__users_userprofile.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_programrun.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_coursetopic.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_course.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__ecommerce_line.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__mysql__bulk_email_optout.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__ecommerce_discountproduct.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__cms_instructorpage.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__flexiblepricing_flexiblepricetier.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__api__course_structure.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__ecommerce_basketitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__mysql__courseware_studentmodule.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__b2b_contractpage.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__mysql__grades_subsectiongrade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_department.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__flexiblepricing_currencyexchangerate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__ecommerce_discountredemption.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_blockedcountry.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_programcertificate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__mysql__user_courseaccessrole.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__tracking_logs__user_activity.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__flexiblepricing_countryincomethreshold.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__cms_coursepage_topics.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_courseruncertificate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_course_to_department.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__cms_programpage.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__ecommerce_discount.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__blockcompletion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__courseware_studentmodulehistoryextended.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__ecommerce_transaction.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__cms_coursepage.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/mitxonline/_stg_mitxonline__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_programenrollment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__mysql__edxval_coursevideo.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__openedx__mysql__edxval_video.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__reversion_version.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__users_legaladdress.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__cms_wagtailcore_revision.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__ecommerce_product.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__cms_instructorpagelink.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__courses_courserungrade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/stg__mitxonline__app__postgres__b2b_organizationpage.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxonline/_mitxonline__sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/ocw/_stg_ocw__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/ocw/stg__ocw__studio__postgres__websites_websitecontent.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/ocw/_ocw__sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/ocw/stg__ocw__studio__postgres__websites_website.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/ocw/stg__ocw__studio__postgres__websites_websitestarter.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/_stg_mitxresidential__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__api__course_structure.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__tracking_logs__user_activity.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__courserun_enrollment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__user_courseaccessrole.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__auth_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__auth_userprofile.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__courserun.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__courseware_studentmodulehistoryextended.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__edxval_coursevideo.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__courserun_grade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/_mitxresidential__sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__courseware_studentmodule.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__edxval_video.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxresidential/stg__mitxresidential__openedx__blockcompletion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitlearn/stg__mitlearn__app__postgres__learning_resources_userlist_topics.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitlearn/_mitlearn__sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitlearn/stg__mitlearn__app__postgres__learning_resources_userlist.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitlearn/stg__mitlearn__app__postgres__profiles_profile_topic_interests.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitlearn/stg__mitlearn__app__postgres__learning_resources_search_percolatequery_users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitlearn/stg__mitlearn__app__postgres__users_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitlearn/stg__mitlearn__app__postgres__learning_resources_userlistrelationship.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitlearn/_stg_mitlearn_models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitlearn/stg__mitlearn__app__postgres__learning_resources_search_percolatequery.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitlearn/stg__mitlearn__app__postgres__learning_resources_learningresourcetopic.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitlearn/stg__mitlearn__app__postgres__profiles_profile.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__openedx__mysql__courserun_enrollment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__wagtail_page.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__courses_programenrollment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_couponpaymentversion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__users_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_coupon.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__cms_facultymemberspage.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__cms_coursepage.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__openedx__tracking_logs__user_activity.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/mitxpro/_mitxpro__sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__openedx__mysql__edxval_coursevideo.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_couponredemption.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_company.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__cms_programpage.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_productcouponassignment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__courses_courserun.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__users_profile.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__courses_courserunenrollment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_basket.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__courses_courserungrade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__cms_signatorypage.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_couponbasket.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__courses_programcertificate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__openedx__mysql__courseware_studentmodule.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_receipt.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/_stg_mitxpro__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__users_legaladdress.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__courses_program.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__b2becommerce_b2bcouponaudit.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__django_contenttype.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__openedx__mysql__edxval_video.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_bulkcouponassignment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_couponproduct.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__openedx__mysql__user_courseaccessrole.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__courses_coursetopic.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__emeritus__api__bigquery__user_enrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_basketrunselection.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__cms_certificatepage.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_programrunline.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__b2becommerce_b2bcouponredemption.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__openedx__courseware_studentmodulehistoryextended.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_orderaudit.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_product.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__courses_courseruncertificate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__cms_coursepage_topics.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__courses_programrun.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__b2becommerce_b2borderaudit.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__courses_platform.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__openedx__api__course_structure.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_couponpayment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__openedx__mysql__auth_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__global_alumni__api__bigquery__user_enrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__courses_course.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_couponversion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__cms_coursesinprogrampage.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__b2becommerce_b2breceipt.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__b2becommerce_b2border.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_basketitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_line.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__b2becommerce_b2bcoupon.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_productversion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_linerunselection.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__openedx__blockcompletion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/mitxpro/stg__mitxpro__app__postgres__ecommerce_order.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/salesforce/stg__salesforce__opportunity.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/salesforce/_stg_salesforce__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/salesforce/_salesforce__sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/salesforce/stg__salesforce__opportunitylineitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__courses_electiveset_to_course.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__grades_combinedcoursegrade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/_micromasters__sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__grades_coursecertificate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__ecommerce_order.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__grades_proctoredexamgrade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__ecommerce_line.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__ecommerce_coupon.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__user_program_certificate_override_list.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__grades_programcertificate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__courses_program.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__exams_examrun.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__ecommerce_usercoupon.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__ecommerce_redeemedcoupon.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__courses_course.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__auth_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__courses_courserun.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__dashboard_programenrollment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__profiles_education.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__django_contenttype.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__ecommerce_couponinvoice.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__profiles_employment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__grades_courserungrade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__courses_electiveset.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/_stg_micromasters__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__auth_usersocialauth.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__ecommerce_receipt.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/micromasters/stg__micromasters__app__postgres__profiles_profile.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__programs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/_stg__edxorg__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__api__courserun.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__tracking_logs__user_activity.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__courseware_studentmodule.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__program_courses.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/_edxorg_sources.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__user_courseaccessrole.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__course_policy.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__program_entitlement.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__course_structure.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__courserun_grade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__bigquery__mitx_user_info_combo.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__courserun.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__course_video.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__courserun_enrollment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__bigquery__mitx_person_course.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__courserun_certificate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__bigquery__mitx_user_email_opt_in.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__api__course.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__user_profile.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__bigquery__mitx_courserun.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__program_learner_report.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/staging/edxorg/stg__edxorg__s3__course_certificate_signatory.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__assessment_studenttrainingworkflow.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__django_comment_client_role_users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__course_groups_cohortmembership.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__user_id_map.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__student_courseenrollment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__student_languageproficiency.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__teams.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__assessment_assessmentpart.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__submissions_studentitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__submissions_scoresummary.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__submissions_score.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__grades_persistentsubsectiongrade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__assessment_assessmentfeedback.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__auth_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__teams_membership.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__workflow_assessmentworkflow.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__auth_userprofile.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__assessment_assessmentfeedback_options.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__assessment_studenttrainingworkflowitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__assessment_peerworkflowitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__bigquery__email_opt_in.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__assessment_peerworkflow.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__grades_persistentcoursegrade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__assessment_assessment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__student_anonymoususerid.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__workflow_assessmentworkflowstep.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/_irx_mitxonline__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__assessment_assessmentfeedback_assessments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__student_courseaccessrole.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__certificates_generatedcertificate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__submissions_submission.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__assessment_assessmentfeedbackoption.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__user_api_usercoursetag.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitxonline/irx__mitxonline__openedx__mysql__credit_crediteligibility.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__assessment_peerworkflowitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__grades_persistentsubsectiongrade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__credit_crediteligibility.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__certificates_generatedcertificate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__student_anonymoususerid.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__assessment_assessmentfeedback_assessments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__student_courseaccessrole.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__assessment_assessment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__assessment_peerworkflow.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__assessment_studenttrainingworkflow.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__auth_userprofile.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__submissions_studentitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__teams_membership.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__submissions_scoresummary.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__user_id_map.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/_irx_xpro__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__student_languageproficiency.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__user_api_usercoursetag.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__workflow_assessmentworkflowstep.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__teams.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__django_comment_client_role_users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__assessment_assessmentfeedbackoption.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__course_groups_cohortmembership.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__student_courseenrollment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__submissions_submission.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__assessment_assessmentfeedback.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__assessment_assessmentpart.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__workflow_assessmentworkflow.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__bigquery__email_opt_in.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__auth_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__assessment_studenttrainingworkflowitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__assessment_assessmentfeedback_options.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__submissions_score.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/xpro/irx__xpro__openedx__mysql__grades_persistentcoursegrade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__workflow_assessmentworkflow.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__submissions_submission.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__workflow_assessmentworkflowstep.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_assessmentfeedback.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__credit_crediteligibility.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_peerworkflow.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_assessment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_rubric.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__teams_membership.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__bigquery__email_opt_in.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__teams.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_peerworkflowitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_aitrainingworkflow_training_examples.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__courseware_studentmodulehistoryextended.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_criterion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_trainingexample_options_selected.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/_irx_mitx__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__student_courseenrollment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__auth_user.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__student_languageproficiency.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__user_api_usercoursetag.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__django_comment_client_role_users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__auth_userprofile.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__course_groups_cohortmembership.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_aiclassifier.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_studenttrainingworkflow.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_aigradingworkflow.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__submissions_scoresummary.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__student_anonymoususerid.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__grades_persistentsubsectiongrade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_assessmentfeedback_options.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__certificates_generatedcertificate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__grades_persistentcoursegrade.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_assessmentfeedbackoption.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__submissions_studentitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_aitrainingworkflow.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_criterionoption.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_trainingexample.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__user_id_map.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__submissions_score.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_aiclassifierset.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_studenttrainingworkflowitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_assessmentpart.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__student_courseaccessrole.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/external/irx/mitx/irx__mitx__openedx__mysql__assessment_assessmentfeedback_assessments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/mitxonline/marts__mitxonline_course_engagements_daily.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/marts/mitxonline/marts__mitxonline_problem_submissions.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/mitxonline/marts__mitxonline_video_engagements.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/marts/mitxonline/marts__mitxonline_user_profiles.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/mitxonline/marts__mitxonline_course_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/mitxonline/marts__mitxonline_discussions.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/mitxonline/marts__mitxonline_course_enrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/mitxonline/_marts__mitxonline__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/marts/mitxonline/marts__mitxonline_problem_summary.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/ocw/_marts__ocw__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/ocw/marts__ocw_courses.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/marts/mitxpro/marts__mitxpro_ecommerce_productlist.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/marts/mitxpro/marts__mitxpro_all_coupons.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/mitxpro/_marts__mitxpro__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/micromasters/marts__micromasters_program_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/micromasters/_marts_micromasters__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/micromasters/marts__micromasters_dedp_exam_grades.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/micromasters/marts__micromasters_summary.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/micromasters/marts__micromasters_course_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/micromasters/marts__micromasters_summary_timeseries.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/marts/combined/marts__combined__orders.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/combined/marts__combined_video_engagements.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/combined/marts__combined_course_engagements.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/marts/combined/marts__combined__users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/combined/marts__combined_discounts.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/combined/marts__combined_program_enrollment_detail.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/combined/marts__combined_total_course_engagements.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/combined/marts__combined__products.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/combined/_marts__combined__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/combined/marts__combined_problem_submissions.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/combined/marts__combined_coursesinprogram.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/marts/combined/marts__combined_course_enrollment_detail.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/migration/edxorg_to_mitxonline_users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/migration/_migration__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/migration/edxorg_to_mitxonline_course_runs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/migration/edxorg_to_mitxonline_enrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 3 changes/30d

### `src/ol_dbt/models/intermediate/learn-ai/int__learn_ai__tutorbot.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/learn-ai/int__learn_ai__chatbot.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/learn-ai/_learn_ai__models.yml.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/ovs/_int_ovs__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/ovs/int__ovs__videos.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/zendesk/int__zendesk__ticket.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/zendesk/int__zendesk__ticket_comment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/zendesk/_zendesk_models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/bootcamps/int__bootcamps__users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/bootcamps/int__bootcamps__ecommerce_wiretransferreceipt.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/bootcamps/int__bootcamps__applications.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/bootcamps/int__bootcamps__ecommerce_order.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/bootcamps/int__bootcamps__courserun_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/bootcamps/int__bootcamps__courserunenrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/bootcamps/_int_bootcamps__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/bootcamps/int__bootcamps__ecommerce_receipt.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/bootcamps/int__bootcamps__course_runs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/bootcamps/int__bootcamps__courses.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__ecommerce_discountredemption.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__flexiblepricing_flexiblepriceapplication.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__courses.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__flexiblepricing_flexiblepricetier.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__user_courseactivities.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__courserunenrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__courserunenrollments_with_programs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__course_runs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__ecommerce_basket.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__courserun_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__ecommerce_product.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__courserun_subsection_grades.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__flexiblepricing_currencyexchangerate.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__course_to_topics.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__user_courseactivity_discussion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__proctored_exam_grades.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__program_requirements.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__user_courseactivity_problemsubmitted.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__user_courseactivities_daily.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__program_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__ecommerce_userdiscount.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__course_to_departments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__ecommerce_discountproduct.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__ecommerce_discount.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__bulk_email_optin.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__programs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__program_instructors.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__ecommerce_order.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__courserun_grades.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__flexiblepricing_countryincomethreshold.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__course_structure.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__course_instructors.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__user_courseactivity_problemcheck.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__ecommerce_transaction.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__b2b_contract_to_courseruns.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__course_blockedcountries.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__user_courseactivity_video.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__ecommerce_basketitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__user_courseactivity_showanswer.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/_int_mitxonline__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__courserun_videos.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__ecommerce_basketdiscount.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/int__mitxonline__programenrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/subqueries/__mitxonline_good_economics_for_hard_times_program.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxonline/subqueries/__int_mitxonline_subqueries__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/ocw/int__ocw__courses.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/ocw/_int_ocw__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/ocw/int__ocw__course_departments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/ocw/int__ocw__course_instructors.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/ocw/int__ocw__course_topics.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/ocw/int__ocw__resources.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__course_structure.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/_int_mitxresidential__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__user_courseactivities_daily.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__user_courseactivity_discussion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__user_courseactivity_problemsubmitted.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__user_courseactivity_showanswer.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__user_courseactivity_video.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__courserun_grades.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__user_courseactivity_problemcheck.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__courserun_enrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__user_courseactivities.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__courserun_videos.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__courseruns.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxresidential/int__mitxresidential__users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitx/int__mitx__courserun_enrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitx/int__mitx__programs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitx/int__mitx__program_requirements.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitx/int__mitx__users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_dbt/models/intermediate/mitx/int__mitx__courserun_grades.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitx/_int_mitx__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_dbt/models/intermediate/mitx/int__mitx__program_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitx/int__mitx__courses.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitx/int__mitx__courserun_enrollments_with_programs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitx/int__mitx__courserun_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__course_runs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_linerunselection.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_coupon.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__user_courseactivity_video.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__course_structure.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__programsfaculty.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__user_courseactivity_discussion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/_int_mitxpro__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_product.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__coursesfaculty.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__coursesinprogram.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_couponredemption.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_allcoupons.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__program_runs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__coursetopic.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__courses.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__program_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__b2becommerce_b2border.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_order.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__courserunenrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__user_courseactivity_showanswer.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_productversion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__courses_to_topics.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__user_courseactivities.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__programs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_allorders.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_basketitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__programenrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__platforms.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_productcouponassignment.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__courserun_grades.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__user_courseactivities_daily.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_basket.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__courserun_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_basketrunselection.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__user_courseactivity_problemsubmitted.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_couponversion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_line.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_company.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_couponpaymentversion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_receipt.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__b2becommerce_b2bcoupon.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__ecommerce_couponproduct.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__user_courseactivity_problemcheck.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__courserun_videos.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__b2becommerce_b2bcouponredemption.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/mitxpro/int__mitxpro__b2becommerce_b2breceipt.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/salesforce/int__salesforce__opportunity.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/salesforce/int__salesforce__opportunitylineitem.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/salesforce/_int_salesforce__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/int__micromasters__course_enrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/int__micromasters__course_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/int__micromasters__users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/_int_micromasters__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/int__micromasters__dedp_proctored_exam_grades.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/int__micromasters__course_grades.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/int__micromasters__program_requirements.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/int__micromasters__program_enrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/int__micromasters__program_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/int__micromasters__programs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/int__micromasters__orders.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/subqueries/__micromasters_course_grades_dedp_from_mitxonline.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/subqueries/__micromasters_course_grades_dedp_from_micromasters.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/subqueries/__micromasters_program_certificates_non_dedp.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/subqueries/__micromasters_course_grades_non_dedp_from_edxorg.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/subqueries/__micromasters_program_certificates_dedp_from_micromasters.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/subqueries/__micromasters_program_certificates_dedp_from_mitxonline.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/subqueries/__micromasters_course_certificates_dedp_from_micromasters.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/subqueries/__micromasters_course_certificates_dedp_from_mitxonline.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/subqueries/__micromasters_course_certificates_non_dedp_from_edxorg.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/subqueries/__int_micromasters_subqueries__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/micromasters/subqueries/__micromasters__users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_courseruns.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_courserun_enrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_user_courseactivity_video.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_user_courseactivities_daily.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_user_courseactivities.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_product.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_program_courses.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_program_enrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_user_courseactivity_problemsubmitted.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_user_courseactivity_discussion.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_program_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_courserun_grades.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/_int_edxorg__models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_user_activity.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_course_structure.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_courserun_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/edxorg/int__edxorg__mitx_user_courseactivity_problemcheck.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/combined/int__combined__users.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/combined/int__combined__course_videos.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_dbt/models/intermediate/combined/_combined_models.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/combined/int__combined__course_structure.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/combined/int__combined__course_runs.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_dbt/models/intermediate/combined/int__combined__courserun_enrollments.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/combined/int__combined__user_course_roles.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_dbt/models/intermediate/combined/int__combined__courserun_certificates.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/sync_config.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/metadata.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/databases/Trino.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/databases/Superset_Metadata_DB.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/dashboards/Learner_Demographic_and_Course_Data_be0ba018-dff2-42a5-a12a-8215ff5bd75a.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/dashboards/Enrollment_Detail_by_Learner_da9e03d3-e1bb-45b8-981f-208deca90e7a.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/dashboards/Coupons_06b246fd-65db-440b-9a98-183ca37a2660.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/dashboards/Organization_Administration_Dashboard_e71b9aea-9503-4bed-be3d-232fb5c3e67e.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/dashboards/Products_20e6140c-d3dd-4d23-be26-c1642d73b288.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/dashboards/Distribution_of_Number_of_Videos_Watched_b54af54e-1da9-4835-a65b-3ba03c6b3e57.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/dashboards/Orders_7b9f141d-14d2-40c6-aa01-fef8a0375ce8.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/dashboards/MITx_and_xPro_Products_be482a19-1c1e-4f4d-87be-aad2b50d54bf.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/dashboards/Course_AI_Chatbot_b6b79d2a-4a21-4454-a4df-d12549e9bd7d.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/dashboards/Instructor_Level_Administration_Dashboard_5495ac4d-bac4-429c-8a7b-070f27f34904.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/dashboards/Course_Enrollment_Activity_101c4123-af4c-492b-a087-246d06569a1d.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/dashboards/Course_Engagement_2311d08c-60b3-4b6d-87d2-b417dccb64f7.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/dashboards/Combined_Learners_Search_68d00b7a-8f6b-4f18-b738-9ecc0a9dd294.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/dashboards/Suspicious_Behavior_Report_1e2883d9-d122-4af6-aa33-43a0f0ac2c3b.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/dashboards/Learner_Engagement_ca0fe164-7452-4e90-be12-e0c793f0ac05.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/dashboards/Learn_User_Profile_47b963a4-74a2-472c-9a3b-a9986be146e9.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/dashboards/Program_Enrollment_and_Credential_203bbba1-adb8-4f95-8951-7e958f2d6260.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/dashboards/xPro_Reference_Dashboard_45b6c06a-1e2d-43d3-8b98-a95b82b375d5.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined_course_enrollment_detail_836dd1f0-3e2e-45a9-a721-62a471a43de8.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/raw__learn_ai__app__postgres__ai_chatbots_tutorbotoutput_757ec475-ddad-436a-9a7c-3da657b69a9b.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/Data_Detail_Discuss_5bab95fd-d465-44f3-bed8-40c559958fc4.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/page_engagement_views_c3182341-5246-40c2-8f04-885369c38093.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/int__ocw__resources_8bb67686-3d31-4418-bda9-87fdeb25b665.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined_discounts_a5df905c-0480-4227-b234-1a1064672b32.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/program_summary_report_0d77ec2b-8489-47f8-b0c3-3abde0b1b8f3.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/instructor_module_report_8c2b6f11-28f8-4353-8e43-6c53ea6b1d91.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/Data_Detail_Nav_32e283f5-fc02-403a-9c92-b8286352cdba.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined_video_engagements_w_video_counts_42f063d3-3c06-4834-b993-777fdbc6dea7.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined_problem_submissions_70adedf0-bc96-4922-a720-d579f2b4065c.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/learner_engagement_report_4752cd11-a13e-4a8e-be31-4d9227b07ca2.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined_coursesinprogram_f841a3e6-d864-4499-94dd-6ceafe8ac74f.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined__orders_02e97623-3edd-4d3a-acbe-119e889a043a.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/afact_discussion_engagement_956060cb-b34d-4042-a1c6-ea1c4b4eca9f.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__mitxonline_problem_submissions_9e61277c-345a-4958-947b-2436eb4abf15.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/datasets/Trino/tfact_discussion_events_368125b7-c1c9-4f72-a360-9547536b4945.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/engagement_problem_completion_raw_4490876f-d440-4df8-8e42-a467bac0821f.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__ocw_courses_5e9078ef-d0a9-4db7-9635-75fb9a2321de.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/datasets/Trino/Data_Detail_Problems_dc0886e8-1861-4bd9-a694-25a063adcf83.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__mitxpro_all_coupons_50998478-4b82-451d-82ed-5ea60fd48b05.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/student_risk_probability_report_ca346322-251e-455b-a2cc-b11976e69ce5.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined__products_d53b0a52-4450-4d2a-8ce4-143b9f9e327b.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/Learner_Demographics_And_Cert_Info_232090f5-bb02-4327-9067-2ae49b64074b.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__mitxonline_problem_summary_dc51305d-a55b-42b6-84d2-a412f96ac900.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/dim_course_content_466da6d4-e870-4afd-866a-4c95044400b6.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__micromasters_dedp_exam_grades_b22c2064-0dd4-4e1a-9cdf-a74a9302f39d.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/dim_platform_0e455533-8a1c-4dd8-a894-cff7a228889c.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__mitxonline_discussions_75610c3a-34e1-47f7-ab74-f350afcd9f66.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/video_engagements_report_4168432c-fd99-4ef6-bf8c-14acd0cb9b33.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/int__learn_ai__tutorbot_4fe652f8-e672-4e71-89da-fb964985847b.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/tfact_studentmodule_problems_c6006f03-b7e0-4f47-b275-dd3d8f022500.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/chatbot_usage_report_b1f7c663-9faf-4c95-bdeb-d786a3f4cd3c.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/engagement_problem_summary_test1_d763f86e-5c1b-4996-9b35-f8cb13947f11.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/tfact_course_navigation_events_2189d254-14fd-4b38-85a8-6af918546dd0.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__micromasters_program_certificates_e531ebf4-6189-4c02-9729-6c6ef18b81ef.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/datasets/Trino/dim_user_7f46cdba-1bf0-4f10-9606-a41b77b9e77c.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined__orders_2f64a0b1-a1d4-4dec-95c3-7978296a3555.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/tfact_video_events_2a608e5d-c828-4457-83c2-0912a1534430.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__mitxonline_course_engagements_daily_e7330108-bdfa-4ff0-8ca3-084d7e8cbda8.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__mitxonline_video_engagements_2eadf96c-5d64-4ad2-bd41-c8e41c316e65.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__mitxonline_user_profiles_000eb064-5511-455c-bbdb-33ffe0f0af68.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/organization_administration_report_4a71d2a9-c1b2-44e7-8c8d-a4a336779ab8.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/dim_problem_23a7a643-e426-42ea-9759-c05f7a524e22.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/int__learn_ai__chatbot_f1ec896e-86d4-451a-84cc-841d234e70a6.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/afact_course_page_engagement_68c544d7-726d-495a-bf87-81255b2e8604.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/tfact_problem_events_5fc7287d-1bf8-4fc2-b008-c80f84e3a6d9.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/combined_enrollments_with_gender_and_date_f3e517dd-4012-441e-8dfe-edaef1318000.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__mitxonline_course_certificates_45f0412f-0d34-4d04-a3ff-e595a3bada19.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__mitxpro_ecommerce_productlist_dc5b25f5-cf3a-41b4-9b15-4b58532da463.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined_course_engagements_f221af29-5df4-4025-8355-401041f94835.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined__users_5f006731-f052-4586-88f2-ad1b3c904ca9.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/combined_learners_enrollment_detail_b579034e-2b79-4d3a-ba84-94c9fcfa0cc5.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined_total_course_engagements_edf21d6a-1f41-4812-a1aa-3fcbc8358466.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__micromasters_course_certificates_70bc54c5-1073-4bdc-922b-76f6eff82ae3.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/datasets/Trino/engagment_problem_test1_b9e94ba2-f399-4210-b042-b8aaa4039f58.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/dim_video_135f82ef-b81b-4f5b-8f82-ed299675e618.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/datasets/Trino/mitxonline_video_engagements_w_video_counts_0514985b-ff21-490b-a34e-25ae356da7e9.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined_video_engagements_a7af739c-62dd-4be0-a46f-5771a7e0c466.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/Data_Detail_Video_3967f60c-2d80-41ad-8245-67dbf555bd82.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/engagement_problem_summary_test2_a2198d6f-df2d-492c-b30b-9e3279466bdb.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/afact_video_engagement_7ac81107-1993-427e-b2ed-b8835b1ce58d.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/datasets/Trino/dim_discussion_topic_62e16051-719e-48d6-b256-e40600ec3764.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/Enrollment_Activity_Counts_Dataset_a9301703-0ac1-4eb7-a409-f65da5d8cba1.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/Program_Enrollment_with_user_cc496da8-03f6-43ea-9b6c-900ba695e4b6.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/learner_demographics_and_cert_info_b6b616b4-f695-4bf6-ad11-ea234f86e6e0.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/cheating_detection_report_65bdc57c-00f9-42d0-bd37-d4363532fd81.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/tfact_chatbot_events_83431f55-aaaf-4fe5-aa60-a3502e1442f9.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__mitxonline_course_enrollments_811f8301-4bea-461e-8359-d354af75c4b1.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__mitxonline_video_engagements_w_video_counts_bf17ec0d-2a0a-4f97-ab5b-ae2df862d4b5.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/engagement_problem_completion_summary_6e06ce54-f2a2-4df1-9bcb-5c556f42d247.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__micromasters_summary_8e87819b-5332-4cb5-8cda-02f7b8502446.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__combined_program_enrollment_detail_0983d23f-8182-482a-9f0f-b32d69984efc.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/marts__micromasters_summary_timeseries_14b2945b-3ad0-4a39-9b10-9362c3b54022.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/datasets/Trino/video_engagement_report_232bb992-50ba-4dfb-bb9f-bfb403a3517a.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/enrollment_detail_report_01f179b6-cb75-465f-8ceb-0525c24fa223.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Trino/afact_problem_engagement_37bb25c7-421f-432a-bc42-5cc10a129746.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/datasets/Superset_Metadata_DB/tables_3b10e411-e497-4e8c-8132-08f673e8d72d.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Latest_Activity_Date_f9e19a79-18f9-4a54-ad7a-85c5f0b5b801.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Order_Dashboard_Last_Updated_0ef1c6be-600c-4802-aa04-33f1b6dd9e9b.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Percentage_of_Video_Played_9bb14cc1-d787-4f47-b6d3-86adb3d4ec47.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Problem_Engagement_by_Section_ec8dc53c-60d0-4bd1-9913-4388b41ca53d.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Latest_Dashboard_Activity_Recorded_Date_582d2109-e097-4acc-a39e-f19932afa98d.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/MITxOnline_Enrollment_Demographics_by_Gender_57721cfb-3413-484d-abfa-cb1be38daafe.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Learn_User_Profile_2e3e900a-3782-4738-80fe-0d60802d4461.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Content_Engagement_-_Weekly_fb5f7dd7-f56e-44f4-97f6-ed0c3804382f.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 3 changes/30d

### `src/ol_superset/assets/charts/Video_Engagement_per_Section_52f9966c-2de9-41fd-b29a-ccd1781696cb.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/MITx_Enrollments_89862956-6021-420f-b56e-cd73e6680a78.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Micromasters_Users_d7f0a985-f4b0-4643-9832-88d106aa087c.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Enrollment_Demographics_by_Gender_e9c00f99-deb8-4a1f-99d4-d4e592b7c8db.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Course_AI_Chatbot_Table_Metadata_3ac40124-8856-4823-8b81-4be13975e103.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Problem_Engagement_by_Courserun_1e30a45b-d97d-4f44-ac2c-1d9de9e05bc1.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Problem_Results_8247b593-276a-4e86-96e1-62869ec2c59b.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Data_Detail_Problems_5e8a4f03-1504-4f8b-9990-de300d73ff93.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Data_Detail_Discussion_39c99c2d-1290-4d37-9b0f-eef559172947.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Coupon_Discount_Summary_2e066386-dc90-48e3-859b-2b665b3cb257.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Coupon_Dashboard_Last_Updated_a468ef05-11af-4a02-b61c-f928f36f17fb.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Learners_Enrolled_37d70f20-6dcc-4237-921b-521dc43425a7.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 3 changes/30d

### `src/ol_superset/assets/charts/Video_Engagement_By_Courserun_93c228c1-4ad3-4268-830a-d99befebaaee.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Counts_by_course_run_5670e704-3dc6-4b28-a12c-20d4faabcd46.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Learner_Video_Engagement_3c5fdc59-85d7-484b-9fdf-170336c8a4c0.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Video_Engagement_per_Section_f9c49065-6eb1-4c47-ab2b-a03654cdcbc4.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Problem_Submission_Results_d0bcae8d-1f6a-415b-a3af-52323e8eeee2.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Course_AI_Chatbot_Deprecated_148f6894-7e0b-4750-aef4-501db89a4543.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Chatbot_Usage_By_Course_Section_and_Subsection_9ad6f248-c9cd-42bd-9285-5dbe6d30d5c3.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/MITxOnline_Enrollment_Geography_de62ba2c-c4c8-4973-99eb-f1a7bcbe16e6.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Tutorbot_with_filter_bc2f4ec2-0532-4a55-8482-e12ecae7e7de.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/course_user_mapping_08141743-0bc0-4a79-a3b4-39d34d221742.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Order_detail_fb906f1f-c07f-472f-9387-ad02f73cae55.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Program_Enrollment_and_Certificate_d9047161-f8d8-4af2-adb0-283c74b639f2.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/DEDP_Learner_Grades_by_Course_1ec63597-fd4e-4e55-b5e0-aa09309f3cce.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Organization_Administration_Detail_Report_caf22ae5-3cde-427d-8627-cd55c5febd87.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Record_Count_1e441a91-5d1a-4f4f-9bf8-90fcc9d12988.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Order_detail_d58f3f14-9d41-4e6e-8245-d194d15aac01.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Course_Run_Metadata_c6e47f3c-aeb2-4e25-bf43-e9bd3f068127.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Data_Detail_Video_8cd66663-f93f-4751-be11-14c5d4c28ed5.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Course_AI_Chatbot_92488983-505d-4642-a76d-6d5225275577.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Learner_Course_Engagement_6df62a4b-28e2-4d78-9e22-e3dfb56fd96a.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Daily_Learner_Enrollment-_All_Courses_65762bf7-1c08-4abb-ad17-e569311a67d0.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Course_Run_Metadata_01f0a8ee-45f0-40ef-a96e-250a40aebf10.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Video_Engagement_By_Section_f37fc707-aeb4-4731-b0d5-634b47a57eae.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Problem_Engagement_By_Subsection_bec01f31-3a3e-4bba-a280-9160e00e2b87.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/OCW_Resources_cd72f611-dac4-45a0-99ca-8b3c9e260597.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/MITxOnline_Content_Engagement_3267dca3-cc86-47f9-ae47-f338d1af4071.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Suspicious_Behavior_Report_3acf6da0-1add-486f-9e70-884a1bb306f9.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/MITxOnline_Engagement_Totals_c5db1f81-e676-4565-a158-ef68de95dfb1.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Content_Engagement_984bd054-65c0-4f76-b7ee-7fb0608ccd6e.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Organization_Administration_Problems_Tried_fe95c76a-352c-41a4-8e41-9252b68421ea.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 3 changes/30d

### `src/ol_superset/assets/charts/MITxOnline_Content_Engagement_836bab76-b440-4f9e-935d-54817dd3dc25.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Course_to_Program_Reference_5a5e1d10-7bbe-4329-891d-029255d6efe0.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/MITxOnline_Learner_Enrollments-_All_Course_ab3dd918-2308-446f-8d81-f89ac4f342cf.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/MITxOnline_Enrollment_Activity_6fd11c69-4110-465f-8ed6-bfcdbe59b8b4.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Coupon_Summary_ae86fc71-d19e-4e6a-80b6-c68ca638b536.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/MITxOnline_Learner_Enrollments-_course-v1MITxT14.100x3T2023_3b710d6c-6265-43ce-82ef-4c57409b8fda.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Student_Level_Course_Grades_1a78ac33-5081-4fb7-9593-89b1aed6daad.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Student_Level-_Course_Grades_1ffe71c4-0732-4e17-a343-67ef3dd28f3d.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Organization_Administration_Videos_Watched_5d97d317-30ee-46df-882b-0451efe2ac1d.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Video_Engagement_per_Section_ac95bf65-b2ea-4e6a-9fdf-8fdff4758f5e.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Page_Engagement_By_Courserun_008cffdc-9283-4daf-8507-746491486bd4.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/DEDP_3T2023_certificates_by_course_runs_092c45b2-f7d3-4c7e-b4aa-99890c07746a.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Percent_Content_Engagement_822d24da-190a-49ea-9253-8a26637a89c8.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Products_36ade680-7ae9-4d35-89b0-a46235139418.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Data_Detail_Navigation_cf8305f6-fe5d-4791-8185-3051b76f4738.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Learner_Demographic_Including_Income_and_Course_Data_11b1455f-25f1-45aa-8358-b8449013bb24.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Videos_Rewatched_397698ec-916f-46e4-bd4c-cae296806b10.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/MITxOnline_Earned_Certificate_d953e953-a5d6-4e48-af54-5b0e033a401c.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/MITx_Online_Course_Run_Metadata_c46d73a1-16c3-450b-a43d-63383fad7be2.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Video_Engagement_By_Section_and_Subsection_738b9337-2477-4f49-95e6-4201a90c6f28.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Latest_Course_Activity_Date_5f95a268-4339-4d73-b8d8-d082ca53b28d.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Distribution_of_Number_of_Videos_Watched_9bdb6168-d5c9-4651-af36-556e29f3b5db.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Product_Dashboard_Last_Updated_6733b1cd-bb65-44e6-959e-ca21305807e7.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Enrollment_Detail_1cf394ec-8561-4b0d-9d9b-f394a6029b33.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Chatbot_data_for_Saliha_8fb96290-8e60-48c0-93c1-bf0f5b3c1823.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Engagement_By_Section_And_Subsection_b503879e-45e5-43aa-90eb-de7044e442b4.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Page_Engagement_By_Subsection_f41fcf95-edc7-4dcd-bbe8-54406e775b37.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Combined_Learners_0cf1e9cf-4645-4397-ac5a-d9a7b75d0ad5.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Order_detail_aff18084-6079-49b3-9604-d68c8a315296.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/OCW_Resources_c697af06-b2be-4653-9680-e9af0c822e38.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Video_Engagement_By_Subsection_8146a868-1014-48d3-9e0d-8223de1ae1a9.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Enrollment_Demographics_by_Education_aa6bdf8d-b5be-4142-a3fc-df4f0032189e.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Page_Engagement_By_Section_b4d14d82-feb2-49bf-847f-2cb8b2c11d20.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Tutorbot_c1d81d88-a705-4c90-a816-f488f7cbbaea.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/of_Watches_By_Video_cb328531-f862-467c-b073-4a2cec5dfbe2.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/dim_user_last_updated_1e1419f1-f836-43de-964e-6ea9d9521645.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Latest_Fulfilled_Order_Date_686fd4b2-e9f4-401b-bd85-b03f8b8824fd.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Combined_Learners_f2f10600-7302-4887-af04-d0aad29333ea.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Daily_Learner_Enrollment_Graph_e197cb29-a6e4-4880-a28f-35a959c77ed8.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Learner_Page_Engagement_9bd2269c-fd5c-463d-b63e-14fa63e90a55.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Organization_Administration_Chatbot_Use_a8eba8e2-dff3-4975-8b54-9f6f4dd39478.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Chatbots_37348ff8-4ec6-4b33-a2a6-5d8d8bf62356.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Learner_Deferred_Report_5ce15be9-994b-4377-8c99-21d35267a2dd.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Program_Enrollment_and_Certificate_b100bef9-c9f8-46f5-b6ef-20b2badecef4.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 3 changes/30d

### `src/ol_superset/assets/charts/Learn_New_Users_5cba1239-2f4c-472b-82f6-788f18de0fd2.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/MITxOnline_Engagement_Totals_0cad65c5-cfb7-4530-95ff-289c093da51d.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Program_Summary_8350fe92-c02c-4e98-92ed-adabae3fb582.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Organization_Administration_Unique_Active_Learners_33b8ff2e-ddd7-4fa6-a438-d422da92fb27.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 3 changes/30d

### `src/ol_superset/assets/charts/Content_Engagement_aa66927b-cc60-4950-8ad8-f79081736841.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 3 changes/30d

### `src/ol_superset/assets/charts/Latest_Dashboard_Activity_Recorded_Date_af403a98-7ff4-407a-b1c9-5161ffc10522.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Enrollment_Data_Updated_Date_9eb01f0f-df02-421e-9c26-d5fdb8cff986.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Problem_Results_f07a7065-db29-4749-a4c6-d2c75c9d55f8.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Course_Run_Metadata_23fb7405-da8f-4983-839d-b1d7fb07e733.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Percent_Engagement_Out_of_Total_Engagement_Opportunities_3bc78cde-60af-405c-9d7d-13e61558c228.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Daily_Learner_Enrollment_0805cae0-185d-4796-9ed4-a240ab047352.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Learner_Performance_d747faf0-d2f8-4dde-84ca-54b60775e051.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Order_detail_c0ce9f7b-a8e8-49d3-909b-9c44718fae8a.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Enrollment_Activity_Over_Time_07019136-a885-4261-8960-cfca368642d7.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Chatbot_Usage_By_Type_751da4ab-6e41-44de-a2b8-e54dc7b2c6b0.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/xPRO_Product_List_-_Standard_Products_Only_244158fe-79de-4ad8-bc53-f82ef3f32ffa.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Chatbots_90099854-5b34-4d06-926c-f58f42b2d69e.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Enrollment_Detail_Dashboard_Last_Updated_1ed19d7a-4f9b-4c13-a6f9-ba348f1c4d3d.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Organization_Administration_Certificates_f1674827-3018-4ff5-bafc-8d4e0fbea7a6.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Problem_Engagement_Test_Report_c05f9d50-bb41-4058-9f35-1ec46ec907c9.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Individual_Enrollment_Detail_f8aa5d0c-f838-4236-9057-4f118d340a53.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Enrollment_Activity_b7056cdf-6d2a-43c0-b0a8-b66ab3f3980c.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/MITxOnline_Enrollment_Demographics_by_Education_5cfc7ea9-6636-41b4-9af7-68c98aeff4de.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/assets/charts/Latest_Product_Created_Date_cdba7fac-5019-4d70-9f0c-817fb7f194d8.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Enrollment_Geography_118ba89d-4c33-4720-b22e-a2576ff93316.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Users_Receiving_Program_Certificates_Over_Time_faf44954-50d0-4135-9efc-b26ebc06e5d8.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Learner_Problem_Engagement_695dd2d8-48d5-436b-a646-204bdf5f2be5.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Learners_Enrolled_c0066291-5b04-437d-b41d-3a4412aa8c82.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/assets/charts/Organization_Administration_Enrollment_Count_cumulative_01f7089f-1355-4a0f-8a51-277c79f26e2b.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 3 changes/30d

### `src/ol_superset/assets/charts/Video_Engagement_by_Section_ebcf2551-ca8e-4fce-b04b-55e382b1c963.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 2 changes/30d

### `src/ol_superset/assets/charts/Engagement_Totals_24ea41c4-da94-443a-af6b-77bc7e09c303.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/.sup/state.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `src/ol_superset/ol_superset/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/cli.py`
**Purpose:** None
**Complexity:** 5.0 | **Velocity:** 2 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/commands/refresh.py`
**Purpose:** None
**Complexity:** 27.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/commands/lock.py`
**Purpose:** None
**Complexity:** 48.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/commands/dedupe.py`
**Purpose:** None
**Complexity:** 44.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/commands/apply_rls.py`
**Purpose:** None
**Complexity:** 24.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/commands/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/commands/sync.py`
**Purpose:** None
**Complexity:** 18.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/commands/validate.py`
**Purpose:** None
**Complexity:** 14.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/commands/export.py`
**Purpose:** None
**Complexity:** 4.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/commands/promote.py`
**Purpose:** None
**Complexity:** 34.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/lib/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/lib/utils.py`
**Purpose:** None
**Complexity:** 20.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/lib/database_mapping.py`
**Purpose:** None
**Complexity:** 27.0 | **Velocity:** 0 changes/30d

### `src/ol_superset/ol_superset/lib/superset_api.py`
**Purpose:** None
**Complexity:** 97.0 | **Velocity:** 3 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/ol_orchestrate/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/jobs/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/sensors/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/sensors/object_storage.py`
**Purpose:** None
**Complexity:** 6.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/ops/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/yaml_config_helper.py`
**Purpose:** None
**Complexity:** 3.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/glue_helper.py`
**Purpose:** None
**Complexity:** 5.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/openedx.py`
**Purpose:** None
**Complexity:** 31.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/automation_policies.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/hooks.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/utils.py`
**Purpose:** None
**Complexity:** 10.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/constants.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 1 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/file_rendering.py`
**Purpose:** None
**Complexity:** 3.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_helpers.py`
**Purpose:** None
**Complexity:** 3.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/arrow_helper.py`
**Purpose:** None
**Complexity:** 4.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/event_log.py`
**Purpose:** None
**Complexity:** 5.0 | **Velocity:** 4 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/schedule_storage.py`
**Purpose:** None
**Complexity:** 6.0 | **Velocity:** 4 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/run_storage.py`
**Purpose:** None
**Complexity:** 5.0 | **Velocity:** 4 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/postgres/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_types/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_types/files.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/lib/dagster_types/google.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/schedules/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/assets/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/io_managers/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/io_managers/filepath.py`
**Purpose:** None
**Complexity:** 11.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/partitions/edxorg.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/partitions/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/outputs.py`
**Purpose:** None
**Complexity:** 3.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/athena_db.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/gcp_gcs.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/oauth.py`
**Purpose:** None
**Complexity:** 12.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client_factory.py`
**Purpose:** None
**Complexity:** 4.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/openedx.py`
**Purpose:** None
**Complexity:** 7.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/bigquery_db.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/api_client.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/github.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/learn_api.py`
**Purpose:** None
**Complexity:** 3.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/canvas_api.py`
**Purpose:** None
**Complexity:** 7.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/postgres_db.py`
**Purpose:** None
**Complexity:** 3.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/secrets/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `packages/ol-orchestrate-lib/src/ol_orchestrate/resources/secrets/vault.py`
**Purpose:** None
**Complexity:** 29.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/build.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/canvas/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/canvas/definitions.py`
**Purpose:** None
**Complexity:** 6.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/canvas/sensors/canvas.py`
**Purpose:** None
**Complexity:** 5.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/canvas/sensors/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/canvas/lib/canvas.py`
**Purpose:** None
**Complexity:** 3.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/canvas/lib/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/canvas/assets/canvas.py`
**Purpose:** None
**Complexity:** 8.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/canvas/assets/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/canvas/resources/api_client_factory.py`
**Purpose:** None
**Complexity:** 4.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/canvas/resources/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/canvas/defs/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/canvas/canvas_tests/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/build.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/definitions.py`
**Purpose:** None
**Complexity:** 5.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/jobs/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/jobs/normalize_logs.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/sensors/openedx.py`
**Purpose:** None
**Complexity:** 11.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/sensors/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/components/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/components/openedx_deployment.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/ops/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/ops/normalize_logs.py`
**Purpose:** None
**Complexity:** 9.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/lib/magic_numbers.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/lib/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/lib/assets_helper.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/schedules/open_edx.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/schedules/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/assets/openedx.py`
**Purpose:** None
**Complexity:** 16.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/assets/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/partitions/openedx.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx/partitions/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/openedx/openedx_tests/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/build.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/definitions.py`
**Purpose:** None
**Complexity:** 6.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/jobs/open_edx.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/jobs/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/sensors/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/ops/open_edx.py`
**Purpose:** None
**Complexity:** 19.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/ops/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/lib/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/schedules/open_edx.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/schedules/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/repositories/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/resources/mysql_db.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/resources/sqlite_db.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/resources/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx/resources/healthchecks.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 0 changes/30d

### `dg_projects/legacy_openedx/legacy_openedx_tests/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/data_platform/build.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/data_platform/orchestration_platform_tests/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/data_platform/data_platform/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/data_platform/data_platform/definitions.py`
**Purpose:** None
**Complexity:** 10.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/data_platform/data_platform/lib/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/data_platform/data_platform/assets/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/data_platform/data_platform/assets/metadata/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/data_platform/data_platform/assets/metadata/databases.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/data_platform/data_platform/defs/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/build.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/definitions.py`
**Purpose:** None
**Complexity:** 8.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/sensors/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/sensors/video_shorts.py`
**Purpose:** None
**Complexity:** 4.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/lib/video_processing.py`
**Purpose:** None
**Complexity:** 13.0 | **Velocity:** 2 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/lib/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/lib/contants.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/lib/google_sheets.py`
**Purpose:** None
**Complexity:** 23.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/assets/sloan_api.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/assets/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/assets/open_learning_library.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/assets/video_shorts.py`
**Purpose:** None
**Complexity:** 25.0 | **Velocity:** 3 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/resources/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources/defs/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/learning_resources/learning_resources_tests/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/b2b_organization/build.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/b2b_organization/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/b2b_organization/b2b_organization_tests/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/b2b_organization/b2b_organization/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/b2b_organization/b2b_organization/definitions.py`
**Purpose:** None
**Complexity:** 3.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/b2b_organization/b2b_organization/sensors/b2b_organization.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/b2b_organization/b2b_organization/sensors/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/b2b_organization/b2b_organization/assets/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/b2b_organization/b2b_organization/assets/data_export.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/b2b_organization/b2b_organization/partitions/b2b_organization.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/b2b_organization/b2b_organization/partitions/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/b2b_organization/b2b_organization/defs/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/student_risk_probability/build.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/student_risk_probability/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/student_risk_probability/student_risk_probability/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/student_risk_probability/student_risk_probability/definitions.py`
**Purpose:** None
**Complexity:** 4.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/student_risk_probability/student_risk_probability/lib/helper.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/student_risk_probability/student_risk_probability/lib/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/student_risk_probability/student_risk_probability/assets/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/student_risk_probability/student_risk_probability/assets/risk_probability.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 2 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/student_risk_probability/student_risk_probability/resources/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/data_loading/build.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 1 changes/30d

### `dg_projects/data_loading/data_loading_tests/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `dg_projects/data_loading/data_loading/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `dg_projects/data_loading/data_loading/definitions.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/data_loading/data_loading/components/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `dg_projects/data_loading/data_loading/defs/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/defs.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/dagster_assets.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/data_loading/data_loading/defs/edxorg_s3_ingest/loads.py`
**Purpose:** None
**Complexity:** 6.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/build.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg_tests/test_edxorg_lib.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg_tests/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/definitions.py`
**Purpose:** None
**Complexity:** 3.0 | **Velocity:** 2 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/jobs/edx_gcs_courses.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/jobs/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/jobs/retrieve_edx_exports.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/sensors/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/ops/edx_gcs_courses.py`
**Purpose:** None
**Complexity:** 5.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/ops/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/ops/object_storage.py`
**Purpose:** None
**Complexity:** 8.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/lib/edxorg.py`
**Purpose:** None
**Complexity:** 6.0 | **Velocity:** 3 changes/30d

### `dg_projects/edxorg/edxorg/lib/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/assets/edxorg_archive.py`
**Purpose:** None
**Complexity:** 20.0 | **Velocity:** 6 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/assets/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/assets/openedx_course_archives.py`
**Purpose:** None
**Complexity:** 10.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/assets/edxorg_api.py`
**Purpose:** None
**Complexity:** 13.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/assets/edxorg_db_table_specs.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `dg_projects/edxorg/edxorg/io_managers/gcs.py`
**Purpose:** None
**Complexity:** 4.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/io_managers/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/edxorg/edxorg/defs/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/build.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse_tests/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse/definitions.py`
**Purpose:** None
**Complexity:** 12.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse/lib/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse/assets/instructor_onboarding.py`
**Purpose:** None
**Complexity:** 3.0 | **Velocity:** 3 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse/assets/superset.py`
**Purpose:** None
**Complexity:** 4.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse/assets/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse/assets/lakehouse/dbt.py`
**Purpose:** None
**Complexity:** 2.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse/assets/lakehouse/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse/resources/airbyte.py`
**Purpose:** None
**Complexity:** 6.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse/resources/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse/resources/superset_api.py`
**Purpose:** None
**Complexity:** 7.0 | **Velocity:** 0 changes/30d

### `dg_projects/lakehouse/lakehouse/defs/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `.gemini/config.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_deployments/reconcile_edxorg_partitions.py`
**Purpose:** None
**Complexity:** 32.0 | **Velocity:** 3 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_deployments/local/workspace.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `dg_deployments/local/dagster.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `bin/dbt-create-staging-models.py`
**Purpose:** None
**Complexity:** 81.0 | **Velocity:** 0 changes/30d

### `bin/dbt-local-dev.py`
**Purpose:** None
**Complexity:** 165.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `bin/uv-operations.py`
**Purpose:** None
**Complexity:** 19.0 | **Velocity:** 0 changes/30d

### `bin/utils/chunk_tracking_logs_by_day.py`
**Purpose:** None
**Complexity:** 11.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

## 3. Data Lineage Summary
Total Modules: 1302
Total Dependencies: 695
