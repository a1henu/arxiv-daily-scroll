---
layout: default
title: AnyDepth: Depth Estimation Made Easy
---

# AnyDepth: Depth Estimation Made Easy
**arXiv**：[2601.02760v1](https://arxiv.org/abs/2601.02760) · [PDF](https://arxiv.org/pdf/2601.02760.pdf)  
**作者**：Zeyu Ren, Zeyu Zhang, Wukai Li, Qingxiang Liu, Hao Tang  

**一句话要点**：提出AnyDepth框架，通过轻量解码器和数据过滤实现高效零样本单目深度估计。

**关键词**：单目深度估计, 零样本学习, Transformer解码器, 数据过滤, 轻量模型

## 3 点简述
- 核心问题：现有方法依赖大规模数据集和复杂解码器，效率与泛化能力受限。
- 方法要点：采用DINOv3编码器，设计Simple Depth Transformer解码器，减少参数约85%-89%。
- 实验或效果：在五个基准测试中超越DPT，强调模型设计与数据质量的平衡。

## 摘要（原文）

> Monocular depth estimation aims to recover the depth information of 3D scenes from 2D images. Recent work has made significant progress, but its reliance on large-scale datasets and complex decoders has limited its efficiency and generalization ability. In this paper, we propose a lightweight and data-centric framework for zero-shot monocular depth estimation. We first adopt DINOv3 as the visual encoder to obtain high-quality dense features. Secondly, to address the inherent drawbacks of the complex structure of the DPT, we design the Simple Depth Transformer (SDT), a compact transformer-based decoder. Compared to the DPT, it uses a single-path feature fusion and upsampling process to reduce the computational overhead of cross-scale feature fusion, achieving higher accuracy while reducing the number of parameters by approximately 85%-89%. Furthermore, we propose a quality-based filtering strategy to filter out harmful samples, thereby reducing dataset size while improving overall training quality. Extensive experiments on five benchmarks demonstrate that our framework surpasses the DPT in accuracy. This work highlights the importance of balancing model design and data quality for achieving efficient and generalizable zero-shot depth estimation. Code: https://github.com/AIGeeksGroup/AnyDepth. Website: https://aigeeksgroup.github.io/AnyDepth.

