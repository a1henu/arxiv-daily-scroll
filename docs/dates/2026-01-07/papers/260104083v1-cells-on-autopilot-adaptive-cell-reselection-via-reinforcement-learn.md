---
layout: default
title: Cells on Autopilot: Adaptive Cell (Re)Selection via Reinforcement Learning
---

# Cells on Autopilot: Adaptive Cell (Re)Selection via Reinforcement Learning
**arXiv**：[2601.04083v1](https://arxiv.org/abs/2601.04083) · [PDF](https://arxiv.org/pdf/2601.04083.pdf)  
**作者**：Marvin Illian, Ramin Khalili, Antonio A. de A. Rocha, Lin Wang  

**一句话要点**：提出基于强化学习的CellPilot框架，自适应调整蜂窝网络重选参数以提升性能。

**关键词**：蜂窝网络重选, 强化学习, 自适应优化, 网络性能提升, 5G/4G共存

## 3 点简述
- 核心问题：5G/4G网络共存下，手动配置蜂窝重选参数难以适应动态网络条件，影响整体性能。
- 方法要点：利用强化学习代理学习网络时空模式，自动调整重选参数，实现自适应优化。
- 实验或效果：基于真实数据验证，轻量级代理相比传统启发式方法性能提升高达167%，泛化能力强。

## 摘要（原文）

> The widespread deployment of 5G networks, together with the coexistence of 4G/LTE networks, provides mobile devices a diverse set of candidate cells to connect to. However, associating mobile devices to cells to maximize overall network performance, a.k.a. cell (re)selection, remains a key challenge for mobile operators. Today, cell (re)selection parameters are typically configured manually based on operator experience and rarely adapted to dynamic network conditions. In this work, we ask: Can an agent automatically learn and adapt cell (re)selection parameters to consistently improve network performance? We present a reinforcement learning (RL)-based framework called CellPilot that adaptively tunes cell (re)selection parameters by learning spatiotemporal patterns of mobile network dynamics. Our study with real-world data demonstrates that even a lightweight RL agent can outperform conventional heuristic reconfigurations by up to 167%, while generalizing effectively across different network scenarios. These results indicate that data-driven approaches can significantly improve cell (re)selection configurations and enhance mobile network performance.

