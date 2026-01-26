---
layout: default
title: Standardizing Longitudinal Radiology Report Evaluation via Large Language Model Annotation
---

# Standardizing Longitudinal Radiology Report Evaluation via Large Language Model Annotation
**arXiv**：[2601.16753v1](https://arxiv.org/abs/2601.16753) · [PDF](https://arxiv.org/pdf/2601.16753.pdf)  
**作者**：Xinyi Wang, Grazziela Figueredo, Ruizhe Li, Xin Chen  

**一句话要点**：提出基于大语言模型的标注流程，以标准化放射学报告纵向信息评估。

**关键词**：放射学报告生成, 纵向信息标注, 大语言模型应用, 疾病进展跟踪, 标准化评估基准

## 3 点简述
- 核心问题：缺乏自动化工具标注放射学报告中的纵向信息，影响模型验证。
- 方法要点：使用大语言模型自动检测相关句子并提取疾病进展，提升标注效率与准确性。
- 实验或效果：在500份报告上评估五个大语言模型，Qwen2.5-32B表现最佳，并标注95,169份报告建立标准化基准。

## 摘要（原文）

> Longitudinal information in radiology reports refers to the sequential tracking of findings across multiple examinations over time, which is crucial for monitoring disease progression and guiding clinical decisions. Many recent automated radiology report generation methods are designed to capture longitudinal information; however, validating their performance is challenging. There is no proper tool to consistently label temporal changes in both ground-truth and model-generated texts for meaningful comparisons. Existing annotation methods are typically labor-intensive, relying on the use of manual lexicons and rules. Complex rules are closed-source, domain specific and hard to adapt, whereas overly simple ones tend to miss essential specialised information. Large language models (LLMs) offer a promising annotation alternative, as they are capable of capturing nuanced linguistic patterns and semantic similarities without extensive manual intervention. They also adapt well to new contexts. In this study, we therefore propose an LLM-based pipeline to automatically annotate longitudinal information in radiology reports. The pipeline first identifies sentences containing relevant information and then extracts the progression of diseases. We evaluate and compare five mainstream LLMs on these two tasks using 500 manually annotated reports. Considering both efficiency and performance, Qwen2.5-32B was subsequently selected and used to annotate another 95,169 reports from the public MIMIC-CXR dataset. Our Qwen2.5-32B-annotated dataset provided us with a standardized benchmark for evaluating report generation models. Using this new benchmark, we assessed seven state-of-the-art report generation models. Our LLM-based annotation method outperforms existing annotation solutions, achieving 11.3\% and 5.3\% higher F1-scores for longitudinal information detection and disease tracking, respectively.

