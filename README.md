# SEO Methodology Skill

---

**Name**: seo-methodology

**Description**: "Apply Exalt Growth's SEO and GEO methodology to any SaaS growth challenge. Combines the Proof of Importance citation model, EGOS operating system, and Entity-First Framework to evaluate content, plan strategy, audit architecture, and optimize for AI search visibility. Use whenever someone is making an SEO or content decision, evaluating a page for AI citation readiness, planning site architecture, assessing keyword strategy, optimizing for LLM visibility, auditing entity infrastructure, building a content brief, or applying structured SEO methodology to a SaaS growth problem. Also triggers on: 'how should I approach this SEO problem', 'evaluate this content', 'is this page ready for AI search', 'audit my site structure', 'how do I get cited by ChatGPT/Perplexity/Gemini', 'what's wrong with my SEO strategy', 'help me think through this content decision', 'GEO readiness check', 'entity audit', 'content evaluation', 'SEO methodology', 'citation optimization', or any reference to PoI signals, EGOS modules, or Entity-First pillars."

---

# SEO Methodology

Apply the Exalt Growth methodology to SEO and GEO decisions for SaaS companies. This skill routes problems through three interconnected frameworks to produce structured, actionable recommendations.

Source: Exalt Growth (www.exaltgrowth.com/methodology)
Author: Jack Boutchard (www.jackboutchard.com)

## Framework Overview

Three frameworks work together. Each addresses a different layer of the problem.

| Framework | Purpose | When to Apply |
|---|---|---|
| Proof of Importance (PoI) | 7 signals that determine whether LLMs cite your content | Content evaluation, citation optimization, GEO audits |
| EGOS (Exalt Growth Operating System) | 4 systems, 12 modules for building AI visibility | Strategy planning, engagement scoping, system design |
| Entity-First Framework | 4 pillars for entity architecture and AI readiness | Site architecture, schema deployment, entity audits |

---

## Core Modes

Identify the user's problem type and route to the correct mode.

### Mode 1: Content Evaluation

Trigger: User provides a draft, URL, content brief, or asks whether content is "ready" for AI search.

Workflow:
1. If a URL is provided, scrape it using Firecrawl (`firecrawl_scrape`) to extract content and structure
2. Evaluate the content against all 7 PoI signals, starting with Tier 1 (retrieval gate):
   - Tier 1 (Retrieval Gate): Structural Accessibility + Semantic Relevance. If content fails here, flag it. The other signals are irrelevant until retrieval is solved.
   - Tier 2 (Citation Scoring): Source Authority, Entity Relationships, Evidence Density, Recency, Corroboration
3. Score each signal: Pass / Partial / Fail with specific evidence
4. Apply the content quality standards: atomic knowledge units, evidence density, structure-as-signal
5. Produce a structured evaluation with:
   - Signal-by-signal assessment
   - Top 3 priority fixes with specific rewrite suggestions
   - Citation readiness verdict (Ready / Needs Work / Not Retrievable)

### Mode 2: Strategy and Planning

Trigger: User asks about SEO or GEO strategy, roadmaps, priorities, engagement planning, or how to approach a growth challenge.

Workflow:
1. Identify which EGOS system and modules are most relevant:
   - Intelligence System (Modules 1-3): Research, strategy, topical mapping
   - Content System (Modules 4-6): Content production, proof infrastructure
   - Amplification System (Modules 7-9): Distribution, PLG, agent enablement
   - Optimization System (Modules 10-12): Measurement, revenue, defensibility
2. Map the user's challenge to the relevant modules
3. If keyword or topic research is needed, use InfraNodus tools:
   - `analyze_google_search_results` for SERP landscape analysis
   - `generate_topical_clusters` for topic architecture
   - `generate_content_gaps` for opportunity identification
4. If search volume data is needed, use DataForSEO:
   - `kw_data_google_ads_search_volume` for volume and competition
   - `serp_organic_live_advanced` for current SERP composition
5. Produce a structured recommendation that:
   - Names the relevant EGOS modules and explains why
   - Provides a prioritized action sequence
   - Identifies dependencies between modules
   - Specifies measurable outcomes for each action

### Mode 3: Architecture Advisory

