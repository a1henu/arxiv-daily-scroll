---
layout: default
title: Discovering Hidden Gems in Model Repositories
---

# Discovering Hidden Gems in Model Repositories
**arXiv**：[2601.22157v1](https://arxiv.org/abs/2601.22157) · [PDF](https://arxiv.org/pdf/2601.22157.pdf)  
**作者**：Jonathan Kahana, Eliahu Horwitz, Yedid Hoshen  

**一句话要点**：提出基于多臂老虎机的方法，加速发现模型仓库中性能优越但被忽视的微调模型。

**关键词**：模型发现, 多臂老虎机, 序列减半搜索, 模型仓库, 微调模型, 性能评估

## 3 点简述
- 核心问题：公共模型仓库中，社区使用高度集中于少数基础模型，可能遗漏性能更优的微调模型。
- 方法要点：将模型发现建模为多臂老虎机问题，通过共享查询集和激进淘汰策略加速序列减半搜索算法。
- 实验或效果：在Llama-3.1-8B家族中，发现罕见下载的检查点将数学性能从83.2%提升至96.0%，且发现速度提升超过50倍。

## 摘要（原文）

> Public repositories host millions of fine-tuned models, yet community usage remains disproportionately concentrated on a small number of foundation checkpoints. We investigate whether this concentration reflects efficient market selection or if superior models are systematically overlooked. Through an extensive evaluation of over 2,000 models, we show the prevalence of "hidden gems", unpopular fine-tunes that significantly outperform their popular counterparts. Notably, within the Llama-3.1-8B family, we find rarely downloaded checkpoints that improve math performance from 83.2% to 96.0% without increasing inference costs. However, discovering these models through exhaustive evaluation of every uploaded model is computationally infeasible. We therefore formulate model discovery as a Multi-Armed Bandit problem and accelerate the Sequential Halving search algorithm by using shared query sets and aggressive elimination schedules. Our method retrieves top models with as few as 50 queries per candidate, accelerating discovery by over 50x.

