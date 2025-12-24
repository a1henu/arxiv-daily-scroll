---
layout: default
title: Bridging Modalities and Transferring Knowledge: Enhanced Multimodal Understanding and Recognition
---

# Bridging Modalities and Transferring Knowledge: Enhanced Multimodal Understanding and Recognition
**arXiv**：[2512.20501v1](https://arxiv.org/abs/2512.20501) · [PDF](https://arxiv.org/pdf/2512.20501.pdf)  
**作者**：Gorjan Radevski  

**一句话要点**：提出多模态对齐、翻译、融合与转移方法，以增强机器对复杂输入的理解与识别能力

**关键词**：多模态对齐, 空间语言翻译, 医学文本映射, 知识图链接, 动作识别, 知识蒸馏

## 3 点简述
- 核心问题：多模态机器学习中的对齐、翻译、融合与知识转移挑战，如空间语言解码、医学文本映射、知识图链接和动作识别
- 方法要点：包括Spatial-Reasoning Bert、基于空间共现的损失函数、多模态融合与知识蒸馏技术，用于场景生成、医学导航、知识图丰富和动作识别
- 实验或效果：提升空间语言理解、医学文本可导航性、知识图清晰度和动作识别鲁棒性，同时通过蒸馏减少计算需求

## 摘要（原文）

> This manuscript explores multimodal alignment, translation, fusion, and transference to enhance machine understanding of complex inputs. We organize the work into five chapters, each addressing unique challenges in multimodal machine learning.
>   Chapter 3 introduces Spatial-Reasoning Bert for translating text-based spatial relations into 2D arrangements between clip-arts. This enables effective decoding of spatial language into visual representations, paving the way for automated scene generation aligned with human spatial understanding.
>   Chapter 4 presents a method for translating medical texts into specific 3D locations within an anatomical atlas. We introduce a loss function leveraging spatial co-occurrences of medical terms to create interpretable mappings, significantly enhancing medical text navigability.
>   Chapter 5 tackles translating structured text into canonical facts within knowledge graphs. We develop a benchmark for linking natural language to entities and predicates, addressing ambiguities in text extraction to provide clearer, actionable insights.
>   Chapter 6 explores multimodal fusion methods for compositional action recognition. We propose a method fusing video frames and object detection representations, improving recognition robustness and accuracy.
>   Chapter 7 investigates multimodal knowledge transference for egocentric action recognition. We demonstrate how multimodal knowledge distillation enables RGB-only models to mimic multimodal fusion-based capabilities, reducing computational requirements while maintaining performance.
>   These contributions advance methodologies for spatial language understanding, medical text interpretation, knowledge graph enrichment, and action recognition, enhancing computational systems' ability to process complex, multimodal inputs across diverse applications.

