---
layout: default
title: Efficient Reinforcement Learning with Semantic and Token Entropy for LLM Reasoning
---

# Efficient Reinforcement Learning with Semantic and Token Entropy for LLM Reasoning
**arXiv**：[2512.04359v1](https://arxiv.org/abs/2512.04359) · [PDF](https://arxiv.org/pdf/2512.04359.pdf)  
**作者**：Hongye Cao, Zhixin Bai, Ziyue Peng, Boyan Wang, Tianpei Yang, Jing Huo, Yuyao Zhang, Yang Gao  

**一句话要点**：提出基于语义与词元熵的高效强化学习框架，以缓解熵崩溃并提升大语言模型推理能力

**关键词**：强化学习, 大语言模型推理, 熵崩溃, 课程学习, KL正则化

## 3 点简述
- 核心问题：强化学习验证奖励方法在提升大语言模型推理时易发生熵崩溃，限制策略探索。
- 方法要点：结合语义熵引导的课程学习与非均匀词元处理，从数据和算法层面优化熵信号。
- 实验或效果：在6个基准测试和3种参数规模模型上验证，优于其他基于熵的方法。

## 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) has demonstrated superior performance in enhancing the reasoning capability of large language models (LLMs). However, this accuracy-oriented learning paradigm often suffers from entropy collapse, which reduces policy exploration and limits reasoning capabilities. To address this challenge, we propose an efficient reinforcement learning framework that leverages entropy signals at both the semantic and token levels to improve reasoning. From the data perspective, we introduce semantic entropy-guided curriculum learning, organizing training data from low to high semantic entropy to guide progressive optimization from easier to more challenging tasks. For the algorithmic design, we adopt non-uniform token treatment by imposing KL regularization on low-entropy tokens that critically impact policy exploration and applying stronger constraints on high-covariance portions within these tokens. By jointly optimizing data organization and algorithmic design, our method effectively mitigates entropy collapse and enhances LLM reasoning. Experimental results across 6 benchmarks with 3 different parameter-scale base models demonstrate that our method outperforms other entropy-based approaches in improving reasoning.

