---
layout: default
title: BRIDGE: Budget-aware Reasoning via Intermediate Distillation with Guided Examples
---

# BRIDGE: Budget-aware Reasoning via Intermediate Distillation with Guided Examples
**arXiv**：[2512.20403v1](https://arxiv.org/abs/2512.20403) · [PDF](https://arxiv.org/pdf/2512.20403.pdf)  
**作者**：Xuan-An Le, Minh-Nam Tran, Son Nguyen  

**一句话要点**：提出BRIDGE框架，通过中间蒸馏解决大模型到小模型知识蒸馏中的容量差距与预算限制问题。

**关键词**：知识蒸馏, 预算感知推理, 中间模型, 合成数据生成, 模型压缩

## 3 点简述
- 核心问题：大模型与小模型间容量差距大，直接蒸馏效果差，且API成本高限制数据收集。
- 方法要点：采用两阶段框架，先训练中等规模教师助手，再生成合成数据训练小模型，利用预算不对称性。
- 实验或效果：在医疗、法律和金融基准上，学生模型性能提升28-41%，使用资源减少90%。

## 摘要（原文）

> Distilling knowledge from large proprietary models (e.g., GPT-4) to tiny deployable models (less than 1B parameters) faces a critical capacity-budget trap: the 1000x capacity gap between teachers and students prevents effective direct transfer, while API costs prohibit extensive data collection. We introduce BRIDGE (Budget-Aware Reasoning via Intermediate Distillation), a two-phase framework that resolves these constraints through strategic intermediation and budget asymmetry. In Phase 1, a mid-sized Teacher Assistant (TA; e.g., about 7B) learns from the black-box teacher on a strictly limited subset of data (e.g., 3-5%), selected via a zero-API-cost pipeline that balances entropic difficulty and semantic diversity using only local TA inference. In Phase 2, we exploit this asymmetry-teacher queries are expensive, whereas TA inference is free to amplify supervision: the refined TA generates synthetic rationales for the full dataset to train the tiny student. Crucially, we apply an instruction-tuning curriculum to establish behavioral alignment in the tiny student before transferring reasoning. Our theoretical analysis shows that BRIDGE yields tighter generalization bounds than direct distillation when data is abundant. Experiments across medical, legal, and financial benchmarks demonstrate consistent improvements: BRIDGE delivers student performance gains of 28-41%, closing the capability gap with proprietary teachers by 12-16% while using 10x fewer teacher queries. Notably, BRIDGE defies the conventional cost-performance frontier, surpassing direct distillation baselines that use 100% of the budget while consuming only 5% of the resources.

