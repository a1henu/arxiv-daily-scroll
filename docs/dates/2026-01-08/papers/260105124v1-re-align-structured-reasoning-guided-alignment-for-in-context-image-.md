---
layout: default
title: Re-Align: Structured Reasoning-guided Alignment for In-Context Image Generation and Editing
---

# Re-Align: Structured Reasoning-guided Alignment for In-Context Image Generation and Editing
**arXiv**：[2601.05124v1](https://arxiv.org/abs/2601.05124) · [PDF](https://arxiv.org/pdf/2601.05124.pdf)  
**作者**：Runze He, Yiji Cheng, Tiankai Hang, Zhimin Li, Yu Xu, Zijin Yin, Shiyi Zhang, Wenxun Dai, Penghui Du, Ao Ma, Chunyu Wang, Qinglin Lu, Jizhong Han, Jiao Dai  

**一句话要点**：提出Re-Align框架，通过结构化推理引导对齐解决上下文图像生成与编辑中的意图理解与执行差距问题。

**关键词**：上下文图像生成, 图像编辑, 结构化推理, 对齐训练, 强化学习, 多模态模型

## 3 点简述
- 核心问题：上下文图像生成与编辑中，多模态模型的理解能力难以有效迁移到图像生成，导致用户意图执行不精确。
- 方法要点：引入In-Context Chain-of-Thooth结构化推理范式，解耦语义引导和参考关联，并采用基于代理奖励的强化学习训练方案提升对齐性能。
- 实验或效果：在上下文图像生成和编辑任务上，Re-Align优于模型规模和资源相当的竞争方法，验证了其有效性。

## 摘要（原文）

> In-context image generation and editing (ICGE) enables users to specify visual concepts through interleaved image-text prompts, demanding precise understanding and faithful execution of user intent. Although recent unified multimodal models exhibit promising understanding capabilities, these strengths often fail to transfer effectively to image generation. We introduce Re-Align, a unified framework that bridges the gap between understanding and generation through structured reasoning-guided alignment. At its core lies the In-Context Chain-of-Thought (IC-CoT), a structured reasoning paradigm that decouples semantic guidance and reference association, providing clear textual target and mitigating confusion among reference images. Furthermore, Re-Align introduces an effective RL training scheme that leverages a surrogate reward to measure the alignment between structured reasoning text and the generated image, thereby improving the model's overall performance on ICGE tasks. Extensive experiments verify that Re-Align outperforms competitive methods of comparable model scale and resources on both in-context image generation and editing tasks.

