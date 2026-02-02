---
layout: default
title: FedCARE: Federated Unlearning with Conflict-Aware Projection and Relearning-Resistant Recovery
---

# FedCARE: Federated Unlearning with Conflict-Aware Projection and Relearning-Resistant Recovery
**arXiv**：[2601.22589v1](https://arxiv.org/abs/2601.22589) · [PDF](https://arxiv.org/pdf/2601.22589.pdf)  
**作者**：Yue Li, Mingmin Chu, Xilei Yang, Da Xiao, Ziqi Xu, Wei Shao, Qipeng Song, Hui Li  

**一句话要点**：提出FedCARE框架以解决联邦学习中高效遗忘与恢复时知识回滚的问题

**关键词**：联邦学习, 联邦遗忘, 梯度上升, 模型反演, 冲突感知, 抗重学恢复

## 3 点简述
- 核心问题：现有联邦遗忘方法存在高开销、效用下降和恢复时无意重学问题
- 方法要点：利用梯度上升和模型反演实现冲突感知遗忘与抗重学恢复
- 实验或效果：在多种数据集和模型上验证了有效遗忘、效用保持和降低重学风险

## 摘要（原文）

> Federated learning (FL) enables collaborative model training without centralizing raw data, but privacy regulations such as the right to be forgotten require FL systems to remove the influence of previously used training data upon request. Retraining a federated model from scratch is prohibitively expensive, motivating federated unlearning (FU). However, existing FU methods suffer from high unlearning overhead, utility degradation caused by entangled knowledge, and unintended relearning during post-unlearning recovery. In this paper, we propose FedCARE, a unified and low overhead FU framework that enables conflict-aware unlearning and relearning-resistant recovery. FedCARE leverages gradient ascent for efficient forgetting when target data are locally available and employs data free model inversion to construct class level proxies of shared knowledge. Based on these insights, FedCARE integrates a pseudo-sample generator, conflict-aware projected gradient ascent for utility preserving unlearning, and a recovery strategy that suppresses rollback toward the pre-unlearning model. FedCARE supports client, instance, and class level unlearning with modest overhead. Extensive experiments on multiple datasets and model architectures under both IID and non-IID settings show that FedCARE achieves effective forgetting, improved utility retention, and reduced relearning risk compared to state of the art FU baselines.

