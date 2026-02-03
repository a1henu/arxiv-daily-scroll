---
layout: default
title: Two-Stage Grid Optimization for Group-wise Quantization of LLMs
---

# Two-Stage Grid Optimization for Group-wise Quantization of LLMs
**arXiv**：[2602.02126v1](https://arxiv.org/abs/2602.02126) · [PDF](https://arxiv.org/pdf/2602.02126.pdf)  
**作者**：Junhan Kim, Gukryeol Lee, Seungwoo Son, Jeewook Kim, Yongkweon Jeon  

**一句话要点**：提出两阶段网格优化框架以最小化层重构损失，提升大语言模型分组量化精度。

**关键词**：大语言模型量化, 分组量化, 层重构损失, 坐标下降优化, 量化误差累积

## 3 点简述
- 核心问题：GPTQ等现有方法忽略输入统计和组间相关性，导致层重构损失不匹配。
- 方法要点：第一阶段基于输入统计初始化组尺度；第二阶段冻结整数权重，用坐标下降法优化组尺度。
- 实验或效果：实验显示方法能一致提升分组量化精度，且开销可忽略。

## 摘要（原文）

> Group-wise quantization is an effective strategy for mitigating accuracy degradation in low-bit quantization of large language models (LLMs). Among existing methods, GPTQ has been widely adopted due to its efficiency; however, it neglects input statistics and inter-group correlations when determining group scales, leading to a mismatch with its goal of minimizing layer-wise reconstruction loss. In this work, we propose a two-stage optimization framework for group scales that explicitly minimizes the layer-wise reconstruction loss. In the first stage, performed prior to GPTQ, we initialize each group scale to minimize the group-wise reconstruction loss, thereby incorporating input statistics. In the second stage, we freeze the integer weights obtained via GPTQ and refine the group scales to minimize the layer-wise reconstruction loss. To this end, we employ the coordinate descent algorithm and derive a closed-form update rule, which enables efficient refinement without costly numerical optimization. Notably, our derivation incorporates the quantization errors from preceding layers to prevent error accumulation. Experimental results demonstrate that our method consistently enhances group-wise quantization, achieving higher accuracy with negligible overhead.

