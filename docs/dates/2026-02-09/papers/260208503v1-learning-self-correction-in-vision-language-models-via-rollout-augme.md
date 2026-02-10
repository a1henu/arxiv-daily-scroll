---
layout: default
title: Learning Self-Correction in Vision-Language Models via Rollout Augmentation
---

# Learning Self-Correction in Vision-Language Models via Rollout Augmentation
**arXiv**：[2602.08503v1](https://arxiv.org/abs/2602.08503) · [PDF](https://arxiv.org/pdf/2602.08503.pdf)  
**作者**：Yi Ding, Ziliang Qiu, Bolian Li, Ruqi Zhang  

**一句话要点**：提出Octopus框架以解决视觉语言模型中自校正学习信号稀疏问题

**关键词**：视觉语言模型, 自校正学习, 强化学习, rollout增强, 推理能力, 样本效率

## 3 点简述
- 核心问题：现有强化学习方法在视觉语言模型中学习自校正时，因有效行为罕见导致信号稀疏。
- 方法要点：通过校正特定rollout合成密集自校正示例，结合响应掩码策略解耦自校正与直接推理。
- 实验或效果：Octopus-8B在7个基准测试中达到开源视觉语言模型最优性能，训练效率提升。

## 摘要（原文）

> Self-correction is essential for solving complex reasoning problems in vision-language models (VLMs). However, existing reinforcement learning (RL) methods struggle to learn it, as effective self-correction behaviors emerge only rarely, making learning signals extremely sparse. To address this challenge, we propose correction-specific rollouts (Octopus), an RL rollout augmentation framework that synthesizes dense self-correction examples by recombining existing rollouts. This augmentation simultaneously improves sample efficiency due to rollout reuse and stabilizes RL optimization through balanced supervision. Furthermore, we introduce a response-masking strategy that decouples self-correction from direct reasoning, avoiding signal conflicts and enabling both behaviors to be learned effectively. Building on this, we introduce Octopus-8B, a reasoning VLM with controllable self-correction capability. Across 7 benchmarks, it achieves SoTA performance among open-source VLMs, outperforming the best RLVR baseline by 1.0 score while requiring only $0.72\times$ training time per step.

