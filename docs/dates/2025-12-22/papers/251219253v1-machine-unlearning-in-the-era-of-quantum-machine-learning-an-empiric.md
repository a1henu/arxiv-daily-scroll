---
layout: default
title: Machine Unlearning in the Era of Quantum Machine Learning: An Empirical Study
---

# Machine Unlearning in the Era of Quantum Machine Learning: An Empirical Study
**arXiv**：[2512.19253v1](https://arxiv.org/abs/2512.19253) · [PDF](https://arxiv.org/pdf/2512.19253.pdf)  
**作者**：Carla Crivoi, Radu Tudor Ionescu  

**一句话要点**：提出首个混合量子-经典神经网络中机器遗忘的实证研究，评估多种遗忘方法在量子环境下的表现。

**关键词**：机器遗忘, 量子机器学习, 混合神经网络, 变分量子电路, 实证研究, 遗忘方法

## 3 点简述
- 核心问题：机器遗忘在量子机器学习中行为未知，尤其在变分量子电路和混合架构中缺乏探索。
- 方法要点：将梯度、蒸馏、正则化和认证遗忘方法适配量子设置，并引入两种新策略。
- 实验或效果：在Iris、MNIST和Fashion-MNIST数据集上测试，发现量子模型支持有效遗忘，但结果受电路深度和任务复杂度影响。

## 摘要（原文）

> We present the first comprehensive empirical study of machine unlearning (MU) in hybrid quantum-classical neural networks. While MU has been extensively explored in classical deep learning, its behavior within variational quantum circuits (VQCs) and quantum-augmented architectures remains largely unexplored. First, we adapt a broad suite of unlearning methods to quantum settings, including gradient-based, distillation-based, regularization-based and certified techniques. Second, we introduce two new unlearning strategies tailored to hybrid models. Experiments across Iris, MNIST, and Fashion-MNIST, under both subset removal and full-class deletion, reveal that quantum models can support effective unlearning, but outcomes depend strongly on circuit depth, entanglement structure, and task complexity. Shallow VQCs display high intrinsic stability with minimal memorization, whereas deeper hybrid models exhibit stronger trade-offs between utility, forgetting strength, and alignment with retrain oracle. We find that certain methods, e.g. EU-k, LCA, and Certified Unlearning, consistently provide the best balance across metrics. These findings establish baseline empirical insights into quantum machine unlearning and highlight the need for quantum-aware algorithms and theoretical guarantees, as quantum machine learning systems continue to expand in scale and capability. We publicly release our code at: https://github.com/CrivoiCarla/HQML.

