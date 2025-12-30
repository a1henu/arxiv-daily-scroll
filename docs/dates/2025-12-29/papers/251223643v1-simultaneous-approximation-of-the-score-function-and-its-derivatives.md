---
layout: default
title: Simultaneous Approximation of the Score Function and Its Derivatives by Deep Neural Networks
---

# Simultaneous Approximation of the Score Function and Its Derivatives by Deep Neural Networks
**arXiv**：[2512.23643v1](https://arxiv.org/abs/2512.23643) · [PDF](https://arxiv.org/pdf/2512.23643.pdf)  
**作者**：Konstantin Yakovlev, Nikita Puchkin  

**一句话要点**：提出深度神经网络同时逼近分数函数及其导数的理论，以处理低维结构且无界支持的数据分布。

**关键词**：分数函数逼近, 深度神经网络, 无界支持分布, 低维结构, 导数逼近, 维度灾难避免

## 3 点简述
- 核心问题：现有方法通常要求数据分布有界支持，限制了在无界支持或低维结构分布中的应用。
- 方法要点：建立同时逼近分数函数及其任意阶导数的理论，放宽有界支持假设，避免维度灾难。
- 实验或效果：逼近误差界与文献匹配，适用于更广泛的数据分布，扩展至高阶导数设置。

## 摘要（原文）

> We present a theory for simultaneous approximation of the score function and its derivatives, enabling the handling of data distributions with low-dimensional structure and unbounded support. Our approximation error bounds match those in the literature while relying on assumptions that relax the usual bounded support requirement. Crucially, our bounds are free from the curse of dimensionality. Moreover, we establish approximation guarantees for derivatives of any prescribed order, extending beyond the commonly considered first-order setting.

