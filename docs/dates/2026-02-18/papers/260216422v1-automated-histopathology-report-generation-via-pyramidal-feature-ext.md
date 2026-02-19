---
layout: default
title: Automated Histopathology Report Generation via Pyramidal Feature Extraction and the UNI Foundation Model
---

# Automated Histopathology Report Generation via Pyramidal Feature Extraction and the UNI Foundation Model
**arXiv**：[2602.16422v1](https://arxiv.org/abs/2602.16422) · [PDF](https://arxiv.org/pdf/2602.16422.pdf)  
**作者**：Ahmet Halici, Ece Tugba Cebeci, Musa Balci, Mustafa Cini, Serkan Sokmen  

**一句话要点**：提出基于金字塔特征提取和UNI基础模型的自动化组织病理学报告生成框架

**关键词**：组织病理学报告生成, 金字塔特征提取, UNI基础模型, Transformer解码器, BioGPT分词, 检索验证

## 3 点简述
- 核心问题：组织病理学全切片图像规模巨大且需精确领域语言，报告生成困难。
- 方法要点：结合冻结病理基础模型与Transformer解码器，通过多分辨率金字塔补丁选择和背景去除处理图像。
- 实验或效果：使用BioGPT分词和检索验证步骤，提高报告可靠性，具体效果未知。

## 摘要（原文）

> Generating diagnostic text from histopathology whole slide images (WSIs) is challenging due to the gigapixel scale of the input and the requirement for precise, domain specific language. We propose a hierarchical vision language framework that combines a frozen pathology foundation model with a Transformer decoder for report generation. To make WSI processing tractable, we perform multi resolution pyramidal patch selection (downsampling factors 2^3 to 2^6) and remove background and artifacts using Laplacian variance and HSV based criteria. Patch features are extracted with the UNI Vision Transformer and projected to a 6 layer Transformer decoder that generates diagnostic text via cross attention. To better represent biomedical terminology, we tokenize the output using BioGPT. Finally, we add a retrieval based verification step that compares generated reports with a reference corpus using Sentence BERT embeddings; if a high similarity match is found, the generated report is replaced with the retrieved ground truth reference to improve reliability.

