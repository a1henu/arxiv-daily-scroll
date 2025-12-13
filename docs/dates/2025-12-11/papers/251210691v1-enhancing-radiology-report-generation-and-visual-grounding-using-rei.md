---
layout: default
title: Enhancing Radiology Report Generation and Visual Grounding using Reinforcement Learning
---

# Enhancing Radiology Report Generation and Visual Grounding using Reinforcement Learning
**arXiv**：[2512.10691v1](https://arxiv.org/abs/2512.10691) · [PDF](https://arxiv.org/pdf/2512.10691.pdf)  
**作者**：Benjamin Gundersen, Nicolas Deperrois, Samuel Ruiperez-Campillo, Thomas M. Sutter, Julia E. Vogt, Michael Moor, Farhad Nooralahzadeh, Michael Krauthammer  

**一句话要点**：提出基于强化学习的医学视觉语言模型优化方法，提升胸部X光报告生成与视觉定位性能

**关键词**：医学视觉语言模型, 强化学习, 胸部X光报告生成, 视觉定位, GRPO优化, 临床任务奖励

## 3 点简述
- 问题：医学视觉语言模型依赖监督微调，缺乏任务质量评估，影响胸部X光解释效果
- 方法：在RadVLM上应用GRPO强化学习，结合临床任务奖励，对比有无显式推理的实验设置
- 效果：强化学习在报告生成和视觉定位任务上带来额外增益，模型达到最先进性能

## 摘要（原文）

> Recent advances in vision-language models (VLMs) have improved Chest X-ray (CXR) interpretation in multiple aspects. However, many medical VLMs rely solely on supervised fine-tuning (SFT), which optimizes next-token prediction without evaluating answer quality. In contrast, reinforcement learning (RL) can incorporate task-specific feedback, and its combination with explicit intermediate reasoning ("thinking") has demonstrated substantial gains on verifiable math and coding tasks. To investigate the effects of RL and thinking in a CXR VLM, we perform large-scale SFT on CXR data to build an updated RadVLM based on Qwen3-VL, followed by a cold-start SFT stage that equips the model with basic thinking ability. We then apply Group Relative Policy Optimization (GRPO) with clinically grounded, task-specific rewards for report generation and visual grounding, and run matched RL experiments on both domain-specific and general-domain Qwen3-VL variants, with and without thinking. Across these settings, we find that while strong SFT remains crucial for high base performance, RL provides additional gains on both tasks, whereas explicit thinking does not appear to further improve results. Under a unified evaluation pipeline, the RL-optimized RadVLM models outperform their baseline counterparts and reach state-of-the-art performance on both report generation and grounding, highlighting clinically aligned RL as a powerful complement to SFT for medical VLMs.

