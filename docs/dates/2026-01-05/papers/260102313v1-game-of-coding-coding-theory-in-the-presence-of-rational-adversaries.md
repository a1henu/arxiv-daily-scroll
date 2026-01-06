---
layout: default
title: Game of Coding: Coding Theory in the Presence of Rational Adversaries, Motivated by Decentralized Machine Learning
---

# Game of Coding: Coding Theory in the Presence of Rational Adversaries, Motivated by Decentralized Machine Learning
**arXiv**：[2601.02313v1](https://arxiv.org/abs/2601.02313) · [PDF](https://arxiv.org/pdf/2601.02313.pdf)  
**作者**：Hanzaleh Akbari Nodehi, Viveck R. Cadambe, Mohammad Ali Maddah-Ali  

**一句话要点**：提出博弈编码框架以解决去中心化机器学习中理性对手下的编码问题

**关键词**：编码理论, 博弈论, 去中心化机器学习, 理性对手, Sybil抵抗, 重复编码

## 3 点简述
- 核心问题：传统编码理论假设最坏情况对手，在去中心化应用中，理性对手基于激励策略行动，需新方法
- 方法要点：引入博弈编码框架，扩展编码理论至信任最小化环境，聚焦重复编码，实现多数对手下的非零数据恢复概率
- 实验或效果：框架展示Sybil抵抗性，对手节点增加时均衡不变，并探讨未知策略场景及未来开放问题

## 摘要（原文）

> Coding theory plays a crucial role in enabling reliable communication, storage, and computation. Classical approaches assume a worst-case adversarial model and ensure error correction and data recovery only when the number of honest nodes exceeds the number of adversarial ones by some margin. However, in some emerging decentralized applications, particularly in decentralized machine learning (DeML), participating nodes are rewarded for accepted contributions. This incentive structure naturally gives rise to rational adversaries who act strategically rather than behaving in purely malicious ways.
>   In this paper, we first motivate the need for coding in the presence of rational adversaries, particularly in the context of outsourced computation in decentralized systems. We contrast this need with existing approaches and highlight their limitations. We then introduce the game of coding, a novel game-theoretic framework that extends coding theory to trust-minimized settings where honest nodes are not in the majority. Focusing on repetition coding, we highlight two key features of this framework: (1) the ability to achieve a non-zero probability of data recovery even when adversarial nodes are in the majority, and (2) Sybil resistance, i.e., the equilibrium remains unchanged even as the number of adversarial nodes increases. Finally, we explore scenarios in which the adversary's strategy is unknown and outline several open problems for future research.

