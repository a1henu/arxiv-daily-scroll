---
layout: default
title: Quantum Maximum Likelihood Prediction via Hilbert Space Embeddings
---

# Quantum Maximum Likelihood Prediction via Hilbert Space Embeddings
**arXiv**：[2602.18364v1](https://arxiv.org/abs/2602.18364) · [PDF](https://arxiv.org/pdf/2602.18364.pdf)  
**作者**：Sreejith Sreekumar, Nir Weinberger  

**一句话要点**：提出基于希尔伯特空间嵌入的量子最大似然预测框架，统一处理经典与量子大语言模型。

**关键词**：量子机器学习, 大语言模型, 信息几何, 最大似然预测, 希尔伯特空间嵌入

## 3 点简述
- 核心问题：从信息几何与统计视角解释大语言模型的上下文预测能力。
- 方法要点：将训练建模为概率分布嵌入量子密度算子空间，上下文学习作为量子模型的最大似然预测。
- 实验或效果：推导非渐近性能保证，包括收敛率和集中不等式，适用于迹范数和量子相对熵。

## 摘要（原文）

> Recent works have proposed various explanations for the ability of modern large language models (LLMs) to perform in-context prediction. We propose an alternative conceptual viewpoint from an information-geometric and statistical perspective. Motivated by Bach[2023], we model training as learning an embedding of probability distributions into the space of quantum density operators, and in-context learning as maximum-likelihood prediction over a specified class of quantum models. We provide an interpretation of this predictor in terms of quantum reverse information projection and quantum Pythagorean theorem when the class of quantum models is sufficiently expressive. We further derive non-asymptotic performance guarantees in terms of convergence rates and concentration inequalities, both in trace norm and quantum relative entropy. Our approach provides a unified framework to handle both classical and quantum LLMs.

