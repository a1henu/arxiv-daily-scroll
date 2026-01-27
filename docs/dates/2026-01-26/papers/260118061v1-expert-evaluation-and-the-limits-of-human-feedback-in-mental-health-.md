---
layout: default
title: Expert Evaluation and the Limits of Human Feedback in Mental Health AI Safety Testing
---

# Expert Evaluation and the Limits of Human Feedback in Mental Health AI Safety Testing
**arXiv**：[2601.18061v1](https://arxiv.org/abs/2601.18061) · [PDF](https://arxiv.org/pdf/2601.18061.pdf)  
**作者**：Kiana Jafari, Paul Ulrich Nikolaus Rust, Duncan Eddy, Robbie Fraser, Nina Vasan, Darja Djordjevic, Akanksha Dadlani, Max Lamparth, Eugenia Kim, Mykel Kochenderfer  

**一句话要点**：揭示心理健康AI安全测试中专家反馈的局限性，质疑基于共识的聚合方法。

**关键词**：心理健康AI安全, 专家反馈评估, 评分者间信度, 安全关键AI, 共识聚合方法, 临床框架分歧

## 3 点简述
- 核心问题：专家反馈在心理健康AI安全评估中是否可靠，高安全风险下专家共识假设面临挑战。
- 方法要点：三位认证精神科医生独立评估LLM生成响应，使用校准评分标准，分析评分者间信度。
- 实验或效果：评分者间信度低（ICC 0.087–0.295），自杀自伤类别分歧最大，定性访谈揭示分歧源于不同临床框架。

## 摘要（原文）

> Learning from human feedback~(LHF) assumes that expert judgments, appropriately aggregated, yield valid ground truth for training and evaluating AI systems. We tested this assumption in mental health, where high safety stakes make expert consensus essential. Three certified psychiatrists independently evaluated LLM-generated responses using a calibrated rubric. Despite similar training and shared instructions, inter-rater reliability was consistently poor ($ICC$ $0.087$--$0.295$), falling below thresholds considered acceptable for consequential assessment. Disagreement was highest on the most safety-critical items. Suicide and self-harm responses produced greater divergence than any other category, and was systematic rather than random. One factor yielded negative reliability (Krippendorff's $α= -0.203$), indicating structured disagreement worse than chance. Qualitative interviews revealed that disagreement reflects coherent but incompatible individual clinical frameworks, safety-first, engagement-centered, and culturally-informed orientations, rather than measurement error. By demonstrating that experts rely on holistic risk heuristics rather than granular factor discrimination, these findings suggest that aggregated labels function as arithmetic compromises that effectively erase grounded professional philosophies. Our results characterize expert disagreement in safety-critical AI as a sociotechnical phenomenon where professional experience introduces sophisticated layers of principled divergence. We discuss implications for reward modeling, safety classification, and evaluation benchmarks, recommending that practitioners shift from consensus-based aggregation to alignment methods that preserve and learn from expert disagreement.

