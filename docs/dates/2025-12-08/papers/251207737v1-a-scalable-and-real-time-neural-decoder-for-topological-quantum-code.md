---
layout: default
title: A scalable and real-time neural decoder for topological quantum codes
---

# A scalable and real-time neural decoder for topological quantum codes
**arXiv**：[2512.07737v1](https://arxiv.org/abs/2512.07737) · [PDF](https://arxiv.org/pdf/2512.07737.pdf)  
**作者**：Andrew W. Senior, Thomas Edlich, Francisco J. H. Heras, Lei M. Zhang, Oscar Higgott, James S. Spencer, Taylor Applebaum, Sam Blackwell, Justin Ledford, Akvilė Žemgulytė, Augustin Žídek, Noah Shutty, Andrew Cowie, Yin Li, George Holland, Peter Brooks, Charlie Beattie, Michael Newman, Alex Davies, Cody Jones, Sergio Boixo, Hartmut Neven, Pushmeet Kohli, Johannes Bausch  

**一句话要点**：提出AlphaQubit 2神经解码器，实现拓扑量子码的高精度实时解码

**关键词**：量子纠错, 神经解码器, 拓扑量子码, 表面码, 颜色码, 实时解码

## 3 点简述
- 量子纠错需解码器兼具快速、准确和可扩展性，现有方法未满足此要求
- AlphaQubit 2基于神经网络，对表面码和颜色码在大规模下实现近最优逻辑错误率
- 实验显示颜色码解码速度比高精度解码器快多个数量级，表面码解码速度快于1微秒每周期

## 摘要（原文）

> Fault-tolerant quantum computing will require error rates far below those achievable with physical qubits. Quantum error correction (QEC) bridges this gap, but depends on decoders being simultaneously fast, accurate, and scalable. This combination of requirements has not yet been met by a machine-learning decoder, nor by any decoder for promising resource-efficient codes such as the colour code. Here we introduce AlphaQubit 2, a neural-network decoder that achieves near-optimal logical error rates for both surface and colour codes at large scales under realistic noise. For the colour code, it is orders of magnitude faster than other high-accuracy decoders. For the surface code, we demonstrate real-time decoding faster than 1 microsecond per cycle up to distance 11 on current commercial accelerators with better accuracy than leading real-time decoders. These results support the practical application of a wider class of promising QEC codes, and establish a credible path towards high-accuracy, real-time neural decoding at the scales required for fault-tolerant quantum computation.

