---
layout: default
title: NoRD: A Data-Efficient Vision-Language-Action Model that Drives without Reasoning
---

# NoRD: A Data-Efficient Vision-Language-Action Model that Drives without Reasoning
**arXiv**：[2602.21172v1](https://arxiv.org/abs/2602.21172) · [PDF](https://arxiv.org/pdf/2602.21172.pdf)  
**作者**：Ishaan Rawal, Shubh Gupta, Yihan Hu, Wei Zhan  

**一句话要点**：提出NoRD模型，以数据高效方式驱动自动驾驶，无需推理标注。

**关键词**：自动驾驶, 视觉-语言-动作模型, 数据高效学习, 难度偏差, 强化学习, 端到端架构

## 3 点简述
- 当前视觉-语言-动作模型依赖大规模数据和密集推理标注，成本高昂。
- NoRD通过减少训练数据和消除推理标注，使用Dr.~GRPO算法克服难度偏差。
- 在Waymo和NAVSIM上实现竞争性能，训练数据减少至<60%，令牌数降低3倍。

## 摘要（原文）

> Vision-Language-Action (VLA) models are advancing autonomous driving by replacing modular pipelines with unified end-to-end architectures. However, current VLAs face two expensive requirements: (1) massive dataset collection, and (2) dense reasoning annotations. In this work, we address both challenges with \modelname (\textbf{No} \textbf{R}easoning for \textbf{D}riving). Compared to existing VLAs, \modelname achieves competitive performance while being fine-tuned on $<$60\% of the data and no reasoning annotations, resulting in 3$\times$ fewer tokens. We identify that standard Group Relative Policy Optimization (GRPO) fails to yield significant improvements when applied to policies trained on such small, reasoning-free datasets. We show that this limitation stems from difficulty bias, which disproportionately penalizes reward signals from scenarios that produce high-variance rollouts within GRPO. \modelname overcomes this by incorporating Dr.~GRPO, a recent algorithm designed to mitigate difficulty bias in LLMs. As a result, \modelname achieves competitive performance on Waymo and NAVSIM with a fraction of the training data and no reasoning overhead, enabling more efficient autonomous systems.

