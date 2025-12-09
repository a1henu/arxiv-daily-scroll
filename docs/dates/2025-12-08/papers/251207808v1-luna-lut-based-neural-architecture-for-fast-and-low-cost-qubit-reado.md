---
layout: default
title: LUNA: LUT-Based Neural Architecture for Fast and Low-Cost Qubit Readout
---

# LUNA: LUT-Based Neural Architecture for Fast and Low-Cost Qubit Readout
**arXiv**：[2512.07808v1](https://arxiv.org/abs/2512.07808) · [PDF](https://arxiv.org/pdf/2512.07808.pdf)  
**作者**：M. A. Farooq, G. Di Guglielmo, A. Rajagopala, N. Tran, V. A. Chhabria, A. Arora  

**一句话要点**：提出LUNA架构，结合LUT神经网络与积分器预处理，实现快速低成本的量子比特读出

**关键词**：量子比特读出, LUT神经网络, 硬件加速, 低延迟推理, 量子计算系统

## 3 点简述
- 量子比特读出中，基于DNN的硬件实现资源密集且延迟高，限制量子纠错应用
- LUNA采用积分器降维和LUT神经网络分类，减少硬件开销并实现超低延迟推理
- 实验显示面积减少10.95倍，延迟降低30%，保真度损失极小，支持可扩展量子系统

## 摘要（原文）

> Qubit readout is a critical operation in quantum computing systems, which maps the analog response of qubits into discrete classical states. Deep neural networks (DNNs) have recently emerged as a promising solution to improve readout accuracy . Prior hardware implementations of DNN-based readout are resource-intensive and suffer from high inference latency, limiting their practical use in low-latency decoding and quantum error correction (QEC) loops. This paper proposes LUNA, a fast and efficient superconducting qubit readout accelerator that combines low-cost integrator-based preprocessing with Look-Up Table (LUT) based neural networks for classification. The architecture uses simple integrators for dimensionality reduction with minimal hardware overhead, and employs LogicNets (DNNs synthesized into LUT logic) to drastically reduce resource usage while enabling ultra-low-latency inference. We integrate this with a differential evolution based exploration and optimization framework to identify high-quality design points. Our results show up to a 10.95x reduction in area and 30% lower latency with little to no loss in fidelity compared to the state-of-the-art. LUNA enables scalable, low-footprint, and high-speed qubit readout, supporting the development of larger and more reliable quantum computing systems.

