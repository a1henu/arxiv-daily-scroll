---
layout: default
title: Provable Target Sample Complexity Improvements as Pre-Trained Models Scale
---

# Provable Target Sample Complexity Improvements as Pre-Trained Models Scale
**arXiv**：[2602.04233v1](https://arxiv.org/abs/2602.04233) · [PDF](https://arxiv.org/pdf/2602.04233.pdf)  
**作者**：Kazuto Fukuchi, Ryuichiro Hataya, Kota Matsui  

**一句话要点**：提出caulking框架，理论证明预训练模型规模提升可降低下游任务样本复杂度

**关键词**：预训练模型, 样本复杂度, 理论分析, 参数高效微调, 缩放定律

## 3 点简述
- 核心问题：现有理论无法解释预训练模型规模扩大如何降低下游学习样本复杂度
- 方法要点：引入caulking框架，灵感来自参数高效微调方法如适配器和低秩适应
- 实验或效果：理论分析证实改进的预训练模型可减少下游任务样本需求，支持经验缩放定律

## 摘要（原文）

> Pre-trained models have become indispensable for efficiently building models across a broad spectrum of downstream tasks. The advantages of pre-trained models have been highlighted by empirical studies on scaling laws, which demonstrate that larger pre-trained models can significantly reduce the sample complexity of downstream learning. However, existing theoretical investigations of pre-trained models lack the capability to explain this phenomenon. In this paper, we provide a theoretical investigation by introducing a novel framework, caulking, inspired by parameter-efficient fine-tuning (PEFT) methods such as adapter-based fine-tuning, low-rank adaptation, and partial fine-tuning. Our analysis establishes that improved pre-trained models provably decrease the sample complexity of downstream tasks, thereby offering theoretical justification for the empirically observed scaling laws relating pre-trained model size to downstream performance, a relationship not covered by existing results.

