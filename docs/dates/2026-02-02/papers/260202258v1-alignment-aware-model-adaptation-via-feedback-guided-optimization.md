---
layout: default
title: Alignment-Aware Model Adaptation via Feedback-Guided Optimization
---

# Alignment-Aware Model Adaptation via Feedback-Guided Optimization
**arXiv**：[2602.02258v1](https://arxiv.org/abs/2602.02258) · [PDF](https://arxiv.org/pdf/2602.02258.pdf)  
**作者**：Gaurav Bhatt, Aditya Chinchure, Jiawei Zhou, Leonid Sigal  

**一句话要点**：提出基于反馈引导优化的对齐感知微调框架，以在适应下游任务时保持模型对齐性。

**关键词**：模型微调, 对齐优化, 策略梯度, 自适应门控, 幻觉避免, 安全对齐

## 3 点简述
- 核心问题：标准微调孤立优化任务目标，可能损害对齐性（如安全性和避免幻觉）。
- 方法要点：通过策略梯度正则化整合外部对齐信号，采用自适应门控机制动态平衡监督和对齐梯度。
- 实验效果：在指令调优基准上减少有害和幻觉输出，不牺牲任务性能，并展示对抗性攻击的鲁棒性。

## 摘要（原文）

> Fine-tuning is the primary mechanism for adapting foundation models to downstream tasks; however, standard approaches largely optimize task objectives in isolation and do not account for secondary yet critical alignment objectives (e.g., safety and hallucination avoidance). As a result, downstream fine-tuning can degrade alignment and fail to correct pre-existing misaligned behavior. We propose an alignment-aware fine-tuning framework that integrates feedback from an external alignment signal through policy-gradient-based regularization. Our method introduces an adaptive gating mechanism that dynamically balances supervised and alignment-driven gradients on a per-sample basis, prioritizing uncertain or misaligned cases while allowing well-aligned examples to follow standard supervised updates. The framework further learns abstention behavior for fully misaligned inputs, incorporating conservative responses directly into the fine-tuned model. Experiments on general and domain-specific instruction-tuning benchmarks demonstrate consistent reductions in harmful and hallucinated outputs without sacrificing downstream task performance. Additional analyses show robustness to adversarial fine-tuning, prompt-based attacks, and unsafe initializations, establishing adaptively gated alignment optimization as an effective approach for alignment-preserving and alignment-recovering model adaptation.

