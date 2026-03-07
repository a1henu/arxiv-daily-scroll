---
layout: default
title: Design Behaviour Codes (DBCs): A Taxonomy-Driven Layered Governance Benchmark for Large Language Models
---

# Design Behaviour Codes (DBCs): A Taxonomy-Driven Layered Governance Benchmark for Large Language Models
**arXiv**：[2603.04837v1](https://arxiv.org/abs/2603.04837) · [PDF](https://arxiv.org/pdf/2603.04837.pdf)  
**作者**：G. Madan Mohan, Veena Kiran Nambiar, Kiranmayee Janardhan  

**一句话要点**：提出动态行为约束基准，评估推理时治理层对大语言模型风险控制的效果。

**关键词**：大语言模型治理, 行为约束基准, 风险分类评估, 推理时控制, 模型无关治理, 可审计性

## 3 点简述
- 核心问题：现有对齐方法如RLHF或后处理API在模型无关、可审计治理方面存在不足。
- 方法要点：引入MDBC系统，作为结构化150控制项的提示层治理，基于30领域风险分类进行评估。
- 实验或效果：DBC层将风险暴露率从7.19%降至4.55%，相对风险降低36.8%，优于标准安全提示。

## 摘要（原文）

> We introduce the Dynamic Behavioral Constraint (DBC) benchmark, the first empirical framework for evaluating the efficacy of a structured, 150-control behavioral governance layer, the MDBC (Madan DBC) system, applied at inference time to large language models (LLMs). Unlike training time alignment methods (RLHF, DPO) or post-hoc content moderation APIs, DBCs constitute a system prompt level governance layer that is model-agnostic, jurisdiction-mappable, and auditable. We evaluate the DBC Framework across a 30 domain risk taxonomy organized into six clusters (Hallucination and Calibration, Bias and Fairness, Malicious Use, Privacy and Data Protection, Robustness and Reliability, and Misalignment Agency) using an agentic red-team protocol with five adversarial attack strategies (Direct, Roleplay, Few-Shot, Hypothetical, Authority Spoof) across 3 model families. Our three-arm controlled design (Base, Base plus Moderation, Base plus DBC) enables causal attribution of risk reduction. Key findings: the DBC layer reduces the aggregate Risk Exposure Rate (RER) from 7.19 percent (Base) to 4.55 percent (Base plus DBC), representing a 36.8 percent relative risk reduction, compared with 0.6 percent for a standard safety moderation prompt. MDBC Adherence Scores improve from 8.6 by 10 (Base) to 8.7 by 10 (Base plus DBC). EU AI Act compliance (automated scoring) reaches 8.5by 10 under the DBC layer. A three judge evaluation ensemble yields Fleiss kappa greater than 0.70 (substantial agreement), validating our automated pipeline. Cluster ablation identifies the Integrity Protection cluster (MDBC 081 099) as delivering the highest per domain risk reduction, while graybox adversarial attacks achieve a DBC Bypass Rate of 4.83 percent . We release the benchmark code, prompt database, and all evaluation artefacts to enable reproducibility and longitudinal tracking as models evolve.

