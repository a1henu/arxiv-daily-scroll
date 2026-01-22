---
layout: default
title: Variance-Adaptive Muon: Accelerating LLM Pretraining with NSR-Modulated and Variance-Scaled Momentum
---

# Variance-Adaptive Muon: Accelerating LLM Pretraining with NSR-Modulated and Variance-Scaled Momentum
**arXiv**：[2601.14603v1](https://arxiv.org/abs/2601.14603) · [PDF](https://arxiv.org/pdf/2601.14603.pdf)  
**作者**：Jingru Li, Yibo Fan, Huan Li  

**一句话要点**：提出方差自适应Muon变体以加速大语言模型预训练

**关键词**：大语言模型预训练, 优化器加速, 方差自适应, 正交动量更新, 噪声信号比调制

## 3 点简述
- 核心问题：大语言模型预训练计算成本高，需优化器提升效率
- 方法要点：在正交动量更新前应用方差自适应归一化，包括NSR调制和方差缩放
- 实验或效果：在GPT-2和LLaMA预训练中加速收敛，验证损失低于基准

## 摘要（原文）

> Large Language Models (LLMs) achieve competitive performance across diverse natural language processing (NLP) tasks, yet pretraining is computationally demanding, making optimizer efficiency an important practical consideration. Muon accelerates LLM pretraining via orthogonal momentum updates that serve as a matrix analogue of the element-wise sign operator. Motivated by the recent perspective that Adam is a variance-adaptive sign update algorithm, we propose two variants of Muon, Muon-NSR and Muon-VS, which apply variance-adaptive normalization to momentum before orthogonalization. Muon-NSR applies noise-to-signal ratio (NSR) modulation, while Muon-VS performs variance-based scaling without introducing additional hyperparameters. Experiments on GPT-2 and LLaMA pretraining demonstrate that our proposed methods accelerate convergence and consistently achieve lower validation loss than both competitive, well-tuned AdamW and Muon baselines. For example, on the LLaMA-1.2B model, Muon-NSR and Muon-VS reduce the iterations required to reach the target validation loss by $1.36\times$ relative to the well-tuned Muon following the recent benchmark.

