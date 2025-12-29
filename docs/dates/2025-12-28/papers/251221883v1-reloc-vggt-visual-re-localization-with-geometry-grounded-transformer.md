---
layout: default
title: Reloc-VGGT: Visual Re-localization with Geometry Grounded Transformer
---

# Reloc-VGGT: Visual Re-localization with Geometry Grounded Transformer
**arXiv**：[2512.21883v1](https://arxiv.org/abs/2512.21883) · [PDF](https://arxiv.org/pdf/2512.21883.pdf)  
**作者**：Tianchen Deng, Wenhua Wu, Kunzhen Wu, Guangming Wang, Siting Zhu, Shenghai Yuan, Xun Chen, Guole Shen, Zhe Liu, Hesheng Wang  

**一句话要点**：提出Reloc-VGGT框架，通过早期融合机制实现多视图空间集成，以提升复杂环境下的视觉重定位精度与实时性。

**关键词**：视觉重定位, 多视图融合, Transformer, 实时定位, 几何编码

## 3 点简述
- 核心问题：传统视觉定位采用后期融合策略，空间信息整合不足，在复杂环境中精度下降。
- 方法要点：基于VGGT骨干网络，引入姿态标记器和投影模块，结合稀疏掩码注意力策略降低计算成本。
- 实验或效果：在约八百万图像对上训练，在多个公共数据集上验证了高精度、强泛化能力和实时性能。

## 摘要（原文）

> Visual localization has traditionally been formulated as a pair-wise pose regression problem. Existing approaches mainly estimate relative poses between two images and employ a late-fusion strategy to obtain absolute pose estimates. However, the late motion average is often insufficient for effectively integrating spatial information, and its accuracy degrades in complex environments. In this paper, we present the first visual localization framework that performs multi-view spatial integration through an early-fusion mechanism, enabling robust operation in both structured and unstructured environments. Our framework is built upon the VGGT backbone, which encodes multi-view 3D geometry, and we introduce a pose tokenizer and projection module to more effectively exploit spatial relationships from multiple database views. Furthermore, we propose a novel sparse mask attention strategy that reduces computational cost by avoiding the quadratic complexity of global attention, thereby enabling real-time performance at scale. Trained on approximately eight million posed image pairs, Reloc-VGGT demonstrates strong accuracy and remarkable generalization ability. Extensive experiments across diverse public datasets consistently validate the effectiveness and efficiency of our approach, delivering high-quality camera pose estimates in real time while maintaining robustness to unseen environments. Our code and models will be publicly released upon acceptance.https://github.com/dtc111111/Reloc-VGGT.

