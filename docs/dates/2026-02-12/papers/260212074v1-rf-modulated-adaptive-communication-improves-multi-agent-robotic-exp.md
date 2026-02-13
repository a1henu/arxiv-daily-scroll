---
layout: default
title: RF-Modulated Adaptive Communication Improves Multi-Agent Robotic Exploration
---

# RF-Modulated Adaptive Communication Improves Multi-Agent Robotic Exploration
**arXiv**：[2602.12074v1](https://arxiv.org/abs/2602.12074) · [PDF](https://arxiv.org/pdf/2602.12074.pdf)  
**作者**：Lorin Achey, Breanne Crockett, Christoffer Heckman, Bradley Hayes  

**一句话要点**：提出自适应射频传输算法以提升通信受限环境下多机器人探索效率

**关键词**：多机器人探索, 自适应通信, 射频调制, 信号强度阈值, 路径规划, 通信受限环境

## 3 点简述
- 核心问题：多机器人探索中通信受限导致协调困难和效率低下
- 方法要点：动态调制传输位置基于信号强度和数据负载，减少不必要回溯
- 实验或效果：在洞穴环境中模拟显示，相比基线方法减少58%移动距离和52%探索时间

## 摘要（原文）

> Reliable coordination and efficient communication are critical challenges for multi-agent robotic exploration of environments where communication is limited. This work introduces Adaptive-RF Transmission (ART), a novel communication-aware planning algorithm that dynamically modulates transmission location based on signal strength and data payload size, enabling heterogeneous robot teams to share information efficiently without unnecessary backtracking. We further explore an extension to this approach called ART-SST, which enforces signal strength thresholds for high-fidelity data delivery. Through over 480 simulations across three cave-inspired environments, ART consistently outperforms existing strategies, including full rendezvous and minimum-signal heuristic approaches, achieving up to a 58% reduction in distance traveled and up to 52% faster exploration times compared to baseline methods. These results demonstrate that adaptive, payload-aware communication significantly improves coverage efficiency and mission speed in complex, communication-constrained environments, offering a promising foundation for future planetary exploration and search-and-rescue missions.

