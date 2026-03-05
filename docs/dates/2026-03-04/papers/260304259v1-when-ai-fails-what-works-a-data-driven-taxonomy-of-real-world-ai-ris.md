---
layout: default
title: When AI Fails, What Works? A Data-Driven Taxonomy of Real-World AI Risk Mitigation Strategies
---

# When AI Fails, What Works? A Data-Driven Taxonomy of Real-World AI Risk Mitigation Strategies
**arXiv**：[2603.04259v1](https://arxiv.org/abs/2603.04259) · [PDF](https://arxiv.org/pdf/2603.04259.pdf)  
**作者**：Evgenija Popchanovska, Ana Gjorgjevikj, Maryan Rizinski, Lubomir Chitkushev, Irena Vodenska, Dimitar Trajanov  

**一句话要点**：提出基于真实AI事件的数据驱动分类法，以缓解系统风险

**关键词**：AI风险缓解, 系统漏洞分类, 数据驱动分析, 事件响应, 端到端监控

## 3 点简述
- 核心问题：AI模型失败在高风险工作流中引发系统性崩溃，需从模型风险转向端到端漏洞管理。
- 方法要点：分析9705篇媒体报道，通过结构化提示提取6893篇中的缓解行动，扩展MIT分类法。
- 实验或效果：新增4个缓解类别，标注23994个标签，覆盖范围增加67%，提升对新兴失败模式的适用性。

## 摘要（原文）

> Large language models (LLMs) are increasingly embedded in high-stakes workflows, where failures propagate beyond isolated model errors into systemic breakdowns that can lead to legal exposure, reputational damage, and material financial losses. Building on this shift from model-centric risks to end-to-end system vulnerabilities, we analyze real-world AI incident reporting and mitigation actions to derive an empirically grounded taxonomy that links failure dynamics to actionable interventions. Using a unified corpus of 9,705 media-reported AI incident articles, we extract explicit mitigation actions from 6,893 texts via structured prompting and then systematically classify responses to extend MIT's AI Risk Mitigation Taxonomy. Our taxonomy introduces four new mitigation categories, including 1) Corrective and Restrictive Actions, 2) Legal/Regulatory and Enforcement Actions, 3) Financial, Economic, and Market Controls, and 4) Avoidance and Denial, capturing response patterns that are becoming increasingly prevalent as AI deployment and regulation evolve. Quantitatively, we label the mitigation dataset with 32 distinct labels, producing 23,994 label assignments; 9,629 of these reflect previously unseen mitigation patterns, yielding a 67% increase of the original subcategory coverage and substantially enhancing the taxonomy's applicability to emerging systemic failure modes. By structuring incident responses, the paper strengthens "diagnosis-to-prescription" guidance and advances continuous, taxonomy-aligned post-deployment monitoring to prevent cascading incidents and downstream impact.

