---
layout: default
title: Distributionally Robust Imitation Learning: Layered Control Architecture for Certifiable Autonomy
---

# Distributionally Robust Imitation Learning: Layered Control Architecture for Certifiable Autonomy
**arXiv**：[2512.17899v1](https://arxiv.org/abs/2512.17899) · [PDF](https://arxiv.org/pdf/2512.17899.pdf)  
**作者**：Aditya Gahlawat, Ahmed Aboudonia, Sandeep Banik, Naira Hovakimyan, Nikolai Matni, Aaron D. Ames, Gioele Zardini, Alberto Speranzon  

**一句话要点**：提出分布鲁棒模仿学习架构以解决动态系统中模仿学习的分布偏移认证问题

**关键词**：模仿学习, 分布鲁棒性, 分层控制架构, 认证自主性, 动态系统, 控制理论

## 3 点简述
- 模仿学习对分布偏移敏感，包括策略误差和不确定性引起的偏移
- 整合TaSIL和ℓ1-DRAC方法，构建分层控制架构以互补应对不同偏移源
- 通过分层设计保证整个控制流程的认证，支持可认证自主系统

## 摘要（原文）

> Imitation learning (IL) enables autonomous behavior by learning from expert demonstrations. While more sample-efficient than comparative alternatives like reinforcement learning, IL is sensitive to compounding errors induced by distribution shifts. There are two significant sources of distribution shifts when using IL-based feedback laws on systems: distribution shifts caused by policy error and distribution shifts due to exogenous disturbances and endogenous model errors due to lack of learning. Our previously developed approaches, Taylor Series Imitation Learning (TaSIL) and $\mathcal{L}_1$ -Distributionally Robust Adaptive Control (\ellonedrac), address the challenge of distribution shifts in complementary ways. While TaSIL offers robustness against policy error-induced distribution shifts, \ellonedrac offers robustness against distribution shifts due to aleatoric and epistemic uncertainties. To enable certifiable IL for learned and/or uncertain dynamical systems, we formulate \textit{Distributionally Robust Imitation Policy (DRIP)} architecture, a Layered Control Architecture (LCA) that integrates TaSIL and~\ellonedrac. By judiciously designing individual layer-centric input and output requirements, we show how we can guarantee certificates for the entire control pipeline. Our solution paves the path for designing fully certifiable autonomy pipelines, by integrating learning-based components, such as perception, with certifiable model-based decision-making through the proposed LCA approach.

