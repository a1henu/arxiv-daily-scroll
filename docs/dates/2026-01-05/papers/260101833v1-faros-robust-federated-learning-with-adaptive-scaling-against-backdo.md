---
layout: default
title: FAROS: Robust Federated Learning with Adaptive Scaling against Backdoor Attacks
---

# FAROS: Robust Federated Learning with Adaptive Scaling against Backdoor Attacks
**arXiv**：[2601.01833v1](https://arxiv.org/abs/2601.01833) · [PDF](https://arxiv.org/pdf/2601.01833.pdf)  
**作者**：Chenyu Hu, Qiming Hu, Sinan Chen, Nianyu Li, Mingyue Zhang, Jialong Li  

**一句话要点**：提出FAROS框架，通过自适应缩放和核心集计算增强联邦学习对后门攻击的鲁棒性。

**关键词**：联邦学习, 后门攻击防御, 自适应缩放, 鲁棒核心集, 梯度分析, 模型安全

## 3 点简述
- 联邦学习中后门攻击威胁严重，现有防御依赖固定参数易受单点故障影响。
- FAROS引入自适应差分缩放和鲁棒核心集计算，动态调整防御敏感度并降低单点故障风险。
- 实验表明，FAROS在多种数据集和攻击场景下优于现有防御，提升主任务精度并降低攻击成功率。

## 摘要（原文）

> Federated Learning (FL) enables multiple clients to collaboratively train a shared model without exposing local data. However, backdoor attacks pose a significant threat to FL. These attacks aim to implant a stealthy trigger into the global model, causing it to mislead on inputs that possess a specific trigger while functioning normally on benign data. Although pre-aggregation detection is a main defense direction, existing state-of-the-art defenses often rely on fixed defense parameters. This reliance makes them vulnerable to single-point-of-failure risks, rendering them less effective against sophisticated attackers. To address these limitations, we propose FAROS, an enhanced FL framework that incorporates Adaptive Differential Scaling (ADS) and Robust Core-set Computing (RCC). The ADS mechanism adjusts the defense's sensitivity dynamically, based on the dispersion of uploaded gradients by clients in each round. This allows it to counter attackers who strategically shift between stealthiness and effectiveness. Furthermore, the RCC effectively mitigates the risk of single-point failure by computing the centroid of a core set comprising clients with the highest confidence. We conducted extensive experiments across various datasets, models, and attack scenarios. The results demonstrate that our method outperforms current defenses in both attack success rate and main task accuracy.

