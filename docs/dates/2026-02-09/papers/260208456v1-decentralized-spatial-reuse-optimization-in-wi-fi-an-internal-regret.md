---
layout: default
title: Decentralized Spatial Reuse Optimization in Wi-Fi: An Internal Regret Minimization Approach
---

# Decentralized Spatial Reuse Optimization in Wi-Fi: An Internal Regret Minimization Approach
**arXiv**：[2602.08456v1](https://arxiv.org/abs/2602.08456) · [PDF](https://arxiv.org/pdf/2602.08456.pdf)  
**作者**：Francesc Wilhelmi, Boris Bellalta, Miguel Casasnovas, Aleksandra Kijanka, Miguel Calvo-Fullana  

**一句话要点**：提出基于内部遗憾最小化的去中心化学习算法，以优化Wi-Fi空间复用参数。

**关键词**：Wi-Fi空间复用, 去中心化优化, 内部遗憾最小化, 相关均衡, 多代理学习, 频谱效率

## 3 点简述
- 核心问题：去中心化优化Wi-Fi空间复用参数（传输功率和载波侦听阈值）面临非平稳环境和次优全局配置挑战。
- 方法要点：采用内部遗憾最小化算法，引导竞争代理向相关均衡收敛，无需显式通信。
- 实验或效果：仿真结果显示该方法达到近最优全局性能，优于传统自私方法。

## 摘要（原文）

> Spatial Reuse (SR) is a cost-effective technique for improving spectral efficiency in dense IEEE 802.11 deployments by enabling simultaneous transmissions. However, the decentralized optimization of SR parameters -- transmission power and Carrier Sensing Threshold (CST) -- across different Basic Service Sets (BSSs) is challenging due to the lack of global state information. In addition, the concurrent operation of multiple agents creates a highly non-stationary environment, often resulting in suboptimal global configurations (e.g., using the maximum possible transmission power by default). To overcome these limitations, this paper introduces a decentralized learning algorithm based on regret-matching, grounded in internal regret minimization. Unlike standard decentralized ``selfish'' approaches that often converge to inefficient Nash Equilibria (NE), internal regret minimization guides competing agents toward Correlated Equilibria (CE), effectively mimicking coordination without explicit communication. Through simulation results, we showcase the superiority of our proposed approach and its ability to reach near-optimal global performance. These results confirm the not-yet-unleashed potential of scalable decentralized solutions and question the need for the heavy signaling overheads and architectural complexity associated with emerging centralized solutions like Multi-Access Point Coordination (MAPC).

