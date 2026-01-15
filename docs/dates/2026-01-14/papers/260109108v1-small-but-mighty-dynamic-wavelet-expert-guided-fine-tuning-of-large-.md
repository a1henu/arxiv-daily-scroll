---
layout: default
title: Small but Mighty: Dynamic Wavelet Expert-Guided Fine-Tuning of Large-Scale Models for Optical Remote Sensing Object Segmentation
---

# Small but Mighty: Dynamic Wavelet Expert-Guided Fine-Tuning of Large-Scale Models for Optical Remote Sensing Object Segmentation
**arXiv**：[2601.09108v1](https://arxiv.org/abs/2601.09108) · [PDF](https://arxiv.org/pdf/2601.09108.pdf)  
**作者**：Yanguang Sun, Chao Wang, Jian Yang, Lei Luo  

**一句话要点**：提出动态小波专家引导微调范式WEFT，以高效适配大规模模型于光学遥感图像分割任务。

**关键词**：光学遥感图像分割, 大规模模型微调, 小波专家, 条件适配器, 动态调节, 参数高效训练

## 3 点简述
- 核心问题：大规模模型全参数微调导致训练困难，如GPU内存消耗大和计算成本高，限制了其在遥感分割中的应用。
- 方法要点：引入任务特定小波专家提取器建模并动态调节小波专家，构建专家引导条件适配器注入可训练特征以增强冻结特征的细粒度感知。
- 实验或效果：在三个光学遥感图像数据集上超越21种先进方法，并在伪装、自然和医疗场景中取得最优结果。

## 摘要（原文）

> Accurately localizing and segmenting relevant objects from optical remote sensing images (ORSIs) is critical for advancing remote sensing applications. Existing methods are typically built upon moderate-scale pre-trained models and employ diverse optimization strategies to achieve promising performance under full-parameter fine-tuning. In fact, deeper and larger-scale foundation models can provide stronger support for performance improvement. However, due to their massive number of parameters, directly adopting full-parameter fine-tuning leads to pronounced training difficulties, such as excessive GPU memory consumption and high computational costs, which result in extremely limited exploration of large-scale models in existing works. In this paper, we propose a novel dynamic wavelet expert-guided fine-tuning paradigm with fewer trainable parameters, dubbed WEFT, which efficiently adapts large-scale foundation models to ORSIs segmentation tasks by leveraging the guidance of wavelet experts. Specifically, we introduce a task-specific wavelet expert extractor to model wavelet experts from different perspectives and dynamically regulate their outputs, thereby generating trainable features enriched with task-specific information for subsequent fine-tuning. Furthermore, we construct an expert-guided conditional adapter that first enhances the fine-grained perception of frozen features for specific tasks by injecting trainable features, and then iteratively updates the information of both types of feature, allowing for efficient fine-tuning. Extensive experiments show that our WEFT not only outperforms 21 state-of-the-art (SOTA) methods on three ORSIs datasets, but also achieves optimal results in camouflage, natural, and medical scenarios. The source code is available at: https://github.com/CSYSI/WEFT.

