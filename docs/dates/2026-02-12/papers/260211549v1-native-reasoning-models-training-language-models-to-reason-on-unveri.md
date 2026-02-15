---
layout: default
title: Native Reasoning Models: Training Language Models to Reason on Unverifiable Data
---

# Native Reasoning Models: Training Language Models to Reason on Unverifiable Data
**arXiv**：[2602.11549v1](https://arxiv.org/abs/2602.11549) · [PDF](https://arxiv.org/pdf/2602.11549.pdf)  
**作者**：Yuanfu Wang, Zhixuan Liu, Xiangtian Li, Chaochao Lu, Chao Yang  

**一句话要点**：提出NRT框架，通过自生成推理轨迹训练语言模型在不可验证数据上进行推理。

**关键词**：推理训练, 无验证器方法, 隐变量建模, 自生成数据, 强化学习, 语言模型

## 3 点简述
- 核心问题：传统方法依赖高质量人工标注和外部验证器，成本高且局限于可验证领域。
- 方法要点：将推理过程建模为隐变量，使用统一训练目标，通过优化问题奖励推理路径。
- 实验或效果：在Llama和Mistral模型上验证，NRT在无验证器方法中达到最先进性能，提升复杂推理能力。

## 摘要（原文）

> The prevailing paradigm for training large reasoning models--combining Supervised Fine-Tuning (SFT) with Reinforcement Learning with Verifiable Rewards (RLVR)--is fundamentally constrained by its reliance on high-quality, human-annotated reasoning data and external verifiers. This dependency incurs significant data-collection costs, risks embedding human cognitive biases, and confines the reinforcement learning stage to objectively assessable domains like mathematics and coding, leaving a wide range of unverifiable tasks beyond its scope. To overcome these limitations, we introduce NRT (Native Reasoning Training), a novel framework that cultivates complex reasoning by having the model generate its own reasoning traces using only standard question-answer pairs, thereby obviating the need for expert-written demonstrations. NRT reframes the training problem by treating the reasoning process as a latent variable. It employs a unified training objective that models reasoning as an optimization problem, intrinsically rewarding paths that increase the model's likelihood of producing the ground-truth answer. This unified perspective allows us to analyze intrinsic failure modes of prior methods, such as policy collapse, and systematically design more robust reward aggregation functions, creating a self-reinforcing feedback loop where the model learns to think in ways that resolve its own uncertainty. Empirical evaluation on Llama and Mistral model families demonstrates that NRT achieves state-of-the-art performance among verifier-free methods, significantly outperforming standard SFT baselines and prior verifier-free RL methods. Our approach yields particularly strong performance gains in complex reasoning domains and exhibits high robustness to policy collapse, offering a general, scalable path toward building more powerful and broadly applicable reasoning systems.

