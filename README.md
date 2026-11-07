# SNOW technical overview

**Review draft prepared 7 November 2026.** Engineering confirmation is required before treating this refresh as an approved deployment specification. The previous README is preserved in the [June 2016 archive](docs/archive/README-2016-06-06.md).

SNOW combines endpoint evidence, backend correlation and human-led investigation. It brings process activity, host state, network relationships and external intelligence into a workflow for investigating suspicious activity and coordinating authorized follow-up.

Collection depends on the operating system, sensor version, enabled profile and engagement scope. A capability described here is not a promise that every collector or response action is enabled on every host. Event schemas, limits and configuration defaults must be matched to the deployed version.

## Platform responsibilities

| Component | Responsibility |
| --- | --- |
| SNOW Sensor | Collect configured endpoint records, raise host-side findings and support scoped follow-up collection. |
| SNOW Cloud | Organize records, correlate activity, apply detection rules, group investigation leads and add external context. |
| SNOWboard | Present investigation, Timeline, process, host, network and Perimeter context to authorized users, with evidence navigation and exports. |
| Analysts and operators | Evaluate the evidence, document uncertainty and decide or obtain authority for response. |

## Technical documentation

- [Telemetry and evidence](docs/telemetry-and-evidence.md): data families, collection modes, memory artifacts and sensitive content.
- [Correlation and AI tool tracking](docs/correlation-and-ai-tool-tracking.md): process/network relationships, external enrichment, AI-agent sessions and rollout boundaries.
- [Deployment and security scope](docs/deployment-and-security-scope.md): the versioned deployment record, access, task authority, retention and validation.
- [Historical telemetry notes](docs/archive/README-2016-06-06.md): the original 2016 description, not current defaults.

## Capability and rollout scope

| Capability | Scope of this overview |
| --- | --- |
| Endpoint activity and host-state collection | Available through configured collectors; coverage and fields vary by platform, version and profile. |
| Memory and covert-execution investigation | Findings and available follow-up artifacts support review. A detection does not guarantee that the relevant memory bytes were retained. |
| Cross-host process relationships | Require suitable observations from both enrolled endpoints. Unknown or off-fleet ends must not be invented. |
| Shodan and threat-intelligence context | Enrichment has its own source, timestamp and confidence. A public scan is not a live endpoint test. |
| AI-agent work-session analysis | Backend session tracking relates supported tools to observed process activity and review flags. It is not account-organization verification or proof of a leak. |
| Selected AI-tool configuration-file changes | Staged and profile-dependent; not universal configuration, account, hook or MCP inventory. |
| Expanded AI-tool account and configuration inventory | Not established as generally available by this review; do not assume rollout from a design or collector specification. |
| Additional prompt or transcript collection | Separately scoped and opt-in; not implied by the activity-tracking module. |
| Broader OSINT investigation layer | Roadmap. Existing external enrichment does not establish a completed OSINT integration. |

## Interpreting findings

A new relationship, a trusted signature, a vulnerable driver or an empty scan is not a verdict by itself. Investigations must distinguish observed events, inferred context, missing evidence and confirmed conclusions.

Collection timing, check-in timing and backend processing delay are different measurements. This overview does not set a universal polling interval, response time, footprint estimate or retention period.

## Review before deployment

Use the [deployment record](docs/deployment-and-security-scope.md#deployment-record) to confirm platform support, collector enablement, field schemas, limits, transport/security settings, data handling and allowed actions. This overview is not a certification, response authorization or statement of legal admissibility.

## Documentation checks

Run the dependency-free Markdown/link and archive checks with:

```sh
python3 tools/check_docs.py
```
