---
layout: default
title: Toward Enhancing Representation Learning in Federated Multi-Task Settings
---

# Toward Enhancing Representation Learning in Federated Multi-Task Settings
**arXiv**：[2602.01626v1](https://arxiv.org/abs/2602.01626) · [PDF](https://arxiv.org/pdf/2602.01626.pdf)  
**作者**：Mehdi Setayesh, Mahdi Beitollahi, Yasser H. Khalil, Hongliang Li  

**一句话要点**：提出Muscle损失与FedMuscle算法，以增强联邦多任务学习中的表示学习能力。

**关键词**：联邦学习, 多任务学习, 表示学习, 对比学习, 异构模型, 通信效率

## 3 点简述
- 核心问题：现有联邦多任务学习方法假设模型同质性，限制了在异构任务和模型下的适用性。
- 方法要点：通过Muscle损失，一种对比学习目标，对齐所有参与模型的表示，最大化表示间的互信息。
- 实验或效果：在图像和语言任务上，FedMuscle优于现有基线，在异构设置中表现稳健且高效。

## 摘要（原文）

> Federated multi-task learning (FMTL) seeks to collaboratively train customized models for users with different tasks while preserving data privacy. Most existing approaches assume model congruity (i.e., the use of fully or partially homogeneous models) across users, which limits their applicability in realistic settings. To overcome this limitation, we aim to learn a shared representation space across tasks rather than shared model parameters. To this end, we propose Muscle loss, a novel contrastive learning objective that simultaneously aligns representations from all participating models. Unlike existing multi-view or multi-model contrastive methods, which typically align models pairwise, Muscle loss can effectively capture dependencies across tasks because its minimization is equivalent to the maximization of mutual information among all the models' representations. Building on this principle, we develop FedMuscle, a practical and communication-efficient FMTL algorithm that naturally handles both model and task heterogeneity. Experiments on diverse image and language tasks demonstrate that FedMuscle consistently outperforms state-of-the-art baselines, delivering substantial improvements and robust performance across heterogeneous settings.

