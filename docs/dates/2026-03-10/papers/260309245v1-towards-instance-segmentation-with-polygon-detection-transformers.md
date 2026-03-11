---
layout: default
title: Towards Instance Segmentation with Polygon Detection Transformers
---

# Towards Instance Segmentation with Polygon Detection Transformers
**arXiv**：[2603.09245v1](https://arxiv.org/abs/2603.09245) · [PDF](https://arxiv.org/pdf/2603.09245.pdf)  
**作者**：Jiacheng Sun, Jiaqi Lin, Wenlong Hu, Haoyang Li, Xinghong Zhou, Chenghai Mao, Yan Peng, Xiaomao Li  

**一句话要点**：提出Poly-DETR以解决实例分割中高分辨率输入与轻量实时推理的冲突

**关键词**：实例分割, Transformer, 极坐标表示, 轻量推理, 顶点回归, 可变形注意力

## 3 点简述
- 核心问题：实例分割依赖密集像素掩码预测，导致高分辨率下内存消耗大、推理慢。
- 方法要点：将实例分割重构为稀疏顶点回归，采用极坐标表示和可变形注意力机制。
- 实验效果：在COCO等数据集上提升性能，高分辨率场景下内存减半，适用于规则形状实例。

## 摘要（原文）

> One of the bottlenecks for instance segmentation today lies in the conflicting requirements of high-resolution inputs and lightweight, real-time inference. To address this bottleneck, we present a Polygon Detection Transformer (Poly-DETR) to reformulate instance segmentation as sparse vertex regression via Polar Representation, thereby eliminating the reliance on dense pixel-wise mask prediction. Considering the box-to-polygon reference shift in Detection Transformers, we propose Polar Deformable Attention and Position-Aware Training Scheme to dynamically update supervision and focus attention on boundary cues. Compared with state-of-the-art polar-based methods, Poly-DETR achieves a 4.7 mAP improvement on MS COCO test-dev. Moreover, we construct a parallel mask-based counterpart to support a systematic comparison between polar and mask representations. Experimental results show that Poly-DETR is more lightweight in high-resolution scenarios, reducing memory consumption by almost half on Cityscapes dataset. Notably, on PanNuke (cell segmentation) and SpaceNet (building footprints) datasets, Poly-DETR surpasses its mask-based counterpart on all metrics, which validates its advantage on regular-shaped instances in domain-specific settings.

