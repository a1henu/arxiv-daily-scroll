---
layout: default
title: Attention-Based SINR Estimation in User-Centric Non-Terrestrial Networks
---

# Attention-Based SINR Estimation in User-Centric Non-Terrestrial Networks
**arXiv**：[2602.21116v1](https://arxiv.org/abs/2602.21116) · [PDF](https://arxiv.org/pdf/2602.21116.pdf)  
**作者**：Bruno De Filippo, Alessandro Guidotti, Alessandro Vanelli-Coralli  

**一句话要点**：提出基于多头自注意力的低复杂度SINR估计框架，用于用户中心非地面网络

**关键词**：非地面网络, SINR估计, 多头自注意力, 用户中心波束赋形, 低复杂度算法

## 3 点简述
- 核心问题：SINR估计在卫星NTN中需专用导频或高计算开销的MMSE计算
- 方法要点：利用多头自注意力从信道状态信息或用户位置报告提取干扰特征
- 实验或效果：计算复杂度降低3倍至两个数量级，均方根误差通常低于1 dB

## 摘要（原文）

> The signal-to-interference-plus-noise ratio (SINR) is central to performance optimization in user-centric beamforming for satellite-based non-terrestrial networks (NTNs). Its assessment either requires the transmission of dedicated pilots or relies on computing the beamforming matrix through minimum mean squared error (MMSE)-based formulations beforehand, a process that introduces significant computational overhead. In this paper, we propose a low-complexity SINR estimation framework that leverages multi-head self-attention (MHSA) to extract inter-user interference features directly from either channel state information or user location reports. The proposed dual MHSA (DMHSA) models evaluate the SINR of a scheduled user group without requiring explicit MMSE calculations. The architecture achieves a computational complexity reduction by a factor of three in the CSI-based setting and by two orders of magnitude in the location-based configuration, the latter benefiting from the lower dimensionality of user reports. We show that both DMHSA models maintain high estimation accuracy, with the root mean squared error typically below 1 dB with priority-queuing-based scheduled users. These results enable the integration of DMHSA-based estimators into scheduling procedures, allowing the evaluation of multiple candidate user groups and the selection of those offering the highest average SINR and capacity.

