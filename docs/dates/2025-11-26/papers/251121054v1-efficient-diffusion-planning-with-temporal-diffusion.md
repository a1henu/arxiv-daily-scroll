---
layout: default
title: Efficient Diffusion Planning with Temporal Diffusion
---

# Efficient Diffusion Planning with Temporal Diffusion
**arXiv**：[2511.21054v1](https://arxiv.org/abs/2511.21054) · [PDF](https://arxiv.org/pdf/2511.21054.pdf)  
**作者**：Jiaming Guo, Rui Zhang, Zerun Li, Yunkai Gao, Shaohui Peng, Siming Lan, Xing Hu, Zidong Du, Xishan Zhang, Ling Li  

**一句话要点**：提出Temporal Diffusion Planner以提升扩散规划决策效率

**关键词**：扩散规划, 决策效率, 离线强化学习, 去噪过程, 自动重规划

## 3 点简述
- 扩散规划中频繁生成新计划导致高计算开销和低决策频率
- TDP通过时间维度分布去噪步骤，逐步更新而非重新生成计划
- 在D4RL实验中决策频率提升11-24.8倍，性能相当或更高

## 摘要（原文）

> Diffusion planning is a promising method for learning high-performance policies from offline data. To avoid the impact of discrepancies between planning and reality on performance, previous works generate new plans at each time step. However, this incurs significant computational overhead and leads to lower decision frequencies, and frequent plan switching may also affect performance. In contrast, humans might create detailed short-term plans and more general, sometimes vague, long-term plans, and adjust them over time. Inspired by this, we propose the Temporal Diffusion Planner (TDP) which improves decision efficiency by distributing the denoising steps across the time dimension. TDP begins by generating an initial plan that becomes progressively more vague over time. At each subsequent time step, rather than generating an entirely new plan, TDP updates the previous one with a small number of denoising steps. This reduces the average number of denoising steps, improving decision efficiency. Additionally, we introduce an automated replanning mechanism to prevent significant deviations between the plan and reality. Experiments on D4RL show that, compared to previous works that generate new plans every time step, TDP improves the decision-making frequency by 11-24.8 times while achieving higher or comparable performance.

