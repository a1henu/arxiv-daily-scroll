---
layout: default
title: Understanding the Role of Rehearsal Scale in Continual Learning under Varying Model Capacities
---

# Understanding the Role of Rehearsal Scale in Continual Learning under Varying Model Capacities
**arXiv**：[2602.20791v1](https://arxiv.org/abs/2602.20791) · [PDF](https://arxiv.org/pdf/2602.20791.pdf)  
**作者**：JinLi He, Liang Bai, Xian Yang  

**一句话要点**：分析排练规模在持续学习中对模型适应性与记忆性的影响

**关键词**：持续学习, 排练机制, 模型容量, 灾难性遗忘, 优化分析

## 3 点简述
- 核心问题：排练规模如何影响持续学习中的遗忘与性能，理论理解有限
- 方法要点：将排练式持续学习建模为多维优化问题，推导排练规模对适应性和记忆性的闭式分析
- 实验或效果：通过数值模拟和深度网络实验验证排练可能损害适应性，记忆误差有下限

## 摘要（原文）

> Rehearsal is one of the key techniques for mitigating catastrophic forgetting and has been widely adopted in continual learning algorithms due to its simplicity and practicality. However, the theoretical understanding of how rehearsal scale influences learning dynamics remains limited. To address this gap, we formulate rehearsal-based continual learning as a multidimensional effectiveness-driven iterative optimization problem, providing a unified characterization across diverse performance metrics. Within this framework, we derive a closed-form analysis of adaptability, memorability, and generalization from the perspective of rehearsal scale. Our results uncover several intriguing and counterintuitive findings. First, rehearsal can impair model's adaptability, in sharp contrast to its traditionally recognized benefits. Second, increasing the rehearsal scale does not necessarily improve memory retention. When tasks are similar and noise levels are low, the memory error exhibits a diminishing lower bound. Finally, we validate these insights through numerical simulations and extended analyses on deep neural networks across multiple real-world datasets, revealing statistical patterns of rehearsal mechanisms in continual learning.

