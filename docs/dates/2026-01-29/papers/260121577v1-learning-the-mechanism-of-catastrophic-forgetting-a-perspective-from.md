---
layout: default
title: Learning the Mechanism of Catastrophic Forgetting: A Perspective from Gradient Similarity
---

# Learning the Mechanism of Catastrophic Forgetting: A Perspective from Gradient Similarity
**arXiv**：[2601.21577v1](https://arxiv.org/abs/2601.21577) · [PDF](https://arxiv.org/pdf/2601.21577.pdf)  
**作者**：Mutian Yang, Zisen Zhan, Yutong Chen, Haolin Li, Kaiwen Wang, Kaili Zheng, Yuguang Wang, Qi Wang, Jiandong Gao, Ji Wu  

**一句话要点**：提出基于梯度相似性的理论框架与协作神经元学习方法，以解决大语言模型知识注入中的灾难性遗忘问题。

**关键词**：灾难性遗忘, 梯度相似性, 协作神经元学习, 大语言模型, 持续学习, 知识注入

## 3 点简述
- 核心问题：灾难性遗忘严重削弱大语言模型的持续学习能力，现有方法缺乏理论基础。
- 方法要点：证明强负梯度相似性是遗忘根本原因，识别冲突与协作神经元，提出协作神经元学习方法。
- 实验或效果：在多种模型、数据集和优化器上，实现零遗忘或显著减少遗忘，效果达59.1%-81.7%。

## 摘要（原文）

> Catastrophic forgetting during knowledge injection severely undermines the continual learning capability of large language models (LLMs). Although existing methods attempt to mitigate this issue, they often lack a foundational theoretical explanation. We establish a gradient-based theoretical framework to explain catastrophic forgetting. We first prove that strongly negative gradient similarity is a fundamental cause of forgetting. We then use gradient similarity to identify two types of neurons: conflicting neurons that induce forgetting and account for 50%-75% of neurons, and collaborative neurons that mitigate forgetting and account for 25%-50%. Based on this analysis, we propose a knowledge injection method, Collaborative Neural Learning (CNL). By freezing conflicting neurons and updating only collaborative neurons, CNL theoretically eliminates catastrophic forgetting under an infinitesimal learning rate eta and an exactly known mastered set. Experiments on five LLMs, four datasets, and four optimizers show that CNL achieves zero forgetting in in-set settings and reduces forgetting by 59.1%-81.7% in out-of-set settings.

