---
layout: default
title: CTIS-QA: Clinical Template-Informed Slide-level Question Answering for Pathology
---

# CTIS-QA: Clinical Template-Informed Slide-level Question Answering for Pathology
**arXiv**：[2601.01769v1](https://arxiv.org/abs/2601.01769) · [PDF](https://arxiv.org/pdf/2601.01769.pdf)  
**作者**：Hao Lu, Ziniu Qian, Yifu Li, Yang Zhou, Bingzheng Wei, Yan Xu  

**一句话要点**：提出CTIS-QA模型，基于临床模板的病理切片级问答，提升诊断准确性。

**关键词**：病理切片问答, 视觉语言对齐, 临床模板, 双流架构, 全局局部特征

## 3 点简述
- 核心问题：病理报告信息非结构化，影响视觉语言对齐与问答准确性。
- 方法要点：设计临床病理报告模板，构建双流模型模拟病理学家诊断流程。
- 实验或效果：在多个基准测试中优于现有模型，验证临床实用性。

## 摘要（原文）

> In this paper, we introduce a clinical diagnosis template-based pipeline to systematically collect and structure pathological information. In collaboration with pathologists and guided by the the College of American Pathologists (CAP) Cancer Protocols, we design a Clinical Pathology Report Template (CPRT) that ensures comprehensive and standardized extraction of diagnostic elements from pathology reports. We validate the effectiveness of our pipeline on TCGA-BRCA. First, we extract pathological features from reports using CPRT. These features are then used to build CTIS-Align, a dataset of 80k slide-description pairs from 804 WSIs for vision-language alignment training, and CTIS-Bench, a rigorously curated VQA benchmark comprising 977 WSIs and 14,879 question-answer pairs. CTIS-Bench emphasizes clinically grounded, closed-ended questions (e.g., tumor grade, receptor status) that reflect real diagnostic workflows, minimize non-visual reasoning, and require genuine slide understanding. We further propose CTIS-QA, a Slide-level Question Answering model, featuring a dual-stream architecture that mimics pathologists' diagnostic approach. One stream captures global slide-level context via clustering-based feature aggregation, while the other focuses on salient local regions through attention-guided patch perception module. Extensive experiments on WSI-VQA, CTIS-Bench, and slide-level diagnostic tasks show that CTIS-QA consistently outperforms existing state-of-the-art models across multiple metrics. Code and data are available at https://github.com/HLSvois/CTIS-QA.

