---
layout: default
title: Fine-tuning Pre-trained Vision-Language Models in a Human-Annotation-Free Manner
---

# Fine-tuning Pre-trained Vision-Language Models in a Human-Annotation-Free Manner
**arXiv**：[2602.04337v1](https://arxiv.org/abs/2602.04337) · [PDF](https://arxiv.org/pdf/2602.04337.pdf)  
**作者**：Qian-Wei Wang, Guanghao Meng, Ren Cai, Yaguang Song, Shu-Tao Xia  

**一句话要点**：提出CoFT框架，通过双模型跨模态协作实现无标注视觉语言模型微调。

**关键词**：视觉语言模型, 无监督微调, 伪标签学习, 跨模态协作, 提示学习, 对比学习

## 3 点简述
- 核心问题：无监督自训练方法存在伪标签不可靠、确认偏差和低置信度样本利用不足。
- 方法要点：引入双提示学习策略，依赖样本建模伪标签清洁度，无需手动阈值或噪声假设。
- 实验或效果：在无监督方法中表现一致提升，甚至超越少样本监督基线。

## 摘要（原文）

> Large-scale vision-language models (VLMs) such as CLIP exhibit strong zero-shot generalization, but adapting them to downstream tasks typically requires costly labeled data. Existing unsupervised self-training methods rely on pseudo-labeling, yet often suffer from unreliable confidence filtering, confirmation bias, and underutilization of low-confidence samples. We propose Collaborative Fine-Tuning (CoFT), an unsupervised adaptation framework that leverages unlabeled data through a dual-model, cross-modal collaboration mechanism. CoFT introduces a dual-prompt learning strategy with positive and negative textual prompts to explicitly model pseudo-label cleanliness in a sample-dependent manner, removing the need for hand-crafted thresholds or noise assumptions. The negative prompt also regularizes lightweight visual adaptation modules, improving robustness under noisy supervision. CoFT employs a two-phase training scheme, transitioning from parameter-efficient fine-tuning on high-confidence samples to full fine-tuning guided by collaboratively filtered pseudo-labels. Building on CoFT, CoFT+ further enhances adaptation via iterative fine-tuning, momentum contrastive learning, and LLM-generated prompts. Extensive experiments demonstrate consistent gains over existing unsupervised methods and even few-shot supervised baselines.

