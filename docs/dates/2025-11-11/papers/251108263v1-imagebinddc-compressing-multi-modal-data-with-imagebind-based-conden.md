---
layout: default
title: ImagebindDC: Compressing Multi-modal Data with Imagebind-based Condensation
---

# ImagebindDC: Compressing Multi-modal Data with Imagebind-based Condensation
**arXiv**：[2511.08263v1](https://arxiv.org/abs/2511.08263) · [PDF](https://arxiv.org/pdf/2511.08263.pdf)  
**作者**：Yue Min, Shaobo Wang, Jiaze Li, Tianle Niu, Junxin Fan, Yongliang Miao, Lijin Yang, Linfeng Zhang  

**一句话要点**：提出ImageBindDC以解决多模态数据压缩中模态间依赖保留问题

**关键词**：数据压缩, 多模态学习, 特征函数损失, ImageBind框架, 分布对齐

## 3 点简述
- 核心问题：传统数据压缩方法在多模态场景中难以保持模态间复杂依赖关系
- 方法要点：在ImageBind统一特征空间使用特征函数损失实现精确统计对齐
- 实验效果：在NYU-v2数据集上，每类5个压缩数据点实现无损性能，超越现有方法

## 摘要（原文）

> Data condensation techniques aim to synthesize a compact dataset from a larger one to enable efficient model training, yet while successful in unimodal settings, they often fail in multimodal scenarios where preserving intricate inter-modal dependencies is crucial. To address this, we introduce ImageBindDC, a novel data condensation framework operating within the unified feature space of ImageBind. Our approach moves beyond conventional distribution-matching by employing a powerful Characteristic Function (CF) loss, which operates in the Fourier domain to facilitate a more precise statistical alignment via exact infinite moment matching. We design our objective to enforce three critical levels of distributional consistency: (i) uni-modal alignment, which matches the statistical properties of synthetic and real data within each modality; (ii) cross-modal alignment, which preserves pairwise semantics by matching the distributions of hybrid real-synthetic data pairs; and (iii) joint-modal alignment, which captures the complete multivariate data structure by aligning the joint distribution of real data pairs with their synthetic counterparts. Extensive experiments highlight the effectiveness of ImageBindDC: on the NYU-v2 dataset, a model trained on just 5 condensed datapoints per class achieves lossless performance comparable to one trained on the full dataset, achieving a new state-of-the-art with an 8.2\% absolute improvement over the previous best method and more than 4$\times$ less condensation time.

