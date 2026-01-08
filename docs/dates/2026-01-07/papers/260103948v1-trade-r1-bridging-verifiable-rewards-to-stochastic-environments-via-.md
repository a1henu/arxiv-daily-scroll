---
layout: default
title: Trade-R1: Bridging Verifiable Rewards to Stochastic Environments via Process-Level Reasoning Verification
---

# Trade-R1: Bridging Verifiable Rewards to Stochastic Environments via Process-Level Reasoning Verification
**arXiv**：[2601.03948v1](https://arxiv.org/abs/2601.03948) · [PDF](https://arxiv.org/pdf/2601.03948.pdf)  
**作者**：Rui Sun, Yifan Sun, Sheng Xu, Li Zhao, Jing Li, Daxin Jiang, Chen Hua, Zuo Bai  

**一句话要点**：提出Trade-R1框架，通过过程级推理验证将可验证奖励桥接至随机环境以解决金融决策中的奖励黑客问题。

**关键词**：强化学习, 金融决策, 过程级推理验证, 检索增强生成, 奖励黑客, 跨市场泛化

## 3 点简述
- 核心问题：金融市场的随机性导致可验证但噪声的奖励使标准强化学习退化为奖励黑客。
- 方法要点：设计结构化RAG任务和三角一致性度量，验证推理链与证据的对齐以过滤噪声奖励。
- 实验或效果：在不同国家资产选择实验中，动态效应语义奖励策略实现跨市场泛化并保持最高推理一致性。

## 摘要（原文）

> Reinforcement Learning (RL) has enabled Large Language Models (LLMs) to achieve remarkable reasoning in domains like mathematics and coding, where verifiable rewards provide clear signals. However, extending this paradigm to financial decision is challenged by the market's stochastic nature: rewards are verifiable but inherently noisy, causing standard RL to degenerate into reward hacking. To address this, we propose Trade-R1, a model training framework that bridges verifiable rewards to stochastic environments via process-level reasoning verification. Our key innovation is a verification method that transforms the problem of evaluating reasoning over lengthy financial documents into a structured Retrieval-Augmented Generation (RAG) task. We construct a triangular consistency metric, assessing pairwise alignment between retrieved evidence, reasoning chains, and decisions to serve as a validity filter for noisy market returns. We explore two reward integration strategies: Fixed-effect Semantic Reward (FSR) for stable alignment signals, and Dynamic-effect Semantic Reward (DSR) for coupled magnitude optimization. Experiments on different country asset selection demonstrate that our paradigm reduces reward hacking, with DSR achieving superior cross-market generalization while maintaining the highest reasoning consistency.

