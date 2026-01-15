---
layout: default
title: Distribution-Aligned Sequence Distillation for Superior Long-CoT Reasoning
---

# Distribution-Aligned Sequence Distillation for Superior Long-CoT Reasoning
**arXiv**：[2601.09088v1](https://arxiv.org/abs/2601.09088) · [PDF](https://arxiv.org/pdf/2601.09088.pdf)  
**作者**：Shaotian Yan, Kaiyuan Liu, Chen Shen, Bing Wang, Sinan Fan, Jun Zhang, Yue Wu, Zheng Wang, Jieping Ye  

**一句话要点**：提出分布对齐序列蒸馏方法，以提升长链推理模型的性能

**关键词**：序列蒸馏, 长链推理, 分布对齐, 模型泛化, 开源模型

## 3 点简述
- 核心问题：现有序列蒸馏方法忽视教师模型输出分布，导致学生模型泛化能力不足
- 方法要点：设计增强的序列级蒸馏训练流程，解决分布表示、对齐和曝光偏差问题
- 实验或效果：DASD-4B-Thinking在数学、科学推理和代码生成基准上达到开源模型SOTA，仅用448K样本

## 摘要（原文）

> In this report, we introduce DASD-4B-Thinking, a lightweight yet highly capable, fully open-source reasoning model. It achieves SOTA performance among open-source models of comparable scale across challenging benchmarks in mathematics, scientific reasoning, and code generation -- even outperforming several larger models. We begin by critically reexamining a widely adopted distillation paradigm in the community: SFT on teacher-generated responses, also known as sequence-level distillation. Although a series of recent works following this scheme have demonstrated remarkable efficiency and strong empirical performance, they are primarily grounded in the SFT perspective. Consequently, these approaches focus predominantly on designing heuristic rules for SFT data filtering, while largely overlooking the core principle of distillation itself -- enabling the student model to learn the teacher's full output distribution so as to inherit its generalization capability. Specifically, we identify three critical limitations in current practice: i) Inadequate representation of the teacher's sequence-level distribution; ii) Misalignment between the teacher's output distribution and the student's learning capacity; and iii) Exposure bias arising from teacher-forced training versus autoregressive inference. In summary, these shortcomings reflect a systemic absence of explicit teacher-student interaction throughout the distillation process, leaving the essence of distillation underexploited. To address these issues, we propose several methodological innovations that collectively form an enhanced sequence-level distillation training pipeline. Remarkably, DASD-4B-Thinking obtains competitive results using only 448K training samples -- an order of magnitude fewer than those employed by most existing open-source efforts. To support community research, we publicly release our models and the training dataset.

