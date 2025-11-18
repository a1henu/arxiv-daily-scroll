---
layout: default
title: Video Finetuning Improves Reasoning Between Frames
---

# Video Finetuning Improves Reasoning Between Frames
**arXiv**：[2511.12868v1](https://arxiv.org/abs/2511.12868) · [PDF](https://arxiv.org/pdf/2511.12868.pdf)  
**作者**：Ruiqi Yang, Tian Yun, Zihan Wang, Ellie Pavlick  

**一句话要点**：提出视觉思维链以提升多模态大模型在视频中的帧间推理能力

**关键词**：多模态大语言模型, 视频微调, 视觉思维链, 帧间推理, 长视频问答, 视觉推理

## 3 点简述
- 核心问题：多模态大模型从图像扩展到视频时，常简单拼接帧令牌，缺乏帧间推理。
- 方法要点：引入视觉思维链，生成连续帧间的过渡事件描述，用于系统比较模型。
- 实验或效果：视频微调模型在长视频问答中表现更优，并能迁移到静态视觉推理任务。

## 摘要（原文）

> Multimodal large language models (LLMs) have made rapid progress in visual understanding, yet their extension from images to videos often reduces to a naive concatenation of frame tokens. In this work, we investigate what video finetuning brings to multimodal LLMs. We propose Visual Chain-of-Thought (vCoT), an explicit reasoning process that generates transitional event descriptions between consecutive frames. Using vCoT, we systematically compare image-only LVLMs with their video-finetuned counterparts, both with and without access to these transitional cues. Our experiments show that vCoT significantly improves the performance of image-only models on long-form video question answering, while yielding only marginal gains for video-finetuned models. This suggests that the latter already capture frame-to-frame transitions implicitly. Moreover, we find that video models transfer this temporal reasoning ability to purely static settings, outperforming image models' baselines on relational visual reasoning tasks.

