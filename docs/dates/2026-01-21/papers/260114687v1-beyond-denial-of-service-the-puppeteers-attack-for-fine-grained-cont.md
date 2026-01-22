---
layout: default
title: Beyond Denial-of-Service: The Puppeteer's Attack for Fine-Grained Control in Ranking-Based Federated Learning
---

# Beyond Denial-of-Service: The Puppeteer's Attack for Fine-Grained Control in Ranking-Based Federated Learning
**arXiv**：[2601.14687v1](https://arxiv.org/abs/2601.14687) · [PDF](https://arxiv.org/pdf/2601.14687.pdf)  
**作者**：Zhihao Chen, Zirui Gong, Jianting Ning, Yanjun Zhang, Leo Yu Zhang  

**一句话要点**：提出边缘控制攻击以揭示基于排名的联邦学习中的细粒度控制漏洞

**关键词**：联邦学习, 模型中毒攻击, 排名学习, 细粒度控制, 拜占庭鲁棒性, 安全漏洞

## 3 点简述
- 联邦排名学习因离散排名更新机制被认为抗模型中毒攻击，但本文揭示其仍存在细粒度控制攻击漏洞
- 提出边缘控制攻击，通过操纵上升和下降边缘及扩大选择边界间隙，精确控制目标模型精度
- 在七个基准数据集和九种拜占庭鲁棒聚合规则上实验，攻击平均误差仅0.224%，优于基线达17倍

## 摘要（原文）

> Federated Rank Learning (FRL) is a promising Federated Learning (FL) paradigm designed to be resilient against model poisoning attacks due to its discrete, ranking-based update mechanism. Unlike traditional FL methods that rely on model updates, FRL leverages discrete rankings as a communication parameter between clients and the server. This approach significantly reduces communication costs and limits an adversary's ability to scale or optimize malicious updates in the continuous space, thereby enhancing its robustness. This makes FRL particularly appealing for applications where system security and data privacy are crucial, such as web-based auction and bidding platforms. While FRL substantially reduces the attack surface, we demonstrate that it remains vulnerable to a new class of local model poisoning attack, i.e., fine-grained control attacks. We introduce the Edge Control Attack (ECA), the first fine-grained control attack tailored to ranking-based FL frameworks. Unlike conventional denial-of-service (DoS) attacks that cause conspicuous disruptions, ECA enables an adversary to precisely degrade a competitor's accuracy to any target level while maintaining a normal-looking convergence trajectory, thereby avoiding detection. ECA operates in two stages: (i) identifying and manipulating Ascending and Descending Edges to align the global model with the target model, and (ii) widening the selection boundary gap to stabilize the global model at the target accuracy. Extensive experiments across seven benchmark datasets and nine Byzantine-robust aggregation rules (AGRs) show that ECA achieves fine-grained accuracy control with an average error of only 0.224%, outperforming the baseline by up to 17x. Our findings highlight the need for stronger defenses against advanced poisoning attacks. Our code is available at: https://github.com/Chenzh0205/ECA

