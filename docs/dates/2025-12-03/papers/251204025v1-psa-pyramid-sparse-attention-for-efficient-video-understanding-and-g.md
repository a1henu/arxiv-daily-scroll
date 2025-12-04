---
layout: default
title: PSA: Pyramid Sparse Attention for Efficient Video Understanding and Generation
---

# PSA: Pyramid Sparse Attention for Efficient Video Understanding and Generation
**arXiv**：[2512.04025v1](https://arxiv.org/abs/2512.04025) · [PDF](https://arxiv.org/pdf/2512.04025.pdf)  
**作者**：Xiaolong Li, Youping Gu, Xi Lin, Weijie Wang, Bohan Zhuang  

**一句话要点**：提出金字塔稀疏注意力以解决视频理解与生成中高稀疏度下的信息损失问题

**关键词**：稀疏注意力, 视频理解, 视频生成, 计算效率, 金字塔结构, 硬件友好内核

## 3 点简述
- 核心问题：现有稀疏注意力方法在高稀疏度下因二进制掩码导致关键信息丢失
- 方法要点：引入多级池化键值表示，动态分配池化级别以精细控制保留与剪枝
- 实验或效果：在视频理解与生成基准测试中优于或媲美现有稀疏注意力基线，效率-质量权衡更优

## 摘要（原文）

> Attention mechanisms are the core of foundation models, but their quadratic complexity remains a critical bottleneck for scaling. This challenge has driven the development of efficient attention mechanisms, with sparsity emerging as the dominant paradigm. Current methods typically retain or discard entire key-value blocks with binary masks, resulting in substantial information loss under high sparsity. To mitigate this gap, we present Pyramid Sparse Attention (PSA), a versatile module applicable to both video understanding and generation tasks. Instead of binary masking, PSA introduces multi-level pooled KV representations, enabling finer mask granularity. Specifically, each query block dynamically allocates lower pooling levels to critical KV blocks and higher levels to less important ones, creating an informative interpolation between full retention and complete pruning. This design, analogous to fixed-point quantization and classical feature pyramid networks in computer vision, effectively mitigates information loss while preserving computational efficiency under a low compute budget. It works with a native, hardware-friendly kernel that leverages decoupled block-tile design to ensure efficient execution. Across video understanding and generation benchmarks, PSA preserves contextual information and visual fidelity, consistently outperforming or achieving comparable performance over existing sparse attention baselines with superior efficiency-quality trade-offs. Our code and model weights are publicly available at: http://ziplab.co/PSA

