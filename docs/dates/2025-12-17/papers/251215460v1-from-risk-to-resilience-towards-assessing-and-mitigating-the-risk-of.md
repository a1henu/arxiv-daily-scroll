---
layout: default
title: From Risk to Resilience: Towards Assessing and Mitigating the Risk of Data Reconstruction Attacks in Federated Learning
---

# From Risk to Resilience: Towards Assessing and Mitigating the Risk of Data Reconstruction Attacks in Federated Learning
**arXiv**：[2512.15460v1](https://arxiv.org/abs/2512.15460) · [PDF](https://arxiv.org/pdf/2512.15460.pdf)  
**作者**：Xiangrui Xu, Zhize Li, Yufei Han, Bin Wang, Jiqiang Liu, Wei Wang  

**一句话要点**：提出可逆性损失以量化联邦学习中数据重构攻击风险，并开发风险估计器与防御方法。

**关键词**：联邦学习, 数据重构攻击, 风险量化, 可逆性损失, 隐私防御, 雅可比矩阵

## 3 点简述
- 核心问题：缺乏理论框架量化联邦学习中数据重构攻击风险，阻碍风险评估与缓解。
- 方法要点：引入可逆性损失量化攻击最大效果，基于雅可比矩阵谱性质统一解释防御机制。
- 实验或效果：在真实数据集上验证框架，实现系统化风险评估与自适应噪声防御，保持分类精度。

## 摘要（原文）

> Data Reconstruction Attacks (DRA) pose a significant threat to Federated Learning (FL) systems by enabling adversaries to infer sensitive training data from local clients. Despite extensive research, the question of how to characterize and assess the risk of DRAs in FL systems remains unresolved due to the lack of a theoretically-grounded risk quantification framework. In this work, we address this gap by introducing Invertibility Loss (InvLoss) to quantify the maximum achievable effectiveness of DRAs for a given data instance and FL model. We derive a tight and computable upper bound for InvLoss and explore its implications from three perspectives. First, we show that DRA risk is governed by the spectral properties of the Jacobian matrix of exchanged model updates or feature embeddings, providing a unified explanation for the effectiveness of defense methods. Second, we develop InvRE, an InvLoss-based DRA risk estimator that offers attack method-agnostic, comprehensive risk evaluation across data instances and model architectures. Third, we propose two adaptive noise perturbation defenses that enhance FL privacy without harming classification accuracy. Extensive experiments on real-world datasets validate our framework, demonstrating its potential for systematic DRA risk evaluation and mitigation in FL systems.