Trigger: User asks about site structure, information architecture, schema deployment, entity mapping, or URL hierarchy.

Workflow:
1. If a URL is provided, scrape using Firecrawl to extract current structure and schema
2. Evaluate against the Entity-First Framework's four pillars:
   - Foundation: Are core entities defined? Do Organization, Person, and WebPage schemas exist?
   - Structure: Is the IA organized around entities and topics, not arbitrary categories?
   - Signals: Are entity relationships expressed through schema, internal links, and content patterns?
   - Measurement: Can entity visibility be tracked across AI surfaces?
3. Apply PoI Signal 3 (Entity Relationships) and Signal 6 (Structural Accessibility) as evaluation lenses
4. If InfraNodus is available, use `generate_knowledge_graph` or `analyze_text` to map the entity landscape
5. Produce architectural recommendations:
   - Entity map (what entities must be defined and connected)
   - Schema requirements (specific JSON-LD types needed)
   - IA structure (URL hierarchy, topic clustering, internal linking patterns)
   - Retrieval readiness assessment (will AI systems find and parse this structure?)

### Mode 4: GEO Readiness Assessment

Trigger: User asks about AI search optimization, LLM visibility, getting cited by ChatGPT/Perplexity/Gemini/AI Mode, or GEO strategy.

Workflow:
1. If a URL is provided, scrape using Firecrawl and evaluate entity/schema presence
2. Apply the two-tier PoI model:
   - Tier 1 (Retrieval Gate): Can this content be retrieved at all? Evaluate Structural Accessibility and Semantic Relevance.
   - Tier 2 (Citation Scoring): Among retrieved candidates, how competitive is this content? Evaluate the remaining five signals.
3. Distinguish between AI platforms. Each has distinct retrieval characteristics:

| Platform | Retrieval Layer | Key Signals |
|---|---|---|
| Google AI Mode | Authority-weighted, positional bias, text fragment extraction | Source Authority, Structural Accessibility |
| Gemini | Separate domain pool from AI Mode, Google ecosystem signals | Entity Relationships, Corroboration |
| ChatGPT | Training data + Bing retrieval, different freshness weighting | Evidence Density, Recency |
| Perplexity | Real-time retrieval, source diversity, citation-forward UX | Semantic Relevance, Structural Accessibility |

4. Produce a GEO readiness report:
   - Platform-specific assessment (not generic "AI search" recommendations)
   - Retrieval gate pass/fail with specific fixes
   - Citation competitiveness score per platform
   - Priority actions ranked by impact and effort

---

## Key Principles

Apply these throughout every mode and output.

### The Unit of Competition Has Shrunk
Pages do not compete in AI search. Chunks do. RAG systems chunk content into 256 to 512 token segments. Each chunk is evaluated independently. Your 2,000 word guide may contribute one paragraph to an AI response.

### Retrieval Before Citation
Content must pass retrieval before it can compete for citation. Structural Accessibility and Semantic Relevance are Tier 1 gate signals. Optimizing Source Authority or Evidence Density is pointless if the content never gets retrieved.

### Multi-Vector Retrieval
Modern retrieval systems produce multiple embeddings per document. Scoring uses Chamfer Similarity: for each query token, the system finds the best matching document token, then sums those matches. Content that covers multiple query dimensions moderately beats content that covers one dimension deeply.

### Entity Architecture is Prerequisite
All content and optimization work starts with entity graph mapping. Entities are the connective tissue between traditional SEO and AI visibility. Without entity infrastructure, content lacks the relational context LLMs use to validate expertise.

### Information Gain Over Volume
Content must offer something LLMs cannot synthesize from existing training data. Proprietary data, named frameworks, original findings, and unique entity relationships produce embeddings no competitor page can replicate.

### Platform Specificity
AI platforms have distinct retrieval layers. Domain overlap between AI Mode and Gemini is under 4%. Never produce generic "AI search" recommendations. Always specify the target platform.

---

## Proof of Importance: The 7 Citation Consensus Signals

Proof of Importance (PoI) is a citation scoring model that explains how LLMs decide what to cite. It identifies seven signals that determine whether a content chunk gets included in an AI generated answer or ignored.

