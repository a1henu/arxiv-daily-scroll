---
layout: default
title: Coffee: Controllable Diffusion Fine-tuning
---

# Coffee: Controllable Diffusion Fine-tuning
**arXiv**：[2511.14113v1](https://arxiv.org/abs/2511.14113) · [PDF](https://arxiv.org/pdf/2511.14113.pdf)  
**作者**：Ziyao Zeng, Jingcheng Ni, Ruyi Liu, Alex Wong  

**一句话要点**：提出Coffee方法以解决扩散模型微调中不期望概念学习的问题

**关键词**：扩散模型微调, 可控生成, 概念对齐, 文本到图像, 偏见缓解

## 3 点简述
- 核心问题：扩散模型微调时易学习不期望概念并与用户提示纠缠
- 方法要点：使用语言指定不期望概念，防止用户提示嵌入与其对齐
- 实验或效果：在图像微调中优于现有方法，无需额外训练

## 摘要（原文）

> Text-to-image diffusion models can generate diverse content with flexible prompts, which makes them well-suited for customization through fine-tuning with a small amount of user-provided data. However, controllable fine-tuning that prevents models from learning undesired concepts present in the fine-tuning data, and from entangling those concepts with user prompts, remains an open challenge. It is crucial for downstream tasks like bias mitigation, preventing malicious adaptation, attribute disentanglement, and generalizable fine-tuning of diffusion policy. We propose Coffee that allows using language to specify undesired concepts to regularize the adaptation process. The crux of our method lies in keeping the embeddings of the user prompt from aligning with undesired concepts. Crucially, Coffee requires no additional training and enables flexible modification of undesired concepts by modifying textual descriptions. We evaluate Coffee by fine-tuning on images associated with user prompts paired with undesired concepts. Experimental results demonstrate that Coffee can prevent text-to-image models from learning specified undesired concepts during fine-tuning and outperforms existing methods. Code will be released upon acceptance.

