---
layout: default
title: BioPIE: A Biomedical Protocol Information Extraction Dataset for High-Reasoning-Complexity Experiment Question Answer
---

# BioPIE: A Biomedical Protocol Information Extraction Dataset for High-Reasoning-Complexity Experiment Question Answer
**arXiv**：[2601.04524v1](https://arxiv.org/abs/2601.04524) · [PDF](https://arxiv.org/pdf/2601.04524.pdf)  
**作者**：Haofei Hou, Shunyi Zhao, Fanxu Meng, Kairui Yang, Lecheng Ruan, Qining Wang  

**一句话要点**：提出BioPIE数据集以解决生物医学实验问答中高信息密度和多步推理的挑战

**关键词**：生物医学实验问答, 知识图谱构建, 高信息密度推理, 多步推理, 信息提取数据集

## 3 点简述
- 核心问题：现有生物医学数据集缺乏细粒度实验知识，难以支持高信息密度和多步推理的问答需求
- 方法要点：构建以实验流程为中心的知识图谱，包含实验实体、动作和关系，支持跨协议推理
- 实验或效果：评估信息提取方法，并实现问答系统，在测试、高信息密度和多步推理问题上展示性能提升

## 摘要（原文）

> Question Answer (QA) systems for biomedical experiments facilitate cross-disciplinary communication, and serve as a foundation for downstream tasks, e.g., laboratory automation. High Information Density (HID) and Multi-Step Reasoning (MSR) pose unique challenges for biomedical experimental QA. While extracting structured knowledge, e.g., Knowledge Graphs (KGs), can substantially benefit biomedical experimental QA. Existing biomedical datasets focus on general or coarsegrained knowledge and thus fail to support the fine-grained experimental reasoning demanded by HID and MSR. To address this gap, we introduce Biomedical Protocol Information Extraction Dataset (BioPIE), a dataset that provides procedure-centric KGs of experimental entities, actions, and relations at a scale that supports reasoning over biomedical experiments across protocols. We evaluate information extraction methods on BioPIE, and implement a QA system that leverages BioPIE, showcasing performance gains on test, HID, and MSR question sets, showing that the structured experimental knowledge in BioPIE underpins both AI-assisted and more autonomous biomedical experimentation.

