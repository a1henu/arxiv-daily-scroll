---
layout: default
title: FHAIM: Fully Homomorphic AIM For Private Synthetic Data Generation
---

# FHAIM: Fully Homomorphic AIM For Private Synthetic Data Generation
**arXiv**：[2602.05838v1](https://arxiv.org/abs/2602.05838) · [PDF](https://arxiv.org/pdf/2602.05838.pdf)  
**作者**：Mayank Kumar, Qian Lou, Paulo Barreto, Martine De Cock, Sikha Pentyala  

**一句话要点**：提出FHAIM框架，基于全同态加密在加密表格数据上训练合成数据生成器以解决隐私泄露问题。

**关键词**：全同态加密, 合成数据生成, 隐私保护, 差分隐私, 表格数据, AIM算法

## 3 点简述
- 核心问题：合成数据生成服务需信任提供商访问私有数据，存在隐私风险。
- 方法要点：将AIM算法适配全同态加密，开发新协议确保数据全程加密并满足差分隐私。
- 实验或效果：实证分析显示FHAIM保持AIM性能，运行时间可行。

## 摘要（原文）

> Data is the lifeblood of AI, yet much of the most valuable data remains locked in silos due to privacy and regulations. As a result, AI remains heavily underutilized in many of the most important domains, including healthcare, education, and finance. Synthetic data generation (SDG), i.e. the generation of artificial data with a synthesizer trained on real data, offers an appealing solution to make data available while mitigating privacy concerns, however existing SDG-as-a-service workflow require data holders to trust providers with access to private data.We propose FHAIM, the first fully homomorphic encryption (FHE) framework for training a marginal-based synthetic data generator on encrypted tabular data. FHAIM adapts the widely used AIM algorithm to the FHE setting using novel FHE protocols, ensuring that the private data remains encrypted throughout and is released only with differential privacy guarantees. Our empirical analysis show that FHAIM preserves the performance of AIM while maintaining feasible runtimes.

