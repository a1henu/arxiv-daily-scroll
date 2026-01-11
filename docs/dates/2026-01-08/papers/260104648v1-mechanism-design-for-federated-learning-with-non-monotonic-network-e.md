---
layout: default
title: Mechanism Design for Federated Learning with Non-Monotonic Network Effects
---

# Mechanism Design for Federated Learning with Non-Monotonic Network Effects
**arXiv**：[2601.04648v1](https://arxiv.org/abs/2601.04648) · [PDF](https://arxiv.org/pdf/2601.04648.pdf)  
**作者**：Xiang Li, Bing Luo, Jianwei Huang, Yuan Luo  

**一句话要点**：提出SWAN机制以解决联邦学习中非单调网络效应和特定应用性能需求的激励问题

**关键词**：联邦学习, 机制设计, 网络效应, 社会福利优化, 模型交易, 激励兼容

## 3 点简述
- 核心问题：现有联邦学习机制忽略网络效应和模型性能的多样化应用需求，导致激励不足和社会福利低下
- 方法要点：基于非单调网络效应理论模型，设计MoTS框架和SWAN机制，通过模型交易和客户支付优化激励
- 实验或效果：硬件原型实验显示，SWAN机制提升社会福利高达352.42%，减少额外激励成本93.07%

## 摘要（原文）

> Mechanism design is pivotal to federated learning (FL) for maximizing social welfare by coordinating self-interested clients. Existing mechanisms, however, often overlook the network effects of client participation and the diverse model performance requirements (i.e., generalization error) across applications, leading to suboptimal incentives and social welfare, or even inapplicability in real deployments. To address this gap, we explore incentive mechanism design for FL with network effects and application-specific requirements of model performance. We develop a theoretical model to quantify the impact of network effects on heterogeneous client participation, revealing the non-monotonic nature of such effects. Based on these insights, we propose a Model Trading and Sharing (MoTS) framework, which enables clients to obtain FL models through either participation or purchase. To further address clients' strategic behaviors, we design a Social Welfare maximization with Application-aware and Network effects (SWAN) mechanism, exploiting model customer payments for incentivization. Experimental results on a hardware prototype demonstrate that our SWAN mechanism outperforms existing FL mechanisms, improving social welfare by up to $352.42\%$ and reducing extra incentive costs by $93.07\%$.

