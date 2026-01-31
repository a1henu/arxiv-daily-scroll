---
layout: default
title: Rate-Distortion Optimization for Transformer Inference
---

# Rate-Distortion Optimization for Transformer Inference
**arXiv**：[2601.22002v1](https://arxiv.org/abs/2601.22002) · [PDF](https://arxiv.org/pdf/2601.22002.pdf)  
**作者**：Anderson de Andrade, Alon Harell, Ivan V. Bajić  

**一句话要点**：提出基于率失真优化的Transformer中间表示压缩框架，以提升多设备推理效率。

**关键词**：Transformer推理, 率失真优化, 中间表示压缩, 多设备分区, 信息理论分析

## 3 点简述
- 核心问题：Transformer推理时计算和内存需求高，多设备分区需压缩中间表示。
- 方法要点：引入率失真理论框架，学习紧凑编码以权衡比特率与准确性。
- 实验或效果：在语言基准测试中实现显著节省，部分情况下准确性提升，优于复杂基线方法。

## 摘要（原文）

> Transformers achieve superior performance on many tasks, but impose heavy compute and memory requirements during inference. This inference can be made more efficient by partitioning the process across multiple devices, which, in turn, requires compressing its intermediate representations. In this work, we introduce a principled rate-distortion-based framework for lossy compression that learns compact encodings that explicitly trade off bitrate against accuracy. Experiments on language benchmarks show that the proposed codec achieves substantial savings with improved accuracy in some cases, outperforming more complex baseline methods. We characterize and analyze the rate-distortion performance of transformers, offering a unified lens for understanding performance in representation coding. This formulation extends information-theoretic concepts to define the gap between rate and entropy, and derive some of its bounds. We further develop probably approximately correct (PAC)-style bounds for estimating this gap. For different architectures and tasks, we empirically demonstrate that their rates are driven by these bounds, adding to the explainability of the formulation.

