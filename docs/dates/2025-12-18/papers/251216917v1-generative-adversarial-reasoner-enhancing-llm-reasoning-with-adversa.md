---
layout: default
title: Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning
---

# Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning
**arXiv**：[2512.16917v1](https://arxiv.org/abs/2512.16917) · [PDF](https://arxiv.org/pdf/2512.16917.pdf)  
**作者**：Qihao Liu, Luoxin Ye, Wufei Ma, Yu-Cheng Chou, Alan Yuille  

**一句话要点**：提出生成对抗推理器框架，通过对抗强化学习增强大语言模型的推理能力。

**关键词**：大语言模型推理, 对抗强化学习, 步骤级奖励, 数学推理增强, 判别器模块化

## 3 点简述
- 核心问题：大语言模型在数学推理中仍存在计算错误、逻辑脆弱等过程性错误。
- 方法要点：采用同策略联合训练，让推理器和判别器通过对抗强化学习共同进化，生成密集的步骤级奖励。
- 实验或效果：在多个数学基准上提升性能，如在AIME24上显著改进DeepSeek模型的得分。

## 摘要（原文）

> Large language models (LLMs) with explicit reasoning capabilities excel at mathematical reasoning yet still commit process errors, such as incorrect calculations, brittle logic, and superficially plausible but invalid steps. In this paper, we introduce Generative Adversarial Reasoner, an on-policy joint training framework designed to enhance reasoning by co-evolving an LLM reasoner and an LLM-based discriminator through adversarial reinforcement learning. A compute-efficient review schedule partitions each reasoning chain into logically complete slices of comparable length, and the discriminator evaluates each slice's soundness with concise, structured justifications. Learning couples complementary signals: the LLM reasoner is rewarded for logically consistent steps that yield correct answers, while the discriminator earns rewards for correctly detecting errors or distinguishing traces in the reasoning process. This produces dense, well-calibrated, on-policy step-level rewards that supplement sparse exact-match signals, improving credit assignment, increasing sample efficiency, and enhancing overall reasoning quality of LLMs. Across various mathematical benchmarks, the method delivers consistent gains over strong baselines with standard RL post-training. Specifically, on AIME24, we improve DeepSeek-R1-Distill-Qwen-7B from 54.0 to 61.3 (+7.3) and DeepSeek-R1-Distill-Llama-8B from 43.7 to 53.7 (+10.0). The modular discriminator also enables flexible reward shaping for objectives such as teacher distillation, preference alignment, and mathematical proof-based reasoning.

