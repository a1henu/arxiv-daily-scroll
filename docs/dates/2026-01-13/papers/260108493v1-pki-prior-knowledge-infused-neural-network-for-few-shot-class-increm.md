---
layout: default
title: PKI: Prior Knowledge-Infused Neural Network for Few-Shot Class-Incremental Learning
---

# PKI: Prior Knowledge-Infused Neural Network for Few-Shot Class-Incremental Learning
**arXiv**：[2601.08493v1](https://arxiv.org/abs/2601.08493) · [PDF](https://arxiv.org/pdf/2601.08493.pdf)  
**作者**：Kexin Baoa, Fanzhao Lin, Zichen Wang, Yong Li, Dan Zeng, Shiming Ge  

**一句话要点**：提出先验知识注入神经网络以解决少样本类增量学习中的灾难性遗忘和过拟合问题

**关键词**：少样本类增量学习, 灾难性遗忘, 过拟合, 先验知识注入, 投影器集成, 资源优化

## 3 点简述
- 核心问题：少样本类增量学习面临灾难性遗忘和新类过拟合挑战
- 方法要点：通过级联投影器集成，冻结大部分网络组件，仅微调新投影器和分类器
- 实验或效果：在三个基准测试中优于现有方法，并设计变体平衡资源消耗与性能

## 摘要（原文）

> Few-shot class-incremental learning (FSCIL) aims to continually adapt a model on a limited number of new-class examples, facing two well-known challenges: catastrophic forgetting and overfitting to new classes. Existing methods tend to freeze more parts of network components and finetune others with an extra memory during incremental sessions. These methods emphasize preserving prior knowledge to ensure proficiency in recognizing old classes, thereby mitigating catastrophic forgetting. Meanwhile, constraining fewer parameters can help in overcoming overfitting with the assistance of prior knowledge. Following previous methods, we retain more prior knowledge and propose a prior knowledge-infused neural network (PKI) to facilitate FSCIL. PKI consists of a backbone, an ensemble of projectors, a classifier, and an extra memory. In each incremental session, we build a new projector and add it to the ensemble. Subsequently, we finetune the new projector and the classifier jointly with other frozen network components, ensuring the rich prior knowledge is utilized effectively. By cascading projectors, PKI integrates prior knowledge accumulated from previous sessions and learns new knowledge flexibly, which helps to recognize old classes and efficiently learn new classes. Further, to reduce the resource consumption associated with keeping many projectors, we design two variants of the prior knowledge-infused neural network (PKIV-1 and PKIV-2) to trade off a balance between resource consumption and performance by reducing the number of projectors. Extensive experiments on three popular benchmarks demonstrate that our approach outperforms state-of-the-art methods.

