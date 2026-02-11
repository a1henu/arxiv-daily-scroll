---
layout: default
title: NOWJ @BioCreative IX ToxHabits: An Ensemble Deep Learning Approach for Detecting Substance Use and Contextual Information in Clinical Texts
---

# NOWJ @BioCreative IX ToxHabits: An Ensemble Deep Learning Approach for Detecting Substance Use and Contextual Information in Clinical Texts
**arXiv**：[2602.09469v1](https://arxiv.org/abs/2602.09469) · [PDF](https://arxiv.org/pdf/2602.09469.pdf)  
**作者**：Huu-Huy-Hoang Tran, Gia-Bao Duong, Quoc-Viet-Anh Tran, Thi-Hai-Yen Vuong, Hoang-Quynh Le  

**一句话要点**：提出多输出集成系统NOWJ，用于检测西班牙临床文本中的药物使用信息

**关键词**：临床文本处理, 药物使用检测, 序列标注, 集成学习, 低资源语言处理

## 3 点简述
- 核心问题：从非结构化电子健康记录中提取药物使用信息是临床自然语言处理的挑战
- 方法要点：集成BETO与CRF层，采用多输出架构和句子过滤策略
- 实验效果：在ToxHabits任务中，触发检测F1达0.94，论元检测F1达0.91

## 摘要（原文）

> Extracting drug use information from unstructured Electronic Health Records remains a major challenge in clinical Natural Language Processing. While Large Language Models demonstrate advancements, their use in clinical NLP is limited by concerns over trust, control, and efficiency. To address this, we present NOWJ submission to the ToxHabits Shared Task at BioCreative IX. This task targets the detection of toxic substance use and contextual attributes in Spanish clinical texts, a domain-specific, low-resource setting. We propose a multi-output ensemble system tackling both Subtask 1 - ToxNER and Subtask 2 - ToxUse. Our system integrates BETO with a CRF layer for sequence labeling, employs diverse training strategies, and uses sentence filtering to boost precision. Our top run achieved 0.94 F1 and 0.97 precision for Trigger Detection, and 0.91 F1 for Argument Detection.

