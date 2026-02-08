---
layout: default
title: AI Agent Systems for Supply Chains: Structured Decision Prompts and Memory Retrieval
---

# AI Agent Systems for Supply Chains: Structured Decision Prompts and Memory Retrieval
**arXiv**：[2602.05524v1](https://arxiv.org/abs/2602.05524) · [PDF](https://arxiv.org/pdf/2602.05524.pdf)  
**作者**：Konosuke Yoshizato, Kazuma Shimizu, Ryota Higa, Takanobu Otsuka  

**一句话要点**：提出AIM-RM代理以增强基于LLM的多代理系统在供应链库存管理中的适应性和性能

**关键词**：多代理系统, 库存管理, 大语言模型, 相似性匹配, 供应链优化

## 3 点简述
- 核心问题：基于LLM的多代理系统在库存管理中能否稳定生成最优订购策略并适应多样场景
- 方法要点：引入AIM-RM代理，通过相似性匹配利用历史经验提升决策适应性
- 实验或效果：AIM-RM在多种供应链场景中优于基准方法，显示其鲁棒性和适应性

## 摘要（原文）

> This study investigates large language model (LLM) -based multi-agent systems (MASs) as a promising approach to inventory management, which is a key component of supply chain management. Although these systems have gained considerable attention for their potential to address the challenges associated with typical inventory management methods, key uncertainties regarding their effectiveness persist. Specifically, it is unclear whether LLM-based MASs can consistently derive optimal ordering policies and adapt to diverse supply chain scenarios. To address these questions, we examine an LLM-based MAS with a fixed-ordering strategy prompt that encodes the stepwise processes of the problem setting and a safe-stock strategy commonly used in inventory management. Our empirical results demonstrate that, even without detailed prompt adjustments, an LLM-based MAS can determine optimal ordering decisions in a restricted scenario. To enhance adaptability, we propose a novel agent called AIM-RM, which leverages similar historical experiences through similarity matching. Our results show that AIM-RM outperforms benchmark methods across various supply chain scenarios, highlighting its robustness and adaptability.

