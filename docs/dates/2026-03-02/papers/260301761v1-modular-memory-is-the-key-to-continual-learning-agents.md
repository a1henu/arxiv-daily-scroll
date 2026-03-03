---
layout: default
title: Modular Memory is the Key to Continual Learning Agents
---

# Modular Memory is the Key to Continual Learning Agents
**arXiv**：[2603.01761v1](https://arxiv.org/abs/2603.01761) · [PDF](https://arxiv.org/pdf/2603.01761.pdf)  
**作者**：Vaggelis Dorovatas, Malte Schwerin, Andrew D. Bagdanov, Lucas Caccia, Antonio Carta, Laurent Charlin, Barbara Hammer, Tyler L. Hayes, Timm Hess, Christopher Kanan, Dhireesha Kudithipudi, Xialei Liu, Vincenzo Lomonaco, Jorge Mendez-Mendez, Darshan Patil, Ameya Prabhu, Elisa Ricci, Tinne Tuytelaars, Gido M. van de Ven, Liyuan Wang, Joost van de Weijer, Jonghyun Choi, Martin Mundt, Rahaf Aljundi  

**一句话要点**：提出模块化内存框架以结合权重内学习和上下文内学习，实现大规模持续学习代理

**关键词**：持续学习, 模块化内存, 上下文内学习, 权重内学习, 灾难性遗忘, 自适应智能

## 3 点简述
- 核心问题：基础模型在持续操作、经验积累和个性化方面存在局限，传统持续学习依赖权重内学习易导致灾难性遗忘
- 方法要点：设计模块化内存中心架构，利用上下文内学习快速适应和积累知识，权重内学习稳定更新模型能力
- 实验或效果：未知，论文为概念框架，未报告具体实验或效果

## 摘要（原文）

> Foundation models have transformed machine learning through large-scale pretraining and increased test-time compute. Despite surpassing human performance in several domains, these models remain fundamentally limited in continuous operation, experience accumulation, and personalization, capabilities that are central to adaptive intelligence. While continual learning research has long targeted these goals, its historical focus on in-weight learning (IWL), i.e., updating a single model's parameters to absorb new knowledge, has rendered catastrophic forgetting a persistent challenge. Our position is that combining the strengths of In-Weight Learning (IWL) and the newly emerged capabilities of In-Context Learning (ICL) through the design of modular memory is the missing piece for continual adaptation at scale. We outline a conceptual framework for modular memory-centric architectures that leverage ICL for rapid adaptation and knowledge accumulation, and IWL for stable updates to model capabilities, charting a practical roadmap toward continually learning agents.