The name draws from blockchain consensus mechanisms. In NEM's Proof of Importance protocol, nodes earn importance scores from multiple weighted signals: stake, transaction partners, network activity, and relationship graph position. AI citation works the same way. No single signal guarantees inclusion. The system evaluates all signals together and assigns composite importance to each content chunk.

### Two-Tier Architecture

The seven signals operate in two tiers. Most frameworks treat all signals as equal inputs. They are not.

Tier 1 (Retrieval Gate): Signals 1 and 6 (Semantic Relevance and Structural Accessibility) form the retrieval gate. This is a binary filter. Content that fails Tier 1 is never surfaced for scoring. The other five signals become irrelevant.

Tier 2 (Citation Scoring): Signals 2, 3, 4, 5, and 7 determine competitive ranking among retrieved candidates. These signals differentiate your content from other chunks that also passed the retrieval gate.

Practical implication: Fix retrieval problems before optimizing anything else. A page with perfect evidence density but broken structure will never be cited.

### Signal 1: Semantic Relevance (Tier 1)

Definition: How precisely a content chunk matches the intent and meaning of the query.

This is not keyword matching. LLMs measure conceptual distance in vector space using dense retrieval methods. A chunk about "project management software pricing" will not surface for "project management methodologies" even if both mention "project management."

Multi-vector scoring: Modern retrieval systems produce multiple embeddings per document, often one per token. Scoring uses Chamfer Similarity. For each query token embedding, the system finds the best matching document token. Then it sums those matches across all query tokens. Content that covers multiple query dimensions moderately outscores content that covers one dimension deeply.

Evaluation criteria:
- Does the chunk directly address the query's core intent?
- Does it cover multiple dimensions of the query topic?
- Is there semantic distance between the chunk and the target query?
- Would this chunk make sense as a standalone answer fragment?

### Signal 2: Source Authority (Tier 2)

Definition: The cumulative trust a domain and brand entity carry across the web.

This includes traditional signals like backlink profiles and domain age. It also includes newer signals: citation frequency by other trusted sources, Knowledge Graph presence, and training data representation. Authority is recursive and relational. It is conferred by those who already have it.

Evaluation criteria:
- Does the domain have a strong backlink profile from topically relevant sources?
- Is the brand entity present in knowledge graphs?
- Do other authoritative sources cite or reference this domain?
- Is there training data representation (parametric memory)?

### Signal 3: Entity Relationships (Tier 2)

Definition: How well a brand connects to other trusted entities in its knowledge domain.

LLMs decompose queries into entities and evaluate which sources have established relationships with those entities. Sources deeply connected to query entities are more likely to be retrieved and cited than sources with weak or superficial associations.

Evaluation criteria:
- Are the brand's core entities explicitly defined (schema, content, external references)?
- Does the content connect to entities the query references?
- Are entity relationships expressed through structured data?
- Do third-party sources associate this brand with relevant entities?

### Signal 4: Evidence Density (Tier 2)

Definition: The ratio of verifiable claims, data points, and supporting evidence within a content chunk.

LLMs favor content that provides proof over content that makes unsupported assertions. "Our software improves productivity" carries far less weight than "Our software reduced average task completion time by 23% across 500 enterprise deployments."

Evaluation criteria:
- Does the chunk contain specific data points, statistics, or metrics?
- Are claims supported with evidence rather than assertions?
- Does the content reference named methodologies, studies, or frameworks?
- Would an LLM extract this chunk with confidence in its factual accuracy?

### Signal 5: Recency (Tier 2)

Definition: How current the information is relative to the topic's pace of change.

For rapidly evolving subjects, recency carries disproportionate weight. For stable topics, recency matters less but is never irrelevant. Publication dates, update timestamps, and temporal language all contribute.

Evaluation criteria:
- Is the content dated? When was it last updated?
- Does it reference current data, events, or versions?
- Is the topic fast-moving (high recency weight) or stable (lower weight)?
- Are there temporal markers that signal freshness to retrieval systems?

### Signal 6: Structural Accessibility (Tier 1)

Definition: How easily machines can parse, chunk, and retrieve the content.

This is not just a signal. It is the prerequisite that makes the other six count. Structural Accessibility operates at the retrieval layer, not the ranking layer. If the retrieval system cannot cleanly extract chunks, the page never enters the scoring phase.

