---
layout: default
title: FairGU: Fairness-aware Graph Unlearning in Social Network
---

# FairGU: Fairness-aware Graph Unlearning in Social Network
**arXiv**：[2601.09469v1](https://arxiv.org/abs/2601.09469) · [PDF](https://arxiv.org/pdf/2601.09469.pdf)  
**作者**：Renqiang Luo, Yongshuai Yang, Huafei Huang, Qing Qing, Mingliang Hou, Ziqi Xu, Yi Yu, Jingjing Zhou, Feng Xia  

**一句话要点**：提出FairGU框架以解决社交网络中图遗忘技术公平性不足的问题

**关键词**：图遗忘, 公平性增强, 社交网络, 数据保护, 算法公平

## 3 点简述
- 现有图遗忘技术保护敏感属性不足，导致算法公平性下降
- FairGU集成公平感知模块与数据保护策略，平衡效用与公平
- 在多个真实数据集上验证，FairGU在准确性和公平性指标上优于现有方法

## 摘要（原文）

> Graph unlearning has emerged as a critical mechanism for supporting sustainable and privacy-preserving social networks, enabling models to remove the influence of deleted nodes and thereby better safeguard user information. However, we observe that existing graph unlearning techniques insufficiently protect sensitive attributes, often leading to degraded algorithmic fairness compared with traditional graph learning methods. To address this gap, we introduce FairGU, a fairness-aware graph unlearning framework designed to preserve both utility and fairness during the unlearning process. FairGU integrates a dedicated fairness-aware module with effective data protection strategies, ensuring that sensitive attributes are neither inadvertently amplified nor structurally exposed when nodes are removed. Through extensive experiments on multiple real-world datasets, we demonstrate that FairGU consistently outperforms state-of-the-art graph unlearning methods and fairness-enhanced graph learning baselines in terms of both accuracy and fairness metrics. Our findings highlight a previously overlooked risk in current unlearning practices and establish FairGU as a robust and equitable solution for the next generation of socially sustainable networked systems. The codes are available at https://github.com/LuoRenqiang/FairGU.

