---
layout: default
title: EVCC: Enhanced Vision Transformer-ConvNeXt-CoAtNet Fusion for Classification
---

# EVCC: Enhanced Vision Transformer-ConvNeXt-CoAtNet Fusion for Classification
**arXiv**：[2511.18691v1](https://arxiv.org/abs/2511.18691) · [PDF](https://arxiv.org/pdf/2511.18691.pdf)  
**作者**：Kazi Reyazul Hasan, Md Nafiu Rahman, Wasif Jalal, Sadif Ahmed, Shahriar Raj, Mubasshira Musarrat, Muhammad Abdullah Adnan  

**一句话要点**：提出EVCC融合架构以高效结合Transformer与CNN，提升图像分类精度并降低计算成本。

**关键词**：图像分类, 混合架构, 自适应令牌剪枝, 门控交叉注意力, 多任务学习, 计算效率

## 3 点简述
- 混合视觉架构计算成本高，难以平衡精度与效率。
- 集成ViT、ConvNeXt和CoAtNet，采用自适应令牌剪枝和门控交叉注意力。
- 在多个数据集上实现SOTA精度，FLOPs减少25-35%，提升达2个百分点。

## 摘要（原文）

> Hybrid vision architectures combining Transformers and CNNs have significantly advanced image classification, but they usually do so at significant computational cost. We introduce EVCC (Enhanced Vision Transformer-ConvNeXt-CoAtNet), a novel multi-branch architecture integrating the Vision Transformer, lightweight ConvNeXt, and CoAtNet through key innovations: (1) adaptive token pruning with information preservation, (2) gated bidirectional cross-attention for enhanced feature refinement, (3) auxiliary classification heads for multi-task learning, and (4) a dynamic router gate employing context-aware confidence-driven weighting. Experiments across the CIFAR-100, Tobacco3482, CelebA, and Brain Cancer datasets demonstrate EVCC's superiority over powerful models like DeiT-Base, MaxViT-Base, and CrossViT-Base by consistently achieving state-of-the-art accuracy with improvements of up to 2 percentage points, while reducing FLOPs by 25 to 35%. Our adaptive architecture adjusts computational demands to deployment needs by dynamically reducing token count, efficiently balancing the accuracy-efficiency trade-off while combining global context, local details, and hierarchical features for real-world applications. The source code of our implementation is available at https://anonymous.4open.science/r/EVCC.

