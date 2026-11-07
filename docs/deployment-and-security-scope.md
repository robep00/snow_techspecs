# Deployment and security scope

Part of the [SNOW technical overview](../README.md), review draft dated 7 November 2026. A deployment record connects the public capability description to the version, profile, data handling and authority actually in use.

## Deployment record

Engineering and the service owner should confirm the following for the deployment being described. These are required documentation fields, not implied default values.

| Area | Record to confirm |
| --- | --- |
| Platform | Operating system, architecture, workload and supported sensor build. |
| Collection | Enabled modules, profiles, event schemas and platform-specific gaps. |
| Cadence | Event/periodic collection rates, check-ins and expected delivery/processing behavior as separate measurements. |
| Completeness | Result caps, truncation/completeness indicators and handling of offline or failed collections. |
| Identity | Program/file identifiers, hash algorithms and how identities are associated with process and event time. |
| Transport and authentication | Actual protocols, authentication, certificate/key management and cryptographic parameters for the released components. |
| Task controls | Allowed task set, authorization checks, signing/verifying components and operator approval requirements. |
| Data location and access | Processing/storage locations, scope boundaries, roles and access logging. |
| Retention | Separate retention/deletion rules for activity, snapshots, findings, session records, requested artifacts and exports. |
| External providers | Which enrichment providers are used, what indicators/data are sent and the approval scope. |
| AI-specific data | Supported catalog, session scope, staged file watches, account/configuration inventory availability and any opt-in content collection. |
| Operations | Health/coverage checks, update and rollback workflow, resource measurements and escalation responsibilities. |

The 2016 README is not evidence that a polling mean, hash format or collection default still applies. Likewise, a new build or design document does not establish that a feature is enabled on every platform or customer profile.

## Task authority

Distinguish an observed finding, an analyst's assessment, a requested task, its authorization and its returned result.

- Task authenticity and allowlisting constrain execution; they do not decide whether the proposed action is appropriate.
- Evidence collection and containment can have different permissions and approval requirements.
- Do not infer universal isolation, process-termination or remediation authority from the presence of a remote task mechanism.
- Review the allowed command set for the actual deployment rather than promising a fixed count of commands.

## Data handling

Routine metadata and targeted file or memory collection have different sensitivity. Agree which records are required, who can view them, where they are processed and how long they remain available.

Validate redaction in the relevant data paths. Redacted AI-session commands do not establish that general process telemetry or requested artifacts contain no sensitive information. Additional prompt/transcript collection requires a separately agreed opt-in scope.

Record external enrichment egress explicitly. Looking up an address or indicator is different from sending an entire event, command line, file or case record to a third party.

## Operational validation

Use representative systems and workloads to validate compatibility, collection health, resource use and update behavior. Keep collection gaps and stale data visible during investigation.

A user-space sensor does not introduce its own kernel driver, but it cannot keep collecting from a host whose operating system has crashed or is offline. Architectural diversity is not a guarantee of uninterrupted collection or zero operational risk.

Response time and human-review coverage are service arrangements; they cannot be inferred from an event polling interval or the existence of automation.

## Publication review

Before this draft becomes an approved specification, confirm the version/profile matrix and the deployment-record fields above. Verify examples are synthetic or approved for publication and contain no client identifiers, credentials, private paths, patient data or raw internal case records.

Keep interface schemas and version-specific limits tied to a released implementation. Do not add guessed cipher suites, default footprint numbers, universal retention periods, certification claims or guaranteed detection/containment outcomes.
