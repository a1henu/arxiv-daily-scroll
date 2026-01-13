---
layout: default
title: Graph Inference Towards ICD Coding
---

# Graph Inference Towards ICD Coding
**arXiv**：[2601.07496v1](https://arxiv.org/abs/2601.07496) · [PDF](https://arxiv.org/pdf/2601.07496.pdf)  
**作者**：Xiaoxiao Deng  

**一句话要点**：提出LabGraph框架，将ICD编码重构为图生成任务以提升预测精度

**关键词**：ICD编码, 图生成, 对抗域适应, 强化学习, 临床文本分析

## 3 点简述
- 核心问题：ICD编码面临标签空间大和类别极度不平衡的挑战
- 方法要点：结合对抗域适应、图强化学习和扰动正则化增强模型鲁棒性
- 实验或效果：在基准数据集上，LabGraph在多个指标上优于先前方法

## 摘要（原文）

> Automated ICD coding involves assigning standardized diagnostic codes to clinical narratives. The vast label space and extreme class imbalance continue to challenge precise prediction. To address these issues, LabGraph is introduced -- a unified framework that reformulates ICD coding as a graph generation task. By combining adversarial domain adaptation, graph-based reinforcement learning, and perturbation regularization, LabGraph effectively enhances model robustness and generalization. In addition, a label graph discriminator dynamically evaluates each generated code, providing adaptive reward feedback during training. Experiments on benchmark datasets demonstrate that LabGraph consistently outperforms previous approaches on micro-F1, micro-AUC, and P@K.

