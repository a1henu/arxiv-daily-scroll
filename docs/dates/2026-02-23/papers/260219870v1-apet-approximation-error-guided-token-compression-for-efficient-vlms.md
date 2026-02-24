---
layout: default
title: ApET: Approximation-Error Guided Token Compression for Efficient VLMs
---

# ApET: Approximation-Error Guided Token Compression for Efficient VLMs
**arXiv**：[2602.19870v1](https://arxiv.org/abs/2602.19870) · [PDF](https://arxiv.org/pdf/2602.19870.pdf)  
**作者**：Qiankun Ma, Ziyao Zhang, Haofei Wang, Jie Chen, Zhen Song, Hairong Zheng  

**一句话要点**：提出ApET框架，通过近似误差引导视觉令牌压缩，提升视觉语言模型效率。

**关键词**：视觉语言模型, 令牌压缩, 信息论, 高效推理, FlashAttention, 多模态理解

## 3 点简述
- 视觉语言模型中冗余视觉令牌导致计算开销大，现有方法依赖注意力机制，存在位置偏差且不兼容高效注意力内核。
- ApET从信息论角度出发，使用线性近似重构视觉令牌，基于近似误差识别并丢弃信息量最低的令牌，无需注意力参与。
- 实验显示，ApET在图像和视频理解任务中分别压缩88.9%和87.5%令牌，性能保留95.2%和100.4%，并兼容FlashAttention加速推理。

## 摘要（原文）

> Recent Vision-Language Models (VLMs) have demonstrated remarkable multimodal understanding capabilities, yet the redundant visual tokens incur prohibitive computational overhead and degrade inference efficiency. Prior studies typically relies on [CLS] attention or text-vision cross-attention to identify and discard redundant visual tokens. Despite promising results, such solutions are prone to introduce positional bias and, more critically, are incompatible with efficient attention kernels such as FlashAttention, limiting their practical deployment for VLM acceleration. In this paper, we step away from attention dependencies and revisit visual token compression from an information-theoretic perspective, aiming to maximally preserve visual information without any attention involvement. We present ApET, an Approximation-Error guided Token compression framework. ApET first reconstructs the original visual tokens with a small set of basis tokens via linear approximation, then leverages the approximation error to identify and drop the least informative tokens. Extensive experiments across multiple VLMs and benchmarks demonstrate that ApET retains 95.2% of the original performance on image-understanding tasks and even attains 100.4% on video-understanding tasks, while compressing the token budgets by 88.9% and 87.5%, respectively. Thanks to its attention-free design, ApET seamlessly integrates with FlashAttention, enabling further inference acceleration and making VLM deployment more practical. Code is available at https://github.com/MaQianKun0/ApET.

