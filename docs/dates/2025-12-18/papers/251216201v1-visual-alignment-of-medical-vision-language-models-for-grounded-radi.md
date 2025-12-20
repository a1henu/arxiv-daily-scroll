---
layout: default
title: Visual Alignment of Medical Vision-Language Models for Grounded Radiology Report Generation
---

# Visual Alignment of Medical Vision-Language Models for Grounded Radiology Report Generation
**arXiv**：[2512.16201v1](https://arxiv.org/abs/2512.16201) · [PDF](https://arxiv.org/pdf/2512.16201.pdf)  
**作者**：Sarosij Bose, Ravi K. Rajendran, Biplob Debnath, Konstantinos Karydis, Amit K. Roy-Chowdhury, Srimat Chakradhar  

**一句话要点**：提出VALOR方法，通过强化学习后对齐解决医学视觉-语言模型在放射学报告生成中的幻觉问题。

**关键词**：放射学报告生成, 医学视觉-语言模型, 强化学习对齐, 视觉基础性, 跨模态对齐

## 3 点简述
- 核心问题：现有医学视觉-语言模型在放射学报告生成中因跨模态对齐不足导致幻觉，影响临床准确性。
- 方法要点：采用基于GRPO的强化学习后对齐框架，分两阶段提升文本准确性和视觉投影模块的疾病对齐。
- 实验或效果：在多个基准测试中显著提高事实准确性和视觉基础性，优于当前最优方法。

## 摘要（原文）

> Radiology Report Generation (RRG) is a critical step toward automating healthcare workflows, facilitating accurate patient assessments, and reducing the workload of medical professionals. Despite recent progress in Large Medical Vision-Language Models (Med-VLMs), generating radiology reports that are both visually grounded and clinically accurate remains a significant challenge. Existing approaches often rely on large labeled corpora for pre-training, costly task-specific preference data, or retrieval-based methods. However, these strategies do not adequately mitigate hallucinations arising from poor cross-modal alignment between visual and linguistic representations. To address these limitations, we propose VALOR:Visual Alignment of Medical Vision-Language Models for GrOunded Radiology Report Generation. Our method introduces a reinforcement learning-based post-alignment framework utilizing Group-Relative Proximal Optimization (GRPO). The training proceeds in two stages: (1) improving the Med-VLM with textual rewards to encourage clinically precise terminology, and (2) aligning the vision projection module of the textually grounded model with disease findings, thereby guiding attention toward image re gions most relevant to the diagnostic task. Extensive experiments on multiple benchmarks demonstrate that VALOR substantially improves factual accuracy and visual grounding, achieving significant performance gains over state-of-the-art report generation methods.

