# Devops-IA-1

This project demonstrates how to use **Fluentd** to collect logs from multiple sources, filter and parse them, and send them to **Elasticsearch** for storage, search, and visualization. It can also be extended to visualize logs using **Kibana**.

---

## **Features**

1. **Collect logs from multiple sources**

   - Fluentd can tail log files from different applications or servers.
   - Supports both structured (JSON) and unstructured logs.

2. **Filter and parse logs**

   - Logs can be parsed into structured fields (e.g., timestamp, log level, message).
   - Filters allow only relevant logs to be sent forward.

3. **Send logs to Elasticsearch**
   - Logs are stored in Elasticsearch indices for easy searching and analysis.
   - Supports time-based indices for daily or hourly log storage.

---

## **Architecture Overview**

```
[Multiple Log Files / Sources]
              |
              v
           Fluentd
      (Filtering, Parsing)
              |
              v
       Elasticsearch
              |
              v
           Kibana
    (Visualize and search logs)

```

---

## **Description**

- Fluentd acts as a **log collector and router**, reading logs from one or more sources.
- It can **filter and parse logs** into structured formats.
- Logs are sent to **Elasticsearch**, where they are indexed and made searchable.
- Optionally, **Kibana** can be used to visualize, analyze, and create dashboards from the logs.

---

## **Key Points**

- Fluentd uses `<source>` blocks to define where logs come from.
- `<match>` blocks define where logs are sent (Elasticsearch in this case).
- Elasticsearch stores logs in **indices** with defined fields and data types.
- Kibana provides a **graphical interface** to explore, filter, and visualize log data.
