---
layout: default
title: Measuring all the noises of LLM Evals
---

# Measuring all the noises of LLM Evals
**arXiv**：[2512.21326v1](https://arxiv.org/abs/2512.21326) · [PDF](https://arxiv.org/pdf/2512.21326.pdf)  
**作者**：Sida Wang  

**一句话要点**：提出全对配对方法以测量LLM评估中的噪声，提升统计功效

**关键词**：LLM评估, 噪声测量, 统计方法, 预测噪声, 数据噪声, 全对配对分析

## 3 点简述
- 核心问题：LLM评估中存在预测噪声、数据噪声和总噪声，影响实验可靠性。
- 方法要点：定义并测量三种噪声，应用全对配对方法分析所有模型对，基于百万级预测数据。
- 实验或效果：发现总噪声可预测，预测噪声通常大于数据噪声，平均化可显著提高统计功效。

## 摘要（原文）

> Separating signal from noise is central to experimental science. Applying well-established statistical method effectively to LLM evals requires consideration of their unique noise characteristics. We clearly define and measure three types of noise: prediction noise from generating different answers on a given question, data noise from sampling questions, and their combined total noise following the law of total variance. To emphasize relative comparisons and gain statistical power, we propose the all-pairs paired method, which applies the paired analysis to all pairs of LLMs and measures all the noise components based on millions of question-level predictions across many evals and settings. These measurements revealed clear patterns. First, each eval exhibits a characteristic and highly predictable total noise level across all model pairs. Second, paired prediction noise typically exceeds paired data noise, which means reducing prediction noise by averaging can significantly increase statistical power. These findings enable practitioners to assess significance without custom testing and to detect much smaller effects in controlled experiments.

