---
layout: default
title: Democratizing Pathology Co-Pilots: An Open Pipeline and Dataset for Whole-Slide Vision-Language Modelling
---

# Democratizing Pathology Co-Pilots: An Open Pipeline and Dataset for Whole-Slide Vision-Language Modelling
**arXiv**：[2512.17326v1](https://arxiv.org/abs/2512.17326) · [PDF](https://arxiv.org/pdf/2512.17326.pdf)  
**作者**：Sander Moonemans, Sebastiaan Ram, Frédérique Meeuwsen, Carlijn Lems, Jeroen van der Laak, Geert Litjens, Francesco Ciompi  

**一句话要点**：提出Polysome工具和HISTAI-Instruct数据集，训练ANTONI-α视觉语言模型以增强病理学全切片图像分析。

**关键词**：全切片图像分析, 视觉语言模型, 指令调优, 病理学辅助诊断, 公开数据集

## 3 点简述
- 现有视觉语言模型在全切片图像分析中存在区域局限、输出静态或数据不公开问题，限制可复现性和进展。
- 引入Polysome工具生成合成指令，应用于HISTAI数据集创建HISTAI-Instruct，包含大量指令-响应对。
- 基于HISTAI-Instruct训练ANTONI-α模型，在组织识别、肿瘤检测和鉴别诊断任务上优于MedGemma，所有资源公开。

## 摘要（原文）

> Vision-language models (VLMs) have the potential to become co-pilots for pathologists. However, most VLMs either focus on small regions of interest within whole-slide images, provide only static slide-level outputs, or rely on data that is not publicly available, limiting reproducibility. Furthermore, training data containing WSIs paired with detailed clinical reports is scarce, restricting progress toward transparent and generalisable VLMs. We address these limitations with three main contributions. First, we introduce Polysome, a standardised tool for synthetic instruction generation. Second, we apply Polysome to the public HISTAI dataset, generating HISTAI-Instruct, a large whole-slide instruction tuning dataset spanning 24,259 slides and over 1.1 million instruction-response pairs. Finally, we use HISTAI-Instruct to train ANTONI-α, a VLM capable of visual-question answering (VQA). We show that ANTONI-α outperforms MedGemma on WSI-level VQA tasks of tissue identification, neoplasm detection, and differential diagnosis. We also compare the performance of multiple incarnations of ANTONI-α trained with different amounts of data. All methods, data, and code are publicly available.

