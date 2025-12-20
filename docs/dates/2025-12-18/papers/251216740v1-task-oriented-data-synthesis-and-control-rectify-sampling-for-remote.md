---
layout: default
title: Task-Oriented Data Synthesis and Control-Rectify Sampling for Remote Sensing Semantic Segmentation
---

# Task-Oriented Data Synthesis and Control-Rectify Sampling for Remote Sensing Semantic Segmentation
**arXiv**：[2512.16740v1](https://arxiv.org/abs/2512.16740) · [PDF](https://arxiv.org/pdf/2512.16740.pdf)  
**作者**：Yunkai Yang, Yudong Zhang, Kunquan Zhang, Jinxiao Zhang, Xinying Chen, Haohuan Fu, Runmin Dong  

**一句话要点**：提出任务导向数据合成框架TODSynth，以解决遥感语义分割中合成数据效用受限的问题。

**关键词**：遥感语义分割, 可控生成, 数据合成, 扩散模型, 任务导向采样, 多模态注意力

## 3 点简述
- 核心问题：遥感语义分割中，语义掩码控制的复杂性和采样质量的不确定性限制合成数据在下游任务中的效用。
- 方法要点：基于DiT构建多模态扩散变换器MM-DiT，采用文本-图像-掩码联合注意力方案，并结合控制校正流匹配CRFM动态调整采样方向。
- 实验或效果：在少样本和复杂场景下，显著提升合成数据质量，优于现有可控生成方法，增强下游分割任务性能。

## 摘要（原文）

> With the rapid progress of controllable generation, training data synthesis has become a promising way to expand labeled datasets and alleviate manual annotation in remote sensing (RS). However, the complexity of semantic mask control and the uncertainty of sampling quality often limit the utility of synthetic data in downstream semantic segmentation tasks. To address these challenges, we propose a task-oriented data synthesis framework (TODSynth), including a Multimodal Diffusion Transformer (MM-DiT) with unified triple attention and a plug-and-play sampling strategy guided by task feedback. Built upon the powerful DiT-based generative foundation model, we systematically evaluate different control schemes, showing that a text-image-mask joint attention scheme combined with full fine-tuning of the image and mask branches significantly enhances the effectiveness of RS semantic segmentation data synthesis, particularly in few-shot and complex-scene scenarios. Furthermore, we propose a control-rectify flow matching (CRFM) method, which dynamically adjusts sampling directions guided by semantic loss during the early high-plasticity stage, mitigating the instability of generated images and bridging the gap between synthetic data and downstream segmentation tasks. Extensive experiments demonstrate that our approach consistently outperforms state-of-the-art controllable generation methods, producing more stable and task-oriented synthetic data for RS semantic segmentation.

