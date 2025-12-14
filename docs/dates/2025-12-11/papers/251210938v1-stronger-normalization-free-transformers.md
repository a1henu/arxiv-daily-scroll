---
layout: default
title: Stronger Normalization-Free Transformers
---

# Stronger Normalization-Free Transformers
**arXiv**：[2512.10938v1](https://arxiv.org/abs/2512.10938) · [PDF](https://arxiv.org/pdf/2512.10938.pdf)  
**作者**：Mingzhi Chen, Taiming Lu, Jiachen Zhu, Mingjie Sun, Zhuang Liu  

**一句话要点**：提出Derf函数以替代归一化层，在Transformer中实现更强性能

**关键词**：归一化替代, Transformer架构, 点函数设计, 图像识别, 语音表示, DNA序列建模

## 3 点简述
- 研究点函数内在属性对训练和性能的影响，指导函数设计
- 通过大规模搜索，引入Derf函数作为最有效的归一化替代方案
- 在视觉、语音和DNA建模等任务中，Derf超越现有归一化方法

## 摘要（原文）

> Although normalization layers have long been viewed as indispensable components of deep learning architectures, the recent introduction of Dynamic Tanh (DyT) has demonstrated that alternatives are possible. The point-wise function DyT constrains extreme values for stable convergence and reaches normalization-level performance; this work seeks further for function designs that can surpass it. We first study how the intrinsic properties of point-wise functions influence training and performance. Building on these findings, we conduct a large-scale search for a more effective function design. Through this exploration, we introduce $\mathrm{Derf}(x) = \mathrm{erf}(αx + s)$, where $\mathrm{erf}(x)$ is the rescaled Gaussian cumulative distribution function, and identify it as the most performant design. Derf outperforms LayerNorm, RMSNorm, and DyT across a wide range of domains, including vision (image recognition and generation), speech representation, and DNA sequence modeling. Our findings suggest that the performance gains of Derf largely stem from its improved generalization rather than stronger fitting capacity. Its simplicity and stronger performance make Derf a practical choice for normalization-free Transformer architectures.

