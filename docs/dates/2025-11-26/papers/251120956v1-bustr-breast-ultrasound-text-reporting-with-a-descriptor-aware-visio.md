---
layout: default
title: BUSTR: Breast Ultrasound Text Reporting with a Descriptor-Aware Vision-Language Model
---

# BUSTR: Breast Ultrasound Text Reporting with a Descriptor-Aware Vision-Language Model
**arXiv**：[2511.20956v1](https://arxiv.org/abs/2511.20956) · [PDF](https://arxiv.org/pdf/2511.20956.pdf)  
**作者**：Rawa Mohammed, Mina Attin, Bryar Shareef  

**一句话要点**：提出BUSTR框架，通过描述符感知视觉语言模型生成乳腺超声报告，无需配对图像-报告数据。

**关键词**：乳腺超声报告生成, 描述符感知视觉语言模型, 多任务学习, 视觉文本对齐, 无配对数据训练

## 3 点简述
- 核心问题：乳腺超声自动报告生成缺乏配对数据集，且大语言模型易产生幻觉。
- 方法要点：使用多任务Swin编码器学习描述符感知视觉表示，结合双级目标对齐视觉与文本。
- 实验或效果：在BrEaST和BUS-BRA数据集上提升自然语言生成和临床疗效指标。

## 摘要（原文）

> Automated radiology report generation (RRG) for breast ultrasound (BUS) is limited by the lack of paired image-report datasets and the risk of hallucinations from large language models. We propose BUSTR, a multitask vision-language framework that generates BUS reports without requiring paired image-report supervision. BUSTR constructs reports from structured descriptors (e.g., BI-RADS, pathology, histology) and radiomics features, learns descriptor-aware visual representations with a multi-head Swin encoder trained using a multitask loss over dataset-specific descriptor sets, and aligns visual and textual tokens via a dual-level objective that combines token-level cross-entropy with a cosine-similarity alignment loss between input and output representations. We evaluate BUSTR on two public BUS datasets, BrEaST and BUS-BRA, which differ in size and available descriptors. Across both datasets, BUSTR consistently improves standard natural language generation metrics and clinical efficacy metrics, particularly for key targets such as BI-RADS category and pathology. Our results show that this descriptor-aware vision model, trained with a combined token-level and alignment loss, improves both automatic report metrics and clinical efficacy without requiring paired image-report data. The source code can be found at https://github.com/AAR-UNLV/BUSTR