What good structure looks like:
- Clean HTML with logical heading hierarchies
- Self-contained paragraphs that function as standalone chunks
- Schema markup (JSON-LD) defining entities and relationships
- Explicit definitions, not implied ones
- FAQ structures with clear question/answer pairs
- No critical information buried in images, JavaScript, or interactive elements

Evaluation criteria:
- Can a RAG system cleanly extract coherent chunks from this page?
- Are heading hierarchies logical and consistent?
- Are key claims in parseable text, not embedded in images or scripts?
- Does schema markup define the page's entities and relationships?
- Do paragraph boundaries align with semantic boundaries?

### Signal 7: Corroboration (Tier 2)

Definition: Whether other trusted sources confirm the same claims.

LLMs cross-reference claims across multiple sources. Content that appears corroborated across independent sources earns higher citation confidence.

Ghost citations: A brand can have its content cited by LLMs while the brand name is omitted. This happens when the information is corroborated but the brand-to-claim association is weak. Ghost citations are a brand problem, not a content problem. Strengthening Corroboration through third-party mentions and entity associations addresses this.

Evaluation criteria:
- Do other trusted sources make similar claims?
- Is the brand mentioned by name in third-party contexts?
- Are there reviews, case studies, or industry mentions that corroborate the brand's expertise?
- Would an LLM find this claim confirmed across multiple independent sources?

### PoI Evaluation Sequence

When evaluating content against PoI, follow this order:

1. Start with Tier 1. Assess Structural Accessibility first. If the content is not machine-parseable, stop. Fix structure before evaluating anything else.
2. Then assess Semantic Relevance. Does the content match the target queries?
3. Only then score Tier 2. Evaluate Source Authority, Entity Relationships, Evidence Density, Recency, and Corroboration.
4. Prioritize by impact. A new brand should prioritize Corroboration and Entity Relationships. An established brand with weak content should prioritize Evidence Density and Structural Accessibility.

### Signal Scoring Template

| Rating | Meaning |
|---|---|
| Pass | Signal is well-optimized. No immediate action needed. |
| Partial | Signal has some strength but clear gaps exist. Specific improvements identified. |
| Fail | Signal is absent or critically weak. Must be addressed before citation is likely. |

Always provide specific evidence for each rating. Never score without citing the exact content or structural element being evaluated.

---

## EGOS: Exalt Growth Operating System

EGOS is a 4-system, 12-module operating system for building AI visibility. It is not a service menu. It is an integrated operating system where each module feeds the others. Pull one piece out and the flywheel breaks.

### North Star

Be the default answer wherever your buyer or their AI agent searches.

Every module maps back to four foundational principles:

| Principle | Definition |
|---|---|
| Retrievable | Content that fails retrieval never reaches the ranking phase. |
| Understandable | Both humans and machines must parse expertise without ambiguity. |
| Credible | AI systems evaluate trust through source authority, corroboration, and entity associations. |
| Defensible | Moats come from proprietary data, network effects, and compounding authority. |

### System 1: Intelligence System

Build a comprehensive map of the competitive landscape before creating anything.

Module 1: Discovery Module
Deep competitive intelligence across traditional search and AI surfaces. Audit how LLMs currently represent the brand, competitors, and category.
Key output: AI Visibility Audit + Competitive Gap Map.
Tools: Firecrawl for site scraping, InfraNodus for entity extraction, DataForSEO for SERP data, manual LLM prompt testing.

Module 2: Strategy Module
Translate intelligence into a prioritized roadmap. Score every initiative against effort, impact, and defensibility.
Key output: Prioritized GEO Roadmap + KPI Framework.

Module 3: Topical Engine
Define the semantic territories the brand needs to own. Map entity relationships, topic clusters, and knowledge graph structures.
Key output: Topical Authority Blueprint + Entity Map.
Tools: InfraNodus (`generate_knowledge_graph`, `generate_topical_clusters`, `analyze_google_search_results`), DataForSEO for search volume.

### System 2: Content System

Engineer content at the chunk level. That is the unit of competition in AI search.

