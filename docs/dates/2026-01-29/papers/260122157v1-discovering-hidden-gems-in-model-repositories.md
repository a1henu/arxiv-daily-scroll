---
layout: default
title: Discovering Hidden Gems in Model Repositories
---

# Discovering Hidden Gems in Model Repositories
**arXiv**：[2601.22157v1](https://arxiv.org/abs/2601.22157) · [PDF](https://arxiv.org/pdf/2601.22157.pdf)  
**作者**：Jonathan Kahana, Eliahu Horwitz, Yedid Hoshen  

**一句话要点**：提出基于多臂老虎机的高效模型发现方法，以解决公共模型库中优质模型被忽视的问题。

**关键词**：模型发现, 多臂老虎机, 序列减半算法, 模型评估, 公共模型库, 微调模型

## 3 点简述
- 核心问题：公共模型库中模型使用高度集中，可能忽视性能更优的冷门微调模型。
- 方法要点：将模型发现建模为多臂老虎机问题，优化序列减半算法以加速搜索。
- 实验或效果：在Llama-3.1-8B家族中，发现冷门模型将数学性能从83.2%提升至96.0%，加速发现超50倍。

## 摘要（原文）

> Public repositories host millions of fine-tuned models, yet community usage remains disproportionately concentrated on a small number of foundation checkpoints. We investigate whether this concentration reflects efficient market selection or if superior models are systematically overlooked. Through an extensive evaluation of over 2,000 models, we show the prevalence of "hidden gems", unpopular fine-tunes that significantly outperform their popular counterparts. Notably, within the Llama-3.1-8B family, we find rarely downloaded checkpoints that improve math performance from 83.2% to 96.0% without increasing inference costs. However, discovering these models through exhaustive evaluation of every uploaded model is computationally infeasible. We therefore formulate model discovery as a Multi-Armed Bandit problem and accelerate the Sequential Halving search algorithm by using shared query sets and aggressive elimination schedules. Our method retrieves top models with as few as 50 queries per candidate, accelerating discovery by over 50x.

