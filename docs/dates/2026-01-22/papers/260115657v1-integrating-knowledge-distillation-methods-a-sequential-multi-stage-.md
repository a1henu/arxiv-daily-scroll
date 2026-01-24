---
layout: default
title: Integrating Knowledge Distillation Methods: A Sequential Multi-Stage Framework
---

# Integrating Knowledge Distillation Methods: A Sequential Multi-Stage Framework
**arXiv**：[2601.15657v1](https://arxiv.org/abs/2601.15657) · [PDF](https://arxiv.org/pdf/2601.15657.pdf)  
**作者**：Yinxi Tian, Changwu Huang, Ke Tang, Xin Yao  

**一句话要点**：提出SMSKD框架以解决异构知识蒸馏方法集成中的遗忘与组合难题

**关键词**：知识蒸馏, 多阶段蒸馏, 灾难性遗忘, 参考模型, 自适应加权, 模型压缩

## 3 点简述
- 核心问题：异构知识蒸馏方法集成常导致复杂实现、组合不灵活和灾难性遗忘，限制实际效果。
- 方法要点：SMSKD采用顺序多阶段蒸馏，每阶段用特定方法训练学生模型，并冻结前一阶段参考模型锚定知识以减轻遗忘。
- 实验或效果：实验表明SMSKD在多种师生架构和方法组合下提升学生准确率，优于基线，且计算开销可忽略。

## 摘要（原文）

> Knowledge distillation (KD) transfers knowledge from large teacher models to compact student models, enabling efficient deployment on resource constrained devices. While diverse KD methods, including response based, feature based, and relation based approaches, capture different aspects of teacher knowledge, integrating multiple methods or knowledge sources is promising but often hampered by complex implementation, inflexible combinations, and catastrophic forgetting, which limits practical effectiveness.
>   This work proposes SMSKD (Sequential Multi Stage Knowledge Distillation), a flexible framework that sequentially integrates heterogeneous KD methods. At each stage, the student is trained with a specific distillation method, while a frozen reference model from the previous stage anchors learned knowledge to mitigate forgetting. In addition, we introduce an adaptive weighting mechanism based on the teacher true class probability (TCP) that dynamically adjusts the reference loss per sample to balance knowledge retention and integration.
>   By design, SMSKD supports arbitrary method combinations and stage counts with negligible computational overhead. Extensive experiments show that SMSKD consistently improves student accuracy across diverse teacher student architectures and method combinations, outperforming existing baselines. Ablation studies confirm that stage wise distillation and reference model supervision are primary contributors to performance gains, with TCP based adaptive weighting providing complementary benefits. Overall, SMSKD is a practical and resource efficient solution for integrating heterogeneous KD methods.

