---
layout: default
title: Whatever Remains Must Be True: Filtering Drives Reasoning in LLMs, Shaping Diversity
---

# Whatever Remains Must Be True: Filtering Drives Reasoning in LLMs, Shaping Diversity
**arXiv**：[2512.05962v1](https://arxiv.org/abs/2512.05962) · [PDF](https://arxiv.org/pdf/2512.05962.pdf)  
**作者**：Germán Kruszewski, Pierre Erbacher, Jos Rozen, Marc Dymetman  

**一句话要点**：提出基于α-散度的过滤方法以解决LLM推理任务中的多样性损失问题

**关键词**：大语言模型推理, 强化学习调优, α-散度, 精度-多样性权衡, 定理证明基准, 过滤方法

## 3 点简述
- 核心问题：强化学习调优LLM导致多样性损失，源于反向KL散度的模式寻求特性
- 方法要点：通过过滤错误答案构建目标分布，使用α-散度近似以控制精度-多样性权衡
- 实验或效果：在Lean定理证明基准上，沿覆盖-精度帕累托前沿实现最优性能

## 摘要（原文）

> Reinforcement Learning (RL) has become the de facto standard for tuning LLMs to solve tasks involving reasoning. However, growing evidence shows that models trained in such way often suffer from a significant loss in diversity. We argue that this arises because RL implicitly optimizes the "mode-seeking" or "zero-forcing" Reverse KL to a target distribution causing the model to concentrate mass on certain high-probability regions of the target while neglecting others. In this work, we instead begin from an explicit target distribution, obtained by filtering out incorrect answers while preserving the relative probabilities of correct ones. Starting from a pre-trained LLM, we approximate this target distribution using the $α$-divergence family, which unifies prior approaches and enables direct control of the precision-diversity trade-off by interpolating between mode-seeking and mass-covering divergences. On a Lean theorem-proving benchmark, our method achieves state-of-the-art performance along the coverage-precision Pareto frontier, outperforming all prior methods on the coverage axis.

