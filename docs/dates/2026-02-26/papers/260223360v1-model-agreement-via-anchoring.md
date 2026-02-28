---
layout: default
title: Model Agreement via Anchoring
---

# Model Agreement via Anchoring
**arXiv**：[2602.23360v1](https://arxiv.org/abs/2602.23360) · [PDF](https://arxiv.org/pdf/2602.23360.pdf)  
**作者**：Eric Eaton, Surbhi Goel, Marcel Hussing, Michael Kearns, Aaron Roth, Sikata Bela Sengupta, Jessica Sorrell  

**一句话要点**：提出锚定技术以分析独立训练模型在实值预测中的分歧，并应用于四种常见算法证明分歧界限。

**关键词**：模型分歧, 锚定技术, 实值预测, 独立训练, 算法分析, 强凸损失

## 3 点简述
- 核心问题：研究独立训练模型在实值预测中的分歧，即预测平方差的期望，旨在通过训练参数驱动分歧为零。
- 方法要点：开发基于锚定到两模型平均的通用技术，用于证明独立模型分歧的界限，适用于现有训练方法。
- 实验或效果：应用该技术证明四种算法的分歧界限：堆叠聚合、梯度提升、神经网络架构搜索和回归树训练，均能随参数趋近零。

## 摘要（原文）

> Numerous lines of aim to control $\textit{model disagreement}$ -- the extent to which two machine learning models disagree in their predictions. We adopt a simple and standard notion of model disagreement in real-valued prediction problems, namely the expected squared difference in predictions between two models trained on independent samples, without any coordination of the training processes. We would like to be able to drive disagreement to zero with some natural parameter(s) of the training procedure using analyses that can be applied to existing training methodologies.
>   We develop a simple general technique for proving bounds on independent model disagreement based on $\textit{anchoring}$ to the average of two models within the analysis. We then apply this technique to prove disagreement bounds for four commonly used machine learning algorithms: (1) stacked aggregation over an arbitrary model class (where disagreement is driven to 0 with the number of models $k$ being stacked) (2) gradient boosting (where disagreement is driven to 0 with the number of iterations $k$) (3) neural network training with architecture search (where disagreement is driven to 0 with the size $n$ of the architecture being optimized over) and (4) regression tree training over all regression trees of fixed depth (where disagreement is driven to 0 with the depth $d$ of the tree architecture). For clarity, we work out our initial bounds in the setting of one-dimensional regression with squared error loss -- but then show that all of our results generalize to multi-dimensional regression with any strongly convex loss.

