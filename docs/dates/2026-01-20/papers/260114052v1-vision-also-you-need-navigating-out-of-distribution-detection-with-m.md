---
layout: default
title: Vision Also You Need: Navigating Out-of-Distribution Detection with Multimodal Large Language Model
---

# Vision Also You Need: Navigating Out-of-Distribution Detection with Multimodal Large Language Model
**arXiv**：[2601.14052v1](https://arxiv.org/abs/2601.14052) · [PDF](https://arxiv.org/pdf/2601.14052.pdf)  
**作者**：Haoran Xu, Yanlin Liu, Zizhao Tong, Jiaze Li, Kexue Fu, Yuyang Zhang, Longxiang Gao, Shuaiguang Li, Xingyu Li, Yanran Xu, Changwei Wang  

**一句话要点**：提出MM-OOD方法，利用多模态大语言模型增强分布外检测性能

**关键词**：分布外检测, 多模态大语言模型, 零样本学习, 图像空间挑战, 多轮对话

## 3 点简述
- 核心问题：现有零样本OOD检测方法过度依赖文本知识，忽视图像空间挑战。
- 方法要点：利用MLLMs多模态推理能力，针对近OOD和远OOD任务设计不同检测流程。
- 实验效果：在Food-101等数据集上性能显著提升，验证了在ImageNet-1K上的可扩展性。

## 摘要（原文）

> Out-of-Distribution (OOD) detection is a critical task that has garnered significant attention. The emergence of CLIP has spurred extensive research into zero-shot OOD detection, often employing a training-free approach. Current methods leverage expert knowledge from large language models (LLMs) to identify potential outliers. However, these approaches tend to over-rely on knowledge in the text space, neglecting the inherent challenges involved in detecting out-of-distribution samples in the image space. In this paper, we propose a novel pipeline, MM-OOD, which leverages the multimodal reasoning capabilities of MLLMs and their ability to conduct multi-round conversations for enhanced outlier detection. Our method is designed to improve performance in both near OOD and far OOD tasks. Specifically, (1) for near OOD tasks, we directly feed ID images and corresponding text prompts into MLLMs to identify potential outliers; and (2) for far OOD tasks, we introduce the sketch-generate-elaborate framework: first, we sketch outlier exposure using text prompts, then generate corresponding visual OOD samples, and finally elaborate by using multimodal prompts. Experiments demonstrate that our method achieves significant improvements on widely used multimodal datasets such as Food-101, while also validating its scalability on ImageNet-1K.

