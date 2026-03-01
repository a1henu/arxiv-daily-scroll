---
layout: default
title: TriLite: Efficient Weakly Supervised Object Localization with Universal Visual Features and Tri-Region Disentanglement
---

# TriLite: Efficient Weakly Supervised Object Localization with Universal Visual Features and Tri-Region Disentanglement
**arXiv**：[2602.23120v1](https://arxiv.org/abs/2602.23120) · [PDF](https://arxiv.org/pdf/2602.23120.pdf)  
**作者**：Arian Sabaghi, José Oramas  

**一句话要点**：提出TriLite框架，利用冻结ViT和TriHead模块解决弱监督目标定位中的部分覆盖和训练成本问题。

**关键词**：弱监督目标定位, 视觉Transformer, 特征解耦, 参数效率, 自监督学习, 目标覆盖

## 3 点简述
- 弱监督目标定位面临部分对象覆盖和训练成本高的挑战。
- TriLite采用冻结Dinov2预训练ViT，通过TriHead模块分解特征为前景、背景和模糊区域。
- 在CUB-200-2011等数据集上实现新SOTA，参数少于800K，训练更高效。

## 摘要（原文）

> Weakly supervised object localization (WSOL) aims to localize target objects in images using only image-level labels. Despite recent progress, many approaches still rely on multi-stage pipelines or full fine-tuning of large backbones, which increases training cost, while the broader WSOL community continues to face the challenge of partial object coverage. We present TriLite, a single-stage WSOL framework that leverages a frozen Vision Transformer with Dinov2 pre-training in a self-supervised manner, and introduces only a minimal number of trainable parameters (fewer than 800K on ImageNet-1K) for both classification and localization. At its core is the proposed TriHead module, which decomposes patch features into foreground, background, and ambiguous regions, thereby improving object coverage while suppressing spurious activations. By disentangling classification and localization objectives, TriLite effectively exploits the universal representations learned by self-supervised ViTs without requiring expensive end-to-end training. Extensive experiments on CUB-200-2011, ImageNet-1K, and OpenImages demonstrate that TriLite sets a new state of the art, while remaining significantly more parameter-efficient and easier to train than prior methods. The code will be released soon.

