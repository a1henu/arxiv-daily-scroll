---
layout: default
title: IMS: Intelligent Hardware Monitoring System for Secure SoCs
---

# IMS: Intelligent Hardware Monitoring System for Secure SoCs
**arXiv**：[2601.11447v1](https://arxiv.org/abs/2601.11447) · [PDF](https://arxiv.org/pdf/2601.11447.pdf)  
**作者**：Wadid Foudhaili, Aykut Rencber, Anouar Nechi, Rainer Buchty, Mladen Berekovic, Andres Gomez, Saleh Mulhem  

**一句话要点**：提出智能硬件监控系统IMS，以实时检测AXI协议违规，增强SoC安全性。

**关键词**：AXI协议安全, 硬件监控系统, 神经网络检测, 实时协议分析, SoC安全增强, 边缘计算安全

## 3 点简述
- 核心问题：AXI协议存在安全漏洞，易受协议违规攻击导致DoS，现有对策缺乏实时语义分析。
- 方法要点：IMS利用神经网络进行实时监控，通过量化优化模型，实现高精度检测与低延迟开销。
- 实验或效果：在RISC-V SoC集成IMS，硬件开销小（如9.04% LUTs），检测准确率达98.7%，适用于资源受限边缘环境。

## 摘要（原文）

> In the modern Systems-on-Chip (SoC), the Advanced eXtensible Interface (AXI) protocol exhibits security vulnerabilities, enabling partial or complete denial-of-service (DoS) through protocol-violation attacks. The recent countermeasures lack a dedicated real-time protocol semantic analysis and evade protocol compliance checks. This paper tackles this AXI vulnerability issue and presents an intelligent hardware monitoring system (IMS) for real-time detection of AXI protocol violations. IMS is a hardware module leveraging neural networks to achieve high detection accuracy. For model training, we perform DoS attacks through header-field manipulation and systematic malicious operations, while recording AXI transactions to build a training dataset. We then deploy a quantization-optimized neural network, achieving 98.7% detection accuracy with <=3% latency overhead, and throughput of >2.5 million inferences/s. We subsequently integrate this IMS into a RISC-V SoC as a memory-mapped IP core to monitor its AXI bus. For demonstration and initial assessment for later ASIC integration, we implemented this IMS on an AMD Zynq UltraScale+ MPSoC ZCU104 board, showing an overall small hardware footprint (9.04% look-up-tables (LUTs), 0.23% DSP slices, and 0.70% flip-flops) and negligible impact on the overall design's achievable frequency. This demonstrates the feasibility of lightweight, security monitoring for resource-constrained edge environments.

