---
layout: default
title: Balancing Privacy-Quality-Efficiency in Federated Learning through Round-Based Interleaving of Protection Techniques
---

# Balancing Privacy-Quality-Efficiency in Federated Learning through Round-Based Interleaving of Protection Techniques
**arXiv**：[2603.05158v1](https://arxiv.org/abs/2603.05158) · [PDF](https://arxiv.org/pdf/2603.05158.pdf)  
**作者**：Yenan Wang, Carla Fabiana Chiasserini, Elad Michael Schiller  

**一句话要点**：提出Alt-FL框架，通过轮次交错策略平衡联邦学习中的隐私、质量和效率。

**关键词**：联邦学习, 隐私保护, 差分隐私, 同态加密, 合成数据, 轮次交错

## 3 点简述
- 核心问题：联邦学习中隐私保护机制如差分隐私和同态加密常导致学习质量下降或系统开销大。
- 方法要点：Alt-FL结合差分隐私、同态加密和合成数据，采用轮次交错策略实现灵活的质量-效率权衡。
- 实验或效果：在CIFAR-10和Fashion-MNIST上评估，隐私交错在高隐私级别表现最佳，差分隐私方法在中等隐私需求下更优。

## 摘要（原文）

> In federated learning (FL), balancing privacy protection, learning quality, and efficiency remains a challenge. Privacy protection mechanisms, such as Differential Privacy (DP), degrade learning quality, or, as in the case of Homomorphic Encryption (HE), incur substantial system overhead. To address this, we propose Alt-FL, a privacy-preserving FL framework that combines DP, HE, and synthetic data via a novel round-based interleaving strategy. Alt-FL introduces three new methods, Privacy Interleaving (PI), Synthetic Interleaving with DP (SI/DP), and Synthetic Interleaving with HE (SI/HE), that enable flexible quality-efficiency trade-offs while providing privacy protection.
>   We systematically evaluate Alt-FL against representative reconstruction attacks, including Deep Leakage from Gradients, Inverting Gradients, When the Curious Abandon Honesty, and Robbing the Fed, using a LeNet-5 model on CIFAR-10 and Fashion-MNIST. To enable fair comparison between DP- and HE-based defenses, we introduce a new attacker-centric framework that compares empirical attack success rates across the three proposed interleaving methods. Our results show that, for the studied attacker model and dataset, PI achieves the most balanced trade-offs at high privacy protection levels, while DP-based methods are preferable at intermediate privacy requirements. We also discuss how such results can be the basis for selecting privacy-preserving FL methods under varying privacy and resource constraints.

