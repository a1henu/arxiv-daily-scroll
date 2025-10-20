---
layout: default
title: FreqPDE: Rethinking Positional Depth Embedding for Multi-View 3D Object Detection Transformers
---

# FreqPDE: Rethinking Positional Depth Embedding for Multi-View 3D Object Detection Transformers
**arXiv**：[2510.15385v1](https://arxiv.org/abs/2510.15385) · [PDF](https://arxiv.org/pdf/2510.15385.pdf)  
**作者**：Haisheng Su, Junjie Zhang, Feixiang Song, Sanping Zhou, Wei Wu, Nanning Zheng, Junchi Yan  

**一句话要点**：提出FreqPDE方法，通过频率感知深度嵌入改进多视图3D目标检测

**关键词**：多视图3D目标检测, 频率感知深度嵌入, 跨视图一致性, 尺度不变性, 深度预测, Transformer解码器

## 3 点简述
- 核心问题：现有方法依赖深度预测，但存在边界不连续和小物体模糊问题，且忽略跨视图一致性和尺度不变性。
- 方法要点：使用频率感知空间金字塔编码器、跨视图尺度不变深度预测器和位置深度编码器生成3D深度感知特征。
- 实验效果：在nuScenes数据集上验证了方法的有效性和优越性，通过混合深度监督提升性能。

## 摘要（原文）

> Detecting 3D objects accurately from multi-view 2D images is a challenging
> yet essential task in the field of autonomous driving. Current methods resort
> to integrating depth prediction to recover the spatial information for object
> query decoding, which necessitates explicit supervision from LiDAR points
> during the training phase. However, the predicted depth quality is still
> unsatisfactory such as depth discontinuity of object boundaries and
> indistinction of small objects, which are mainly caused by the sparse
> supervision of projected points and the use of high-level image features for
> depth prediction. Besides, cross-view consistency and scale invariance are also
> overlooked in previous methods. In this paper, we introduce Frequency-aware
> Positional Depth Embedding (FreqPDE) to equip 2D image features with spatial
> information for 3D detection transformer decoder, which can be obtained through
> three main modules. Specifically, the Frequency-aware Spatial Pyramid Encoder
> (FSPE) constructs a feature pyramid by combining high-frequency edge clues and
> low-frequency semantics from different levels respectively. Then the Cross-view
> Scale-invariant Depth Predictor (CSDP) estimates the pixel-level depth
> distribution with cross-view and efficient channel attention mechanism.
> Finally, the Positional Depth Encoder (PDE) combines the 2D image features and
> 3D position embeddings to generate the 3D depth-aware features for query
> decoding. Additionally, hybrid depth supervision is adopted for complementary
> depth learning from both metric and distribution aspects. Extensive experiments
> conducted on the nuScenes dataset demonstrate the effectiveness and superiority
> of our proposed method.

