---
layout: default
title: Chimera: Neuro-Symbolic Attention Primitives for Trustworthy Dataplane Intelligence
---

# Chimera: Neuro-Symbolic Attention Primitives for Trustworthy Dataplane Intelligence
**arXiv**：[2602.12851v1](https://arxiv.org/abs/2602.12851) · [PDF](https://arxiv.org/pdf/2602.12851.pdf)  
**作者**：Rong Fu, Wenxin Zhang, Xiaowen Ma, Kun Liu, Wangyu Wu, Ziyu Kong, Jia Yee Tan, Tailong Luo, Xianda Li, Zeli Su, Youjin Wang, Yongtai Liu, Simon Fong  

**一句话要点**：提出Chimera框架，将神经符号注意力原语映射到数据平面，实现可编程交换机上的可信推理。

**关键词**：神经符号计算, 可编程数据平面, 注意力机制, 硬件映射, 可信推理, 流量分析

## 3 点简述
- 核心问题：可编程数据平面部署学习模型受硬件限制和可预测行为需求阻碍。
- 方法要点：结合核化线性注意力近似、两层键选择层次和级联融合机制，确保符号保证和神经表达性。
- 实验或效果：在商用交换机资源限制下实现高保真推理，支持线速稳定操作。

## 摘要（原文）

> Deploying expressive learning models directly on programmable dataplanes promises line-rate, low-latency traffic analysis but remains hindered by strict hardware constraints and the need for predictable, auditable behavior. Chimera introduces a principled framework that maps attention-oriented neural computations and symbolic constraints onto dataplane primitives, enabling trustworthy inference within the match-action pipeline. Chimera combines a kernelized, linearized attention approximation with a two-layer key-selection hierarchy and a cascade fusion mechanism that enforces hard symbolic guarantees while preserving neural expressivity. The design includes a hardware-aware mapping protocol and a two-timescale update scheme that together permit stable, line-rate operation under realistic dataplane budgets. The paper presents the Chimera architecture, a hardware mapping strategy, and empirical evidence showing that neuro-symbolic attention primitives can achieve high-fidelity inference within the resource envelope of commodity programmable switches.

