---
layout: default
title: Human-Aligned MLLM Judges for Fine-Grained Image Editing Evaluation: A Benchmark, Framework, and Analysis
---

# Human-Aligned MLLM Judges for Fine-Grained Image Editing Evaluation: A Benchmark, Framework, and Analysis
**arXiv**：[2602.13028v1](https://arxiv.org/abs/2602.13028) · [PDF](https://arxiv.org/pdf/2602.13028.pdf)  
**作者**：Runzhou Liu, Hailey Weingord, Sejal Mittal, Prakhar Dungarwal, Anusha Nandula, Bo Ni, Samyadeep Basu, Hongjie Chen, Nesreen K. Ahmed, Li Li, Jiayi Zhang, Koustava Goswami, Subhojyoti Mukherjee, Branislav Kveton, Puneet Mathur, Franck Dernoncourt, Yue Zhao, Yu Wang, Ryan A. Rossi, Zhengzhong Tu, Hongru Du  

**一句话要点**：提出细粒度MLLM评估框架以解决图像编辑模型评估的粗粒度与低可解释性问题

**关键词**：图像编辑评估, 多模态大语言模型, 细粒度评估, 人类对齐, 基准构建, 可解释性

## 3 点简述
- 核心问题：传统图像编辑评估指标粗粒度、低可解释性，难以捕捉人类感知与意图的关键方面
- 方法要点：将评估分解为12个细粒度可解释因素，涵盖图像保持、编辑质量和指令忠实度
- 实验或效果：通过人类研究验证MLLM评估与人类判断高度对齐，优于传统指标

## 摘要（原文）

> Evaluating image editing models remains challenging due to the coarse granularity and limited interpretability of traditional metrics, which often fail to capture aspects important to human perception and intent. Such metrics frequently reward visually plausible outputs while overlooking controllability, edit localization, and faithfulness to user instructions. In this work, we introduce a fine-grained Multimodal Large Language Model (MLLM)-as-a-Judge framework for image editing that decomposes common evaluation notions into twelve fine-grained interpretable factors spanning image preservation, edit quality, and instruction fidelity. Building on this formulation, we present a new human-validated benchmark that integrates human judgments, MLLM-based evaluations, model outputs, and traditional metrics across diverse image editing tasks. Through extensive human studies, we show that the proposed MLLM judges align closely with human evaluations at a fine granularity, supporting their use as reliable and scalable evaluators. We further demonstrate that traditional image editing metrics are often poor proxies for these factors, failing to distinguish over-edited or semantically imprecise outputs, whereas our judges provide more intuitive and informative assessments in both offline and online settings. Together, this work introduces a benchmark, a principled factorization, and empirical evidence positioning fine-grained MLLM judges as a practical foundation for studying, comparing, and improving image editing approaches.

