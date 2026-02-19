---
layout: default
title: Designing Production-Scale OCR for India: Multilingual and Domain-Specific Systems
---

# Designing Production-Scale OCR for India: Multilingual and Domain-Specific Systems
**arXiv**：[2602.16430v1](https://arxiv.org/abs/2602.16430) · [PDF](https://arxiv.org/pdf/2602.16430.pdf)  
**作者**：Ali Faraz, Raja Kolla, Ashish Kulkarni, Shubham Agarwal  

**一句话要点**：提出Chitrapathak和Parichay系列OCR系统，以解决印度多语言和特定领域文档识别问题。

**关键词**：多语言OCR, 视觉语言模型, 文档识别, 生产级系统, 印度语言处理

## 3 点简述
- 核心问题：印度OCR需平衡语言多样性、文档异质性和部署约束。
- 方法要点：比较两种训练策略，包括端到端多模态方法和微调现有OCR模型。
- 实验或效果：Chitrapathak-2在泰卢固语达到SOTA，Parichay在9种政府文档上实现89.8%精确匹配。

## 摘要（原文）

> Designing Optical Character Recognition (OCR) systems for India requires balancing linguistic diversity, document heterogeneity, and deployment constraints. In this paper, we study two training strategies for building multilingual OCR systems with Vision-Language Models through the Chitrapathak series. We first follow a popular multimodal approach, pairing a generic vision encoder with a strong multilingual language model and training the system end-to-end for OCR. Alternatively, we explore fine-tuning an existing OCR model, despite not being trained for the target languages. Through extensive evaluation on multilingual Indic OCR benchmarks and deployment-oriented metrics, we find that the second strategy consistently achieves better accuracy-latency trade-offs. Chitrapathak-2 achieves 3-6x speedup over its predecessor with being state-of-the-art (SOTA) in Telugu (6.69 char ANLS) and second best in the rest. In addition, we present Parichay, an independent OCR model series designed specifically for 9 Indian government documents to extract structured key fields, achieving 89.8% Exact Match score with a faster inference. Together, these systems achieve SOTA performance and provide practical guidance for building production-scale OCR pipelines in the Indian context.

