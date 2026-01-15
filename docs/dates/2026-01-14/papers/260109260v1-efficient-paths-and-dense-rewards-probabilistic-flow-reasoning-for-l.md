---
layout: default
title: Efficient Paths and Dense Rewards: Probabilistic Flow Reasoning for Large Language Models
---

# Efficient Paths and Dense Rewards: Probabilistic Flow Reasoning for Large Language Models
**arXiv**：[2601.09260v1](https://arxiv.org/abs/2601.09260) · [PDF](https://arxiv.org/pdf/2601.09260.pdf)  
**作者**：Yan Liu, Feng Zhang, Zhanyu Ma, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He, Han Liu, Yangdong Deng  

**一句话要点**：提出CoT-Flow框架，通过概率流量化推理步骤贡献，提升大语言模型推理效率与性能

**关键词**：大语言模型, 思维链推理, 概率流建模, 推理效率优化, 强化学习, 解码策略

## 3 点简述
- 核心问题：现有思维链方法缺乏量化步骤信息增益的机制，导致推理效率低和优化困难
- 方法要点：将离散推理步骤建模为连续概率流，实现流引导解码和流强化学习
- 实验或效果：在挑战性基准测试中，CoT-Flow在推理效率和性能间取得优越平衡

## 摘要（原文）

> High-quality chain-of-thought has demonstrated strong potential for unlocking the reasoning capabilities of large language models. However, current paradigms typically treat the reasoning process as an indivisible sequence, lacking an intrinsic mechanism to quantify step-wise information gain. This granularity gap manifests in two limitations: inference inefficiency from redundant exploration without explicit guidance, and optimization difficulty due to sparse outcome supervision or costly external verifiers. In this work, we propose CoT-Flow, a framework that reconceptualizes discrete reasoning steps as a continuous probabilistic flow, quantifying the contribution of each step toward the ground-truth answer. Built on this formulation, CoT-Flow enables two complementary methodologies: flow-guided decoding, which employs a greedy flow-based decoding strategy to extract information-efficient reasoning paths, and flow-based reinforcement learning, which constructs a verifier-free dense reward function. Experiments on challenging benchmarks demonstrate that CoT-Flow achieves a superior balance between inference efficiency and reasoning performance.

