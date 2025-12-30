---
layout: default
title: Joint Link Adaptation and Device Scheduling Approach for URLLC Industrial IoT Network: A DRL-based Method with Bayesian Optimization
---

# Joint Link Adaptation and Device Scheduling Approach for URLLC Industrial IoT Network: A DRL-based Method with Bayesian Optimization
**arXiv**：[2512.23493v1](https://arxiv.org/abs/2512.23493) · [PDF](https://arxiv.org/pdf/2512.23493.pdf)  
**作者**：Wei Gao, Paul Zheng, Peng Wu, Yulin Hu, Anke Schmeink  

**一句话要点**：提出基于贝叶斯优化的TD3方法，以解决URLLC工业物联网中联合链路适应与设备调度的优化问题。

**关键词**：URLLC工业物联网, 联合链路适应与设备调度, 深度强化学习, 贝叶斯优化, TD3算法, 信道状态信息不完美

## 3 点简述
- 核心问题：在CSI不完美的URLLC工业物联网中，联合优化链路适应和设备调度以最大化总传输速率。
- 方法要点：采用贝叶斯优化驱动的TD3算法，自适应确定设备服务顺序和MCS，并改进训练机制以提升收敛速度。
- 实验或效果：通过仿真验证，算法相比现有方案实现更快收敛和更高总速率性能。

## 摘要（原文）

> In this article, we consider an industrial internet of things (IIoT) network supporting multi-device dynamic ultra-reliable low-latency communication (URLLC) while the channel state information (CSI) is imperfect. A joint link adaptation (LA) and device scheduling (including the order) design is provided, aiming at maximizing the total transmission rate under strict block error rate (BLER) constraints. In particular, a Bayesian optimization (BO) driven Twin Delayed Deep Deterministic Policy Gradient (TD3) method is proposed, which determines the device served order sequence and the corresponding modulation and coding scheme (MCS) adaptively based on the imperfect CSI. Note that the imperfection of CSI, error sample imbalance in URLLC networks, as well as the parameter sensitivity nature of the TD3 algorithm likely diminish the algorithm's convergence speed and reliability. To address such an issue, we proposed a BO based training mechanism for the convergence speed improvement, which provides a more reliable learning direction and sample selection method to track the imbalance sample problem. Via extensive simulations, we show that the proposed algorithm achieves faster convergence and higher sum-rate performance compared to existing solutions.

