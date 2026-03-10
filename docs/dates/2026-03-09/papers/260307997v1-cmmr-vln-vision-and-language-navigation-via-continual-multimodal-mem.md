---
layout: default
title: CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval
---

# CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval
**arXiv**：[2603.07997v1](https://arxiv.org/abs/2603.07997) · [PDF](https://arxiv.org/pdf/2603.07997.pdf)  
**作者**：Haozhou Li, Xiangyu Dong, Huiyan Jiang, Yaoming Zhou, Xiaoguang Ma  

**一句话要点**：提出CMMR-VLN框架，通过持续多模态记忆检索提升视觉语言导航在长视野和陌生场景中的性能。

**关键词**：视觉语言导航, 多模态记忆检索, 大语言模型, 检索增强生成, 反思学习, 全景视觉

## 3 点简述
- 核心问题：现有基于大语言模型的视觉语言导航缺乏选择性回忆先验经验的能力，限制在长视野和陌生场景的表现。
- 方法要点：构建基于全景视觉图像和显著地标的多模态经验记忆，引入检索增强生成管道和反思式记忆更新策略。
- 实验或效果：在模拟和真实测试中，相比基线模型NavGPT、MapGPT和DiscussNav，平均成功率提升显著，最高达200%。

## 摘要（原文）

> Although large language models (LLMs) are introduced into vision-and-language navigation (VLN) to improve instruction comprehension and generalization, existing LLM- based VLN lacks the ability to selectively recall and use relevant priori experiences to help navigation tasks, limiting their performance in long-horizon and unfamiliar scenarios. In this work, we propose CMMR-VLN (Continual Multimodal Memory Retrieval based VLN), a VLN framework that endows LLM agents with structured memory and reflection capabilities. Specifically, the CMMR-VLN constructs a multimodal experi- ence memory indexed by panoramic visual images and salient landmarks to retrieve relevant experiences during navigation, introduces a retrieved-augmented generation pipeline to mimick how experienced human navigators leverage priori knowledge, and incorporates a reflection-based memory update strategy that selectively stores complete successful paths and the key initial mistake in failure cases. Comprehensive tests illustrate average success rate improvements of 52.9%, 20.9% and 20.9%, and 200%, 50% and 50% over the NavGPT, the MapGPT, and the DiscussNav in simulation and real tests, respectively eluci- dating the great potential of the CMMR-VLN as a backbone VLN framework.

