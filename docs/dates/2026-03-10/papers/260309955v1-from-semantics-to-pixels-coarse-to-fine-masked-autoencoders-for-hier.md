---
layout: default
title: From Semantics to Pixels: Coarse-to-Fine Masked Autoencoders for Hierarchical Visual Understanding
---

# From Semantics to Pixels: Coarse-to-Fine Masked Autoencoders for Hierarchical Visual Understanding
**arXiv**：[2603.09955v1](https://arxiv.org/abs/2603.09955) · [PDF](https://arxiv.org/pdf/2603.09955.pdf)  
**作者**：Wenzhao Xiang, Yue Wu, Hongyang Yu, Feng Gao, Fan Yang, Xilin Chen  

**一句话要点**：提出C2FMAE，通过粗到细掩码自编码器解决自监督视觉预训练中全局语义与局部细节的权衡问题。

**关键词**：自监督学习, 掩码自编码器, 层次化表示, 视觉预训练, 多粒度数据集

## 3 点简述
- 核心问题：自监督视觉预训练中，对比学习丢失细粒度细节，掩码图像建模因随机掩码导致注意力漂移。
- 方法要点：设计级联解码器和渐进掩码课程，从语义到像素学习层次化表示，建立跨粒度依赖。
- 实验或效果：在图像分类、目标检测和语义分割上取得显著性能提升，验证了层次化设计的有效性。

## 摘要（原文）

> Self-supervised visual pre-training methods face an inherent tension: contrastive learning (CL) captures global semantics but loses fine-grained detail, while masked image modeling (MIM) preserves local textures but suffers from "attention drift" due to semantically-agnostic random masking. We propose C2FMAE, a coarse-to-fine masked autoencoder that resolves this tension by explicitly learning hierarchical visual representations across three data granularities: semantic masks (scene-level), instance masks (object-level), and RGB images (pixel-level). Two synergistic innovations enforce a strict top-down learning principle. First, a cascaded decoder sequentially reconstructs from scene semantics to object instances to pixel details, establishing explicit cross-granularity dependencies that parallel decoders cannot capture. Second, a progressive masking curriculum dynamically shifts the training focus from semantic-guided to instance-guided and finally to random masking, creating a structured learning path from global context to local features. To support this framework, we construct a large-scale multi-granular dataset with high-quality pseudo-labels for all 1.28M ImageNet-1K images. Extensive experiments show that C2FMAE achieves significant performance gains on image classification, object detection, and semantic segmentation, validating the effectiveness of our hierarchical design in learning more robust and generalizable representations.

