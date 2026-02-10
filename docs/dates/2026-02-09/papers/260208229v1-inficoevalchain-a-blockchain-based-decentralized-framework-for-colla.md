---
layout: default
title: InfiCoEvalChain: A Blockchain-Based Decentralized Framework for Collaborative LLM Evaluation
---

# InfiCoEvalChain: A Blockchain-Based Decentralized Framework for Collaborative LLM Evaluation
**arXiv**：[2602.08229v1](https://arxiv.org/abs/2602.08229) · [PDF](https://arxiv.org/pdf/2602.08229.pdf)  
**作者**：Yifan Yang, Jinjia Li, Kunxi Li, Puhao Zheng, Yuanyi Wang, Zheyan Qu, Yang Yu, Jianmin Wu, Ming Li, Hongxia Yang  

**一句话要点**：提出基于区块链的去中心化框架以解决大语言模型评估中的不稳定性问题

**关键词**：大语言模型评估, 去中心化框架, 区块链协议, 异构计算, 统计稳定性, 模型排名

## 3 点简述
- 核心问题：现有集中式评估存在不透明、过拟合和硬件差异，导致排名统计不可靠
- 方法要点：利用区块链协议激励全球贡献者作为独立验证者，通过异构计算节点实现硬件和参数多样性
- 实验或效果：去中心化框架将同一模型十次运行的标准差降至0.28，显著提升排名统计置信度

## 摘要（原文）

> The rapid advancement of large language models (LLMs) demands increasingly reliable evaluation, yet current centralized evaluation suffers from opacity, overfitting, and hardware-induced variance. Our empirical analysis reveals an alarming inconsistency in existing evaluations: the standard deviation across ten repeated runs of a single model on HumanEval (1.67) actually exceeds the performance gap among the top-10 models on the official leaderboard (0.91), rendering current rankings statistically precarious. To mitigate these instabilities, we propose a decentralized evaluation framework that enables hardware and parameter diversity through large-scale benchmarking across heterogeneous compute nodes. By leveraging the blockchain-based protocol, the framework incentivizes global contributors to act as independent validators, using a robust reward system to ensure evaluation integrity and discourage dishonest participation. This collective verification transforms evaluation from a "centralized black box" into a "decentralized endorsement" where multi-party consensus and diverse inference environments yield a more stable, representative metric. Experimental results demonstrate that the decentralized evaluation framework reduces the standard deviation across ten runs on the same model to 0.28. This significant improvement over conventional frameworks ensures higher statistical confidence in model rankings. We have completely implemented this platform and will soon release it to the community.

