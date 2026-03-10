---
layout: default
title: Don't Look Back in Anger: MAGIC Net for Streaming Continual Learning with Temporal Dependence
---

# Don't Look Back in Anger: MAGIC Net for Streaming Continual Learning with Temporal Dependence
**arXiv**：[2603.08600v1](https://arxiv.org/abs/2603.08600) · [PDF](https://arxiv.org/pdf/2603.08600.pdf)  
**作者**：Federico Giannini, Sandro D'Andrea, Emanuele Della Valle  

**一句话要点**：提出MAGIC Net以解决流式持续学习中概念漂移、时间依赖和灾难性遗忘问题。

**关键词**：流式持续学习, 时间依赖建模, 灾难性遗忘缓解, 在线学习, 循环神经网络, 可学习掩码

## 3 点简述
- 核心问题：概念漂移、时间依赖和灾难性遗忘在数据流学习中构成主要挑战。
- 方法要点：集成持续学习架构策略与循环神经网络，通过可学习掩码回顾过去知识并在线扩展架构。
- 实验或效果：在合成和真实数据流上提升新概念适应能力，限制内存使用并减轻遗忘。

## 摘要（原文）

> Concept drift, temporal dependence, and catastrophic forgetting represent major challenges when learning from data streams. While Streaming Machine Learning and Continual Learning (CL) address these issues separately, recent efforts in Streaming Continual Learning (SCL) aim to unify them. In this work, we introduce MAGIC Net, a novel SCL approach that integrates CL-inspired architectural strategies with recurrent neural networks to tame temporal dependence. MAGIC Net continuously learns, looks back at past knowledge by applying learnable masks over frozen weights, and expands its architecture when necessary. It performs all operations online, ensuring inference availability at all times. Experiments on synthetic and real-world streams show that it improves adaptation to new concepts, limits memory usage, and mitigates forgetting.

