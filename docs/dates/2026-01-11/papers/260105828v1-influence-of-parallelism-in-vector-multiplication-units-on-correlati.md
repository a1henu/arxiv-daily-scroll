---
layout: default
title: Influence of Parallelism in Vector-Multiplication Units on Correlation Power Analysis
---

# Influence of Parallelism in Vector-Multiplication Units on Correlation Power Analysis
**arXiv**：[2601.05828v1](https://arxiv.org/abs/2601.05828) · [PDF](https://arxiv.org/pdf/2601.05828.pdf)  
**作者**：Manuel Brosch, Matthias Probst, Stefan Kögler, Georg Sigl  

**一句话要点**：分析向量乘法单元并行度对相关功耗分析攻击成功率的影响

**关键词**：相关功耗分析, 硬件加速器, 并行处理, 侧信道攻击, 神经网络安全, FPGA验证

## 3 点简述
- 研究神经网络硬件加速器中并行处理对基于功耗的侧信道攻击的影响
- 推导并行度增加导致相关性降低的理论方程
- 在FPGA上实现向量乘法单元验证方程适用性

## 摘要（原文）

> The use of neural networks in edge devices is increasing, which introduces new security challenges related to the neural networks' confidentiality. As edge devices often offer physical access, attacks targeting the hardware, such as side-channel analysis, must be considered. To enhance the performance of neural network inference, hardware accelerators are commonly employed. This work investigates the influence of parallel processing within such accelerators on correlation-based side-channel attacks that exploit power consumption. The focus is on neurons that are part of the same fully-connected layer, which run parallel and simultaneously process the same input value. The theoretical impact of concurrent multiply-and-accumulate operations on overall power consumption is evaluated, as well as the success rate of correlation power analysis. Based on the observed behavior, equations are derived that describe how the correlation decreases with increasing levels of parallelism. The applicability of these equations is validated using a vector-multiplication unit implemented on an FPGA.

