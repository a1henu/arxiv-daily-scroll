---
layout: default
title: Alleviating Sparse Rewards by Modeling Step-Wise and Long-Term Sampling Effects in Flow-Based GRPO
---

# Alleviating Sparse Rewards by Modeling Step-Wise and Long-Term Sampling Effects in Flow-Based GRPO
**arXiv**：[2602.06422v1](https://arxiv.org/abs/2602.06422) · [PDF](https://arxiv.org/pdf/2602.06422.pdf)  
**作者**：Yunze Tong, Mushui Liu, Canyu Zhao, Wanggui He, Shiyi Zhang, Hongwei Zhang, Peng Zhang, Jinlong Liu, Ju Huang, Jiamang Wang, Hao Jiang, Pipei Huang  

**一句话要点**：提出TurningPoint-GRPO以解决流匹配模型在文本到图像生成中的稀疏奖励和长期依赖问题

**关键词**：文本到图像生成, 流匹配模型, GRPO框架, 稀疏奖励, 长期依赖, 转折点检测

## 3 点简述
- 现有GRPO方法传播基于结果的奖励，忽略去噪步骤的局部效应和轨迹内依赖
- TP-GRPO引入步级增量奖励和转折点检测，建模去噪动作的纯效应和延迟影响
- 实验表明TP-GRPO能更有效利用奖励信号，提升生成质量，且无需超参数

## 摘要（原文）

> Deploying GRPO on Flow Matching models has proven effective for text-to-image generation. However, existing paradigms typically propagate an outcome-based reward to all preceding denoising steps without distinguishing the local effect of each step. Moreover, current group-wise ranking mainly compares trajectories at matched timesteps and ignores within-trajectory dependencies, where certain early denoising actions can affect later states via delayed, implicit interactions. We propose TurningPoint-GRPO (TP-GRPO), a GRPO framework that alleviates step-wise reward sparsity and explicitly models long-term effects within the denoising trajectory. TP-GRPO makes two key innovations: (i) it replaces outcome-based rewards with step-level incremental rewards, providing a dense, step-aware learning signal that better isolates each denoising action's "pure" effect, and (ii) it identifies turning points-steps that flip the local reward trend and make subsequent reward evolution consistent with the overall trajectory trend-and assigns these actions an aggregated long-term reward to capture their delayed impact. Turning points are detected solely via sign changes in incremental rewards, making TP-GRPO efficient and hyperparameter-free. Extensive experiments also demonstrate that TP-GRPO exploits reward signals more effectively and consistently improves generation. Demo code is available at https://github.com/YunzeTong/TurningPoint-GRPO.

