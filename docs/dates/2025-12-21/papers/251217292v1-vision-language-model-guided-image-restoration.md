---
layout: default
title: Vision-Language Model Guided Image Restoration
---

# Vision-Language Model Guided Image Restoration
**arXiv**：[2512.17292v1](https://arxiv.org/abs/2512.17292) · [PDF](https://arxiv.org/pdf/2512.17292.pdf)  
**作者**：Cuixin Yang, Rongkang Dong, Kin-Man Lam  

**一句话要点**：提出VLMIR框架，利用视觉语言模型增强图像恢复的语义一致性与细节恢复能力。

**关键词**：图像恢复, 视觉语言模型, 扩散模型, 语义对齐, 特征提取, 退化预测

## 3 点简述
- 核心问题：现有方法难以有效结合视觉与语言知识，导致图像恢复中语义连贯性不足。
- 方法要点：采用两阶段框架，先提取互补的视觉与语言特征，再通过扩散模型集成进行恢复。
- 实验或效果：在通用和特定退化任务中表现优异，验证了视觉语言先验的重要性。

## 摘要（原文）

> Many image restoration (IR) tasks require both pixel-level fidelity and high-level semantic understanding to recover realistic photos with fine-grained details. However, previous approaches often struggle to effectively leverage both the visual and linguistic knowledge. Recent efforts have attempted to incorporate Vision-language models (VLMs), which excel at aligning visual and textual features, into universal IR. Nevertheless, these methods fail to utilize the linguistic priors to ensure semantic coherence during the restoration process. To address this issue, in this paper, we propose the Vision-Language Model Guided Image Restoration (VLMIR) framework, which leverages the rich vision-language priors of VLMs, such as CLIP, to enhance IR performance through improved visual perception and semantic understanding. Our approach consists of two stages: VLM-based feature extraction and diffusion-based image restoration. In the first stage, we extract complementary visual and linguistic representations of input images by condensing the visual perception and high-level semantic priors through VLMs. Specifically, we align the embeddings of captions from low-quality and high-quality images using a cosine similarity loss with LoRA fine-tuning, and employ a degradation predictor to decompose degradation and clean image content embeddings. These complementary visual and textual embeddings are then integrated into a diffusion-based model via cross-attention mechanisms for enhanced restoration. Extensive experiments and ablation studies demonstrate that VLMIR achieves superior performance across both universal and degradation-specific IR tasks, underscoring the critical role of integrated visual and linguistic knowledge from VLMs in advancing image restoration capabilities.

