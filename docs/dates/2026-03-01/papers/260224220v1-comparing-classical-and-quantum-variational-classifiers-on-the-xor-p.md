---
layout: default
title: Comparing Classical and Quantum Variational Classifiers on the XOR Problem
---

# Comparing Classical and Quantum Variational Classifiers on the XOR Problem
**arXiv**：[2602.24220v1](https://arxiv.org/abs/2602.24220) · [PDF](https://arxiv.org/pdf/2602.24220.pdf)  
**作者**：Miras Seilkhan, Adilbek Taizhanov  

**一句话要点**：比较经典与量子变分分类器在XOR问题上的性能，评估模型表达性影响

**关键词**：量子机器学习, 变分量子分类器, XOR问题, 模型表达性, 电路深度, 经典神经网络

## 3 点简述
- 核心问题：量子机器学习在XOR任务中能否匹配或超越经典模型，关注表达性、鲁棒性和效率
- 方法要点：对比逻辑回归、多层感知机和不同深度的两量子比特变分量子分类器，使用合成XOR数据集
- 实验或效果：深度2量子电路与多层感知机在准确率上相当，但后者训练更快、交叉熵更低，未观察到量子优势

## 摘要（原文）

> Quantum machine learning applies principles such as superposition and entanglement to data processing and optimization. Variational quantum models operate on qubits in high-dimensional Hilbert spaces and provide an alternative approach to model expressivity. We compare classical models and a variational quantum classifier on the XOR problem. Logistic regression, a one-hidden-layer multilayer perceptron, and a two-qubit variational quantum classifier with circuit depths 1 and 2 are evaluated on synthetic XOR datasets with varying Gaussian noise and sample sizes using accuracy and binary cross-entropy.
>   Performance is determined primarily by model expressivity. Logistic regression and the depth-1 quantum circuit fail to represent XOR reliably, whereas the multilayer perceptron and the depth-2 quantum circuit achieve perfect test accuracy under representative conditions. Robustness analyses across noise levels, dataset sizes, and random seeds confirm that circuit depth is decisive for quantum performance on this task. Despite matching accuracy, the multilayer perceptron achieves lower binary cross-entropy and substantially shorter training time. Hardware execution preserves the global XOR structure but introduces structured deviations in the decision function. Overall, deeper variational quantum classifiers can match classical neural networks in accuracy on low-dimensional XOR benchmarks, but no clear empirical advantage in robustness or efficiency is observed in the examined settings.

