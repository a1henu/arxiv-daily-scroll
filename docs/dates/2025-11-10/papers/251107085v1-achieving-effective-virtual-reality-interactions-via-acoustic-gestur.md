---
layout: default
title: Achieving Effective Virtual Reality Interactions via Acoustic Gesture Recognition based on Large Language Models
---

# Achieving Effective Virtual Reality Interactions via Acoustic Gesture Recognition based on Large Language Models
**arXiv**：[2511.07085v1](https://arxiv.org/abs/2511.07085) · [PDF](https://arxiv.org/pdf/2511.07085.pdf)  
**作者**：Xijie Zhang, Fengliang He, Hong-Ning Dai  

**一句话要点**：提出基于大语言模型的声学手势识别框架，以解决VR/AR中少样本交互问题

**关键词**：声学手势识别, 大语言模型, 虚拟现实交互, 少样本学习, 信道脉冲响应

## 3 点简述
- 核心问题：VR/AR系统手势识别依赖大量标注数据，难以适应少样本场景
- 方法要点：利用大语言模型处理差分信道脉冲响应数据，实现少样本和零样本学习
- 实验或效果：在真实数据集上，准确率与经典方法相当，无需领域特定重训练

## 摘要（原文）

> Natural and efficient interaction remains a critical challenge for virtual
> reality and augmented reality (VR/AR) systems. Vision-based gesture recognition
> suffers from high computational cost, sensitivity to lighting conditions, and
> privacy leakage concerns. Acoustic sensing provides an attractive alternative:
> by emitting inaudible high-frequency signals and capturing their reflections,
> channel impulse response (CIR) encodes how gestures perturb the acoustic field
> in a low-cost and user-transparent manner. However, existing CIR-based gesture
> recognition methods often rely on extensive training of models on large labeled
> datasets, making them unsuitable for few-shot VR scenarios. In this work, we
> propose the first framework that leverages large language models (LLMs) for
> CIR-based gesture recognition in VR/AR systems. Despite LLMs' strengths, it is
> non-trivial to achieve few-shot and zero-shot learning of CIR gestures due to
> their inconspicuous features. To tackle this challenge, we collect differential
> CIR rather than original CIR data. Moreover, we construct a real-world dataset
> collected from 10 participants performing 15 gestures across three categories
> (digits, letters, and shapes), with 10 repetitions each. We then conduct
> extensive experiments on this dataset using an LLM-adopted classifier. Results
> show that our LLM-based framework achieves accuracy comparable to classical
> machine learning baselines, while requiring no domain-specific retraining.

