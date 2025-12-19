---
layout: default
title: Sequencing to Mitigate Catastrophic Forgetting in Continual Learning
---

# Sequencing to Mitigate Catastrophic Forgetting in Continual Learning
**arXiv**：[2512.16871v1](https://arxiv.org/abs/2512.16871) · [PDF](https://arxiv.org/pdf/2512.16871.pdf)  
**作者**：Hesham G. Moussa, Aroosa Hameed, Arashmid Akhavain  

**一句话要点**：提出任务排序方法以缓解持续学习中的灾难性遗忘

**关键词**：持续学习, 灾难性遗忘, 任务排序, 零样本评分, 神经架构搜索

## 3 点简述
- 核心问题：持续学习中新任务学习导致旧任务性能急剧下降的灾难性遗忘。
- 方法要点：从任务排序角度出发，利用零样本评分算法确定最优任务顺序。
- 实验或效果：智能排序显著减少遗忘，与传统策略结合提升性能和鲁棒性。

## 摘要（原文）

> To cope with real-world dynamics, an intelligent system needs to incrementally acquire, update, and exploit knowledge throughout its lifetime. This ability, known as Continual learning, provides a foundation for AI systems to develop themselves adaptively. Catastrophic forgetting is a major challenge to the progress of Continual Learning approaches, where learning a new task usually results in a dramatic performance drop on previously learned ones. Many approaches have emerged to counteract the impact of CF. Most of the proposed approaches can be categorized into five classes: replay-based, regularization-based, optimization-based, representation-based, and architecture-based. In this work, we approach the problem from a different angle, specifically by considering the optimal sequencing of tasks as they are presented to the model. We investigate the role of task sequencing in mitigating CF and propose a method for determining the optimal task order. The proposed method leverages zero-shot scoring algorithms inspired by neural architecture search (NAS). Results demonstrate that intelligent task sequencing can substantially reduce CF. Moreover, when combined with traditional continual learning strategies, sequencing offers enhanced performance and robustness against forgetting. Additionally, the presented approaches can find applications in other fields, such as curriculum learning.

