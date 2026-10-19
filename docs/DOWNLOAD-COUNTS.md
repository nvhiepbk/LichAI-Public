# Cumulative download counts

The public page shows recorded GitHub asset downloads, not unique people or installations. Each application total is the sum of its installers. Each installer total is the sum of all observed asset IDs using its approved filename: historical periods + current period.

`registry/download-counts.json` preserves the maximum observed `download_count` per GitHub asset ID. Repeated polls do not add the same count again. A new asset ID starts a new period without discarding retired IDs. Unknown release files are ignored. A renamed ID requires manual ownership review.

During an apply reconciliation, counters are sampled and committed before installer processing, again immediately before replacing a group, and after successful reconciliation. If the pre-replacement ledger commit fails, publication stops before replacing those assets. Failed or rolled-back uploads retain recorded old periods. API failures fail the job; they never write zero counters as a replacement for missing data. Counts are observations, not an exact transactional click log: final downloads between sampling and deletion cannot be recovered from GitHub after deletion. Other external writers should use this publisher to preserve their last counts.

`metadata/download-counts.json` is the website projection, with application and per-installer historical/current/total counts. No new file downloads are performed to count usage. No analytics, IP addresses or visitor identifiers are collected. An unchanged sample does not create another timestamp-only commit.

The initial retired asset entries are the actual pre-publication API snapshot captured in the session before reconciliation run 39251705938. They record 18 downloads across 8 assets. They do not reconstruct any deleted periods preceding that snapshot. Existing GitHub asset counters are not edited.

Rollout: merge Public changes first, then the website PR. The existing Public reconciliation and website catalogue schedules refresh the snapshots; manual runs can refresh immediately. Website sync reads counts and catalogue from one immutable Public commit and validates all totals before writing any files. Rendering uses the local synchronized snapshot; unavailable/invalid counts hide the notes, while downloads remain usable.
