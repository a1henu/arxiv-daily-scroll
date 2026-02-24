---
layout: default
title: Behavior Learning (BL): Learning Hierarchical Optimization Structures from Data
---

# Behavior Learning (BL): Learning Hierarchical Optimization Structures from Data
**arXiv**：[2602.20152v1](https://arxiv.org/abs/2602.20152) · [PDF](https://arxiv.org/pdf/2602.20152.pdf)  
**作者**：Zhenyao Ma, Yue Liang, Dongxu Li  

**一句话要点**：提出行为学习框架，从数据中学习可解释的层次化优化结构。

**关键词**：行为学习, 优化结构学习, 可解释机器学习, 层次化优化, 效用最大化问题

## 3 点简述
- 核心问题：如何从数据中学习可解释且可识别的优化结构，适用于科学领域。
- 方法要点：基于行为科学，参数化组合效用函数，支持从单优化问题到层次化组合的架构。
- 实验或效果：理论证明通用逼近性，实证展示强预测性能、可解释性和高维可扩展性。

## 摘要（原文）

> Inspired by behavioral science, we propose Behavior Learning (BL), a novel general-purpose machine learning framework that learns interpretable and identifiable optimization structures from data, ranging from single optimization problems to hierarchical compositions. It unifies predictive performance, intrinsic interpretability, and identifiability, with broad applicability to scientific domains involving optimization. BL parameterizes a compositional utility function built from intrinsically interpretable modular blocks, which induces a data distribution for prediction and generation. Each block represents and can be written in symbolic form as a utility maximization problem (UMP), a foundational paradigm in behavioral science and a universal framework of optimization. BL supports architectures ranging from a single UMP to hierarchical compositions, the latter modeling hierarchical optimization structures. Its smooth and monotone variant (IBL) guarantees identifiability. Theoretically, we establish the universal approximation property of BL, and analyze the M-estimation properties of IBL. Empirically, BL demonstrates strong predictive performance, intrinsic interpretability and scalability to high-dimensional data. Code: https://github.com/MoonYLiang/Behavior-Learning ; install via pip install blnetwork.

