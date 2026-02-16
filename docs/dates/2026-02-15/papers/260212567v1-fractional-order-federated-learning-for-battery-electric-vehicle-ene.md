---
layout: default
title: Fractional Order Federated Learning for Battery Electric Vehicle Energy Consumption Modeling
---

# Fractional Order Federated Learning for Battery Electric Vehicle Energy Consumption Modeling
**arXiv**：[2602.12567v1](https://arxiv.org/abs/2602.12567) · [PDF](https://arxiv.org/pdf/2602.12567.pdf)  
**作者**：Mohammad Partohaghighi, Roummel Marcia, Bruce J. West, YangQuan Chen  

**一句话要点**：提出分数阶粗糙度感知联邦平均方法，以提升电动汽车能耗建模的稳定性。

**关键词**：联邦学习, 电动汽车能耗建模, 分数阶优化, 粗糙度感知正则化, 稳定性提升

## 3 点简述
- 核心问题：电动汽车联邦学习面临间歇连接和客户端差异导致的稳定性挑战。
- 方法要点：结合自适应粗糙度感知正则化和分数阶优化，平滑更新方向。
- 实验或效果：在真实数据集上实现更高精度和更稳定收敛，尤其在低参与度下。

## 摘要（原文）

> Federated learning on connected electric vehicles (BEVs) faces severe instability due to intermittent connectivity, time-varying client participation, and pronounced client-to-client variation induced by diverse operating conditions. Conventional FedAvg and many advanced methods can suffer from excessive drift and degraded convergence under these realistic constraints. This work introduces Fractional-Order Roughness-Informed Federated Averaging (FO-RI-FedAvg), a lightweight and modular extension of FedAvg that improves stability through two complementary client-side mechanisms: (i) adaptive roughness-informed proximal regularization, which dynamically tunes the pull toward the global model based on local loss-landscape roughness, and (ii) non-integer-order local optimization, which incorporates short-term memory to smooth conflicting update directions. The approach preserves standard FedAvg server aggregation, adds only element-wise operations with amortizable overhead, and allows independent toggling of each component. Experiments on two real-world BEV energy prediction datasets, VED and its extended version eVED, show that FO-RI-FedAvg achieves improved accuracy and more stable convergence compared to strong federated baselines, particularly under reduced client participation.

