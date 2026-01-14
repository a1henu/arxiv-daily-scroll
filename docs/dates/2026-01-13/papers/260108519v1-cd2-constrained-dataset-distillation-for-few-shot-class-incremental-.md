---
layout: default
title: CD^2: Constrained Dataset Distillation for Few-Shot Class-Incremental Learning
---

# CD^2: Constrained Dataset Distillation for Few-Shot Class-Incremental Learning
**arXiv**：[2601.08519v1](https://arxiv.org/abs/2601.08519) · [PDF](https://arxiv.org/pdf/2601.08519.pdf)  
**作者**：Kexin Bao, Daichi Zhang, Hansong Zhang, Yong Li, Yutao Yue, Shiming Ge  

**一句话要点**：提出约束数据集蒸馏（CD^2）框架以解决少样本类增量学习中的灾难性遗忘问题。

**关键词**：少样本类增量学习, 数据集蒸馏, 灾难性遗忘, 知识蒸馏, 约束学习, 样本合成

## 3 点简述
- 核心问题：少样本类增量学习面临灾难性遗忘，现有方法难以有效保留先前关键知识。
- 方法要点：通过数据集蒸馏模块合成高浓缩样本，结合蒸馏约束模块保护先前类分布。
- 实验或效果：在三个公共数据集上验证，优于其他先进方法，提升知识保留能力。

## 摘要（原文）

> Few-shot class-incremental learning (FSCIL) receives significant attention from the public to perform classification continuously with a few training samples, which suffers from the key catastrophic forgetting problem. Existing methods usually employ an external memory to store previous knowledge and treat it with incremental classes equally, which cannot properly preserve previous essential knowledge. To solve this problem and inspired by recent distillation works on knowledge transfer, we propose a framework termed \textbf{C}onstrained \textbf{D}ataset \textbf{D}istillation (\textbf{CD$^2$}) to facilitate FSCIL, which includes a dataset distillation module (\textbf{DDM}) and a distillation constraint module~(\textbf{DCM}). Specifically, the DDM synthesizes highly condensed samples guided by the classifier, forcing the model to learn compacted essential class-related clues from a few incremental samples. The DCM introduces a designed loss to constrain the previously learned class distribution, which can preserve distilled knowledge more sufficiently. Extensive experiments on three public datasets show the superiority of our method against other state-of-the-art competitors.

