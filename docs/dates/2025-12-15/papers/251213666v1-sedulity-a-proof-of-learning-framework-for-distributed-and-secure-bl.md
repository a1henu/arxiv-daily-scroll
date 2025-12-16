---
layout: default
title: SEDULity: A Proof-of-Learning Framework for Distributed and Secure Blockchains with Efficient Useful Work
---

# SEDULity: A Proof-of-Learning Framework for Distributed and Secure Blockchains with Efficient Useful Work
**arXiv**：[2512.13666v1](https://arxiv.org/abs/2512.13666) · [PDF](https://arxiv.org/pdf/2512.13666.pdf)  
**作者**：Weihang Cao, Mustafa Doger, Sennur Ulukus  

**一句话要点**：提出SEDULity框架，以高效训练机器学习模型替代工作量证明，实现分布式安全区块链。

**关键词**：区块链安全, 机器学习训练, 分布式系统, 有用工作量证明, 激励机制

## 3 点简述
- 核心问题：现有工作量证明能耗高，有用工作量证明在安全、去中心化或效率方面存在不足。
- 方法要点：设计基于机器学习的训练过程作为有用函数，替代工作量证明谜题，并编码模板块以确保安全。
- 实验或效果：理论分析显示理性矿工诚实训练，仿真结果验证框架性能与安全性。

## 摘要（原文）

> The security and decentralization of Proof-of-Work (PoW) have been well-tested in existing blockchain systems. However, its tremendous energy waste has raised concerns about sustainability. Proof-of-Useful-Work (PoUW) aims to redirect the meaningless computation to meaningful tasks such as solving machine learning (ML) problems, giving rise to the branch of Proof-of-Learning (PoL). While previous studies have proposed various PoLs, they all, to some degree, suffer from security, decentralization, or efficiency issues. In this paper, we propose a PoL framework that trains ML models efficiently while maintaining blockchain security in a fully distributed manner. We name the framework SEDULity, which stands for a Secure, Efficient, Distributed, and Useful Learning-based blockchain system. Specifically, we encode the template block into the training process and design a useful function that is difficult to solve but relatively easy to verify, as a substitute for the PoW puzzle. We show that our framework is distributed, secure, and efficiently trains ML models. We further demonstrate that the proposed PoL framework can be extended to other types of useful work and design an incentive mechanism to incentivize task verification. We show theoretically that a rational miner is incentivized to train fully honestly with well-designed system parameters. Finally, we present simulation results to demonstrate the performance of our framework and validate our analysis.

