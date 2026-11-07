# Correlation and AI tool tracking

Part of the [SNOW technical overview](../README.md), review draft dated 7 November 2026. Correlation gives analysts context; it does not turn every relationship or risk flag into a confirmed incident.

## Process and network relationships

SNOW can relate process activity and network observations across enrolled hosts where suitable evidence is available. A local process, its connection and a receiving process are separate observations that must be linked with the appropriate endpoint identity and time context.

Important boundaries:

- Both enrolled ends need suitable telemetry for a process-to-process relationship. An off-fleet address is not a known remote process.
- NAT, shared addresses, proxies and load balancers can prevent a reliable match. Missing links must not be filled in as fact.
- Program identity may come from observed activity, a process snapshot or operating-system context; its provenance and age matter.
- Direction may be observed or inferred. A port-number heuristic is weaker evidence than a matching connection or listener observation.
- Collection intervals and event sources may miss short connections. TCP relationship analysis does not imply equivalent UDP coverage.
- A newly observed relationship or a changed binary is a lead for review, not proof of malicious lateral movement.

This supports following activity from an administration tool through child processes and network connections when the evidence supports the links. It does not guarantee a complete chain in every investigation.

## Memory and behavior context

Memory/covert-execution findings, suspicious use of legitimate tools and vulnerable-driver observations can be reviewed alongside process, persistence and network context.

Living-off-the-land activity (LOTL) may involve legitimate administration as well as abuse. Bring-your-own-vulnerable-driver (BYOVD) investigation must distinguish a vulnerable driver's presence from evidence that it was loaded or exploited for an attack. Signer reputation and familiar paths are context, not blanket clearance.

## External enrichment

Shodan-sourced service and exposure records and threat-intelligence context can add information about an address or indicator involved in an investigation.

Keep source, observation date and confidence attached to enrichment. A version-based vulnerability match is not proof of exploitation. A public scan is not a live probe, and an open service at a shared public address does not identify which internal device owns it.

A broader open-source intelligence (OSINT) investigation layer remains roadmap; it is distinct from the external enrichment already described here.

## Current AI agent activity analysis

The backend AI-agent module groups observed activity from supported tools into work sessions. It relates recognized root processes to observed children, including shells and scripts, and records activity patterns for analyst review. Supported-tool identification depends on the deployed catalog and telemetry; it is not a complete inventory of every installed AI application or browser interaction.

Session records include redacted command context and flags for review, including credential-related and integrated-authentication patterns. A flag does not establish that credentials were read, access was unauthorized or data leaked. Recognizing a tool does not verify its signed-in organization's identity or whether its use was approved.

Session lineage also does not reveal the model's intentions or prove that every action was observed. Correlate the available records and state the remaining uncertainty.

## Staged and developing AI capabilities

These must not be folded into the baseline session-tracking description:

| Capability | Boundary for this review |
| --- | --- |
| Selected configuration-file watching | Staged, profile-dependent change/hash records are not universal semantic configuration inventory. Do not infer operating-system or fleet-wide coverage. |
| Account identity and MCP/hook inventory | A specialized collector specification does not establish a completed rollout. Confirm the released sensor, profile and backend before claiming availability. MCP is Model Context Protocol. |
| Dedicated AI-agents client interface | Backend records do not by themselves establish a generally available SNOWboard pane. Verify the UI release and access roles separately. |
| Prompt or transcript collection | Additional collection is separately scoped and opt-in. General command-line telemetry can itself contain sensitive text; audit that path independently. |
| Comparing reported actions with execution | A direction for gap detection, not a claim that complete independent verification of model activity already ships. |

## Workspace and response

SNOWboard provides investigation, Timeline/Process Tree, host-event, connection and Perimeter context according to permissions and available records. Evidence exports and their checksums support review of saved copies; a checksum does not prove the interpretation, completeness or legal admissibility of the evidence.

An alert, a session label or an authenticated task does not decide whether an action is appropriate. Collection and response remain subject to the [deployment's authority and controls](deployment-and-security-scope.md#task-authority).
