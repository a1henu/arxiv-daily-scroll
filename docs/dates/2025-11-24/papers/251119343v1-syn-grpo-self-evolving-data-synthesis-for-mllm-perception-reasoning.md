---
layout: default
title: Syn-GRPO: Self-Evolving Data Synthesis for MLLM Perception Reasoning
---

# Syn-GRPO: Self-Evolving Data Synthesis for MLLM Perception Reasoning
**arXiv**：[2511.19343v1](https://arxiv.org/abs/2511.19343) · [PDF](https://arxiv.org/pdf/2511.19343.pdf)  
**作者**：Qihan Huang, Haofei Zhang, Rong Wei, Yi Wang, Rui Tang, Mingli Song, Jie Song  

**一句话要点**：提出Syn-GRPO以解决MLLM强化学习中数据质量低的问题

**关键词**：多模态大语言模型, 强化学习, 数据合成, 视觉感知, 多样性奖励, 自演化强化学习

## 3 点简述
- 核心问题：现有强化学习方法数据质量低，样本无法激发MLLM多样响应，限制探索范围。
- 方法要点：使用在线数据生成器合成高质量训练数据，结合数据服务器和GRPO工作流提升多样性。
- 实验或效果：在三个视觉感知任务中显著提升数据质量和性能，优于现有方法。

## 摘要（原文）

> RL (reinforcement learning) methods (e.g., GRPO) for MLLM (Multimodal LLM) perception ability has attracted wide research interest owing to its remarkable generalization ability. Nevertheless, existing reinforcement learning methods still face the problem of low data quality, where data samples cannot elicit diverse responses from MLLMs, thus restricting the exploration scope for MLLM reinforcement learning. Some methods attempt to mitigate this problem by imposing constraints on entropy, but none address it at its root. Therefore, to tackle this problem, this work proposes Syn-GRPO (Synthesis-GRPO), which employs an online data generator to synthesize high-quality training data with diverse responses in GRPO training. Specifically, Syn-GRPO consists of two components: (1) data server; (2) GRPO workflow. The data server synthesizes new samples from existing ones using an image generation model, featuring a decoupled and asynchronous scheme to achieve high generation efficiency. The GRPO workflow provides the data server with the new image descriptions, and it leverages a diversity reward to supervise the MLLM to predict image descriptions for synthesizing samples with diverse responses. Experiment results across three visual perception tasks demonstrate that Syn-GRPO improves the data quality by a large margin, achieving significant superior performance to existing MLLM perception methods, and Syn-GRPO presents promising potential for scaling long-term self-evolving RL. Our code is available at https://github.com/hqhQAQ/Syn-GRPO.

