---
layout: default
title: Uncertainty-Aware Gradient Signal-to-Noise Data Selection for Instruction Tuning
---

# Uncertainty-Aware Gradient Signal-to-Noise Data Selection for Instruction Tuning
**arXiv**：[2601.13697v1](https://arxiv.org/abs/2601.13697) · [PDF](https://arxiv.org/pdf/2601.13697.pdf)  
**作者**：Zhihang Yuan, Chengyu Yue, Long Huang, Litu Ou, Lei Shi  

**一句话要点**：提出GRADFILTERING框架，利用梯度信噪比进行不确定性感知的数据选择以优化指令调优

**关键词**：指令调优, 数据选择, 梯度信噪比, 不确定性感知, LoRA集成, GPT-2代理

## 3 点简述
- 指令调优数据集庞大、噪声多且冗余，导致全数据微调成本高且效率低
- GRADFILTERING使用小规模GPT-2代理和LoRA集成，计算梯度信噪比作为数据效用指标
- 在LLM评估和人类评估中表现优于随机子集和基线，且收敛速度更快

## 摘要（原文）

> Instruction tuning is a standard paradigm for adapting large language models (LLMs), but modern instruction datasets are large, noisy, and redundant, making full-data fine-tuning costly and often unnecessary. Existing data selection methods either build expensive gradient datastores or assign static scores from a weak proxy, largely ignoring evolving uncertainty, and thus missing a key source of LLM interpretability. We propose GRADFILTERING, an objective-agnostic, uncertainty-aware data selection framework that utilizes a small GPT-2 proxy with a LoRA ensemble and aggregates per-example gradients into a Gradient Signal-to-Noise Ratio (G-SNR) utility. Our method matches or surpasses random subsets and strong baselines in most LLM-as-a-judge evaluations as well as in human assessment. Moreover, GRADFILTERING-selected subsets converge faster than competitive filters under the same compute budget, reflecting the benefit of uncertainty-aware scoring.

