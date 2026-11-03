# TBJ

A static tabletop initiative tracker. Open `index.html` in a browser, or serve this directory with `python3 -m http.server 8000`. No build, package install, backend, or API keys are required.

## Play

In Turn Order, choose any survivor or adversary from the pickers and click Add. Custom character types appear here too. Added characters are listed immediately as ready to play or joining next round; current rolls are preserved.

Jadeguard is an Adversary with a 2–6 range; Rubyguard is 5–9; Bronzeguard is 5–8; and Legacy Assistant is a separate Survivor with a 3–8 range. Poltergeist has a Link to selector in Roster: choose a non-Poltergeist participant and it copies their adjusted range and roll, appearing immediately after them in turn order.

Set the survivor count, add adversaries, select character types, and optionally enter usernames. Each participant has an editable base range. The character library edits defaults and creates custom types.

**Play / roll round** rolls every participant independently, sorts by speed, and randomizes ties. **Confirm turn ✓** beside the current name (or **Next turn**) marks the current participant as acted with an animated strikethrough and a short confirmation ding. Mute controls both the ding and the supplied dice sound. Roster edits never alter the current round's snapshot. Turn Order, Roster, and Character Library have separate keyboard-accessible tabs. Each name shows the range used for that round alongside its rolled speed, and Adversaries use red styling. Reset rounds works immediately without a browser popup and clears the counter and turn order while keeping the roster and remaining effects.

The current turn is yellow with a gold border; upcoming turns are blue. Confirming a turn flashes that card green, then fades it to grey. Selecting or applying quick effects briefly flashes the targeted card blue, with a persistent selection outline. Adversary names remain red.

Click a turn-order card or its Select button to target that participant. The quick-effects panel shows the selected name, next range, effect count, and net speed; its buttons apply only to that participant. Selection does not change the current turn. Starting a round or confirming a turn selects the new current participant.

Quick-effect controls in Turn Order let you choose an amount and full-round duration (or until removed), then apply Haste or Bind directly on a card. Roster cards also offer one-click +1 Haste and −1 Bind for one round; use + Effect for reasons or other settings. These controls update the next range immediately while preserving the current range and roll. Older saved rounds without a stored range display “Range saved before update” until you roll again.

Matching effects are displayed as compact stacks with a total and count. The minus button removes one effect, × removes that stack, and Clear effects removes all effects from that participant. Different amounts, durations, or reasons remain separate. Clearing affects future rolls only.

Haste and Bind stack. Both endpoints clamp to at least 1. Effects apply to the next roll; a timed effect is consumed only after a newly started round uses it. For example, Spotter with Haste +11 for 10 rounds immediately shows 16–19 and uses that range for ten rounds. The effects list shows how many future rounds remain. Conditional effects persist until removed. Advancing a turn never consumes an effect.

Data saves automatically in this browser's local storage, including the current turn. Clearing browser data removes saves. Browser privacy settings may prevent persistence; the app reports storage failure. Offline files and hosted pages may have separate local saves.

## GitHub Pages

Commit and push these files. In repository Settings → Pages, select **Deploy from a branch**, select the branch containing these files and **/ (root)**, then Save. `index.html` is at the repository root. No custom domain is configured. Publication and repository pushes have not been performed by this implementation.

## Offline edition

`TBJ-offline.html` embeds the CSS, JavaScript, supplied MP3, and supplied MP4. Download it and open it directly in a browser; it needs no network connection. To regenerate it after changes:

```sh
python3 scripts/build-offline.py
```

The supplied audio is stored in `assets/dice-roll.mp3`. Mute is persistent. Playback failures never block the round or turn controls. The supplied MP4 plays a random 0.9-second excerpt each round, with a subdued blue tint and no video audio. The six-sided animation is a fallback if playback fails or reduced motion is enabled. Both animations are decorative; results use the participant's actual range.

## Validation

```sh
node --test tests/engine.test.js
```

Browser checks (requires Playwright and Chromium; start the static server first):

```sh
node tests/browser.cjs
```

Set `TBJ_URL` to use a different server address, or `CHROMIUM_PATH` to select another Chromium executable. Browser checks cover both HTML editions, tabs, reset persistence, animated completion, audio triggering and mute, audio failure, final-turn completion, and mobile width.

Engine tests cover duration, clamping, stacked and conditional effects, immutable round snapshots, and tied order. Browser smoke checks were also run for effect entry, rolling, advancing, persistence, responsive width, and the bundled offline edition served locally. This managed browser blocks direct `file:` navigation, so opening the offline file directly should be checked in your own browser.
