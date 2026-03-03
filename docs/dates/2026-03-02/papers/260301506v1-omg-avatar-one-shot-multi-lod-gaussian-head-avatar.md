---
layout: default
title: OMG-Avatar: One-shot Multi-LOD Gaussian Head Avatar
---

# OMG-Avatar: One-shot Multi-LOD Gaussian Head Avatar
**arXiv**：[2603.01506v1](https://arxiv.org/abs/2603.01506) · [PDF](https://arxiv.org/pdf/2603.01506.pdf)  
**作者**：Jianqiang Ren, Lin Liu, Steven Hoi  

**一句话要点**：提出OMG-Avatar，基于多细节层次高斯表示的单图像可动画3D头部重建方法，支持0.2秒快速生成。

**关键词**：单图像3D重建, 高斯表示, 可动画头部, 多细节层次, 快速推理, 多区域分解

## 3 点简述
- 核心问题：从单图像快速重建可动画3D头部，需处理非头部区域如肩膀，并适应不同硬件和速度需求。
- 方法要点：使用基于transformer的全局特征提取和投影采样的局部特征获取，结合深度缓冲融合特征，并采用多区域分解方案。
- 实验或效果：在重建质量、重演性能和计算效率上优于现有方法，支持细节层次功能。

## 摘要（原文）

> We propose OMG-Avatar, a novel One-shot method that leverages a Multi-LOD (Level-of-Detail) Gaussian representation for animatable 3D head reconstruction from a single image in 0.2s. Our method enables LOD head avatar modeling using a unified model that accommodates diverse hardware capabilities and inference speed requirements. To capture both global and local facial characteristics, we employ a transformer-based architecture for global feature extraction and projection-based sampling for local feature acquisition. These features are effectively fused under the guidance of a depth buffer, ensuring occlusion plausibility. We further introduce a coarse-to-fine learning paradigm to support Level-of-Detail functionality and enhance the perception of hierarchical details. To address the limitations of 3DMMs in modeling non-head regions such as the shoulders, we introduce a multi-region decomposition scheme in which the head and shoulders are predicted separately and then integrated through cross-region combination. Extensive experiments demonstrate that OMG-Avatar outperforms state-of-the-art methods in reconstruction quality, reenactment performance, and computational efficiency.