Module 4: Block Factory
Produce modular, chunk-level content blocks engineered for retrieval. Each block is optimized against the seven PoI signals. Blocks are scored for multi-intent coverage because retrieval systems evaluate how well a single block matches across multiple query dimensions simultaneously.
Key output: Citation-Ready Content Blocks.
PoI connection: Directly operationalizes all seven signals.

Module 5: Content Engine
Systematic content production across formats. Long-form editorial, technical documentation, data assets, comparison resources. Each piece mapped to a specific role in the buyer journey.
Key output: Full-Funnel Content Library.

Module 6: Proof System
Build proof infrastructure through case studies, third-party validation, original research, and corroboration assets. Engineer for information gain: proprietary data, named frameworks, and original findings that produce embeddings no competitor can replicate.
Key output: Evidence Assets + Trust Architecture.
PoI connection: Strengthens Evidence Density (Signal 4) and Corroboration (Signal 7).

### System 3: Amplification System

Distribute authority signals across every surface where LLMs gather training data and retrieval context.

Module 7: Distribution Engine
Strategic syndication and placement across publications, platforms, and directories that AI systems use as trusted sources.
Key output: Multi-Surface Distribution Map.
PoI connection: Strengthens Source Authority (Signal 2) and Corroboration (Signal 7).

Module 8: Product-Led Studio
Create tools, calculators, templates, and interactive assets that generate organic backlinks, brand mentions, and entity associations while serving the sales funnel.
Key output: Growth Tools + Interactive Assets.

Module 9: Agent Enablement
Optimize digital presence for the autonomous buying layer. As AI agents handle more purchasing decisions, brands need to be agent-readable and agent-recommendable.
Key output: Agent-Optimized Assets + Schema.

### System 4: Optimization System

Build measurement and feedback loops that maintain advantage as models change and competition adapts.

Module 10: Feedback Loop
Continuous monitoring of AI visibility metrics across every major LLM surface. Track citation frequency, sentiment, accuracy, and competitive share.
Key output: LLM Visibility Scorecards + Alerts.
Tools: Hall, Goodie AI for AI visibility tracking. Manual prompt testing for validation.

Module 11: Revenue Engine
Connect AI visibility directly to revenue. Build attribution models that track how LLM citations translate into pipeline and closed deals.
Key output: AI Attribution Dashboard + ROI Models.

Module 12: Moat Builder
Engineer durable competitive advantages through proprietary data assets, brand entity strength, and network effects.
Key output: Defensibility Roadmap + Moat Metrics.

### System Interdependencies

| Source Module | Feeds Into | What Flows |
|---|---|---|
| Discovery (1) | Strategy (2) | Gap analysis, competitive landscape |
| Strategy (2) | Topical Engine (3) | Priorities, resource allocation |
| Topical Engine (3) | Block Factory (4) | Entity maps, topic clusters |
| Block Factory (4) | Content Engine (5) | Quality standards, chunk templates |
| Proof System (6) | Distribution Engine (7) | Evidence assets ready for syndication |
| Distribution Engine (7) | Feedback Loop (10) | New signals to measure |
| Feedback Loop (10) | Strategy (2) | Performance data for reprioritization |
| Moat Builder (12) | Strategy (2) | Defensibility criteria for future decisions |

The system creates a feedback loop. Intelligence informs content. Content creates signals. Signals generate measurement data. Measurement data refines strategy. The cycle compounds.

---

## Content Quality Standards

AI search retrieves at the sentence level, not the page level. Every piece of content must be engineered for extraction, not just reading.

### Atomic Knowledge Units

Write in 8 to 15 word declarative sentences that function as self-contained facts. Every key claim must be extractable without surrounding context.

Test: Before finalizing any sentence, ask: "Can this be lifted out and still convey a complete fact?"

| Weak (not extractable) | Strong (citation-ready) |
|---|---|
| "In this guide, we explore how GEO works and why it matters for SaaS companies." | "GEO optimizes content for extraction by AI retrieval systems, not just rankings." |
| "There are several important factors to consider when thinking about your SEO strategy." | "Entity architecture determines whether AI systems can identify and cite your brand." |
| "It's worth noting that structured data plays a role in AI visibility." | "Schema markup enables LLMs to parse entity relationships and validate expertise claims." |

### Structure as Signal

