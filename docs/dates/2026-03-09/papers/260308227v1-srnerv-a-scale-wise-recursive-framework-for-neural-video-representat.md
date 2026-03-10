---
layout: default
title: SRNeRV: A Scale-wise Recursive Framework for Neural Video Representation
---

# SRNeRV: A Scale-wise Recursive Framework for Neural Video Representation
**arXiv**：[2603.08227v1](https://arxiv.org/abs/2603.08227) · [PDF](https://arxiv.org/pdf/2603.08227.pdf)  
**作者**：Jia Wang, Jun Zhu, Xinfeng Zhang  

**一句话要点**：提出SRNeRV框架，通过尺度递归共享架构减少参数冗余，提升神经视频表示效率。

**关键词**：隐式神经表示, 视频压缩, 多尺度生成, 参数效率, 递归架构, 率失真优化

## 3 点简述
- 现有多尺度隐式神经表示生成器存在参数冗余问题，因各尺度独立处理块堆叠导致。
- SRNeRV采用混合共享方案，将处理块解耦为尺度特定空间混合模块和尺度不变通道混合模块，递归共享通道模块。
- 实验表明SRNeRV在率失真性能上显著提升，尤其在INR友好场景中，验证了共享方案的有效性。

## 摘要（原文）

> Implicit Neural Representations (INRs) have emerged as a promising paradigm for video representation and compression. However, existing multi-scale INR generators often suffer from significant parameter redundancy by stacking independent processing blocks for each scale. Inspired by the principle of scale self-similarity in the generation process, we propose SRNeRV, a novel scale-wise recursive framework that replaces this stacked design with a parameter-efficient shared architecture. The core of our approach is a hybrid sharing scheme derived from decoupling the processing block into a scale-specific spatial mixing module and a scale-invariant channel mixing module. We recursively apply the same shared channel mixing module, which contains the majority of the parameters, across all scales, significantly reducing the model size while preserving the crucial capacity to learn scale-specific spatial patterns. Extensive experiments demonstrate that SRNeRV achieves a significant rate-distortion performance boost, especially in INR-friendly scenarios, validating that our sharing scheme successfully amplifies the core strengths of the INR paradigm.

