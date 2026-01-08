---
layout: default
title: ETR: Outcome-Guided Elastic Trust Regions for Policy Optimization
---

# ETR: Outcome-Guided Elastic Trust Regions for Policy Optimization
**arXiv**：[2601.03723v1](https://arxiv.org/abs/2601.03723) · [PDF](https://arxiv.org/pdf/2601.03723.pdf)  
**作者**：Shijie Zhang, Kevin Zhang, Zheyuan Gu, Xiang Guo, Rujun Guo, Shaoyu Liu, Guanjun Jiang, Xiaozhao Wang  

**一句话要点**：提出弹性信任区域（ETR）以解决强化学习中静态约束导致的信号利用不足问题。

**关键词**：强化学习, 策略优化, 信任区域, 信号异质性, 动态约束, 结果驱动学习

## 3 点简述
- 核心问题：GRPO算法使用均匀静态信任区域约束，假设信号同质，与结果驱动学习的异质性不匹配。
- 方法要点：ETR通过基于优势幅度和组方差的动态机制，调整优化约束以匹配信号质量。
- 实验或效果：在AIME和MATH基准测试中，ETR优于GRPO，提高准确性并缓解策略熵退化。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as an important paradigm for unlocking reasoning capabilities in large language models, exemplified by the success of OpenAI o1 and DeepSeek-R1. Currently, Group Relative Policy Optimization (GRPO) stands as the dominant algorithm in this domain due to its stable training and critic-free efficiency. However, we argue that GRPO suffers from a structural limitation: it imposes a uniform, static trust region constraint across all samples. This design implicitly assumes signal homogeneity, a premise misaligned with the heterogeneous nature of outcome-driven learning, where advantage magnitudes and variances fluctuate significantly. Consequently, static constraints fail to fully exploit high-quality signals while insufficiently suppressing noise, often precipitating rapid entropy collapse. To address this, we propose \textbf{E}lastic \textbf{T}rust \textbf{R}egions (\textbf{ETR}), a dynamic mechanism that aligns optimization constraints with signal quality. ETR constructs a signal-aware landscape through dual-level elasticity: at the micro level, it scales clipping boundaries based on advantage magnitude to accelerate learning from high-confidence paths; at the macro level, it leverages group variance to implicitly allocate larger update budgets to tasks in the optimal learning zone. Extensive experiments on AIME and MATH benchmarks demonstrate that ETR consistently outperforms GRPO, achieving superior accuracy while effectively mitigating policy entropy degradation to ensure sustained exploration.

