---
layout: default
title: DeepONet-accelerated Bayesian inversion for moving boundary problems
---

# DeepONet-accelerated Bayesian inversion for moving boundary problems
**arXiv**：[2512.20268v1](https://arxiv.org/abs/2512.20268) · [PDF](https://arxiv.org/pdf/2512.20268.pdf)  
**作者**：Marco A. Iglesias, Michael. E. Causon, Mikhail Y. Matveev, Andreas Endruweit, Michael . V. Tretyakov  

**一句话要点**：提出基于DeepONet的贝叶斯反演框架，加速多孔介质移动边界问题求解，应用于复合材料制造监控。

**关键词**：移动边界问题, 神经算子学习, 贝叶斯反演, 数字孪生, 多孔介质流, 复合材料制造

## 3 点简述
- 核心问题：移动边界系统（如多孔介质单相达西流）的贝叶斯反演计算成本高，阻碍实时数字孪生应用。
- 方法要点：采用DeepONet构建高效代理模型，结合集成卡尔曼反演算法，实现快速参数估计。
- 实验或效果：在树脂传递模塑过程中，使用合成和实验数据，反演速度比全模型方法快几个数量级，支持高分辨率参数实时估计。

## 摘要（原文）

> This work demonstrates that neural operator learning provides a powerful and flexible framework for building fast, accurate emulators of moving boundary systems, enabling their integration into digital twin platforms. To this end, a Deep Operator Network (DeepONet) architecture is employed to construct an efficient surrogate model for moving boundary problems in single-phase Darcy flow through porous media. The surrogate enables rapid and accurate approximation of complex flow dynamics and is coupled with an Ensemble Kalman Inversion (EKI) algorithm to solve Bayesian inverse problems.
>   The proposed inversion framework is demonstrated by estimating the permeability and porosity of fibre reinforcements for composite materials manufactured via the Resin Transfer Moulding (RTM) process. Using both synthetic and experimental in-process data, the DeepONet surrogate accelerates inversion by several orders of magnitude compared with full-model EKI. This computational efficiency enables real-time, accurate, high-resolution estimation of local variations in permeability, porosity, and other parameters, thereby supporting effective monitoring and control of RTM processes, as well as other applications involving moving boundary flows. Unlike prior approaches for RTM inversion that learn mesh-dependent mappings, the proposed neural operator generalises across spatial and temporal domains, enabling evaluation at arbitrary sensor configurations without retraining, and represents a significant step toward practical industrial deployment of digital twins.

