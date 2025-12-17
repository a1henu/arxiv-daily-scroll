---
layout: default
title: Dynamic Learning Rate Scheduling based on Loss Changes Leads to Faster Convergence
---

# Dynamic Learning Rate Scheduling based on Loss Changes Leads to Faster Convergence
**arXiv**：[2512.14527v1](https://arxiv.org/abs/2512.14527) · [PDF](https://arxiv.org/pdf/2512.14527.pdf)  
**作者**：Shreyas Subramanian, Bala Krishnamoorthy, Pranav Murthy  

**一句话要点**：提出GreedyLR调度器，基于损失变化动态调整学习率以加速收敛

**关键词**：学习率调度, 动态优化, 收敛加速, 深度学习训练, 损失函数自适应

## 3 点简述
- 问题：现有调度器如余弦或指数衰减可能未充分利用训练动态，导致收敛慢或次优性能
- 方法：GreedyLR根据当前损失自适应调整学习率，包括理论分析收敛性和最优缩放因子F
- 效果：在NLP、CV和LLM任务上实验，显示在精度、速度和收敛性上优于先进调度器

## 摘要（原文）

> Despite significant advances in optimizers for training, most research works use common scheduler choices like Cosine or exponential decay. In this paper, we study \emph{GreedyLR}, a novel scheduler that adaptively adjusts the learning rate during training based on the current loss. To validate the effectiveness of our proposed scheduler, we conduct experiments on several NLP, CV, and LLM tasks with up to $7B$ parameters, including both fine-tuning and pre-training experiments. The results show that our approach outperforms several state-of-the-art schedulers in terms of accuracy, speed, and convergence. We also provide a theoretical analysis of the GreedyLR algorithm, including a proof of convergence and derivation of the optimal scaling factor $F$ that maximizes the convergence rate, along with experiments to show robustness of the algorithm to realistic noisy landscapes. Our scheduler is easy to implement, computationally efficient, and could be considered a good default scheduler for training.

