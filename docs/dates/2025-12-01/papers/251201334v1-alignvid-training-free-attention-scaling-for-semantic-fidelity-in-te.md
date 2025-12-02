---
layout: default
title: AlignVid: Training-Free Attention Scaling for Semantic Fidelity in Text-Guided Image-to-Video Generation
---

# AlignVid: Training-Free Attention Scaling for Semantic Fidelity in Text-Guided Image-to-Video Generation
**arXiv**：[2512.01334v1](https://arxiv.org/abs/2512.01334) · [PDF](https://arxiv.org/pdf/2512.01334.pdf)  
**作者**：Yexin Liu, Wen-Jie Shu, Zile Huang, Haoze Zheng, Yueze Wang, Manyuan Zhang, Ser-Nam Lim, Harry Yang  

**一句话要点**：提出AlignVid框架以解决文本引导图像到视频生成中的语义疏忽问题

**关键词**：文本引导图像到视频生成, 语义疏忽, 注意力缩放, 无训练框架, 语义保真度评估

## 3 点简述
- 核心问题：现有方法在输入图像需大幅变换时，难以遵循细粒度提示语义，称为语义疏忽。
- 方法要点：通过无训练框架，包括注意力缩放调制和引导调度，直接重加权注意力以提升语义保真度。
- 实验或效果：引入OmitI2V评估集，实验显示AlignVid能增强语义保真度，同时限制视觉质量下降。

## 摘要（原文）

> Text-guided image-to-video (TI2V) generation has recently achieved remarkable progress, particularly in maintaining subject consistency and temporal coherence. However, existing methods still struggle to adhere to fine-grained prompt semantics, especially when prompts entail substantial transformations of the input image (e.g., object addition, deletion, or modification), a shortcoming we term semantic negligence. In a pilot study, we find that applying a Gaussian blur to the input image improves semantic adherence. Analyzing attention maps, we observe clearer foreground-background separation. From an energy perspective, this corresponds to a lower-entropy cross-attention distribution. Motivated by this, we introduce AlignVid, a training-free framework with two components: (i) Attention Scaling Modulation (ASM), which directly reweights attention via lightweight Q or K scaling, and (ii) Guidance Scheduling (GS), which applies ASM selectively across transformer blocks and denoising steps to reduce visual quality degradation. This minimal intervention improves prompt adherence while limiting aesthetic degradation. In addition, we introduce OmitI2V to evaluate semantic negligence in TI2V generation, comprising 367 human-annotated samples that span addition, deletion, and modification scenarios. Extensive experiments demonstrate that AlignVid can enhance semantic fidelity.

