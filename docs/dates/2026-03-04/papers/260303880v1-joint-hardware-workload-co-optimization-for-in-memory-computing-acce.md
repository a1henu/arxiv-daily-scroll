---
layout: default
title: Joint Hardware-Workload Co-Optimization for In-Memory Computing Accelerators
---

# Joint Hardware-Workload Co-Optimization for In-Memory Computing Accelerators
**arXiv**：[2603.03880v1](https://arxiv.org/abs/2603.03880) · [PDF](https://arxiv.org/pdf/2603.03880.pdf)  
**作者**：Olga Krestinskaya, Mohammed E. Fouda, Ahmed Eltawil, Khaled N. Salama  

**一句话要点**：提出联合硬件-工作负载协同优化框架，以设计通用内存计算加速器架构。

**关键词**：内存计算加速器, 硬件-软件协同设计, 进化算法优化, 跨工作负载优化, 能量-延迟-面积积

## 3 点简述
- 现有内存计算加速器优化框架多针对单一工作负载，导致硬件设计泛化能力差。
- 基于优化进化算法，该框架通过捕获跨工作负载权衡，减少专用与通用设计间的性能差距。
- 在RRAM和SRAM架构上评估，优化设计在能量-延迟-面积积上最高减少95.5%。

## 摘要（原文）

> Software-hardware co-design is essential for optimizing in-memory computing (IMC) hardware accelerators for neural networks. However, most existing optimization frameworks target a single workload, leading to highly specialized hardware designs that do not generalize well across models and applications. In contrast, practical deployment scenarios require a single IMC platform that can efficiently support multiple neural network workloads. This work presents a joint hardware-workload co-optimization framework based on an optimized evolutionary algorithm for designing generalized IMC accelerator architectures. By explicitly capturing cross-workload trade-offs rather than optimizing for a single model, the proposed approach significantly reduces the performance gap between workload-specific and generalized IMC designs. The framework is evaluated on both RRAM- and SRAM-based IMC architectures, demonstrating strong robustness and adaptability across diverse design scenarios. Compared to baseline methods, the optimized designs achieve energy-delay-area product (EDAP) reductions of up to 76.2% and 95.5% when optimizing across a small set (4 workloads) and a large set (9 workloads), respectively. The source code of the framework is available at https://github.com/OlgaKrestinskaya/JointHardwareWorkloadOptimizationIMC.

