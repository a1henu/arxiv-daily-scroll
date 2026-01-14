---
layout: default
title: Unified Multi-Site Multi-Sequence Brain MRI Harmonization Enriched by Biomedical Semantic Style
---

# Unified Multi-Site Multi-Sequence Brain MRI Harmonization Enriched by Biomedical Semantic Style
**arXiv**：[2601.08193v1](https://arxiv.org/abs/2601.08193) · [PDF](https://arxiv.org/pdf/2601.08193.pdf)  
**作者**：Mengqi Wu, Yongheng Sun, Qianqian Wang, Pew-Thian Yap, Mingxia Liu  

**一句话要点**：提出MMH框架以解决多站点多序列脑MRI数据中的非生物异质性，实现序列感知的风格对齐。

**关键词**：脑MRI协调, 多序列MRI, 扩散模型, 风格解耦, 生物医学语义, 无配对数据

## 3 点简述
- 核心问题：多站点脑MRI数据因扫描仪和协议差异引入非生物异质性，影响模型泛化性。
- 方法要点：采用两阶段扩散模型，结合生物医学语义先验，通过三平面注意力编码器解耦风格与解剖结构。
- 实验或效果：在4,163个T1和T2加权MRI上验证，在图像聚类、分割和分类任务中优于现有方法。

## 摘要（原文）

> Aggregating multi-site brain MRI data can enhance deep learning model training, but also introduces non-biological heterogeneity caused by site-specific variations (e.g., differences in scanner vendors, acquisition parameters, and imaging protocols) that can undermine generalizability. Recent retrospective MRI harmonization seeks to reduce such site effects by standardizing image style (e.g., intensity, contrast, noise patterns) while preserving anatomical content. However, existing methods often rely on limited paired traveling-subject data or fail to effectively disentangle style from anatomy. Furthermore, most current approaches address only single-sequence harmonization, restricting their use in real-world settings where multi-sequence MRI is routinely acquired. To this end, we introduce MMH, a unified framework for multi-site multi-sequence brain MRI harmonization that leverages biomedical semantic priors for sequence-aware style alignment. MMH operates in two stages: (1) a diffusion-based global harmonizer that maps MR images to a sequence-specific unified domain using style-agnostic gradient conditioning, and (2) a target-specific fine-tuner that adapts globally aligned images to desired target domains. A tri-planar attention BiomedCLIP encoder aggregates multi-view embeddings to characterize volumetric style information, allowing explicit disentanglement of image styles from anatomy without requiring paired data. Evaluations on 4,163 T1- and T2-weighted MRIs demonstrate MMH's superior harmonization over state-of-the-art methods in image feature clustering, voxel-level comparison, tissue segmentation, and downstream age and site classification.

