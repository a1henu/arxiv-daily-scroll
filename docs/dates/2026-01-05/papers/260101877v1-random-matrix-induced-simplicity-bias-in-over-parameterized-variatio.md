---
layout: default
title: Random-Matrix-Induced Simplicity Bias in Over-parameterized Variational Quantum Circuits
---

# Random-Matrix-Induced Simplicity Bias in Over-parameterized Variational Quantum Circuits
**arXiv**：[2601.01877v1](https://arxiv.org/abs/2601.01877) · [PDF](https://arxiv.org/pdf/2601.01877.pdf)  
**作者**：Jun Qi, Chao-Han Huck Yang, Pin-Yu Chen, Min-Hsiu Hsieh  

**一句话要点**：揭示过参数化变分量子电路中随机矩阵诱导的简单性偏差，提出张量结构避免崩溃

**关键词**：变分量子电路, 过参数化, 随机矩阵理论, 简单性偏差, 张量网络, 梯度崩溃

## 3 点简述
- 过参数化变分量子电路常导致训练困难和泛化差，源于函数类视角的简单性偏差
- 使用随机矩阵理论和测度集中工具，证明非结构化电路进入Haar类，导致假设类崩溃
- 张量结构电路如张量网络可避免崩溃，保持输出可变性和梯度信号

## 摘要（原文）

> Over-parameterization is commonly used to increase the expressivity of variational quantum circuits (VQCs), yet deeper and more highly parameterized circuits often exhibit poor trainability and limited generalization. In this work, we provide a theoretical explanation for this phenomenon from a function-class perspective. We show that sufficiently expressive, unstructured variational ansatze enter a Haar-like universality class in which both observable expectation values and parameter gradients concentrate exponentially with system size. As a consequence, the hypothesis class induced by such circuits collapses with high probability to a narrow family of near-constant functions, a phenomenon we term simplicity bias, with barren plateaus arising as a consequence rather than the root cause. Using tools from random matrix theory and concentration of measure, we rigorously characterize this universality class and establish uniform hypothesis-class collapse over finite datasets. We further show that this collapse is not unavoidable: tensor-structured VQCs, including tensor-network-based and tensor-hypernetwork parameterizations, lie outside the Haar-like universality class. By restricting the accessible unitary ensemble through bounded tensor rank or bond dimension, these architectures prevent concentration of measure, preserve output variability for local observables, and retain non-degenerate gradient signals even in over-parameterized regimes. Together, our results unify barren plateaus, expressivity limits, and generalization collapse under a single structural mechanism rooted in random-matrix universality, highlighting the central role of architectural inductive bias in variational quantum algorithms.

