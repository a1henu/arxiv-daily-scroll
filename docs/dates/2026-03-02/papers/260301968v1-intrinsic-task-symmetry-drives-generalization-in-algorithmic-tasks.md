---
layout: default
title: Intrinsic Task Symmetry Drives Generalization in Algorithmic Tasks
---

# Intrinsic Task Symmetry Drives Generalization in Algorithmic Tasks
**arXiv**：[2603.01968v1](https://arxiv.org/abs/2603.01968) · [PDF](https://arxiv.org/pdf/2603.01968.pdf)  
**作者**：Hyeonbin Hwang, Yeachan Park  

**一句话要点**：提出内在任务对称性驱动算法任务泛化的机制，以解释grokking现象。

**关键词**：grokking现象, 任务对称性, 表示学习, 算法推理, 泛化机制

## 3 点简述
- 核心问题：grokking现象中从记忆到泛化的突然转变机制未知。
- 方法要点：识别训练三阶段动态，强调对称性获取驱动泛化。
- 实验或效果：在多种算法任务中验证，并开发对称性诊断加速泛化。

## 摘要（原文）

> Grokking, the sudden transition from memorization to generalization, is characterized by the emergence of low-dimensional representations, yet the mechanism underlying this organization remains elusive. We propose that intrinsic task symmetries primarily drive grokking and shape the geometry of the model's representation space. We identify a consistent three-stage training dynamic underlying grokking: (i) memorization, (ii) symmetry acquisition, and (iii) geometric organization. We show that generalization emerges during the symmetry acquisition phase, after which representations reorganize into a structured, task-aligned geometry. We validate this symmetry-driven account across diverse algorithmic domains, including algebraic, structural, and relational reasoning tasks. Building on these findings, we introduce a symmetry-based diagnostic that anticipates the onset of generalization and propose strategies to accelerate it. Together, our results establish intrinsic symmetry as the key factor enabling neural networks to move beyond memorization and achieve robust algorithmic reasoning.

