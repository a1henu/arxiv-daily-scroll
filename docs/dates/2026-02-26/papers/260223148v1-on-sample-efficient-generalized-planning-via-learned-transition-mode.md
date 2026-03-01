---
layout: default
title: On Sample-Efficient Generalized Planning via Learned Transition Models
---

# On Sample-Efficient Generalized Planning via Learned Transition Models
**arXiv**：[2602.23148v1](https://arxiv.org/abs/2602.23148) · [PDF](https://arxiv.org/pdf/2602.23148.pdf)  
**作者**：Nitin Gupta, Vishal Pallagani, John A. Aydin, Biplav Srivastava  

**一句话要点**：提出基于学习转移模型的广义规划方法，以提升样本效率和分布外泛化能力

**关键词**：广义规划, 转移模型学习, 样本效率, 分布外泛化, 状态预测, 神经网络规划

## 3 点简述
- 核心问题：现有Transformer规划器依赖大数据集，易在长视野任务中因状态漂移而失效
- 方法要点：通过神经网络显式学习转移模型，自回归预测中间状态以生成规划
- 实验或效果：在多个领域，该方法以更少训练数据和更小模型实现更高分布外规划成功率

## 摘要（原文）

> Generalized planning studies the construction of solution strategies that generalize across families of planning problems sharing a common domain model, formally defined by a transition function $γ: S \times A \rightarrow S$. Classical approaches achieve such generalization through symbolic abstractions and explicit reasoning over $γ$. In contrast, recent Transformer-based planners, such as PlanGPT and Plansformer, largely cast generalized planning as direct action-sequence prediction, bypassing explicit transition modeling. While effective on in-distribution instances, these approaches typically require large datasets and model sizes, and often suffer from state drift in long-horizon settings due to the absence of explicit world-state evolution. In this work, we formulate generalized planning as a transition-model learning problem, in which a neural model explicitly approximates the successor-state function $\hatγ \approx γ$ and generates plans by rolling out symbolic state trajectories. Instead of predicting actions directly, the model autoregressively predicts intermediate world states, thereby learning the domain dynamics as an implicit world model. To study size-invariant generalization and sample efficiency, we systematically evaluate multiple state representations and neural architectures, including relational graph encodings. Our results show that learning explicit transition models yields higher out-of-distribution satisficing-plan success than direct action-sequence prediction in multiple domains, while achieving these gains with significantly fewer training instances and smaller models. This is an extended version of a short paper accepted at ICAPS 2026 under the same title.

