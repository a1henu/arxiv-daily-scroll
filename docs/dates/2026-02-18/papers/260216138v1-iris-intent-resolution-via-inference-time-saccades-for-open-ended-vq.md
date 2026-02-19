---
layout: default
title: IRIS: Intent Resolution via Inference-time Saccades for Open-Ended VQA in Large Vision-Language Models
---

# IRIS: Intent Resolution via Inference-time Saccades for Open-Ended VQA in Large Vision-Language Models
**arXiv**：[2602.16138v1](https://arxiv.org/abs/2602.16138) · [PDF](https://arxiv.org/pdf/2602.16138.pdf)  
**作者**：Parsa Madinei, Srijita Karmakar, Russell Cohen Hoffing, Felix Gervitz, Miguel P. Eckstein  

**一句话要点**：提出IRIS方法，利用实时眼动数据解决开放视觉问答中的歧义问题。

**关键词**：视觉语言模型, 开放视觉问答, 眼动追踪, 歧义消解, 实时交互

## 3 点简述
- 核心问题：开放视觉问答中图像-问题对的歧义性影响大型视觉语言模型准确性。
- 方法要点：训练无关，通过推理时眼动注视点数据实时解析用户意图以消歧。
- 实验或效果：在500个图像-问题对用户研究中，歧义问题准确率从35.2%提升至77.2%。

## 摘要（原文）

> We introduce IRIS (Intent Resolution via Inference-time Saccades), a novel training-free approach that uses eye-tracking data in real-time to resolve ambiguity in open-ended VQA. Through a comprehensive user study with 500 unique image-question pairs, we demonstrate that fixations closest to the time participants start verbally asking their questions are the most informative for disambiguation in Large VLMs, more than doubling the accuracy of responses on ambiguous questions (from 35.2% to 77.2%) while maintaining performance on unambiguous queries. We evaluate our approach across state-of-the-art VLMs, showing consistent improvements when gaze data is incorporated in ambiguous image-question pairs, regardless of architectural differences. We release a new benchmark dataset to use eye movement data for disambiguated VQA, a novel real-time interactive protocol, and an evaluation suite.

