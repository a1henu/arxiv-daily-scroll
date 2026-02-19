---
layout: default
title: Structured Unitary Tensor Network Representations for Circuit-Efficient Quantum Data Encoding
---

# Structured Unitary Tensor Network Representations for Circuit-Efficient Quantum Data Encoding
**arXiv**：[2602.16266v1](https://arxiv.org/abs/2602.16266) · [PDF](https://arxiv.org/pdf/2602.16266.pdf)  
**作者**：Guang Lin, Toshihisa Tanaka, Qibin Zhao  

**一句话要点**：提出基于结构化酉张量网络的TNQE框架，以解决量子数据编码的电路效率瓶颈。

**关键词**：量子数据编码, 张量网络, 电路效率, 酉约束, 量子机器学习, 硬件可扩展性

## 3 点简述
- 核心问题：量子机器学习中经典数据编码常需深电路，限制硬件可扩展性。
- 方法要点：通过张量网络分解输入，编译为浅层编码电路，引入酉约束优化参数。
- 实验或效果：编码电路深度降至振幅编码的0.04倍，支持高分辨率图像，硬件可行。

## 摘要（原文）

> Encoding classical data into quantum states is a central bottleneck in quantum machine learning: many widely used encodings are circuit-inefficient, requiring deep circuits and substantial quantum resources, which limits scalability on quantum hardware. In this work, we propose TNQE, a circuit-efficient quantum data encoding framework built on structured unitary tensor network (TN) representations. TNQE first represents each classical input via a TN decomposition and then compiles the resulting tensor cores into an encoding circuit through two complementary core-to-circuit strategies. To make this compilation trainable while respecting the unitary nature of quantum operations, we introduce a unitary-aware constraint that parameterizes TN cores as learnable block unitaries, enabling them to be directly optimized and directly encoded as quantum operators. The proposed TNQE framework enables explicit control over circuit depth and qubit resources, allowing the construction of shallow, resource-efficient circuits. Across a range of benchmarks, TNQE achieves encoding circuits as shallow as $0.04\times$ the depth of amplitude encoding, while naturally scaling to high-resolution images ($256 \times 256$) and demonstrating practical feasibility on real quantum hardware.

