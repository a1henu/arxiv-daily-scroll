---
layout: default
title: Context Patch Fusion With Class Token Enhancement for Weakly Supervised Semantic Segmentation
---

# Context Patch Fusion With Class Token Enhancement for Weakly Supervised Semantic Segmentation
**arXiv**：[2601.14718v1](https://arxiv.org/abs/2601.14718) · [PDF](https://arxiv.org/pdf/2601.14718.pdf)  
**作者**：Yiyang Fu, Hui Li, Wangyu Wu  

**一句话要点**：提出CPF-CTE框架，通过上下文补丁融合与类令牌增强解决弱监督语义分割中上下文依赖不足问题。

**关键词**：弱监督语义分割, 上下文依赖, 补丁融合, 类令牌增强, 空间语义集成

## 3 点简述
- 现有方法忽视图像补丁间复杂上下文依赖，导致局部表示不完整和分割精度受限。
- 核心CF-BiLSTM模块捕获补丁空间依赖，结合可学习类令牌动态编码类特定语义以增强判别能力。
- 在PASCAL VOC 2012和MS COCO 2014上实验验证，CPF-CTE超越先前弱监督语义分割方法。

## 摘要（原文）

> Weakly Supervised Semantic Segmentation (WSSS), which relies only on image-level labels, has attracted significant attention for its cost-effectiveness and scalability. Existing methods mainly enhance inter-class distinctions and employ data augmentation to mitigate semantic ambiguity and reduce spurious activations. However, they often neglect the complex contextual dependencies among image patches, resulting in incomplete local representations and limited segmentation accuracy. To address these issues, we propose the Context Patch Fusion with Class Token Enhancement (CPF-CTE) framework, which exploits contextual relations among patches to enrich feature representations and improve segmentation. At its core, the Contextual-Fusion Bidirectional Long Short-Term Memory (CF-BiLSTM) module captures spatial dependencies between patches and enables bidirectional information flow, yielding a more comprehensive understanding of spatial correlations. This strengthens feature learning and segmentation robustness. Moreover, we introduce learnable class tokens that dynamically encode and refine class-specific semantics, enhancing discriminative capability. By effectively integrating spatial and semantic cues, CPF-CTE produces richer and more accurate representations of image content. Extensive experiments on PASCAL VOC 2012 and MS COCO 2014 validate that CPF-CTE consistently surpasses prior WSSS methods.

