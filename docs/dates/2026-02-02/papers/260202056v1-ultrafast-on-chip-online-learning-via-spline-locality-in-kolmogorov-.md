---
layout: default
title: Ultrafast On-chip Online Learning via Spline Locality in Kolmogorov-Arnold Networks
---

# Ultrafast On-chip Online Learning via Spline Locality in Kolmogorov-Arnold Networks
**arXiv**：[2602.02056v1](https://arxiv.org/abs/2602.02056) · [PDF](https://arxiv.org/pdf/2602.02056.pdf)  
**作者**：Duc Hoang, Aarush Gupta, Philip Harris  

**一句话要点**：提出基于KAN的在线学习方法，以解决量子计算等高频系统在亚微秒级延迟下的快速适应问题。

**关键词**：在线学习, Kolmogorov-Arnold网络, 定点量化, FPGA实现, 低延迟系统, B样条局部性

## 3 点简述
- 核心问题：传统MLP在低延迟、固定精度和内存受限场景下效率低且数值不稳定。
- 方法要点：利用KAN的B样条局部性实现稀疏更新，并展示其对定点量化的鲁棒性。
- 实验或效果：在FPGA上实现定点在线训练，KAN比MLP更高效和表达性强，达到亚微秒级延迟。

## 摘要（原文）

> Ultrafast online learning is essential for high-frequency systems, such as controls for quantum computing and nuclear fusion, where adaptation must occur on sub-microsecond timescales. Meeting these requirements demands low-latency, fixed-precision computation under strict memory constraints, a regime in which conventional Multi-Layer Perceptrons (MLPs) are both inefficient and numerically unstable. We identify key properties of Kolmogorov-Arnold Networks (KANs) that align with these constraints. Specifically, we show that: (i) KAN updates exploiting B-spline locality are sparse, enabling superior on-chip resource scaling, and (ii) KANs are inherently robust to fixed-point quantization. By implementing fixed-point online training on Field-Programmable Gate Arrays (FPGAs), a representative platform for on-chip computation, we demonstrate that KAN-based online learners are significantly more efficient and expressive than MLPs across a range of low-latency and resource-constrained tasks. To our knowledge, this work is the first to demonstrate model-free online learning at sub-microsecond latencies.

