---
layout: default
title: A Multiplicative Neural Network Architecture: Locality and Regularity of Appriximation
---

# A Multiplicative Neural Network Architecture: Locality and Regularity of Appriximation
**arXiv**：[2602.06374v1](https://arxiv.org/abs/2602.06374) · [PDF](https://arxiv.org/pdf/2602.06374.pdf)  
**作者**：Hee-Sun Choi, Beom-Seok Han  

**一句话要点**：提出乘法神经网络架构，以乘法交互为核心表示，分析其在Bessel势空间中的局部性与正则性逼近特性。

**关键词**：乘法神经网络, 通用逼近定理, Bessel势空间, 局部性逼近, 正则性分析, 数值实验

## 3 点简述
- 核心问题：传统神经网络以加法模型为主，乘法交互常作为辅助组件，缺乏对乘法表示格式在逼近局部性和正则性方面影响的系统分析。
- 方法要点：引入乘法神经网络架构，其中乘法交互构成基本表示，而非加法模型中的辅助部分，并建立通用逼近定理，在Bessel势空间中分析其逼近的局部性和正则性。
- 实验或效果：数值实验针对具有尖锐过渡层或高阶正则性点态损失的目标函数，显示该架构的残差误差结构更紧密对齐于正则性降低区域，并在正则性敏感度量中表现出更稳定的收敛。

## 摘要（原文）

> We introduce a multiplicative neural network architecture in which multiplicative interactions constitute the fundamental representation, rather than appearing as auxiliary components within an additive model. We establish a universal approximation theorem for this architecture and analyze its approximation properties in terms of locality and regularity in Bessel potential spaces.
>   To complement the theoretical results, we conduct numerical experiments on representative targets exhibiting sharp transition layers or pointwise loss of higher-order regularity. The experiments focus on the spatial structure of approximation errors and on regularity-sensitive quantities, in particular the convergence of Zygmund-type seminorms. The results show that the proposed multiplicative architecture yields residual error structures that are more tightly aligned with regions of reduced regularity and exhibits more stable convergence in regularity-sensitive metrics.
>   These results demonstrate that adopting a multiplicative representation format has concrete implications for the localization and regularity behavior of neural network approximations, providing a direct connection between architectural design and analytical properties of the approximating functions.

