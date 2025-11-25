---
layout: default
title: FedPoisonTTP: A Threat Model and Poisoning Attack for Federated Test-Time Personalization
---

# FedPoisonTTP: A Threat Model and Poisoning Attack for Federated Test-Time Personalization
**arXiv**：[2511.19248v1](https://arxiv.org/abs/2511.19248) · [PDF](https://arxiv.org/pdf/2511.19248.pdf)  
**作者**：Md Akil Raihan Iftee, Syed Md. Ahnaf Hasan, Amin Ahsan Ali, AKM Mahbubur Rahman, Sajib Mistry, Aneesh Krishna  

**一句话要点**：提出FedPoisonTTP威胁模型与攻击方法，以解决联邦测试时个性化中的安全风险

**关键词**：联邦学习, 测试时个性化, 中毒攻击, 威胁模型, 对抗性更新, 安全漏洞

## 3 点简述
- 核心问题：联邦测试时个性化中，本地适应易受中毒攻击，威胁全局与客户端性能
- 方法要点：利用代理模型蒸馏和特征一致性合成中毒输入，优化攻击目标以规避过滤
- 实验或效果：在视觉基准测试中，中毒攻击显著降低测试时性能

## 摘要（原文）

> Test-time personalization in federated learning enables models at clients to adjust online to local domain shifts, enhancing robustness and personalization in deployment. Yet, existing federated learning work largely overlooks the security risks that arise when local adaptation occurs at test time. Heterogeneous domain arrivals, diverse adaptation algorithms, and limited cross-client visibility create vulnerabilities where compromised participants can craft poisoned inputs and submit adversarial updates that undermine both global and per-client performance. To address this threat, we introduce FedPoisonTTP, a realistic grey-box attack framework that explores test-time data poisoning in the federated adaptation setting. FedPoisonTTP distills a surrogate model from adversarial queries, synthesizes in-distribution poisons using feature-consistency, and optimizes attack objectives to generate high-entropy or class-confident poisons that evade common adaptation filters. These poisons are injected during local adaptation and spread through collaborative updates, leading to broad degradation. Extensive experiments on corrupted vision benchmarks show that compromised participants can substantially diminish overall test-time performance.

