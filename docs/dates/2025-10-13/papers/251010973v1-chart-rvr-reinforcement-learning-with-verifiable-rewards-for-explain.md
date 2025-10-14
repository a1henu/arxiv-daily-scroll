---
layout: default
title: Chart-RVR: Reinforcement Learning with Verifiable Rewards for Explainable Chart Reasoning
---

# Chart-RVR: Reinforcement Learning with Verifiable Rewards for Explainable Chart Reasoning
**arXiv**：[2510.10973v1](https://arxiv.org/abs/2510.10973) · [PDF](https://arxiv.org/pdf/2510.10973.pdf)  
**作者**：Sanchit Sinha, Oana Frunza, Kashif Rasul, Yuriy Nevmyvaka, Aidong Zhang  

**一句话要点**：提出Chart-RVR框架，通过可验证奖励增强大视觉语言模型在图表推理中的鲁棒性和可解释性。

**关键词**：图表推理, 强化学习, 可验证奖励, 大视觉语言模型, 可解释性, 分布外鲁棒性

## 3 点简述
- 核心问题：大视觉语言模型在分布外数据和生成可解释推理链时性能下降。
- 方法要点：结合群组相对策略优化与自动可验证奖励，优化图表分类、表格重建和过程一致性。
- 实验或效果：在多个基准测试中超越标准微调，缩小分布外性能差距并提高推理链忠实度。

## 摘要（原文）

> The capabilities of Large Vision-Language Models (LVLMs) have reached
> state-of-the-art on many visual reasoning tasks, including chart reasoning, yet
> they still falter on out-of-distribution (OOD) data, and degrade further when
> asked to produce their chain-of-thought (CoT) rationales, limiting
> explainability. We present Chart-RVR, a general framework that fine-tunes LVLMs
> to be more robust and explainable for chart reasoning by coupling Group
> Relative Policy Optimization (GRPO) with automatically verifiable rewards. Our
> framework comprises of three rewards that maximize: (i) correct chart-type
> classification, (ii) faithful chart table reconstruction, and (iii) process
> conformity. Applied to 3-billion-parameter LVLMs, Chart-RVR consistently
> outperforms standard supervised fine-tuning (SFT) on both in-distribution and
> out-of-distribution datasets, closing the OOD performance gap while improving
> rationale fidelity. The resulting models, the Chart-RVR-3B series, achieve
> state-of-the-art results on six chart-reasoning benchmarks spanning in-domain
> and OOD settings, surpassing all existing models of comparable size. Beyond
> accuracy, Chart-RVR yields more interpretable CoT rationales, strengthening
> trust and reliability - showcasing the power of verifiable rewards with GRPO
> for training reliable, interpretable chart-reasoning models.

