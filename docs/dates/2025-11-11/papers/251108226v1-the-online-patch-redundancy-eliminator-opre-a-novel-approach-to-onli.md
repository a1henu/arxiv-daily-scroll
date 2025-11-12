---
layout: default
title: The Online Patch Redundancy Eliminator (OPRE): A novel approach to online agnostic continual learning using dataset compression
---

# The Online Patch Redundancy Eliminator (OPRE): A novel approach to online agnostic continual learning using dataset compression
**arXiv**：[2511.08226v1](https://arxiv.org/abs/2511.08226) · [PDF](https://arxiv.org/pdf/2511.08226.pdf)  
**作者**：Raphaël Bayle, Martial Mermillod, Robert M. French  

**一句话要点**：提出OPRE在线数据集压缩方法，实现无先验信息的在线持续学习。

**关键词**：持续学习, 灾难性遗忘, 数据集压缩, 在线学习, 无先验学习

## 3 点简述
- 核心问题：持续学习中灾难性遗忘，现有方法依赖先验信息，缺乏无先验通用性。
- 方法要点：OPRE在线压缩数据集，测试时训练分类器，减少数据冗余。
- 实验或效果：在CIFAR-10和CIFAR-100上性能优于其他在线持续学习方法。

## 摘要（原文）

> In order to achieve Continual Learning (CL), the problem of catastrophic forgetting, one that has plagued neural networks since their inception, must be overcome. The evaluation of continual learning methods relies on splitting a known homogeneous dataset and learning the associated tasks one after the other. We argue that most CL methods introduce a priori information about the data to come and cannot be considered agnostic. We exemplify this point with the case of methods relying on pretrained feature extractors, which are still used in CL. After showing that pretrained feature extractors imply a loss of generality with respect to the data that can be learned by the model, we then discuss other kinds of a priori information introduced in other CL methods. We then present the Online Patch Redundancy Eliminator (OPRE), an online dataset compression algorithm, which, along with the training of a classifier at test time, yields performance on CIFAR-10 and CIFAR-100 superior to a number of other state-of-the-art online continual learning methods. Additionally, OPRE requires only minimal and interpretable hypothesis on the data to come. We suggest that online dataset compression could well be necessary to achieve fully agnostic CL.

