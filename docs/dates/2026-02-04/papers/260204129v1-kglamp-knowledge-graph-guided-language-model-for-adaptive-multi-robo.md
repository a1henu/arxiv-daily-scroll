---
layout: default
title: KGLAMP: Knowledge Graph-guided Language model for Adaptive Multi-robot Planning and Replanning
---

# KGLAMP: Knowledge Graph-guided Language model for Adaptive Multi-robot Planning and Replanning
**arXiv**：[2602.04129v1](https://arxiv.org/abs/2602.04129) · [PDF](https://arxiv.org/pdf/2602.04129.pdf)  
**作者**：Chak Lam Shek, Faizan M. Tariq, Sangjae Bae, David Isele, Piyush Gupta  

**一句话要点**：提出KGLAMP框架，以知识图引导LLM解决异构多机器人动态规划问题

**关键词**：异构多机器人规划, 知识图引导, LLM规划框架, 动态环境适应, PDDL规范生成

## 3 点简述
- 核心问题：异构多机器人系统在动态环境中难以构建准确符号表示并保持规划一致性
- 方法要点：利用知识图编码对象关系、空间可达性和机器人能力，指导LLM生成PDDL问题规范
- 实验或效果：在MAT-THOR基准上，性能比纯LLM和PDDL变体至少提升25.5%

## 摘要（原文）

> Heterogeneous multi-robot systems are increasingly deployed in long-horizon missions that require coordination among robots with diverse capabilities. However, existing planning approaches struggle to construct accurate symbolic representations and maintain plan consistency in dynamic environments. Classical PDDL planners require manually crafted symbolic models, while LLM-based planners often ignore agent heterogeneity and environmental uncertainty. We introduce KGLAMP, a knowledge-graph-guided LLM planning framework for heterogeneous multi-robot teams. The framework maintains a structured knowledge graph encoding object relations, spatial reachability, and robot capabilities, which guides the LLM in generating accurate PDDL problem specifications. The knowledge graph serves as a persistent, dynamically updated memory that incorporates new observations and triggers replanning upon detecting inconsistencies, enabling symbolic plans to adapt to evolving world states. Experiments on the MAT-THOR benchmark show that KGLAMP improves performance by at least 25.5% over both LLM-only and PDDL-based variants.

