---
layout: default
title: Conan: Progressive Learning to Reason Like a Detective over Multi-Scale Visual Evidence
---

# Conan: Progressive Learning to Reason Like a Detective over Multi-Scale Visual Evidence
**arXiv**：[2510.20470v1](https://arxiv.org/abs/2510.20470) · [PDF](https://arxiv.org/pdf/2510.20470.pdf)  
**作者**：Kun Ouyang, Yuanxin Liu, Linli Yao, Yishuo Cai, Hao Zhou, Jie Zhou, Fandong Meng, Xu Sun  

**一句话要点**：提出Conan框架以解决多步视频推理中的证据定位与推理问题

**关键词**：多步视频推理, 证据定位, 强化学习训练, 长视频理解, 多模态大语言模型, 数据集构建

## 3 点简述
- 核心问题：多模态大语言模型在多步视频推理中易产生未接地或幻觉结论
- 方法要点：构建Conan-91K数据集并设计多阶段渐进训练框架增强视觉推理
- 实验或效果：在六个基准测试中平均准确率超基线10%，实现SOTA性能

## 摘要（原文）

> Video reasoning, which requires multi-step deduction across frames, remains a
> major challenge for multimodal large language models (MLLMs). While
> reinforcement learning (RL)-based methods enhance reasoning capabilities, they
> often rely on text-only chains that yield ungrounded or hallucinated
> conclusions. Conversely, frame-retrieval approaches introduce visual grounding
> but still struggle with inaccurate evidence localization. To address these
> challenges, we present Conan, a framework for evidence-grounded multi-step
> video reasoning. Conan identifies contextual and evidence frames, reasons over
> cross-frame clues, and adaptively decides when to conclude or explore further.
> To achieve this, we (1) construct Conan-91K, a large-scale dataset of
> automatically generated reasoning traces that includes frame identification,
> evidence reasoning, and action decision, and (2) design a multi-stage
> progressive cold-start strategy combined with an
> Identification-Reasoning-Action (AIR) RLVR training framework to jointly
> enhance multi-step visual reasoning. Extensive experiments on six multi-step
> reasoning benchmarks demonstrate that Conan surpasses the baseline
> Qwen2.5-VL-7B-Instruct by an average of over 10% in accuracy, achieving
> state-of-the-art performance. Furthermore, Conan generalizes effectively to
> long-video understanding tasks, validating its strong scalability and
> robustness.

