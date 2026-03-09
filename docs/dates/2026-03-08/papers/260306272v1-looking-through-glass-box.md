---
layout: default
title: Looking Through Glass Box
---

# Looking Through Glass Box
**arXiv**：[2603.06272v1](https://arxiv.org/abs/2603.06272) · [PDF](https://arxiv.org/pdf/2603.06272.pdf)  
**作者**：Alexis Kafantaris  

**一句话要点**：提出基于模糊认知图的神经网络实现，通过逆求解提供修改准则以优化服务或产品适配。

**关键词**：模糊认知图, 神经网络实现, 朗之万微分动力学, 逆求解, 因果关系学习

## 3 点简述
- 核心问题：如何用神经网络模拟模糊认知图以学习因果关系模式。
- 方法要点：设计神经网络接受多个模糊认知图输入，使用朗之万微分动力学避免过拟合，进行逆求解。
- 实验或效果：在多个数据集上评估网络性能，逆求解提供修改准则以适配不同服务或产品。

## 摘要（原文）

> This essay is about a neural implementation of the fuzzy cognitive map, the FHM, and corresponding evaluations. Firstly, a neural net has been designed to behave the same way that an FCM does; as inputs it accepts many fuzzy cognitive maps and propagates them in order to learn causality patterns. Moreover, the network uses langevin differential Dynamics, which avoid overfit, to inverse solve the output node values according to some policy. Nevertheless, having obtained an inverse solution provides the user a modification criterion. Having the modification criterion suggests that information is now according to discretion as a different service or product is a better fit. Lastly, evaluation has been done on several data sets in order to examine the networks performance.

