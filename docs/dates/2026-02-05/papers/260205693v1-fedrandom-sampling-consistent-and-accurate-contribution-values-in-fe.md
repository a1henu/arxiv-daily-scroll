---
layout: default
title: FedRandom: Sampling Consistent and Accurate Contribution Values in Federated Learning
---

# FedRandom: Sampling Consistent and Accurate Contribution Values in Federated Learning
**arXiv**：[2602.05693v1](https://arxiv.org/abs/2602.05693) · [PDF](https://arxiv.org/pdf/2602.05693.pdf)  
**作者**：Arno Geimer, Beltran Fiz Pontiveros, Radu State  

**一句话要点**：提出FedRandom以解决联邦学习中贡献评估的不稳定性问题

**关键词**：联邦学习, 贡献评估, 稳定性优化, 统计估计, 隐私保护机器学习

## 3 点简述
- 核心问题：联邦学习中参与者贡献评估存在固有高不稳定性，影响公平性和参与意愿
- 方法要点：将不稳定性视为统计估计问题，通过生成更多样本来提高评估的一致性和可靠性
- 实验或效果：在多个数据集上测试，FedRandom在多数场景中显著减少与真实贡献的距离并提升稳定性

## 摘要（原文）

> Federated Learning is a privacy-preserving decentralized approach for Machine Learning tasks. In industry deployments characterized by a limited number of entities possessing abundant data, the significance of a participant's role in shaping the global model becomes pivotal given that participation in a federation incurs costs, and participants may expect compensation for their involvement. Additionally, the contributions of participants serve as a crucial means to identify and address potential malicious actors and free-riders. However, fairly assessing individual contributions remains a significant hurdle. Recent works have demonstrated a considerable inherent instability in contribution estimations across aggregation strategies. While employing a different strategy may offer convergence benefits, this instability can have potentially harming effects on the willingness of participants in engaging in the federation. In this work, we introduce FedRandom, a novel mitigation technique to the contribution instability problem. Tackling the instability as a statistical estimation problem, FedRandom allows us to generate more samples than when using regular FL strategies. We show that these additional samples provide a more consistent and reliable evaluation of participant contributions. We demonstrate our approach using different data distributions across CIFAR-10, MNIST, CIFAR-100 and FMNIST and show that FedRandom reduces the overall distance to the ground truth by more than a third in half of all evaluated scenarios, and improves stability in more than 90% of cases.

