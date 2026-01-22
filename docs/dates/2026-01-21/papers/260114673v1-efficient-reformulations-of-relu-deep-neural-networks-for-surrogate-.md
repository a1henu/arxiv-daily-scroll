---
layout: default
title: Efficient reformulations of ReLU deep neural networks for surrogate modelling in power system optimisation
---

# Efficient reformulations of ReLU deep neural networks for surrogate modelling in power system optimisation
**arXiv**：[2601.14673v1](https://arxiv.org/abs/2601.14673) · [PDF](https://arxiv.org/pdf/2601.14673.pdf)  
**作者**：Yogesh Pipada Sunil Kumar, S. Ali Pourmousavi, Jon A. R. Liisberg, Julian Lesmos-Vinasco  

**一句话要点**：提出线性规划重构方法，将凸化ReLU深度神经网络嵌入电力系统优化中的代理建模。

**关键词**：电力系统优化, 代理建模, ReLU深度神经网络, 线性规划重构, 凸化神经网络, 分布式能源资源

## 3 点简述
- 电力系统去碳化导致分布式能源交互复杂，传统优化模型难以捕捉非线性关系。
- 针对权重矩阵非负的凸化ReLU深度神经网络，提出线性规划重构以实现紧致且可计算的优化嵌入。
- 在丹麦三级容量市场的聚合商投标案例中验证，相比现有方法，在保持解质量的同时显著提升计算性能。

## 摘要（原文）

> The ongoing decarbonisation of power systems is driving an increasing reliance on distributed energy resources, which introduces complex and nonlinear interactions that are difficult to capture in conventional optimisation models. As a result, machine learning based surrogate modelling has emerged as a promising approach, but integrating machine learning models such as ReLU deep neural networks (DNNs) directly into optimisation often results in nonconvex and computationally intractable formulations. This paper proposes a linear programming (LP) reformulation for a class of convexified ReLU DNNs with non-negative weight matrices beyond the first layer, enabling a tight and tractable embedding of learned surrogate models in optimisation. We evaluate the method using a case study on learning the prosumer's responsiveness within an aggregator bidding problem in the Danish tertiary capacity market. The proposed reformulation is benchmarked against state-of-the-art alternatives, including piecewise linearisation (PWL), MIP-based embedding, and other LP relaxations. Across multiple neural network architectures and market scenarios, the convexified ReLU DNN achieves solution quality comparable to PWL and MIP-based reformulations while significantly improving computational performance and preserving model fidelity, unlike penalty-based reformulations. The results demonstrate that convexified ReLU DNNs offer a scalable and reliable methodology for integrating learned surrogate models in optimisation, with applicability to a wide range of emerging power system applications.

