---
layout: default
title: ITO: Images and Texts as One via Synergizing Multiple Alignment and Training-Time Fusion
---

# ITO: Images and Texts as One via Synergizing Multiple Alignment and Training-Time Fusion
**arXiv**：[2603.02767v1](https://arxiv.org/abs/2603.02767) · [PDF](https://arxiv.org/pdf/2603.02767.pdf)  
**作者**：HanZpeng Liu, Yaqian Li, Zidan Wang, Shuoxi Zhang, Zonglin Zhao, Zihao Bo, Rinyoichi Takezoe, Kaiwen Long, Kun He  

**一句话要点**：提出ITO框架，通过多模态多对齐和训练时融合解决图像-文本对比预训练中的模态组织问题。

**关键词**：图像-文本对比学习, 多模态对齐, 训练时融合, 视觉表示学习, 模态差距消除

## 3 点简述
- 核心问题：现有图像-文本对比预训练方法导致表示部分按模态组织，限制跨模态交互。
- 方法要点：采用多模态多对齐挖掘多样对应关系，并引入轻量训练时融合模块强制结构化交互，推理时丢弃以保持效率。
- 实验或效果：在分类、检索和多模态基准上优于基线，分析显示多对齐提升判别力，训练时融合消除模态差距并稳定训练。

## 摘要（原文）

> Image-text contrastive pretraining has become a dominant paradigm for visual representation learning, yet existing methods often yield representations that remain partially organized by modality. We propose ITO, a framework addressing this limitation through two synergistic mechanisms. Multimodal multiple alignment enriches supervision by mining diverse image-text correspondences, while a lightweight training-time multimodal fusion module enforces structured cross-modal interaction. Crucially, the fusion module is discarded at inference, preserving the efficiency of standard dual-encoder architectures. Extensive experiments show that ITO consistently outperforms strong baselines across classification, retrieval, and multimodal benchmarks. Our analysis reveals that while multiple alignment drives discriminative power, training-time fusion acts as a critical structural regularizer -- eliminating the modality gap and stabilizing training dynamics to prevent the early saturation often observed in aggressive contrastive learning.

