---
layout: default
title: Statsformer: Validated Ensemble Learning with LLM-Derived Semantic Priors
---

# Statsformer: Validated Ensemble Learning with LLM-Derived Semantic Priors
**arXiv**：[2601.21410v1](https://arxiv.org/abs/2601.21410) · [PDF](https://arxiv.org/pdf/2601.21410.pdf)  
**作者**：Erica Zhang, Naomi Sagan, Danny Tse, Fangzhao Zhang, Mert Pilanci, Jose Blanchet  

**一句话要点**：提出Statsformer框架，通过集成学习整合LLM语义先验以提升监督统计学习性能

**关键词**：集成学习, 语义先验, 监督学习, LLM整合, 交叉验证

## 3 点简述
- 现有方法整合LLM知识时适应性有限，易受幻觉影响或嵌入固定学习器
- Statsformer采用防护集成架构，将LLM特征先验嵌入线性和非线性学习器，通过交叉验证自适应校准
- 实验表明，信息性先验提升性能，非信息性先验被自动降权，减轻幻觉影响

## 摘要（原文）

> We introduce Statsformer, a principled framework for integrating large language model (LLM)-derived knowledge into supervised statistical learning. Existing approaches are limited in adaptability and scope: they either inject LLM guidance as an unvalidated heuristic, which is sensitive to LLM hallucination, or embed semantic information within a single fixed learner. Statsformer overcomes both limitations through a guardrailed ensemble architecture. We embed LLM-derived feature priors within an ensemble of linear and nonlinear learners, adaptively calibrating their influence via cross-validation. This design yields a flexible system with an oracle-style guarantee that it performs no worse than any convex combination of its in-library base learners, up to statistical error. Empirically, informative priors yield consistent performance improvements, while uninformative or misspecified LLM guidance is automatically downweighted, mitigating the impact of hallucinations across a diverse range of prediction tasks.

