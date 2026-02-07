---
layout: default
title: Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation
---

# Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation
**arXiv**：[2602.05548v1](https://arxiv.org/abs/2602.05548) · [PDF](https://arxiv.org/pdf/2602.05548.pdf)  
**作者**：Zhiqi Yu, Zhangquan Chen, Mengting Liu, Heye Zhang, Liangqiong Qu  

**一句话要点**：提出非对称组相对优势估计以解决GRPO在探索和难度适应中的瓶颈

**关键词**：强化学习, 可验证奖励, 优势估计, 探索策略, 难度适应, 大语言模型

## 3 点简述
- 核心问题：GRPO因组相对优势估计的隐式对称性，导致探索不足和难度适应差
- 方法要点：引入非对称组相对优势估计，动态调节探索激励和样本难度焦点
- 实验或效果：在七个基准测试中，A-GRAE持续提升GRPO及其变体在LLM和MLLM上的性能

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR), particularly GRPO, has become the standard for eliciting LLM reasoning. However, its efficiency in exploration and difficulty adaptation remains an open challenge. In this work, we argue that these bottlenecks stem from an implicit advantage symmetry inherent in Group Relative Advantage Estimation (GRAE). This symmetry induces two critical limitations: (i) at the group level, strict symmetry in weights between correct and incorrect trajectories leaves unsampled action logits unchanged, thereby hindering exploration of novel correct solution. (ii) at the sample level, the algorithm implicitly prioritizes medium-difficulty samples, remaining agnostic to the non-stationary demands of difficulty focus. Through controlled experiments, we reveal that this symmetric property is sub-optimal, yielding two pivotal insights: (i) asymmetrically suppressing the advantages of correct trajectories encourages essential exploration. (ii) learning efficiency is maximized by a curriculum-like transition-prioritizing simpler samples initially before gradually shifting to complex ones. Motivated by these findings, we propose Asymmetric GRAE (A-GRAE), which dynamically modulates exploration incentives and sample-difficulty focus. Experiments across seven benchmarks demonstrate that A-GRAE consistently improves GRPO and its variants across both LLMs and MLLMs.

