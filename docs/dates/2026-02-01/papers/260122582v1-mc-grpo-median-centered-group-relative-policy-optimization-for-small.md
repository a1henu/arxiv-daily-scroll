---
layout: default
title: MC-GRPO: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning
---

# MC-GRPO: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning
**arXiv**：[2601.22582v1](https://arxiv.org/abs/2601.22582) · [PDF](https://arxiv.org/pdf/2601.22582.pdf)  
**作者**：Youngeun Kim  

**一句话要点**：提出中位数基准的组相对策略优化方法，以解决小规模采样下强化学习训练不稳定的问题

**关键词**：强化学习, 策略优化, 小规模采样, 中位数基准, 语言模型训练

## 3 点简述
- 核心问题：小规模采样时，均值基准噪声导致优势值符号翻转，影响训练准确性
- 方法要点：用中位数替代均值作为基准，对异常奖励不敏感，并排除中位数样本的反向传播
- 实验效果：在多种模型和规模下，小采样训练稳定性和最终准确率均得到提升

## 摘要（原文）

> Group-relative policy optimization methods train language models by generating multiple rollouts per prompt and normalizing rewards with a shared mean reward baseline. In resource-constrained settings where the rollout budget is small, accuracy often degrades. We find that noise in the shared baseline induces advantage sign flips, where some rollouts receive an incorrect advantage sign, and the update direction is reversed. To address this, we propose Median-Centered Group Relative Policy Optimization (MC-GRPO), a simple and effective solution for small-rollout training. Our main idea is to replace the mean baseline with a median baseline: the median is far less sensitive to outlier rewards than the mean, mitigating the sign flips under small rollout size (G). We generate one additional rollout for median reference (G+1), and compute advantages by using the group median. With an odd-sized group, exactly one completion is the median and receives zero advantage, we exclude this pivot rollout from backpropagation so the number of gradient-contributing samples per prompt remains G, preserving the core update cost of standard G-rollout training. Across various GRPO-family methods and a wide range of models and scales, this median-centered training consistently improves stability and final accuracy in the low-rollout regime, reducing the gap between G=2 and G=8 to within 1%. Code is available at https://github.com/lotusroot-kim/MC-GRPO

