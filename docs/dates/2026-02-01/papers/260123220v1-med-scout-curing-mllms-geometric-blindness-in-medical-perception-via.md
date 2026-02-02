---
layout: default
title: Med-Scout: Curing MLLMs' Geometric Blindness in Medical Perception via Geometry-Aware RL Post-Training
---

# Med-Scout: Curing MLLMs' Geometric Blindness in Medical Perception via Geometry-Aware RL Post-Training
**arXiv**：[2601.23220v1](https://arxiv.org/abs/2601.23220) · [PDF](https://arxiv.org/pdf/2601.23220.pdf)  
**作者**：Anglin Liu, Ruichao Chen, Yi Lu, Hongxia Xu, Jintai Chen  

**一句话要点**：提出Med-Scout框架，通过几何感知强化学习解决医学多模态大语言模型的几何盲视问题

**关键词**：医学多模态大语言模型, 几何盲视, 强化学习后训练, 几何感知, 医学视觉问答, 无监督学习

## 3 点简述
- 核心问题：医学多模态大语言模型存在几何盲视，导致输出违反几何约束的幻觉
- 方法要点：利用无标签医学图像的几何逻辑，通过三个代理任务进行强化学习后训练
- 实验或效果：在Med-Scout-Bench基准上性能提升超40%，并泛化至医学视觉问答任务

## 摘要（原文）

> Despite recent Multimodal Large Language Models (MLLMs)' linguistic prowess in medical diagnosis, we find even state-of-the-art MLLMs suffer from a critical perceptual deficit: geometric blindness. This failure to ground outputs in objective geometric constraints leads to plausible yet factually incorrect hallucinations, rooted in training paradigms that prioritize linguistic fluency over geometric fidelity. This paper introduces Med-Scout, a novel framework that "cures" this blindness via Reinforcement Learning (RL) that leverages the intrinsic geometric logic latent within unlabeled medical images. Instead of relying on costly expert annotations, Med-Scout derives verifiable supervision signals through three strategic proxy tasks: Hierarchical Scale Localization, Topological Jigsaw Reconstruction, and Anomaly Consistency Detection. To rigorously quantify this deficit, we present Med-Scout-Bench, a new benchmark specifically designed to evaluate geometric perception. Extensive evaluations show that Med-Scout significantly mitigates geometric blindness, outperforming leading proprietary and open-source MLLMs by over 40% on our benchmark. Furthermore, this enhanced geometric perception generalizes to broader medical understanding, achieving superior results on radiological and comprehensive medical VQA tasks.

