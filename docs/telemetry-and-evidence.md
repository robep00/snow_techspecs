# SNOW telemetry and evidence

Part of the [SNOW technical overview](../README.md), review draft dated 7 November 2026. This describes data families; the deployed collector profile and version define the actual fields and collection behavior.

## Collection modes

Event-driven collection, periodic inventory, host-side detection and requested evidence collection serve different purposes. They should not be presented as one universal continuous capture stream.

| Mode | What it provides | Important limit |
| --- | --- | --- |
| Activity records | Events such as process activity and network connections from enabled collectors. | Short-lived activity, source limitations or delivery gaps may leave no record. |
| Inventory and snapshots | A view of processes, services, drivers, persistence or software at a collection point. | A snapshot is not complete historical execution evidence. Its age and completeness matter. |
| Host-side findings | Signals from detection checks, including memory/covert-execution anomalies where supported. | A signal is not necessarily a retained artifact or a malicious verdict. |
| Targeted follow-up | Requested files, memory-related artifacts or other evidence supported by the deployed task set. | Availability, permissions, collection time and approved scope constrain the result. |

## Data families

The following are capability families, not a claim that every field is collected by default on every platform.

| Family | Examples of relevant context |
| --- | --- |
| Process activity | Starts and exits, program path, command line, parent context and available file identity. |
| Process and module state | Running-process snapshots and executable/module metadata from supported collection paths. |
| Persistence and software | Services, drivers, autoruns and installed-software inventory where collected. |
| Network activity | Addresses, ports, protocol/state, timestamps and the associated local process where available. TCP correlation and UDP observations must not be treated as interchangeable. |
| DNS and address history | Queried domains and reported address context from enabled sources. |
| File and host-state changes | Metadata and changes in configured locations. Watching a location does not imply capturing every file body. |
| Windows authentication | Sign-in, sign-out and explicit-credential event context where the collector and forwarding profile enable it. This is not a universal cross-platform event set. |
| Memory and covert execution | Detection findings and available artifacts related to in-memory code or hidden activity, according to platform and profile. |
| Sensor health | Collection/checkpoint and resource context used to interpret coverage and agent operation. |
| AI-tool activity | Supported-tool process lineage and activity context consumed by the backend session module. Account inventory is a separate capability. |

Actual field names, notification tags, hash algorithms, serialization and size/completeness flags are versioned interfaces. Confirm the schema for the deployed build rather than deriving it from these conceptual field descriptions.

## Memory findings and memory bytes

The historical README described host-side memory checks and said memory pages were not transferred as telemetry. That statement must not be extended to every present collection or response workflow.

Keep four questions separate:

1. Was a memory/covert-execution finding recorded?
2. Were the relevant bytes retained with that finding?
3. Was later, targeted collection requested and authorized?
4. Did that request return a usable artifact?

A clean on-disk executable does not clear an in-memory anomaly. Missing bytes, a failed collection, a disappeared file or no usable scan verdict limits the conclusion; none establishes that a host is clean.

## Time and completeness

Collection cadence, agent/module check-ins, delivery time and backend processing delay are distinct. Record the observation time and the source of an identity or relationship. Do not turn a historical polling mean into an end-to-end detection or response guarantee.

Coverage can be affected by offline hosts, collector/profile settings, missed short-lived states, truncated results, collection errors and retention. Last-known inventory and current observed activity must remain distinguishable.

## Sensitive content

Command-line arguments, paths, user context, addresses and requested artifacts can contain sensitive information even when the main record is metadata. An authorized request for a file or memory artifact can have different content implications from routine event collection.

Document the required collection scope, redaction, access and retention for each deployment. The AI-session module's redacted command context is not a guarantee that every general endpoint record or requested artifact is free of secrets or prompt text.

Additional prompt or transcript collection is separately scoped and opt-in. Process/activity tracking does not establish a complete record of model interactions or reasoning.
