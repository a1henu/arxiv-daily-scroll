---
layout: default
title: Uncertainty propagation through trained multi-layer perceptrons: Exact analytical results
---

# Uncertainty propagation through trained multi-layer perceptrons: Exact analytical results
**arXiv**：[2601.16830v1](https://arxiv.org/abs/2601.16830) · [PDF](https://arxiv.org/pdf/2601.16830.pdf)  
**作者**：Andrew Thompson, Miles McCrory  

**一句话要点**：提出多层感知机不确定性传播的精确解析表达式，适用于单隐层ReLU网络和高斯输入。

**关键词**：不确定性传播, 多层感知机, ReLU激活函数, 高斯输入, 精确解析解, 神经网络分析

## 3 点简述
- 核心问题：多层感知机在输入为高斯分布时，输出不确定性的传播缺乏精确解析解。
- 方法要点：针对单隐层ReLU网络，推导输出均值和方差的精确表达式，无需级数展开。
- 实验或效果：提供理论结果，为不确定性量化提供精确分析工具，优于先前近似方法。

## 摘要（原文）

> We give analytical results for propagation of uncertainty through trained multi-layer perceptrons (MLPs) with a single hidden layer and ReLU activation functions. More precisely, we give expressions for the mean and variance of the output when the input is multivariate Gaussian. In contrast to previous results, we obtain exact expressions without resort to a series expansion.

