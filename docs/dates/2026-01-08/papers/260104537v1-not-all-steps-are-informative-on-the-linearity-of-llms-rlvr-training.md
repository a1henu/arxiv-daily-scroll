---
layout: default
title: Not All Steps are Informative: On the Linearity of LLMs' RLVR Training
---

# Not All Steps are Informative: On the Linearity of LLMs' RLVR Training
**arXiv**：[2601.04537v1](https://arxiv.org/abs/2601.04537) · [PDF](https://arxiv.org/pdf/2601.04537.pdf)  
**作者**：Tianle Wang, Zhongyuan Wu, Shenghao Jin, Hao Xu, Wei Chen, Ning Miao  

**一句话要点**：提出权重与对数概率外推法，以线性预测加速LLM的RLVR训练

**关键词**：强化学习验证奖励, 大语言模型后训练, 线性演化, 权重外推, 对数概率外推, 计算效率

## 3 点简述
- 核心问题：RLVR训练需数千步，计算成本高，源于探索过程冗长
- 方法要点：发现RLVR中模型权重与输出呈强线性，支持外推预测未来状态
- 实验或效果：权重外推性能媲美标准训练，对数概率外推在基准测试中超越持续训练

## 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) has become a central component of large language model (LLM) post-training. Unlike supervised fine-tuning (SFT), RLVR lets an LLM generate multiple candidate solutions and reinforces those that lead to a verifiably correct final answer. However, in practice, RLVR often requires thousands of training steps to reach strong performance, incurring substantial computation largely attributed to prolonged exploration. In this work, we make a surprising observation: during RLVR, LLMs evolve in a strongly linear manner. Specifically, both model weights and model output log-probabilities exhibit strong linear correlations with RL training steps. This suggests that RLVR predominantly amplifies trends that emerge early in training, rather than continuously discovering new behaviors throughout the entire optimization trajectory. Motivated by this linearity, we investigate whether future model states can be predicted from intermediate checkpoints via extrapolation, avoiding continued expensive training. We show that Weight Extrapolation produces models with performance comparable to standard RL training while requiring significantly less computation. Moreover, Logits Extrapolation consistently outperforms continued RL training on all four benchmarks by extrapolating beyond the step range where RL training remains stable.

