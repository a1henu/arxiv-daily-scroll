---
layout: default
title: Adaptive Morph-Patch Transformer for Arotic Vessel Segmentation
---

# Adaptive Morph-Patch Transformer for Arotic Vessel Segmentation
**arXiv**：[2511.06897v1](https://arxiv.org/abs/2511.06897) · [PDF](https://arxiv.org/pdf/2511.06897.pdf)  
**作者**：Zhenxi Zhang, Fuchen Zheng, Adnan Iltaf, Yifei Han, Zhenyu Cheng, Yue Du, Bin Li, Tianyong Liu, Shoujun Zhou  

**一句话要点**：提出自适应形态补丁Transformer以解决主动脉血管分割中结构完整性问题

**关键词**：主动脉血管分割, 自适应补丁划分, 语义聚类注意力, Transformer模型, 医学图像分割

## 3 点简述
- 传统Transformer依赖固定矩形补丁，影响复杂血管结构完整性，导致分割精度不足
- 引入自适应补丁划分策略和语义聚类注意力，动态生成形态感知补丁并聚合相似语义特征
- 在多个开源数据集上验证，MPT实现先进性能，提升复杂血管结构分割效果

## 摘要（原文）

> Accurate segmentation of aortic vascular structures is critical for
> diagnosing and treating cardiovascular diseases.Traditional Transformer-based
> models have shown promise in this domain by capturing long-range dependencies
> between vascular features. However, their reliance on fixed-size rectangular
> patches often influences the integrity of complex vascular structures, leading
> to suboptimal segmentation accuracy. To address this challenge, we propose the
> adaptive Morph Patch Transformer (MPT), a novel architecture specifically
> designed for aortic vascular segmentation. Specifically, MPT introduces an
> adaptive patch partitioning strategy that dynamically generates
> morphology-aware patches aligned with complex vascular structures. This
> strategy can preserve semantic integrity of complex vascular structures within
> individual patches. Moreover, a Semantic Clustering Attention (SCA) method is
> proposed to dynamically aggregate features from various patches with similar
> semantic characteristics. This method enhances the model's capability to
> segment vessels of varying sizes, preserving the integrity of vascular
> structures. Extensive experiments on three open-source dataset(AVT, AortaSeg24
> and TBAD) demonstrate that MPT achieves state-of-the-art performance, with
> improvements in segmenting intricate vascular structures.

