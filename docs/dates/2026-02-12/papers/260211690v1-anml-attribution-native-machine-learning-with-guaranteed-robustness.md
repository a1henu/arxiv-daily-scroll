---
layout: default
title: ANML: Attribution-Native Machine Learning with Guaranteed Robustness
---

# ANML: Attribution-Native Machine Learning with Guaranteed Robustness
**arXiv**：[2602.11690v1](https://arxiv.org/abs/2602.11690) · [PDF](https://arxiv.org/pdf/2602.11690.pdf)  
**作者**：Oliver Zahn, Matt Beton, Simran Chana  

**一句话要点**：提出ANML框架，通过质量加权训练解决专家数据中样本贡献不均问题，提升模型性能与可追溯性。

**关键词**：质量加权训练, 数据溯源, 鲁棒性保证, 梯度一致性, 贡献者声誉, 自适应门控

## 3 点简述
- 核心问题：当前训练管道平等对待所有样本，忽略专家数据中贡献者质量差异，影响模型性能与数据溯源。
- 方法要点：引入四个质量因子（梯度一致性、验证状态、贡献者声誉、时间相关性）加权训练样本，结合Two-Stage Adaptive门控机制保证鲁棒性。
- 实验或效果：在5个数据集上实现33-72%错误率降低，20%高质量数据性能优于100%均匀加权数据47%，贡献者级溯源在检测困难时优于样本级方法。

## 摘要（原文）

> Frontier AI systems increasingly train on specialized expert data, from clinical records to proprietary research to curated datasets, yet current training pipelines treat all samples identically. A Nobel laureate's contribution receives the same weight as an unverified submission. We introduce ANML (Attribution-Native Machine Learning), a framework that weights training samples by four quality factors: gradient-based consistency (q), verification status (v), contributor reputation (r), and temporal relevance (T). By combining what the model observes (gradient signals) with what the system knows about data provenance (external signals), ANML produces per-contributor quality weights that simultaneously improve model performance and enable downstream attribution. Across 5 datasets (178-32,561 samples), ANML achieves 33-72% error reduction over gradient-only baselines. Quality-weighted training is data-efficient: 20% high-quality data outperforms 100% uniformly weighted data by 47%. A Two-Stage Adaptive gating mechanism guarantees that ANML never underperforms the best available baseline, including under strategic joint attacks combining credential faking with gradient alignment. When per-sample detection fails against subtle corruption, contributor-level attribution provides 1.3-5.3x greater improvement than sample-level methods, with the advantage growing as corruption becomes harder to detect.

