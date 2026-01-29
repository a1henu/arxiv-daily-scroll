---
layout: default
title: Efficient Evaluation of LLM Performance with Statistical Guarantees
---

# Efficient Evaluation of LLM Performance with Statistical Guarantees
**arXiv**：[2601.20251v1](https://arxiv.org/abs/2601.20251) · [PDF](https://arxiv.org/pdf/2601.20251.pdf)  
**作者**：Skyler Wu, Yash Nair, Emmanuel J. Candés  

**一句话要点**：提出因子化主动查询方法，以有限查询预算高效评估大语言模型性能并保证统计覆盖。

**关键词**：大语言模型评估, 主动查询, 统计推断, 置信区间, 贝叶斯因子模型, 基准测试

## 3 点简述
- 核心问题：大语言模型在大型基准套件上的全面评估成本高昂，需在固定查询预算下获得紧致置信区间。
- 方法要点：结合贝叶斯因子模型利用历史信息，采用混合方差减少/主动学习策略自适应选择问题，通过主动推断扩展保证覆盖有效性。
- 实验或效果：在两种基准套件上，相比强基线实现高达5倍有效样本量增益，显著减少查询需求。

## 摘要（原文）

> Exhaustively evaluating many large language models (LLMs) on a large suite of benchmarks is expensive. We cast benchmarking as finite-population inference and, under a fixed query budget, seek tight confidence intervals (CIs) for model accuracy with valid frequentist coverage. We propose Factorized Active Querying (FAQ), which (a) leverages historical information through a Bayesian factor model; (b) adaptively selects questions using a hybrid variance-reduction/active-learning sampling policy; and (c) maintains validity through Proactive Active Inference -- a finite-population extension of active inference (Zrnic & Candes, 2024) that enables direct question selection while preserving coverage. With negligible overhead cost, FAQ delivers up to $5\times$ effective sample size gains over strong baselines on two benchmark suites, across varying historical-data missingness levels: this means that it matches the CI width of uniform sampling while using up to $5\times$ fewer queries. We release our source code and our curated datasets to support reproducible evaluation and future research.

