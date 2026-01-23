---
layout: default
title: Sub-Region-Aware Modality Fusion and Adaptive Prompting for Multi-Modal Brain Tumor Segmentation
---

# Sub-Region-Aware Modality Fusion and Adaptive Prompting for Multi-Modal Brain Tumor Segmentation
**arXiv**：[2601.15734v1](https://arxiv.org/abs/2601.15734) · [PDF](https://arxiv.org/pdf/2601.15734.pdf)  
**作者**：Shadi Alijani, Fereshteh Aghaee Meibodi, Homayoun Najjaran  

**一句话要点**：提出子区域感知模态融合与自适应提示框架以提升多模态脑肿瘤分割精度

**关键词**：多模态医学影像, 脑肿瘤分割, 子区域感知融合, 自适应提示, 基础模型适应, 模态注意力

## 3 点简述
- 核心问题：基础模型在多模态医学影像中融合信息困难，难以适应病理组织异质性。
- 方法要点：引入子区域感知模态注意力机制和自适应提示工程，优化模态组合与分割精度。
- 实验或效果：在BraTS 2020数据集上验证，显著超越基线方法，尤其在坏死核心子区域表现突出。

## 摘要（原文）

> The successful adaptation of foundation models to multi-modal medical imaging is a critical yet unresolved challenge. Existing models often struggle to effectively fuse information from multiple sources and adapt to the heterogeneous nature of pathological tissues. To address this, we introduce a novel framework for adapting foundation models to multi-modal medical imaging, featuring two key technical innovations: sub-region-aware modality attention and adaptive prompt engineering. The attention mechanism enables the model to learn the optimal combination of modalities for each tumor sub-region, while the adaptive prompting strategy leverages the inherent capabilities of foundation models to refine segmentation accuracy. We validate our framework on the BraTS 2020 brain tumor segmentation dataset, demonstrating that our approach significantly outperforms baseline methods, particularly in the challenging necrotic core sub-region. Our work provides a principled and effective approach to multi-modal fusion and prompting, paving the way for more accurate and robust foundation model-based solutions in medical imaging.

