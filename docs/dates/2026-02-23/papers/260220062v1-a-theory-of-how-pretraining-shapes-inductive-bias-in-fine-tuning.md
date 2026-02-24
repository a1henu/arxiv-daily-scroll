---
layout: default
title: A Theory of How Pretraining Shapes Inductive Bias in Fine-Tuning
---

# A Theory of How Pretraining Shapes Inductive Bias in Fine-Tuning
**arXiv**：[2602.20062v1](https://arxiv.org/abs/2602.20062) · [PDF](https://arxiv.org/pdf/2602.20062.pdf)  
**作者**：Nicolas Anguita, Francesco Locatello, Andrew M. Saxe, Marco Mondelli, Flavia Mancini, Samuel Lippl, Clementine Domine  

**一句话要点**：提出对角线性网络理论分析预训练-微调管道，揭示初始化参数如何影响特征学习与泛化

**关键词**：预训练微调理论, 特征学习, 初始化参数, 泛化误差, 対角线性网络, 非线性网络实证

## 3 点简述
- 核心问题：预训练初始化如何影响微调中特征重用与精炼的理论理解不足
- 方法要点：在対角线性网络中推导泛化误差的精确表达式，识别四种微调机制
- 实验或效果：在CIFAR-100非线性网络中实证验证初始化参数对泛化的影响

## 摘要（原文）

> Pretraining and fine-tuning are central stages in modern machine learning systems. In practice, feature learning plays an important role across both stages: deep neural networks learn a broad range of useful features during pretraining and further refine those features during fine-tuning. However, an end-to-end theoretical understanding of how choices of initialization impact the ability to reuse and refine features during fine-tuning has remained elusive. Here we develop an analytical theory of the pretraining-fine-tuning pipeline in diagonal linear networks, deriving exact expressions for the generalization error as a function of initialization parameters and task statistics. We find that different initialization choices place the network into four distinct fine-tuning regimes that are distinguished by their ability to support feature learning and reuse, and therefore by the task statistics for which they are beneficial. In particular, a smaller initialization scale in earlier layers enables the network to both reuse and refine its features, leading to superior generalization on fine-tuning tasks that rely on a subset of pretraining features. We demonstrate empirically that the same initialization parameters impact generalization in nonlinear networks trained on CIFAR-100. Overall, our results demonstrate analytically how data and network initialization interact to shape fine-tuning generalization, highlighting an important role for the relative scale of initialization across different layers in enabling continued feature learning during fine-tuning.

