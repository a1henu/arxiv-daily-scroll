---
layout: default
title: Float8@2bits: Entropy Coding Enables Data-Free Model Compression
---

# Float8@2bits: Entropy Coding Enables Data-Free Model Compression
**arXiv**：[2601.22787v1](https://arxiv.org/abs/2601.22787) · [PDF](https://arxiv.org/pdf/2601.22787.pdf)  
**作者**：Patrick Putzky, Martin Genzel, Mattes Mollenhauer, Sebastian Schulze, Thomas Wollmann, Stefan Dietzel  

**一句话要点**：提出EntQuant框架，通过熵编码实现数据无关的极端模型压缩，解决低比特率下功能崩溃问题。

**关键词**：模型压缩, 熵编码, 后训练压缩, 数据无关方法, 极端比特率, 功能保留

## 3 点简述
- 核心问题：后训练压缩在低于4比特的极端比特率下，数据无关方法易功能崩溃，数据依赖方法计算成本高且鲁棒性未知。
- 方法要点：EntQuant利用熵编码解耦数值精度与存储成本，实现快速、数据无关的压缩，无需校准数据或恢复训练。
- 实验或效果：在70B参数模型上压缩时间少于30分钟，在标准评估集和指令调优模型上保持先进性能，推理开销适中。

## 摘要（原文）

> Post-training compression is currently divided into two contrasting regimes. On the one hand, fast, data-free, and model-agnostic methods (e.g., NF4 or HQQ) offer maximum accessibility but suffer from functional collapse at extreme bit-rates below 4 bits. On the other hand, techniques leveraging calibration data or extensive recovery training achieve superior fidelity but impose high computational constraints and face uncertain robustness under data distribution shifts. We introduce EntQuant, the first framework to unite the advantages of these distinct paradigms. By matching the performance of data-dependent methods with the speed and universality of data-free techniques, EntQuant enables practical utility in the extreme compression regime. Our method decouples numerical precision from storage cost via entropy coding, compressing a 70B parameter model in less than 30 minutes. We demonstrate that EntQuant does not only achieve state-of-the-art results on standard evaluation sets and models, but also retains functional performance on more complex benchmarks with instruction-tuned models, all at modest inference overhead.

