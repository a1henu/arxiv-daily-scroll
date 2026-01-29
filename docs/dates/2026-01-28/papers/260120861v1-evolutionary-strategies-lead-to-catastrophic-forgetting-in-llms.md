---
layout: default
title: Evolutionary Strategies lead to Catastrophic Forgetting in LLMs
---

# Evolutionary Strategies lead to Catastrophic Forgetting in LLMs
**arXiv**：[2601.20861v1](https://arxiv.org/abs/2601.20861) · [PDF](https://arxiv.org/pdf/2601.20861.pdf)  
**作者**：Immanuel Abdi, Akshat Gupta, Micah Mok, Alexander Lu, Nicholas Lee, Gopala Anumanchipalli  

**一句话要点**：分析进化策略在LLMs中导致灾难性遗忘，揭示其与梯度优化算法的对比

**关键词**：进化策略, 灾难性遗忘, 持续学习, 梯度优化, LLMs训练, 遗忘曲线

## 3 点简述
- 核心问题：进化策略在LLMs持续学习中引发灾难性遗忘，限制在线训练应用
- 方法要点：对比进化策略与GRPO在数学推理任务上的性能与遗忘曲线
- 实验或效果：进化策略更新非稀疏且范数大，导致遗忘显著，性能接近GRPO但遗忘严重

## 摘要（原文）

> One of the biggest missing capabilities in current AI systems is the ability to learn continuously after deployment. Implementing such continually learning systems have several challenges, one of which is the large memory requirement of gradient-based algorithms that are used to train state-of-the-art LLMs. Evolutionary Strategies (ES) have recently re-emerged as a gradient-free alternative to traditional learning algorithms and have shown encouraging performance on specific tasks in LLMs. In this paper, we perform a comprehensive analysis of ES and specifically evaluate its forgetting curves when training for an increasing number of update steps. We first find that ES is able to reach performance numbers close to GRPO for math and reasoning tasks with a comparable compute budget. However, and most importantly for continual learning, the performance gains in ES is accompanied by significant forgetting of prior abilities, limiting its applicability for training models online. We also explore the reason behind this behavior and show that the updates made using ES are much less sparse and have orders of magnitude larger $\ell_2$ norm compared to corresponding GRPO updates, explaining the contrasting forgetting curves between the two algorithms. With this study, we aim to highlight the issue of forgetting in gradient-free algorithms like ES and hope to inspire future work to mitigate these issues.

