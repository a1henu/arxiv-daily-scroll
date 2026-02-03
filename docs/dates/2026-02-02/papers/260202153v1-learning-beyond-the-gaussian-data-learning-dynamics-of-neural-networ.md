---
layout: default
title: Learning Beyond the Gaussian Data: Learning Dynamics of Neural Networks on an Expressive and Cumulant-Controllable Data Model
---

# Learning Beyond the Gaussian Data: Learning Dynamics of Neural Networks on an Expressive and Cumulant-Controllable Data Model
**arXiv**：[2602.02153v1](https://arxiv.org/abs/2602.02153) · [PDF](https://arxiv.org/pdf/2602.02153.pdf)  
**作者**：Onat Ure, Samet Demir, Zafer Dogan  

**一句话要点**：提出基于可控制高阶矩的非高斯数据模型，研究神经网络学习动态中的高阶统计量影响。

**关键词**：非高斯数据模型, 神经网络学习动态, 高阶累积量控制, Hermite多项式, 在线学习实验, Fashion-MNIST

## 3 点简述
- 核心问题：数据的高阶统计量（如偏度和峰度）如何影响神经网络的学习动态。
- 方法要点：使用生成式两层神经网络构建数据模型，通过Hermite多项式系数控制高阶累积量。
- 实验或效果：在线学习实验显示网络先学习低阶统计量，再逐步学习高阶累积量；在Fashion-MNIST上验证实用性。

## 摘要（原文）

> We study the effect of high-order statistics of data on the learning dynamics of neural networks (NNs) by using a moment-controllable non-Gaussian data model. Considering the expressivity of two-layer neural networks, we first construct the data model as a generative two-layer NN where the activation function is expanded by using Hermite polynomials. This allows us to achieve interpretable control over high-order cumulants such as skewness and kurtosis through the Hermite coefficients while keeping the data model realistic. Using samples generated from the data model, we perform controlled online learning experiments with a two-layer NN. Our results reveal a moment-wise progression in training: networks first capture low-order statistics such as mean and covariance, and progressively learn high-order cumulants. Finally, we pretrain the generative model on the Fashion-MNIST dataset and leverage the generated samples for further experiments. The results of these additional experiments confirm our conclusions and show the utility of the data model in a real-world scenario. Overall, our proposed approach bridges simplified data assumptions and practical data complexity, which offers a principled framework for investigating distributional effects in machine learning and signal processing.

