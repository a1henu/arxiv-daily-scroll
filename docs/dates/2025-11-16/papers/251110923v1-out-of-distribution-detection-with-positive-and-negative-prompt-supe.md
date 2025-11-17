---
layout: default
title: Out-of-Distribution Detection with Positive and Negative Prompt Supervision Using Large Language Models
---

# Out-of-Distribution Detection with Positive and Negative Prompt Supervision Using Large Language Models
**arXiv**：[2511.10923v1](https://arxiv.org/abs/2511.10923) · [PDF](https://arxiv.org/pdf/2511.10923.pdf)  
**作者**：Zhixia He, Chen Zhao, Minglai Shao, Xintao Wu, Xujiang Zhao, Dong Li, Qin Tian, Linlin Yu  

**一句话要点**：提出正负提示监督方法，利用大语言模型增强视觉模态的分布外检测性能。

**关键词**：分布外检测, 视觉语言模型, 提示优化, 图架构, 能量检测器

## 3 点简述
- 核心问题：负提示可能捕获重叠或误导信息，导致分布外检测效果不佳。
- 方法要点：优化正负提示，负提示聚焦类间特征，并通过图架构传播语义监督。
- 实验或效果：在CIFAR-100和ImageNet-1K基准上，优于现有方法。

## 摘要（原文）

> Out-of-distribution (OOD) detection is committed to delineating the classification boundaries between in-distribution (ID) and OOD images. Recent advances in vision-language models (VLMs) have demonstrated remarkable OOD detection performance by integrating both visual and textual modalities. In this context, negative prompts are introduced to emphasize the dissimilarity between image features and prompt content. However, these prompts often include a broad range of non-ID features, which may result in suboptimal outcomes due to the capture of overlapping or misleading information. To address this issue, we propose Positive and Negative Prompt Supervision, which encourages negative prompts to capture inter-class features and transfers this semantic knowledge to the visual modality to enhance OOD detection performance. Our method begins with class-specific positive and negative prompts initialized by large language models (LLMs). These prompts are subsequently optimized, with positive prompts focusing on features within each class, while negative prompts highlight features around category boundaries. Additionally, a graph-based architecture is employed to aggregate semantic-aware supervision from the optimized prompt representations and propagate it to the visual branch, thereby enhancing the performance of the energy-based OOD detector. Extensive experiments on two benchmarks, CIFAR-100 and ImageNet-1K, across eight OOD datasets and five different LLMs, demonstrate that our method outperforms state-of-the-art baselines.

