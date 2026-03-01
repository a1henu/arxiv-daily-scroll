---
layout: default
title: Decentralized Ranking Aggregation: Gossip Algorithms for Borda and Copeland Consensus
---

# Decentralized Ranking Aggregation: Gossip Algorithms for Borda and Copeland Consensus
**arXiv**：[2602.22847v1](https://arxiv.org/abs/2602.22847) · [PDF](https://arxiv.org/pdf/2602.22847.pdf)  
**作者**：Anna Van Elst, Kerrian Le Caillec, Igor Colin, Stephan Clémençon  

**一句话要点**：提出基于随机gossip通信的去中心化排名聚合算法，以解决分布式网络中Borda和Copeland共识计算问题。

**关键词**：去中心化计算, 排名聚合, gossip算法, Borda共识, Copeland共识, 分布式网络

## 3 点简述
- 核心问题：在去中心化网络中聚合分布式排名数据，缺乏可靠共识计算方法。
- 方法要点：利用随机gossip算法实现局部交互，支持Borda、Copeland、中位数排名和局部Kemenization规则。
- 实验或效果：提供收敛保证和速率界限，实证显示算法快速可靠收敛到正确聚合结果。

## 摘要（原文）

> The concept of ranking aggregation plays a central role in preference analysis, and numerous algorithms for calculating median rankings, often originating in social choice theory, have been documented in the literature, offering theoretical guarantees in a centralized setting, i.e., when all the ranking data to be aggregated can be brought together in a single computing unit. For many technologies (e.g. peer-to-peer networks, IoT, multi-agent systems), extending the ability to calculate consensus rankings with guarantees in a decentralized setting, i.e., when preference data is initially distributed across a communicating network, remains a major methodological challenge. Indeed, in recent years, the literature on decentralized computation has mainly focused on computing or optimizing statistics such as arithmetic means using gossip algorithms. The purpose of this article is precisely to study how to achieve reliable consensus on collective rankings using classical rules (e.g. Borda, Copeland) in a decentralized setting, thereby raising new questions, robustness to corrupted nodes, and scalability through reduced communication costs in particular. The approach proposed and analyzed here relies on random gossip communication, allowing autonomous agents to compute global ranking consensus using only local interactions, without coordination or central authority.
>   We provide rigorous convergence guarantees, including explicit rate bounds, for the Borda and Copeland consensus methods. Beyond these rules, we also provide a decentralized implementation of consensus according to the median rank rule and local Kemenization. Extensive empirical evaluations on various network topologies and real and synthetic ranking datasets demonstrate that our algorithms converge quickly and reliably to the correct ranking aggregation.

