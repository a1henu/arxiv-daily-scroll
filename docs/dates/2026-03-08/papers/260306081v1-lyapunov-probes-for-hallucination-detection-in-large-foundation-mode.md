---
layout: default
title: Lyapunov Probes for Hallucination Detection in Large Foundation Models
---

# Lyapunov Probes for Hallucination Detection in Large Foundation Models
**arXiv**：[2603.06081v1](https://arxiv.org/abs/2603.06081) · [PDF](https://arxiv.org/pdf/2603.06081.pdf)  
**作者**：Bozhi Luan, Gen Li, Yalan Qin, Jifeng Guo, Yun Zhou, Faguo Wu, Hongwei Zheng, Wenjun Wu, Zhaoxin Fan  

**一句话要点**：提出Lyapunov Probes，基于动力系统稳定性理论检测大型基础模型中的幻觉问题。

**关键词**：幻觉检测, 动力系统稳定性, Lyapunov Probes, 大型基础模型, 输入扰动分析

## 3 点简述
- 核心问题：将大型语言模型和多模态大型语言模型中的幻觉检测视为动力系统稳定性问题，而非简单分类。
- 方法要点：设计轻量级Lyapunov Probes，通过基于导数的稳定性约束训练，在输入扰动下强制置信度单调衰减。
- 实验或效果：在多样化数据集和模型上实验，相比现有基线方法，检测性能持续提升。

## 摘要（原文）

> We address hallucination detection in Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) by framing the problem through the lens of dynamical systems stability theory. Rather than treating hallucination as a straightforward classification task, we conceptualize (M)LLMs as dynamical systems, where factual knowledge is represented by stable equilibrium points within the representation space. Our main insight is that hallucinations tend to arise at the boundaries of knowledge-transition regions separating stable and unstable zones. To capture this phenomenon, we propose Lyapunov Probes: lightweight networks trained with derivative-based stability constraints that enforce a monotonic decay in confidence under input perturbations. By performing systematic perturbation analysis and applying a two-stage training process, these probes reliably distinguish between stable factual regions and unstable, hallucination-prone regions. Experiments on diverse datasets and models demonstrate consistent improvements over existing baselines.

