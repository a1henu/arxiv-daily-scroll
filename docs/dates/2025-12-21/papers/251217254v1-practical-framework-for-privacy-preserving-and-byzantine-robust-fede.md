---
layout: default
title: Practical Framework for Privacy-Preserving and Byzantine-robust Federated Learning
---

# Practical Framework for Privacy-Preserving and Byzantine-robust Federated Learning
**arXiv**：[2512.17254v1](https://arxiv.org/abs/2512.17254) · [PDF](https://arxiv.org/pdf/2512.17254.pdf)  
**作者**：Baolei Zhang, Minghong Fang, Zhuqing Liu, Biao Yi, Peizhao Zhou, Yuan Wang, Tong Li, Zheli Liu  

**一句话要点**：提出ABBR框架以解决联邦学习中隐私保护与拜占庭鲁棒性的实践效率问题

**关键词**：联邦学习, 隐私保护, 拜占庭鲁棒性, 降维加速, 自适应调优, 计算效率

## 3 点简述
- 核心问题：联邦学习易受拜占庭攻击和隐私推断攻击，现有防御方法计算与通信开销大
- 方法要点：首次利用降维加速隐私保护计算，并引入自适应调优策略最小化恶意模型影响
- 实验或效果：在公共数据集上评估，ABBR运行更快、通信开销小，拜占庭鲁棒性接近基线

## 摘要（原文）

> Federated Learning (FL) allows multiple clients to collaboratively train a model without sharing their private data. However, FL is vulnerable to Byzantine attacks, where adversaries manipulate client models to compromise the federated model, and privacy inference attacks, where adversaries exploit client models to infer private data. Existing defenses against both backdoor and privacy inference attacks introduce significant computational and communication overhead, creating a gap between theory and practice. To address this, we propose ABBR, a practical framework for Byzantine-robust and privacy-preserving FL. We are the first to utilize dimensionality reduction to speed up the private computation of complex filtering rules in privacy-preserving FL. Additionally, we analyze the accuracy loss of vector-wise filtering in low-dimensional space and introduce an adaptive tuning strategy to minimize the impact of malicious models that bypass filtering on the global model. We implement ABBR with state-of-the-art Byzantine-robust aggregation rules and evaluate it on public datasets, showing that it runs significantly faster, has minimal communication overhead, and maintains nearly the same Byzantine-resilience as the baselines.

