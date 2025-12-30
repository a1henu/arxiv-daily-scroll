---
layout: default
title: Certifying the Right to Be Forgotten: Primal-Dual Optimization for Sample and Label Unlearning in Vertical Federated Learning
---

# Certifying the Right to Be Forgotten: Primal-Dual Optimization for Sample and Label Unlearning in Vertical Federated Learning
**arXiv**：[2512.23171v1](https://arxiv.org/abs/2512.23171) · [PDF](https://arxiv.org/pdf/2512.23171.pdf)  
**作者**：Yu Jiang, Xindi Tong, Ziyao Liu, Xiaoxi Zhang, Kwok-Yan Lam, Chee Wei Tan  

**一句话要点**：提出FedORA以解决垂直联邦学习中样本与标签遗忘的挑战

**关键词**：垂直联邦学习, 数据遗忘, 原对偶优化, 样本遗忘, 标签遗忘, 隐私保护

## 3 点简述
- 垂直联邦学习遗忘因特征分布架构复杂，需跨方协调处理样本或标签移除
- FedORA采用原对偶优化框架，设计新遗忘损失函数促进分类不确定性
- 实验证明FedORA在保持模型效用下降低计算与通信开销，接近从头训练效果

## 摘要（原文）

> Federated unlearning has become an attractive approach to address privacy concerns in collaborative machine learning, for situations when sensitive data is remembered by AI models during the machine learning process. It enables the removal of specific data influences from trained models, aligning with the growing emphasis on the "right to be forgotten." While extensively studied in horizontal federated learning, unlearning in vertical federated learning (VFL) remains challenging due to the distributed feature architecture. VFL unlearning includes sample unlearning that removes specific data points' influence and label unlearning that removes entire classes. Since different parties hold complementary features of the same samples, unlearning tasks require cross-party coordination, creating computational overhead and complexities from feature interdependencies. To address such challenges, we propose FedORA (Federated Optimization for data Removal via primal-dual Algorithm), designed for sample and label unlearning in VFL. FedORA formulates the removal of certain samples or labels as a constrained optimization problem solved using a primal-dual framework. Our approach introduces a new unlearning loss function that promotes classification uncertainty rather than misclassification. An adaptive step size enhances stability, while an asymmetric batch design, considering the prior influence of the remaining data on the model, handles unlearning and retained data differently to efficiently reduce computational costs. We provide theoretical analysis proving that the model difference between FedORA and Train-from-scratch is bounded, establishing guarantees for unlearning effectiveness. Experiments on tabular and image datasets demonstrate that FedORA achieves unlearning effectiveness and utility preservation comparable to Train-from-scratch with reduced computation and communication overhead.

