---
layout: default
title: ActiveUltraFeedback: Efficient Preference Data Generation using Active Learning
---

# ActiveUltraFeedback: Efficient Preference Data Generation using Active Learning
**arXiv**：[2603.09692v1](https://arxiv.org/abs/2603.09692) · [PDF](https://arxiv.org/pdf/2603.09692.pdf)  
**作者**：Davit Melikidze, Marian Schneider, Jessica Lam, Martin Wertich, Ido Hakimi, Barna Pásztor, Andreas Krause  

**一句话要点**：提出ActiveUltraFeedback，通过主动学习高效生成偏好数据以解决RLHF成本瓶颈

**关键词**：主动学习, 偏好数据生成, RLHF, 不确定性估计, 标注效率

## 3 点简述
- 核心问题：RLHF中偏好数据获取成本高，尤其在低资源和专家领域
- 方法要点：利用不确定性估计动态选择信息量大的响应进行标注，引入DRTS和DeltaUCB新方法
- 实验或效果：仅需六分之一标注数据即可达到或超越静态基线，提升下游性能

## 摘要（原文）

> Reinforcement Learning from Human Feedback (RLHF) has become the standard for aligning Large Language Models (LLMs), yet its efficacy is bottlenecked by the high cost of acquiring preference data, especially in low-resource and expert domains. To address this, we introduce ACTIVEULTRAFEEDBACK, a modular active learning pipeline that leverages uncertainty estimates to dynamically identify the most informative responses for annotation. Our pipeline facilitates the systematic evaluation of standard response selection methods alongside DOUBLE REVERSE THOMPSON SAMPLING (DRTS) and DELTAUCB, two novel methods prioritizing response pairs with large predicted quality gaps, leveraging recent results showing that such pairs provide good signals for fine-tuning. Our experiments demonstrate that ACTIVEULTRAFEEDBACK yields high-quality datasets that lead to significant improvements in downstream performance, notably achieving comparable or superior results with as little as one-sixth of the annotated data relative to static baselines. Our pipeline is available at https://github.com/lasgroup/ActiveUltraFeedback and our preference datasets at https://huggingface.co/ActiveUltraFeedback.

