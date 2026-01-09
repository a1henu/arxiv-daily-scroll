---
layout: default
title: Timeliness-Oriented Scheduling and Resource Allocation in Multi-Region Collaborative Perception
---

# Timeliness-Oriented Scheduling and Resource Allocation in Multi-Region Collaborative Perception
**arXiv**：[2601.04542v1](https://arxiv.org/abs/2601.04542) · [PDF](https://arxiv.org/pdf/2601.04542.pdf)  
**作者**：Mengmeng Zhu, Yuxuan Sun, Yukuan Jia, Wei Chen, Bo Ai, Sheng Zhou  

**一句话要点**：提出TAMP调度算法以优化多区域协同感知中的时效性与资源分配

**关键词**：协同感知, 时效性调度, 资源分配, 多区域协作, Lyapunov优化, 感知性能优化

## 3 点简述
- 核心问题：协同感知中信息时效性差与通信资源有限影响感知性能
- 方法要点：基于Lyapunov优化，设计时效感知的调度策略平衡精度与资源成本
- 实验或效果：在真实数据集上验证，AP提升最高达27%，优于基线方法

## 摘要（原文）

> Collaborative perception (CP) is a critical technology in applications like autonomous driving and smart cities. It involves the sharing and fusion of information among sensors to overcome the limitations of individual perception, such as blind spots and range limitations. However, CP faces two primary challenges. First, due to the dynamic nature of the environment, the timeliness of the transmitted information is critical to perception performance. Second, with limited computational power at the sensors and constrained wireless bandwidth, the communication volume must be carefully designed to ensure feature representations are both effective and sufficient. This work studies the dynamic scheduling problem in a multi-region CP scenario, and presents a Timeliness-Aware Multi-region Prioritized (TAMP) scheduling algorithm to trade-off perception accuracy and communication resource usage. Timeliness reflects the utility of information that decays as time elapses, which is manifested by the perception performance in CP tasks. We propose an empirical penalty function that maps the joint impact of Age of Information (AoI) and communication volume to perception performance. Aiming to minimize this timeliness-oriented penalty in the long-term, and recognizing that scheduling decisions have a cumulative effect on subsequent system states, we propose the TAMP scheduling algorithm. TAMP is a Lyapunov-based optimization policy that decomposes the long-term average objective into a per-slot prioritization problem, balancing the scheduling worth against resource cost. We validate our algorithm in both intersection and corridor scenarios with the real-world Roadside Cooperative perception (RCooper) dataset. Extensive simulations demonstrate that TAMP outperforms the best-performing baseline, achieving an Average Precision (AP) improvement of up to 27% across various configurations.

