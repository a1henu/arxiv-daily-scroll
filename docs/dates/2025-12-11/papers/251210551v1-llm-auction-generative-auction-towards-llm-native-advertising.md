---
layout: default
title: LLM-Auction: Generative Auction towards LLM-Native Advertising
---

# LLM-Auction: Generative Auction towards LLM-Native Advertising
**arXiv**：[2512.10551v1](https://arxiv.org/abs/2512.10551) · [PDF](https://arxiv.org/pdf/2512.10551.pdf)  
**作者**：Chujie Zhao, Qun Hu, Shiping Song, Dagui Chen, Han Zhu, Jian Xu, Bo Zheng  

**一句话要点**：提出LLM-Auction以解决LLM原生广告中拍卖机制与生成分离的问题

**关键词**：LLM原生广告, 生成拍卖机制, IRPO算法, 分配外部性, 激励兼容性, 模拟评估

## 3 点简述
- 核心问题：LLM原生广告将拍卖对象从离散广告位转向LLM输出分布，现有机制忽略外部性或需多次推理，不实用
- 方法要点：基于学习的生成拍卖机制，通过IRPO算法对齐LLM输出与机制目标，无额外推理成本建模外部性
- 实验或效果：在模拟环境中评估，LLM-Auction在分配效率上显著优于基线，并实现激励属性

## 摘要（原文）

> The rapid advancement of large language models (LLMs) necessitates novel monetization strategies, among which LLM-native advertising has emerged as a promising paradigm by naturally integrating advertisement within LLM-generated responses. However, this paradigm fundamentally shifts the auction object from discrete ad slots to the distribution over LLM outputs, posing new challenges for designing auction mechanisms. Existing mechanisms for LLM-native advertising adopt frameworks that decouple auction and generation, which either ignore externalities or require multiple LLM inferences for ad allocation, rendering them impractical for industrial scenarios. To address these challenges, we propose LLM-Auction, which to the best of our knowledge is the first learning-based generative auction mechanism that integrates auction and LLM generation for LLM-native advertising. By formulating the allocation optimization as a preference alignment problem between LLM outputs and the mechanism's objective which reflects both advertisers' expected value and user experience, we introduce Iterative Reward-Preference Optimization (IRPO) algorithm that alternately optimizes the reward model and the LLM. This approach enables the LLM to inherently model allocation externalities without any extra inference cost. We further identify the allocation monotonicity and continuity of LLM-Auction, which allows us to prove that a simple first-price payment rule exhibits favorable incentive properties. Additionally, we design an LLM-as-a-judge simulation environment to facilitate large-scale data construction and enable comprehensive quantitative evaluation of the mechanism's performance. Extensive quantitative and qualitative experiments demonstrate that LLM-Auction significantly outperforms existing baselines in allocation efficiency, while achieving the desired mechanism properties.

