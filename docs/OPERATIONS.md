# Operations

1. Place authorised source material under data/inbox/.
2. Run validation and normalisation.
3. Inspect the generated manifest.
4. Hand the immutable bundle to skool-playbook-engine.
5. Publish the resulting playbook artefacts.
6. Commit the manifest and generated metadata.

Secrets must be supplied through the deployment environment, never committed.

## Autonomous handoff

The intended production handoff is:

1. authorised material lands in `data/inbox/`.
2. `normalise.yml` creates `data/normalised/bundle.json`.
3. A cross-repository GitHub Actions handoff can publish that bundle into `skool-playbook-engine/input/bundle.json` and trigger its `source-bundle-updated` event.

For that final cross-repo step, configure a GitHub fine-grained token with write access to the engine repository as the `PLAYBOOK_ENGINE_TOKEN` Actions secret. No course credentials are stored or required.
