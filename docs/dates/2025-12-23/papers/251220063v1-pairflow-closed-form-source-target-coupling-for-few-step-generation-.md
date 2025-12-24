---
layout: default
title: PairFlow: Closed-Form Source-Target Coupling for Few-Step Generation in Discrete Flow Models
---

# PairFlow: Closed-Form Source-Target Coupling for Few-Step Generation in Discrete Flow Models
**arXiv**：[2512.20063v1](https://arxiv.org/abs/2512.20063) · [PDF](https://arxiv.org/pdf/2512.20063.pdf)  
**作者**：Mingue Park, Jisung Hwang, Seungwoo Yoo, Kyeongmin Yeo, Minhyuk Sung  

**一句话要点**：提出PairFlow以解决离散流模型采样慢的问题，通过轻量预处理实现少步生成。

**关键词**：离散流模型, 少步生成, 闭式反转, 配对样本, 轻量预处理, 生成模型加速

## 3 点简述
- 离散流模型采样慢，现有加速方法依赖微调，训练开销大。
- PairFlow基于闭式反转构建源-目标配对样本，无需预训练教师模型。
- 实验在分子数据和图像上验证，计算成本低且性能匹配或超越微调方法。

## 摘要（原文）

> We introduce $\texttt{PairFlow}$, a lightweight preprocessing step for training Discrete Flow Models (DFMs) to achieve few-step sampling without requiring a pretrained teacher. DFMs have recently emerged as a new class of generative models for discrete data, offering strong performance. However, they suffer from slow sampling due to their iterative nature. Existing acceleration methods largely depend on finetuning, which introduces substantial additional training overhead. $\texttt{PairFlow}$ addresses this issue with a lightweight preprocessing step. Inspired by ReFlow and its extension to DFMs, we train DFMs from coupled samples of source and target distributions, without requiring any pretrained teacher. At the core of our approach is a closed-form inversion for DFMs, which allows efficient construction of paired source-target samples. Despite its extremely low cost, taking only up to 1.7% of the compute needed for full model training, $\texttt{PairFlow}$ matches or even surpasses the performance of two-stage training involving finetuning. Furthermore, models trained with our framework provide stronger base models for subsequent distillation, yielding further acceleration after finetuning. Experiments on molecular data as well as binary and RGB images demonstrate the broad applicability and effectiveness of our approach.

