---
layout: default
title: Mind the Way You Select Negative Texts: Pursuing the Distance Consistency in OOD Detection with VLMs
---

# Mind the Way You Select Negative Texts: Pursuing the Distance Consistency in OOD Detection with VLMs
**arXiv**：[2603.02618v1](https://arxiv.org/abs/2603.02618) · [PDF](https://arxiv.org/pdf/2603.02618.pdf)  
**作者**：Zhikang Xu, Qianqian Xu, Zitai Wang, Cong Hua, Sicong Li, Zhiyong Yang, Qingming Huang  

**一句话要点**：提出InterNeg框架，通过跨模态距离一致性提升视觉语言模型在分布外检测中的性能。

**关键词**：分布外检测, 视觉语言模型, 跨模态距离, 负文本选择, 图像反转, 性能提升

## 3 点简述
- 核心问题：现有方法在分布外检测中引入模态内距离，与视觉语言模型优化的跨模态距离不一致，导致性能受限。
- 方法要点：从文本视角设计跨模态准则选择负文本，从视觉视角动态识别高置信度分布外图像并反转为文本嵌入，增强跨模态距离一致性。
- 实验或效果：在多个基准测试中表现优异，如在ImageNet上FPR95降低3.47%，在Near-OOD上AUROC提升5.50%。

## 摘要（原文）

> Out-of-distribution (OOD) detection seeks to identify samples from unknown classes, a critical capability for deploying machine learning models in open-world scenarios. Recent research has demonstrated that Vision-Language Models (VLMs) can effectively leverage their multi-modal representations for OOD detection. However, current methods often incorporate intra-modal distance during OOD detection, such as comparing negative texts with ID labels or comparing test images with image proxies. This design paradigm creates an inherent inconsistency against the inter-modal distance that CLIP-like VLMs are optimized for, potentially leading to suboptimal performance. To address this limitation, we propose InterNeg, a simple yet effective framework that systematically utilizes consistent inter-modal distance enhancement from textual and visual perspectives. From the textual perspective, we devise an inter-modal criterion for selecting negative texts. From the visual perspective, we dynamically identify high-confidence OOD images and invert them into the textual space, generating extra negative text embeddings guided by inter-modal distance. Extensive experiments across multiple benchmarks demonstrate the superiority of our approach. Notably, our InterNeg achieves state-of-the-art performance compared to existing works, with a 3.47\% reduction in FPR95 on the large-scale ImageNet benchmark and a 5.50\% improvement in AUROC on the challenging Near-OOD benchmark.

