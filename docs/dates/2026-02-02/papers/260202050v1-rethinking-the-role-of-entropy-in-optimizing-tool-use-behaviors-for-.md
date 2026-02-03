---
layout: default
title: Rethinking the Role of Entropy in Optimizing Tool-Use Behaviors for Large Language Model Agents
---

# Rethinking the Role of Entropy in Optimizing Tool-Use Behaviors for Large Language Model Agents
**arXiv**：[2602.02050v1](https://arxiv.org/abs/2602.02050) · [PDF](https://arxiv.org/pdf/2602.02050.pdf)  
**作者**：Zeping Li, Hongru Wang, Yiwen Zhao, Guanhua Chen, Yixia Li, Keyang Chen, Yixin Cao, Guangnan Ye, Hongfeng Chai, Mengdi Wang, Zhenfei Yin  

**一句话要点**：提出基于熵减的奖励策略以优化大语言模型代理的工具使用行为

**关键词**：大语言模型代理, 工具使用优化, 熵减监督, 奖励策略, 长轨迹推理

## 3 点简述
- 问题：长轨迹中代理工具调用过多且质量低，导致延迟增加和性能下降
- 方法：利用熵减作为监督信号，设计稀疏结果奖励和密集过程奖励策略
- 效果：稀疏奖励减少工具调用72.07%，密集奖励提升性能22.27%

## 摘要（原文）

> Tool-using agents based on Large Language Models (LLMs) excel in tasks such as mathematical reasoning and multi-hop question answering. However, in long trajectories, agents often trigger excessive and low-quality tool calls, increasing latency and degrading inference performance, making managing tool-use behavior challenging. In this work, we conduct entropy-based pilot experiments and observe a strong positive correlation between entropy reduction and high-quality tool calls. Building on this finding, we propose using entropy reduction as a supervisory signal and design two reward strategies to address the differing needs of optimizing tool-use behavior. Sparse outcome rewards provide coarse, trajectory-level guidance to improve efficiency, while dense process rewards offer fine-grained supervision to enhance performance. Experiments across diverse domains show that both reward designs improve tool-use behavior: the former reduces tool calls by 72.07% compared to the average of baselines, while the latter improves performance by 22.27%. These results position entropy reduction as a key mechanism for enhancing tool-use behavior, enabling agents to be more adaptive in real-world applications.

