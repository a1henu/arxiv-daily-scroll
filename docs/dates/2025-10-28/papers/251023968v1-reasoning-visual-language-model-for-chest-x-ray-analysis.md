---
layout: default
title: Reasoning Visual Language Model for Chest X-Ray Analysis
---

# Reasoning Visual Language Model for Chest X-Ray Analysis
**arXiv**：[2510.23968v1](https://arxiv.org/abs/2510.23968) · [PDF](https://arxiv.org/pdf/2510.23968.pdf)  
**作者**：Andriy Myronenko, Dong Yang, Baris Turkbey, Mariam Aboian, Sena Azamat, Esra Akcicek, Hongxu Yin, Pavlo Molchanov, Marc Edgar, Yufan He, Pengfei Guo, Yucheng Tang, Daguang Xu  

**一句话要点**：提出结合思维链推理的视觉语言模型以提升胸部X光分析的透明度和准确性

**关键词**：胸部X光分析, 思维链推理, 视觉语言模型, 可解释AI, 强化学习, 医学图像处理

## 3 点简述
- 核心问题：现有视觉语言模型在医学图像分析中缺乏透明推理，无法提供临床所需的逐步解释。
- 方法要点：采用两阶段训练，包括推理风格监督微调和基于可验证奖励的强化学习。
- 实验或效果：在分布外评估中实现竞争性分类性能，并通过专家研究提高报告效率和可信度。

## 摘要（原文）

> Vision-language models (VLMs) have shown strong promise for medical image
> analysis, but most remain opaque, offering predictions without the transparent,
> stepwise reasoning clinicians rely on. We present a framework that brings
> chain-of-thought (CoT) reasoning to chest X-ray interpretation. Inspired by
> reasoning-first training paradigms, our approach is designed to learn how
> experts reason, not just what they conclude, by aligning intermediate steps
> with observable image evidence and radiology workflow. Beyond accuracy, the
> explicit reasoning traces support clinical auditability: they reveal why a
> conclusion was reached, which alternatives were considered, and where
> uncertainty remains, enabling quality assurance, error analysis, and safer
> human-AI collaboration.
>   Our model couples high-fidelity visual encoding with a two-stage training
> recipe: a reasoning-style supervised fine-tuning (SFT) followed by
> reinforcement learning (RL) that uses verifiable rewards over a list of X-ray
> abnormalities. The model outputs reasoning that mirrors radiologists systematic
> thought process, uncertainty, and differential diagnosis. In
> out-of-distribution evaluation, the approach achieves competitive multi-label
> classification while improving interpretability. In a reader study with expert
> radiologists, full reasoning traces increased confidence, supported error
> auditing, and reduced time to finalize reports. We release code and the model
> NV-Reason-CXR-3B to support community progress toward trustworthy, explainable
> AI in chest radiography and other medical imaging tasks where reasoning quality
> is as critical as prediction quality.

