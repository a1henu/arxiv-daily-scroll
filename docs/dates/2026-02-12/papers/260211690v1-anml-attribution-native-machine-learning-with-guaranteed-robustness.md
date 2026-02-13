---
layout: default
title: ANML: Attribution-Native Machine Learning with Guaranteed Robustness
---

# ANML: Attribution-Native Machine Learning with Guaranteed Robustness
**arXiv**：[2602.11690v1](https://arxiv.org/abs/2602.11690) · [PDF](https://arxiv.org/pdf/2602.11690.pdf)  
**作者**：Oliver Zahn, Matt Beton, Simran Chana  

**一句话要点**：提出ANML框架，通过质量加权训练样本提升模型性能并支持溯源，应用于专家数据场景。

**关键词**：样本加权训练, 数据溯源, 模型鲁棒性, 梯度一致性, 贡献者声誉, 自适应门控

## 3 点简述
- 问题：前沿AI系统训练中专家数据样本权重处理不当，未区分贡献质量。
- 方法：基于梯度一致性、验证状态、贡献者声誉和时间相关性四因素加权样本。
- 效果：在多个数据集上误差降低33-72%，质量加权训练数据效率高，抗攻击能力强。

## 摘要（原文）

> Frontier AI systems increasingly train on specialized expert data, from clinical records to proprietary research to curated datasets, yet current training pipelines treat all samples identically. A Nobel laureate's contribution receives the same weight as an unverified submission. We introduce ANML (Attribution-Native Machine Learning), a framework that weights training samples by four quality factors: gradient-based consistency (q), verification status (v), contributor reputation (r), and temporal relevance (T). By combining what the model observes (gradient signals) with what the system knows about data provenance (external signals), ANML produces per-contributor quality weights that simultaneously improve model performance and enable downstream attribution. Across 5 datasets (178-32,561 samples), ANML achieves 33-72% error reduction over gradient-only baselines. Quality-weighted training is data-efficient: 20% high-quality data outperforms 100% uniformly weighted data by 47%. A Two-Stage Adaptive gating mechanism guarantees that ANML never underperforms the best available baseline, including under strategic joint attacks combining credential faking with gradient alignment. When per-sample detection fails against subtle corruption, contributor-level attribution provides 1.3-5.3x greater improvement than sample-level methods, with the advantage growing as corruption becomes harder to detect.

