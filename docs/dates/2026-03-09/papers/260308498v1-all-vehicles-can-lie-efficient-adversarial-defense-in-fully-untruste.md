---
layout: default
title: All Vehicles Can Lie: Efficient Adversarial Defense in Fully Untrusted-Vehicle Collaborative Perception via Pseudo-Random Bayesian Inference
---

# All Vehicles Can Lie: Efficient Adversarial Defense in Fully Untrusted-Vehicle Collaborative Perception via Pseudo-Random Bayesian Inference
**arXiv**：[2603.08498v1](https://arxiv.org/abs/2603.08498) · [PDF](https://arxiv.org/pdf/2603.08498.pdf)  
**作者**：Yi Yu, Libing Wu, Zhuangzhuang Zhang, Jing Qiu, Lijuan Huo, Jiaqi Feng  

**一句话要点**：提出伪随机贝叶斯推断框架，以高效防御全不可信车辆协同感知中的对抗攻击。

**关键词**：协同感知, 对抗防御, 贝叶斯推断, 伪随机分组, 时序感知, 全不可信环境

## 3 点简述
- 核心问题：全不可信车辆协同感知易受对抗攻击，现有防御方法假设可信自车或需额外分类器，实用性受限。
- 方法要点：利用时序感知差异，以前一帧可靠感知为动态参考，结合伪随机分组和贝叶斯推断检测恶意车辆。
- 实验或效果：平均每帧仅需2.5次验证，显著优于现有方法，检测精度恢复至攻击前水平的79.4%至86.9%。

## 摘要（原文）

> Collaborative perception (CP) enables multiple vehicles to augment their individual perception capacities through the exchange of feature-level sensory data. However, this fusion mechanism is inherently vulnerable to adversarial attacks, especially in fully untrusted-vehicle environments. Existing defense approaches often assume a trusted ego vehicle as a reference or incorporate additional binary classifiers. These assumptions limit their practicality in real-world deployments due to the questionable trustworthiness of ego vehicles, the requirement for real-time detection, and the need for generalizability across diverse scenarios. To address these challenges, we propose a novel Pseudo-Random Bayesian Inference (PRBI) framework, a first efficient defense method tailored for fully untrusted-vehicle CP. PRBI detects adversarial behavior by leveraging temporal perceptual discrepancies, using the reliable perception from the preceding frame as a dynamic reference. Additionally, it employs a pseudo-random grouping strategy that requires only two verifications per frame, while applying Bayesian inference to estimate both the number and identities of malicious vehicles. Theoretical analysis has proven the convergence and stability of the proposed PRBI framework. Extensive experiments show that PRBI requires only 2.5 verifications per frame on average, outperforming existing methods significantly, and restores detection precision to between 79.4% and 86.9% of pre-attack levels.