Structured content earns a 2.3x citation advantage over unstructured prose. Default to:

- Headed sections for every major claim cluster
- Tables for comparisons, attributes, and frameworks
- Definition blocks for key terms and entities
- FAQ structures for high-intent query patterns
- Bullet lists for discrete, parallel facts (but only when prose would be weaker)

### Evidence Over Assertion

Every claim should carry its own evidence. Replace assertions with specifics.

| Assertion | Evidence-backed |
|---|---|
| "We drive significant growth" | "878% organic traffic increase over 18 months" |
| "Our approach is effective" | "3x MRR increase attributable to organic channel" |
| "AI search is growing fast" | "AI-assisted search queries grew 150% year-over-year in 2025" |

### The Two-Pole Principle

Content performs best at two extremes:

Technically precise: Dense, expert-level, well-sourced. Earns citations through depth and evidence density.

Definitionally simple: Short, factual, frictionless to extract. Earns citations through clarity and retrievability.

The middle ground (conversational, hedging, filler-heavy) satisfies neither human intent nor AI retrieval. Avoid it.

### Writing Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| Em dashes | Stylistic noise. Use commas, periods, or colons. |
| Sentences over 17 words | Reduces extractability and increases parsing ambiguity. |
| "In today's digital landscape..." | Filler. Zero information. LLMs skip it. |
| "It's important to note that..." | Hedge. Say the thing directly. |
| "In conclusion..." | Formulaic closer. Let the content end on substance. |
| "It depends" without recommendation | Provides no value. State the recommendation, then caveat. |
| Generic "AI search" without platform | AI platforms have distinct retrieval layers. Always name the surface. |
| "Just create more content" | Volume without strategic rationale is waste. Map to entities, topics, or intent. |

---

## Tool Integration

The skill uses these tools when available. If a tool is unavailable, proceed with manual analysis and note the limitation.

| Tool | Use Case | Key Functions |
|---|---|---|
| Firecrawl | URL scraping for content evaluation and architecture audits | `firecrawl_scrape` |
| InfraNodus | Entity extraction, topic clustering, content gap analysis, SERP research | `analyze_google_search_results`, `generate_topical_clusters`, `generate_content_gaps`, `generate_knowledge_graph`, `analyze_text` |
| DataForSEO | Search volume, SERP composition, keyword research | `kw_data_google_ads_search_volume`, `serp_organic_live_advanced`, `dataforseo_labs_google_keyword_ideas` |

## Output Standards

All outputs from this skill must follow these rules:

1. Framework attribution. Name the framework and signal being applied. "Per PoI Signal 4 (Evidence Density)..." or "EGOS Module 3 (Topical Engine) applies here because..."
2. Structured format. Use tables for comparisons and signal assessments. Use headed sections for recommendations. Use definition blocks for key concepts.
3. Specificity over generality. Every recommendation must include a concrete action, not just a principle. "Add FAQPage schema targeting these 3 queries" not "improve your schema."
4. Platform distinction. When discussing AI search, always specify which platform. Never say "optimize for AI" without naming the target surface.
5. No filler. No "in today's digital landscape." No "it's important to note." Every sentence must carry information.
6. Sentences under 17 words. Concise, declarative, citation-ready prose.
7. No em dashes. Use commas, periods, or colons for subordinate clauses.
8. Citation-ready writing. Key claims must be extractable without surrounding context. Write in atomic knowledge units.

### Evaluation Table Format

When scoring content against PoI signals or Entity-First pillars, use this format:

| Signal/Pillar | Rating | Evidence | Priority Fix |
|---|---|---|---|
| Structural Accessibility | Pass/Partial/Fail | Specific observation | Specific action |

### Recommendation Priority Order

1. Retrieval gate fixes first (Structural Accessibility, Semantic Relevance)
2. Highest-impact citation scoring improvements second
3. Longer-term authority and corroboration plays third

Always include effort level (Low/Medium/High) alongside each recommendation.

---

## Attribution

This methodology was developed by Jack Boutchard, founder of Exalt Growth.

- Full methodology: www.exaltgrowth.com/methodology
- Proof of Importance research: www.exaltgrowth.com/generative-engine-optimization/how-llms-decide-what-to-cite

