---
layout: default
title: Generalisation in Multitask Fitted Q-Iteration and Offline Q-learning
---

# Generalisation in Multitask Fitted Q-Iteration and Offline Q-learning
**arXiv**：[2512.20220v1](https://arxiv.org/abs/2512.20220) · [PDF](https://arxiv.org/pdf/2512.20220.pdf)  
**作者**：Kausthubh Manda, Raghuram Bharadwaj Diddigi  

**一句话要点**：分析多任务离线Q学习在共享低秩表示下的泛化保证与下游任务优势

**关键词**：离线强化学习, 多任务学习, 拟合Q迭代, 泛化理论, 低秩表示, 贝尔曼误差

## 3 点简述
- 研究多任务离线强化学习，任务共享动作值函数的低秩表示
- 提出多任务拟合Q迭代方法，通过贝尔曼误差最小化联合学习共享表示和任务特定值函数
- 在标准假设下建立有限样本泛化保证，并分析下游任务中重用表示可降低学习复杂度

## 摘要（原文）

> We study offline multitask reinforcement learning in settings where multiple tasks share a low-rank representation of their action-value functions. In this regime, a learner is provided with fixed datasets collected from several related tasks, without access to further online interaction, and seeks to exploit shared structure to improve statistical efficiency and generalization. We analyze a multitask variant of fitted Q-iteration that jointly learns a shared representation and task-specific value functions via Bellman error minimization on offline data. Under standard realizability and coverage assumptions commonly used in offline reinforcement learning, we establish finite-sample generalization guarantees for the learned value functions. Our analysis explicitly characterizes how pooling data across tasks improves estimation accuracy, yielding a $1/\sqrt{nT}$ dependence on the total number of samples across tasks, while retaining the usual dependence on the horizon and concentrability coefficients arising from distribution shift. In addition, we consider a downstream offline setting in which a new task shares the same underlying representation as the upstream tasks. We study how reusing the representation learned during the multitask phase affects value estimation for this new task, and show that it can reduce the effective complexity of downstream learning relative to learning from scratch. Together, our results clarify the role of shared representations in multitask offline Q-learning and provide theoretical insight into when and how multitask structure can improve generalization in model-free, value-based reinforcement learning.

