---
layout: default
title: POUR: A Provably Optimal Method for Unlearning Representations via Neural Collapse
---

# POUR: A Provably Optimal Method for Unlearning Representations via Neural Collapse
**arXiv**：[2511.19339v1](https://arxiv.org/abs/2511.19339) · [PDF](https://arxiv.org/pdf/2511.19339.pdf)  
**作者**：Anjie Le, Can Peng, Yuyuan Liu, J. Alison Noble  

**一句话要点**：提出POUR方法以在计算机视觉中实现表示级别的可证明最优遗忘

**关键词**：机器遗忘, 表示学习, 神经崩溃, 几何投影, 蒸馏训练, 分类性能

## 3 点简述
- 核心问题：现有遗忘方法仅修改分类器，导致表示层面遗忘不完整。
- 方法要点：基于神经崩溃理论，设计几何投影算子实现最优表示遗忘。
- 实验效果：在CIFAR和PathMNIST数据集上，POUR在分类和表示级别指标优于现有方法。

## 摘要（原文）

> In computer vision, machine unlearning aims to remove the influence of specific visual concepts or training images without retraining from scratch. Studies show that existing approaches often modify the classifier while leaving internal representations intact, resulting in incomplete forgetting. In this work, we extend the notion of unlearning to the representation level, deriving a three-term interplay between forgetting efficacy, retention fidelity, and class separation. Building on Neural Collapse theory, we show that the orthogonal projection of a simplex Equiangular Tight Frame (ETF) remains an ETF in a lower dimensional space, yielding a provably optimal forgetting operator. We further introduce the Representation Unlearning Score (RUS) to quantify representation-level forgetting and retention fidelity. Building on this, we introduce POUR (Provably Optimal Unlearning of Representations), a geometric projection method with closed-form (POUR-P) and a feature-level unlearning variant under a distillation scheme (POUR-D). Experiments on CIFAR-10/100 and PathMNIST demonstrate that POUR achieves effective unlearning while preserving retained knowledge, outperforming state-of-the-art unlearning methods on both classification-level and representation-level metrics.

