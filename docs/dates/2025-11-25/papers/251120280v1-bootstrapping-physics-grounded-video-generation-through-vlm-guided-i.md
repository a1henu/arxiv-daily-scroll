---
layout: default
title: Bootstrapping Physics-Grounded Video Generation through VLM-Guided Iterative Self-Refinement
---

# Bootstrapping Physics-Grounded Video Generation through VLM-Guided Iterative Self-Refinement
**arXiv**：[2511.20280v1](https://arxiv.org/abs/2511.20280) · [PDF](https://arxiv.org/pdf/2511.20280.pdf)  
**作者**：Yang Liu, Xilin Zhao, Peisong Wen, Siran Dai, Qingming Huang  

**一句话要点**：提出基于VLM引导的迭代自优化框架以提升视频生成的物理一致性

**关键词**：视频生成, 物理一致性, 迭代自优化, 多模态思维链, VLM引导, 训练无关方法

## 3 点简述
- 当前视频生成模型难以遵循真实世界物理原理，导致物理不一致问题
- 采用多模态思维链过程，利用大语言模型和视觉语言模型提供物理感知指导
- 在PhyIQ基准测试中，物理智商分数从56.31提升至62.38，无需额外训练

## 摘要（原文）

> Recent progress in video generation has led to impressive visual quality, yet current models still struggle to produce results that align with real-world physical principles. To this end, we propose an iterative self-refinement framework that leverages large language models and vision-language models to provide physics-aware guidance for video generation. Specifically, we introduce a multimodal chain-of-thought (MM-CoT) process that refines prompts based on feedback from physical inconsistencies, progressively enhancing generation quality. This method is training-free and plug-and-play, making it readily applicable to a wide range of video generation models. Experiments on the PhyIQ benchmark show that our method improves the Physics-IQ score from 56.31 to 62.38. We hope this work serves as a preliminary exploration of physics-consistent video generation and may offer insights for future research.

