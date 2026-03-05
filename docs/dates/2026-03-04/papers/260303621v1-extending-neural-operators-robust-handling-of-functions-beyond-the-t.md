---
layout: default
title: Extending Neural Operators: Robust Handling of Functions Beyond the Training Set
---

# Extending Neural Operators: Robust Handling of Functions Beyond the Training Set
**arXiv**：[2603.03621v1](https://arxiv.org/abs/2603.03621) · [PDF](https://arxiv.org/pdf/2603.03621.pdf)  
**作者**：Blaine Quackenbush, Paul J. Atzberger  

**一句话要点**：提出基于核近似的神经算子扩展框架，以处理分布外输入函数并提升泛化能力。

**关键词**：神经算子扩展, 分布外泛化, 核近似, 再生核希尔伯特空间, 偏微分方程求解, 点云表示

## 3 点简述
- 核心问题：神经算子处理分布外输入函数时缺乏理论保证和可靠性。
- 方法要点：利用核近似技术，在再生核希尔伯特空间理论下建立扩展框架，确保函数值及导数的可靠捕获。
- 实验或效果：通过椭圆偏微分方程求解验证方法，评估精度和计算性能的关键因素。

## 摘要（原文）

> We develop a rigorous framework for extending neural operators to handle out-of-distribution input functions. We leverage kernel approximation techniques and provide theory for characterizing the input-output function spaces in terms of Reproducing Kernel Hilbert Spaces (RKHSs). We provide theorems on the requirements for reliable extensions and their predicted approximation accuracy. We also establish formal relationships between specific kernel choices and their corresponding Sobolev Native Spaces. This connection further allows the extended neural operators to reliably capture not only function values but also their derivatives. Our methods are empirically validated through the solution of elliptic partial differential equations (PDEs) involving operators on manifolds having point-cloud representations and handling geometric contributions. We report results on key factors impacting the accuracy and computational performance of the extension approaches.

