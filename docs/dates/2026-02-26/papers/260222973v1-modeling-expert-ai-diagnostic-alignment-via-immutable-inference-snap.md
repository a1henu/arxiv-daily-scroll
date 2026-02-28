---
layout: default
title: Modeling Expert AI Diagnostic Alignment via Immutable Inference Snapshots
---

# Modeling Expert AI Diagnostic Alignment via Immutable Inference Snapshots
**arXiv**：[2602.22973v1](https://arxiv.org/abs/2602.22973) · [PDF](https://arxiv.org/pdf/2602.22973.pdf)  
**作者**：Dimitrios P. Panagoulias, Evangelia-Aikaterini Tsichrintzi, Georgios Savvidis, Evridiki Tsoureli-Nikita  

**一句话要点**：提出基于不可变推理快照的诊断对齐框架，以量化临床AI与专家验证间的结构化信号。

**关键词**：临床AI诊断对齐, 不可变推理快照, 专家验证建模, 语义相似性评估, 图像报告生成, 结构化信号分析

## 3 点简述
- 核心问题：安全关键临床AI中，模型推理与专家修正间的过渡缺乏结构化分析，导致对齐评估不足。
- 方法要点：集成视觉大语言模型、BERT医学实体提取和SLMI步骤，生成不可变推理状态并与专家结果系统比较。
- 实验或效果：在21个皮肤病案例中，使用四级一致性框架评估，显示语义相似性下对齐稳定，综合一致性率达100%。

## 摘要（原文）

> Human-in-the-loop validation is essential in safety-critical clinical AI, yet the transition between initial model inference and expert correction is rarely analyzed as a structured signal. We introduce a diagnostic alignment framework in which the AI-generated image based report is preserved as an immutable inference state and systematically compared with the physician-validated outcome. The inference pipeline integrates a vision-enabled large language model, BERT- based medical entity extraction, and a Sequential Language Model Inference (SLMI) step to enforce domain-consistent refinement prior to expert review. Evaluation on 21 dermatological cases (21 complete AI physician pairs) em- ployed a four-level concordance framework comprising exact primary match rate (PMR), semantic similarity-adjusted rate (AMR), cross-category alignment, and Comprehensive Concordance Rate (CCR). Exact agreement reached 71.4% and remained unchanged under semantic similarity (t = 0.60), while structured cross-category and differential overlap analysis yielded 100% comprehensive concordance (95% CI: [83.9%, 100%]). No cases demonstrated complete diagnostic divergence. These findings show that binary lexical evaluation substantially un- derestimates clinically meaningful alignment. Modeling expert validation as a structured transformation enables signal-aware quantification of correction dynamics and supports traceable, human aligned evaluation of image based clinical decision support systems.

