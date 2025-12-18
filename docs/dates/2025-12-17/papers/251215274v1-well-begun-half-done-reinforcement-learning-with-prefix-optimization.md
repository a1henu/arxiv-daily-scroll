---
layout: default
title: Well Begun, Half Done: Reinforcement Learning with Prefix Optimization for LLM Reasoning
---

# Well Begun, Half Done: Reinforcement Learning with Prefix Optimization for LLM Reasoning
**arXiv**：[2512.15274v1](https://arxiv.org/abs/2512.15274) · [PDF](https://arxiv.org/pdf/2512.15274.pdf)  
**作者**：Yiliu Sun, Zicheng Zhao, Yang Wei, Yanfang Zhang, Chen Gong  

**一句话要点**：提出渐进前缀策略优化以提升大语言模型推理能力

**关键词**：强化学习, 大语言模型推理, 前缀优化, 路径依赖, 训练策略, 可验证奖励

## 3 点简述
- 当前强化学习与可验证奖励方法忽视前缀令牌对推理的贡献，导致训练效率低下
- PPPO方法聚焦前缀优化，引入渐进前缀保留和延续累积奖励策略
- 实验显示PPPO在多种推理任务上优于现有方法，训练令牌减少但准确率提升

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) significantly enhances the reasoning capability of Large Language Models (LLMs). Current RLVR approaches typically conduct training across all generated tokens, but neglect to explore which tokens (e.g., prefix tokens) actually contribute to reasoning. This uniform training strategy spends substantial effort on optimizing low-return tokens, which in turn impedes the potential improvement from high-return tokens and reduces overall training effectiveness. To address this issue, we propose a novel RLVR approach called Progressive Prefix-token Policy Optimization (PPPO), which highlights the significance of the prefix segment of generated outputs. Specifically, inspired by the well-established human thinking theory of Path Dependence, where early-stage thoughts substantially constrain subsequent thinking trajectory, we identify an analogous phenomenon in LLM reasoning termed Beginning Lock-in Effect (BLE). PPPO leverages this finding by focusing its optimization objective on the prefix reasoning process of LLMs. This targeted optimization strategy can positively influence subsequent reasoning processes, and ultimately improve final results. To improve the learning effectiveness of LLMs on how to start reasoning with high quality, PPPO introduces two training strategies: (a) Progressive Prefix Retention, which shapes a progressive learning process by increasing the proportion of retained prefix tokens during training; (b) Continuation Accumulated Reward, which mitigates reward bias by sampling multiple continuations for one prefix token sequence, and accumulating their scores as the reward signal. Extensive experimental results on various reasoning tasks demonstrate that our proposed PPPO outperforms representative RLVR methods, with the accuracy improvements of 18.02% on only 26.17% training tokens.

