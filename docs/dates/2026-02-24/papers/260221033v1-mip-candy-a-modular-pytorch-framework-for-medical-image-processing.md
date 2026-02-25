---
layout: default
title: MIP Candy: A Modular PyTorch Framework for Medical Image Processing
---

# MIP Candy: A Modular PyTorch Framework for Medical Image Processing
**arXiv**：[2602.21033v1](https://arxiv.org/abs/2602.21033) · [PDF](https://arxiv.org/pdf/2602.21033.pdf)  
**作者**：Tianhao Fu, Yucheng Chen  

**一句话要点**：提出MIP Candy框架以解决医学图像处理中软件集成困难与流程僵化问题

**关键词**：医学图像处理, PyTorch框架, 模块化设计, 深度学习训练, 开源软件

## 3 点简述
- 核心问题：现有框架集成复杂或流程僵化，难以适应医学图像处理的高维数据与领域需求
- 方法要点：基于PyTorch的模块化框架，通过build_network和LayerT机制实现灵活配置与控制
- 实验或效果：提供完整流程与扩展包，支持交叉验证、实验跟踪等功能，开源可用

## 摘要（原文）

> Medical image processing demands specialized software that handles high-dimensional volumetric data, heterogeneous file formats, and domain-specific training procedures. Existing frameworks either provide low-level components that require substantial integration effort or impose rigid, monolithic pipelines that resist modification. We present MIP Candy (MIPCandy), a freely available, PyTorch-based framework designed specifically for medical image processing. MIPCandy provides a complete, modular pipeline spanning data loading, training, inference, and evaluation, allowing researchers to obtain a fully functional process workflow by implementing a single method, $\texttt{build_network}$, while retaining fine-grained control over every component. Central to the design is $\texttt{LayerT}$, a deferred configuration mechanism that enables runtime substitution of convolution, normalization, and activation modules without subclassing. The framework further offers built-in $k$-fold cross-validation, dataset inspection with automatic region-of-interest detection, deep supervision, exponential moving average, multi-frontend experiment tracking (Weights & Biases, Notion, MLflow), training state recovery, and validation score prediction via quotient regression. An extensible bundle ecosystem provides pre-built model implementations that follow a consistent trainer--predictor pattern and integrate with the core framework without modification. MIPCandy is open-source under the Apache-2.0 license and requires Python~3.12 or later. Source code and documentation are available at https://github.com/ProjectNeura/MIPCandy.

