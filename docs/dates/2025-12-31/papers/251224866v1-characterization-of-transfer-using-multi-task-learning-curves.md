---
layout: default
title: Characterization of Transfer Using Multi-task Learning Curves
---

# Characterization of Transfer Using Multi-task Learning Curves
**arXiv**：[2512.24866v1](https://arxiv.org/abs/2512.24866) · [PDF](https://arxiv.org/pdf/2512.24866.pdf)  
**作者**：András Millinghoffer, Bence Bolgár, Péter Antal  

**一句话要点**：提出基于多任务学习曲线的迁移效应量化方法，以数据扰动替代模型扰动进行表征。

**关键词**：多任务学习曲线, 迁移效应量化, 数据扰动, 归纳推理, 药物-靶点交互

## 3 点简述
- 核心问题：迁移效应在训练和归纳推理中的表征不足，传统方法依赖模型梯度更新。
- 方法要点：通过多任务学习曲线近似不同样本量下的归纳性能，提供更基础的迁移效应量化。
- 实验或效果：在药物-靶点交互数据集上评估，学习曲线能更好捕捉多任务学习效果及基础模型中的迁移效应。

## 摘要（原文）

> Transfer effects manifest themselves both during training using a fixed data set and in inductive inference using accumulating data. We hypothesize that perturbing the data set by including more samples, instead of perturbing the model by gradient updates, provides a complementary and more fundamental characterization of transfer effects. To capture this phenomenon, we quantitatively model transfer effects using multi-task learning curves approximating the inductive performance over varying sample sizes. We describe an efficient method to approximate multi-task learning curves analogous to the Task Affinity Grouping method applied during training. We compare the statistical and computational approaches to transfer, which indicates considerably higher compute costs for the previous but better power and broader applicability. Evaluations are performed using a benchmark drug-target interaction data set. Our results show that learning curves can better capture the effects of multi-task learning and their multi-task extensions can delineate pairwise and contextual transfer effects in foundation models.

