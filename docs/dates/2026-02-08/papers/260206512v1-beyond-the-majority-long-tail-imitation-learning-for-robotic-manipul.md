---
layout: default
title: Beyond the Majority: Long-tail Imitation Learning for Robotic Manipulation
---

# Beyond the Majority: Long-tail Imitation Learning for Robotic Manipulation
**arXiv**：[2602.06512v1](https://arxiv.org/abs/2602.06512) · [PDF](https://arxiv.org/pdf/2602.06512.pdf)  
**作者**：Junhong Zhu, Ji Zhang, Jingkuan Song, Lianli Gao, Heng Tao Shen  

**一句话要点**：提出Approaching-Phase Augmentation以解决机器人模仿学习中长尾分布导致的尾任务泛化问题。

**关键词**：机器人模仿学习, 长尾分布, 知识迁移, 空间推理, 任务泛化

## 3 点简述
- 核心问题：模仿学习训练数据呈长尾分布，导致策略在数据稀缺的尾任务上泛化能力差。
- 方法要点：引入Approaching-Phase Augmentation，从数据丰富的头任务迁移知识至尾任务，无需额外演示。
- 实验或效果：在仿真和真实机器人任务中验证了方法的有效性，提升了尾任务性能。

## 摘要（原文）

> While generalist robot policies hold significant promise for learning diverse manipulation skills through imitation, their performance is often hindered by the long-tail distribution of training demonstrations. Policies learned on such data, which is heavily skewed towards a few data-rich head tasks, frequently exhibit poor generalization when confronted with the vast number of data-scarce tail tasks. In this work, we conduct a comprehensive analysis of the pervasive long-tail challenge inherent in policy learning. Our analysis begins by demonstrating the inefficacy of conventional long-tail learning strategies (e.g., re-sampling) for improving the policy's performance on tail tasks. We then uncover the underlying mechanism for this failure, revealing that data scarcity on tail tasks directly impairs the policy's spatial reasoning capability. To overcome this, we introduce Approaching-Phase Augmentation (APA), a simple yet effective scheme that transfers knowledge from data-rich head tasks to data-scarce tail tasks without requiring external demonstrations. Extensive experiments in both simulation and real-world manipulation tasks demonstrate the effectiveness of APA. Our code and demos are publicly available at: https://mldxy.github.io/Project-VLA-long-tail/.

