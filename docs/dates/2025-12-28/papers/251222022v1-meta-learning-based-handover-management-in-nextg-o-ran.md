---
layout: default
title: Meta-Learning-Based Handover Management in NextG O-RAN
---

# Meta-Learning-Based Handover Management in NextG O-RAN
**arXiv**：[2512.22022v1](https://arxiv.org/abs/2512.22022) · [PDF](https://arxiv.org/pdf/2512.22022.pdf)  
**作者**：Michail Kalntis, George Iosifidis, José Suárez-Varela, Andra Lutu, Fernando A. Kuipers  

**一句话要点**：提出CONTRA框架以优化下一代O-RAN中的切换管理

**关键词**：切换管理, O-RAN, 元学习, 条件切换, 移动网络优化, 6G控制

## 3 点简述
- 传统和条件切换在密集部署中存在失败和延迟问题，需自适应控制
- CONTRA首次在O-RAN中联合优化两种切换类型，采用元学习算法适应实时观测
- 基于真实数据集评估，CONTRA提升用户吞吐量并降低切换成本，优于基准方法

## 摘要（原文）

> While traditional handovers (THOs) have served as a backbone for mobile connectivity, they increasingly suffer from failures and delays, especially in dense deployments and high-frequency bands. To address these limitations, 3GPP introduced Conditional Handovers (CHOs) that enable proactive cell reservations and user-driven execution. However, both handover (HO) types present intricate trade-offs in signaling, resource usage, and reliability. This paper presents unique, countrywide mobility management datasets from a top-tier mobile network operator (MNO) that offer fresh insights into these issues and call for adaptive and robust HO control in next-generation networks. Motivated by these findings, we propose CONTRA, a framework that, for the first time, jointly optimizes THOs and CHOs within the O-RAN architecture. We study two variants of CONTRA: one where users are a priori assigned to one of the HO types, reflecting distinct service or user-specific requirements, as well as a more dynamic formulation where the controller decides on-the-fly the HO type, based on system conditions and needs. To this end, it relies on a practical meta-learning algorithm that adapts to runtime observations and guarantees performance comparable to an oracle with perfect future information (universal no-regret). CONTRA is specifically designed for near-real-time deployment as an O-RAN xApp and aligns with the 6G goals of flexible and intelligent control. Extensive evaluations leveraging crowdsourced datasets show that CONTRA improves user throughput and reduces both THO and CHO switching costs, outperforming 3GPP-compliant and Reinforcement Learning (RL) baselines in dynamic and real-world scenarios.

