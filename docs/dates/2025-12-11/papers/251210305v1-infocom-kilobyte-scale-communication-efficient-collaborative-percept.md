---
layout: default
title: InfoCom: Kilobyte-Scale Communication-Efficient Collaborative Perception with Information Bottleneck
---

# InfoCom: Kilobyte-Scale Communication-Efficient Collaborative Perception with Information Bottleneck
**arXiv**：[2512.10305v1](https://arxiv.org/abs/2512.10305) · [PDF](https://arxiv.org/pdf/2512.10305.pdf)  
**作者**：Quanmin Wei, Penglin Dai, Wei Li, Bingyi Liu, Xiao Wu  

**一句话要点**：提出InfoCom框架，通过信息瓶颈理论实现千字节级通信高效的协同感知，解决自动驾驶中的通信-性能权衡问题。

**关键词**：协同感知, 信息瓶颈, 通信效率, 自动驾驶, 信息净化, 千字节级通信

## 3 点简述
- 核心问题：协同感知面临通信开销与感知性能的权衡，现有方法假设兆字节级传输，可能受实际网络限制影响。
- 方法要点：引入信息净化范式，包括信息感知编码、稀疏掩码生成和多尺度解码，以提取最小充分任务关键信息。
- 实验或效果：在多个数据集上验证，InfoCom实现近无损感知，通信开销从兆字节降至千字节级，相比基准方法大幅降低。

## 摘要（原文）

> Precise environmental perception is critical for the reliability of autonomous driving systems. While collaborative perception mitigates the limitations of single-agent perception through information sharing, it encounters a fundamental communication-performance trade-off. Existing communication-efficient approaches typically assume MB-level data transmission per collaboration, which may fail due to practical network constraints. To address these issues, we propose InfoCom, an information-aware framework establishing the pioneering theoretical foundation for communication-efficient collaborative perception via extended Information Bottleneck principles. Departing from mainstream feature manipulation, InfoCom introduces a novel information purification paradigm that theoretically optimizes the extraction of minimal sufficient task-critical information under Information Bottleneck constraints. Its core innovations include: i) An Information-Aware Encoding condensing features into minimal messages while preserving perception-relevant information; ii) A Sparse Mask Generation identifying spatial cues with negligible communication cost; and iii) A Multi-Scale Decoding that progressively recovers perceptual information through mask-guided mechanisms rather than simple feature reconstruction. Comprehensive experiments across multiple datasets demonstrate that InfoCom achieves near-lossless perception while reducing communication overhead from megabyte to kilobyte-scale, representing 440-fold and 90-fold reductions per agent compared to Where2comm and ERMVP, respectively.

