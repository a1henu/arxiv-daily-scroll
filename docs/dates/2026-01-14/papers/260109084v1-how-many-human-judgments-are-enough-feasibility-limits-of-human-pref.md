---
layout: default
title: How Many Human Judgments Are Enough? Feasibility Limits of Human Preference Evaluation
---

# How Many Human Judgments Are Enough? Feasibility Limits of Human Preference Evaluation
**arXiv**：[2601.09084v1](https://arxiv.org/abs/2601.09084) · [PDF](https://arxiv.org/pdf/2601.09084.pdf)  
**作者**：Wilson Y. Lee  

**一句话要点**：揭示人类偏好评估中样本量不足导致检测能力受限，提出优化策略以提升模型比较可靠性

**关键词**：人类偏好评估, 样本量优化, 模型比较, 检测能力, 提示变异性, 评估协议

## 3 点简述
- 核心问题：人类偏好评估中，样本量不足常导致无法可靠检测模型间微小改进，而非模型等效
- 方法要点：分析显示，当偏好信号在提示间分散时，比例分配为最优策略，但需大量判断；减少提示变异性可提升检测能力
- 实验或效果：实证表明，大规模数据集普遍存在分散偏好，而优化基准能通过降低方差实现1.5倍检测能力提升

## 摘要（原文）

> Human preference evaluations are widely used to compare generative models, yet it remains unclear how many judgments are required to reliably detect small improvements. We show that when preference signal is diffuse across prompts (i.e., all prompt types are similarly informative), proportional allocation is minimax-optimal: no allocation strategy substantially improves detectability. Empirical analysis of large-scale human preference datasets shows that most comparisons fall into this diffuse regime, exhibiting small preference margins that require far more judgments than typically collected, even in well-sampled comparisons. These limits persist across evaluation protocols and modalities, including chat, image generation, and code generation with execution feedback. In contrast, curated benchmarks that reduce prompt induced variability systematically induce larger margins and improve detectability through a $1.5\times$ reduction in prompt-level variance. Our results show that inconclusive or negative human evaluation outcomes frequently reflect underpowered evaluation rather than model equivalence, underscoring the need to account explicitly for effect size, budget, and protocol design.

