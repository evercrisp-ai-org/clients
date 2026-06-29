# Workflow Maps

## How these render

GitHub renders **Mermaid** diagrams natively inside fenced ` ```mermaid ` code blocks. You do not need an image, a plugin, or ASCII art. View this file on GitHub (or in any Mermaid-aware Markdown preview) and every diagram below draws as a real flowchart or sequence diagram. If you ever open it in a plain text editor, you will see the Mermaid source, which is still readable.

This is the answer to "can you do a sequence diagram that renders in GitHub": yes, the `sequenceDiagram` block below is exactly that.

---

## 1. The skill map (how the 6 skills relate)

```mermaid
flowchart TD
    QP["Quarterly / editorial plan"] --> RS["research-scan<br/>weekly freshness pass"]
    RS --> GB["generate-batch<br/>master orchestrator"]
    GB --> IB["image-brief"]
    GB --> LC["linkedin-check"]
    GB --> VC["voice-check"]
    GB --> VAL["validate"]
    IB --> OUT
    LC --> OUT
    VC --> OUT
    VAL --> OUT["outputs/drafts/content-batch-YYYY-MM-DD/"]
    OUT --> XL["Excel summary<br/>export_content_batch.py"]
    OUT --> SL["Slack #content-review"]
    SL --> HUMAN{{"Human review<br/>before publish"}}
    XL --> HUMAN
```

`generate-batch` is the engine. The other five skills are either run before it (`research-scan`) or called by it as gates (`image-brief`, `linkedin-check`, `voice-check`, `validate`). All five gates can also be invoked standalone on any draft.

---

## 2. generate-batch, end to end (flowchart)

```mermaid
flowchart TD
    A["Trigger: week-NN (or date / range)"] --> B["Step 1: Load brand context<br/>voice, recipe, plans, calendar, config, rules"]
    B --> C["Step 2: Resolve week to dates<br/>+ date-alignment validation"]
    C --> D["Step 3: Draft 10 core pieces + 2-5 clips<br/>blog, podcast, 3 LinkedIn, 5 Facebook"]
    D --> E["Step 4: Apply running ledger<br/>banned templates, device rotation,<br/>image color + subject rotation"]
    E --> F["Step 5: Enforce production rules<br/>while drafting"]
    F --> G["Step 6: Run quality gates"]
    G --> H["image-brief: 9-point prompts, rotation-aware"]
    G --> I["linkedin-check: 17-item, each LinkedIn post"]
    G --> J["voice-check: every piece"]
    G --> K["validate: integrity + date + relevance"]
    H --> L["Literal verification:<br/>grep body for em-dash + pivot constructions"]
    I --> L
    J --> L
    K --> L
    L --> M["Step 7: Write files +<br/>completeness check"]
    M --> N["Regenerate Excel summary"]
    N --> O["Post summary to Slack #content-review<br/>(or print in chat)"]
    O --> P{{"Human reviews batch<br/>(async, post-run)"}}
    P -->|approved| Q["Publish"]
    P -->|fixes needed| D
```

> Note: the gates do **not** block execution mid-run. The batch is drafted, gated, fixed, written to disk, and summarized in one pass; the human review happens **after** the run completes, against the folder and the Slack summary. See the time-study (`05-time-study.md`) for where the human-wait time sits.

---

## 3. generate-batch gate orchestration (sequence diagram)

```mermaid
sequenceDiagram
    actor U as User
    participant GB as generate-batch
    participant DOCS as Brand docs + rules
    participant IB as image-brief
    participant LC as linkedin-check
    participant VC as voice-check
    participant VAL as validate
    participant FS as outputs/ + Excel
    participant SL as Slack

    U->>GB: generate-batch week-NN
    GB->>DOCS: load voice, recipe, plans, calendar, config, rules
    DOCS-->>GB: brand context (~62K tokens)
    GB->>GB: draft 10 core pieces + clips (rules + ledger applied)
    GB->>IB: brief every visual asset (rotation-aware)
    IB-->>GB: 9-point prompts + rotation ledger
    GB->>LC: check each LinkedIn post (17 items)
    LC-->>GB: pass / fixes per post + opening device
    GB->>VC: voice-check every piece
    VC-->>GB: on-voice / drift + line-level fixes
    GB->>VAL: validate every piece
    VAL-->>GB: Green / Yellow / Red per piece
    GB->>GB: apply fixes, literal em-dash + pivot scan
    GB->>FS: write files, completeness check, regenerate Excel
    GB->>SL: post review summary to #content-review
    SL-->>U: notify for async review
    Note over U: Human reviews before publish (blocking dependency)
```

---

## 4. validate, the final gate (flowchart)

```mermaid
flowchart TD
    A["Input: draft file / batch folder / pasted text"] --> B["Load rules + recipe sections + plans + inventory"]
    B --> C["Trust nothing the draft says about itself<br/>(ignore its own checklist marks)"]
    C --> D["Check 1: Content Integrity<br/>Clean / Flagged / Blocked"]
    C --> E["Check 2: Date Alignment<br/>Pass / Fail"]
    C --> F["Check 3: Relevance<br/>Green / Yellow / Red"]
    D --> G{"All clear?"}
    E --> G
    F --> G
    G -->|Integrity Clean AND Date Pass AND Relevance Green| GR["VERDICT: GREEN (publish)"]
    G -->|Blocked or Fail| RD["VERDICT: RED (hold)"]
    G -->|otherwise| YL["VERDICT: YELLOW (revise)"]
```

---

## Maintaining these diagrams

When a skill's sequence changes, edit the Mermaid source here. Keep node labels short and avoid characters that confuse the Mermaid parser (stick to letters, numbers, commas, and `<br/>` for line breaks). Preview on GitHub to confirm they still render before committing.
