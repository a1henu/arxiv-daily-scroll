---
layout: default
title: Distilling Lightweight Domain Experts from Large ML Models by Identifying Relevant Subspaces
---

# Distilling Lightweight Domain Experts from Large ML Models by Identifying Relevant Subspaces
**arXiv**：[2601.05913v1](https://arxiv.org/abs/2601.05913) · [PDF](https://arxiv.org/pdf/2601.05913.pdf)  
**作者**：Pattarawat Chormai, Ali Hashemi, Klaus-Robert Müller, Grégoire Montavon  

**一句话要点**：提出SubDistill算法，通过识别相关子空间从大模型中蒸馏轻量级领域专家模型。

**关键词**：知识蒸馏, 轻量级模型, 子空间识别, 领域专家, 层间蒸馏, 可解释AI

## 3 点简述
- 核心问题：现有蒸馏方法未明确针对相关子任务，导致资源浪费。
- 方法要点：仅蒸馏教师模型每层中与相关类别和概念相关的组件。
- 实验或效果：在CIFAR-100和ImageNet上优于现有层间蒸馏技术，学生模型决策结构更接近教师。

## 摘要（原文）

> Knowledge distillation involves transferring the predictive capabilities of large, high-performing AI models (teachers) to smaller models (students) that can operate in environments with limited computing power. In this paper, we address the scenario in which only a few classes and their associated intermediate concepts are relevant to distill. This scenario is common in practice, yet few existing distillation methods explicitly focus on the relevant subtask. To address this gap, we introduce 'SubDistill', a new distillation algorithm with improved numerical properties that only distills the relevant components of the teacher model at each layer. Experiments on CIFAR-100 and ImageNet with Convolutional and Transformer models demonstrate that SubDistill outperforms existing layer-wise distillation techniques on a representative set of subtasks. Our benchmark evaluations are complemented by Explainable AI analyses showing that our distilled student models more closely match the decision structure of the original teacher model.

