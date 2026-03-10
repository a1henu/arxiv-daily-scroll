---
layout: default
title: Hospitality-VQA: Decision-Oriented Informativeness Evaluation for Vision-Language Models
---

# Hospitality-VQA: Decision-Oriented Informativeness Evaluation for Vision-Language Models
**arXiv**：[2603.07868v1](https://arxiv.org/abs/2603.07868) · [PDF](https://arxiv.org/pdf/2603.07868.pdf)  
**作者**：Jeongwoo Lee, Baek Duhyeong, Eungyeol Han, Soyeon Shin, Gukin han, Seungduk Kim, Jaehyun Jeon, Taewoo Jeong  

**一句话要点**：提出Hospitality-VQA数据集与信息性框架，评估视觉语言模型在酒店决策场景中的适用性。

**关键词**：视觉语言模型, 视觉问答, 酒店决策, 信息性评估, 领域微调

## 3 点简述
- 核心问题：现有VQA基准未关注用户决策信息需求，视觉语言模型在酒店领域应用未知。
- 方法要点：引入信息性框架量化图像-问题对的信息价值，构建酒店专用VQA数据集。
- 实验或效果：实验显示模型需领域微调才能有效利用视觉信号进行信息性推理。

## 摘要（原文）

> Recent advances in Vision-Language Models (VLMs) have demonstrated impressive multimodal understanding in general domains. However, their applicability to decision-oriented domains such as hospitality remains largely unexplored. In this work, we investigate how well VLMs can perform visual question answering (VQA) about hotel and facility images that are central to consumer decision-making. While many existing VQA benchmarks focus on factual correctness, they rarely capture what information users actually find useful. To address this, we first introduce Informativeness as a formal framework to quantify how much hospitality-relevant information an image-question pair provides. Guided by this framework, we construct a new hospitality-specific VQA dataset that covers various facility types, where questions are specifically designed to reflect key user information needs. Using this benchmark, we conduct experiments with several state-of-the-art VLMs, revealing that VLMs are not intrinsically decision-aware-key visual signals remain underutilized, and reliable informativeness reasoning emerges only after modest domain-specific finetuning.

