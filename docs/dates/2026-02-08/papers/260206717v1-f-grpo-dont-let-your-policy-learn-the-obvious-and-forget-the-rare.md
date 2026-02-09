---
layout: default
title: F-GRPO: Don't Let Your Policy Learn the Obvious and Forget the Rare
---

# F-GRPO: Don't Let Your Policy Learn the Obvious and Forget the Rare
**arXiv**：[2602.06717v1](https://arxiv.org/abs/2602.06717) · [PDF](https://arxiv.org/pdf/2602.06717.pdf)  
**作者**：Daniil Plyusov, Alexey Gorbatovski, Boris Shaposhnikov, Viacheslav Sinii, Alexey Malakhov, Daniil Gavrilov  

**一句话要点**：提出F-GRPO方法，通过难度感知优势缩放解决强化学习中罕见正确轨迹被忽略的问题。

**关键词**：强化学习, 组采样, 罕见轨迹, 优势缩放, Focal loss, 代码生成

## 3 点简述
- 核心问题：基于组采样的强化学习因计算限制，偏向常见轨迹，忽略罕见正确模式。
- 方法要点：引入受Focal loss启发的难度感知系数，降低高成功提示的更新权重，轻量集成到GRPO等算法。
- 实验或效果：在Qwen2.5-7B上提升pass@256性能，如GRPO从64.1增至70.3，不增加计算成本。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) is commonly based on group sampling to estimate advantages and stabilize policy updates. In practice, large group sizes are not feasible due to computational limits, which biases learning toward trajectories that are already likely. Smaller groups often miss rare-correct trajectories while still containing mixed rewards, concentrating probability on common solutions. We derive the probability that updates miss rare-correct modes as a function of group size, showing non-monotonic behavior, and characterize how updates redistribute mass within the correct set, revealing that unsampled-correct mass can shrink even as total correct mass grows. Motivated by this analysis, we propose a difficulty-aware advantage scaling coefficient, inspired by Focal loss, that down-weights updates on high-success prompts. The lightweight modification can be directly integrated into any group-relative RLVR algorithm such as GRPO, DAPO, and CISPO. On Qwen2.5-7B across in-domain and out-of-domain benchmarks, our method improves pass@256 from 64.1 $\rightarrow$ 70.3 (GRPO), 69.3 $\rightarrow$ 72.5 (DAPO), and 73.2 $\rightarrow$ 76.8 (CISPO), while preserving or improving pass@1, without increasing group size or computational cost.

