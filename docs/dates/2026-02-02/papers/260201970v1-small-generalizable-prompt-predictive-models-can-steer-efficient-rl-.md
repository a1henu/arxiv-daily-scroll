---
layout: default
title: Small Generalizable Prompt Predictive Models Can Steer Efficient RL Post-Training of Large Reasoning Models
---

# Small Generalizable Prompt Predictive Models Can Steer Efficient RL Post-Training of Large Reasoning Models
**arXiv**：[2602.01970v1](https://arxiv.org/abs/2602.01970) · [PDF](https://arxiv.org/pdf/2602.01970.pdf)  
**作者**：Yun Qu, Qi Wang, Yixiu Mao, Heming Zou, Yuhang Jiang, Weijie Liu, Clive Bai, Kai Yang, Yangkun Chen, Saiyong Yang, Xiangyang Ji  

**一句话要点**：提出通用预测提示选择方法以提升大型推理模型强化学习后训练效率

**关键词**：强化学习后训练, 提示选择, 贝叶斯推断, 轻量生成模型, 推理模型优化, 计算效率

## 3 点简述
- 核心问题：强化学习后训练计算成本高，现有提示选择方法依赖昂贵评估或缺乏跨提示泛化能力。
- 方法要点：使用轻量生成模型基于优化历史进行贝叶斯推断，结合难度优先和多样性原则选择信息性提示批次。
- 实验或效果：在多种推理基准测试中，显著提升训练效率、最终性能和测试时效率，优于基线方法。

## 摘要（原文）

> Reinforcement learning enhances the reasoning capabilities of large language models but often involves high computational costs due to rollout-intensive optimization. Online prompt selection presents a plausible solution by prioritizing informative prompts to improve training efficiency. However, current methods either depend on costly, exact evaluations or construct prompt-specific predictive models lacking generalization across prompts. This study introduces Generalizable Predictive Prompt Selection (GPS), which performs Bayesian inference towards prompt difficulty using a lightweight generative model trained on the shared optimization history. Intermediate-difficulty prioritization and history-anchored diversity are incorporated into the batch acquisition principle to select informative prompt batches. The small predictive model also generalizes at test-time for efficient computational allocation. Experiments across varied reasoning benchmarks indicate GPS's substantial improvements in training efficiency, final performance, and test-time efficiency over superior baseline methods.

