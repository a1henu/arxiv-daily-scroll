---
layout: default
title: Forget Less, Retain More: A Lightweight Regularizer for Rehearsal-Based Continual Learning
---

# Forget Less, Retain More: A Lightweight Regularizer for Rehearsal-Based Continual Learning
**arXiv**：[2512.01818v1](https://arxiv.org/abs/2512.01818) · [PDF](https://arxiv.org/pdf/2512.01818.pdf)  
**作者**：Lama Alssum, Hasan Abed Al Kader Hammoud, Motasem Alfarra, Juan C Leon Alcazar, Bernard Ghanem  

**一句话要点**：提出信息最大化正则器以解决基于回放的持续学习中的灾难性遗忘问题

**关键词**：持续学习, 灾难性遗忘, 正则化方法, 回放策略, 信息最大化, 视频学习

## 3 点简述
- 核心问题：深度神经网络在持续学习中面临灾难性遗忘，即新任务训练导致旧任务性能下降
- 方法要点：基于预期标签分布设计类无关正则器，轻量集成到回放方法中减少遗忘并加速收敛
- 实验或效果：跨数据集和任务数验证性能提升，计算开销小，适用于视频数据等实际场景

## 摘要（原文）

> Deep neural networks suffer from catastrophic forgetting, where performance on previous tasks degrades after training on a new task. This issue arises due to the model's tendency to overwrite previously acquired knowledge with new information. We present a novel approach to address this challenge, focusing on the intersection of memory-based methods and regularization approaches. We formulate a regularization strategy, termed Information Maximization (IM) regularizer, for memory-based continual learning methods, which is based exclusively on the expected label distribution, thus making it class-agnostic. As a consequence, IM regularizer can be directly integrated into various rehearsal-based continual learning methods, reducing forgetting and favoring faster convergence. Our empirical validation shows that, across datasets and regardless of the number of tasks, our proposed regularization strategy consistently improves baseline performance at the expense of a minimal computational overhead. The lightweight nature of IM ensures that it remains a practical and scalable solution, making it applicable to real-world continual learning scenarios where efficiency is paramount. Finally, we demonstrate the data-agnostic nature of our regularizer by applying it to video data, which presents additional challenges due to its temporal structure and higher memory requirements. Despite the significant domain gap, our experiments show that IM regularizer also improves the performance of video continual learning methods.

