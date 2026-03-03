---
layout: default
title: A Practical Guide to Streaming Continual Learning
---

# A Practical Guide to Streaming Continual Learning
**arXiv**：[2603.01677v1](https://arxiv.org/abs/2603.01677) · [PDF](https://arxiv.org/pdf/2603.01677.pdf)  
**作者**：Andrea Cossu, Federico Giannini, Giacomo Ziffer, Alessio Bernardo, Alexander Gepperth, Emanuele Della Valle, Barbara Hammer, Davide Bacciu  

**一句话要点**：提出流式持续学习以统一解决快速适应与知识保留问题

**关键词**：流式持续学习, 持续学习, 流式机器学习, 概念漂移, 知识保留, 快速适应

## 3 点简述
- 核心问题：持续学习与流式机器学习在非平稳数据流中面临不同挑战，需结合以同时实现快速适应和知识保留。
- 方法要点：流式持续学习作为新兴范式，连接两个领域，促进设计能快速适应新信息且不遗忘旧知识的混合方法。
- 实验或效果：通过示例和实验展示单独使用持续学习或流式机器学习在快速适应和知识保留方面的不足，突显流式持续学习的必要性。

## 摘要（原文）

> Continual Learning (CL) and Streaming Machine Learning (SML) study the ability of agents to learn from a stream of non-stationary data. Despite sharing some similarities, they address different and complementary challenges. While SML focuses on rapid adaptation after changes (concept drifts), CL aims to retain past knowledge when learning new tasks. After a brief introduction to CL and SML, we discuss Streaming Continual Learning (SCL), an emerging paradigm providing a unifying solution to real-world problems, which may require both SML and CL abilities. We claim that SCL can i) connect the CL and SML communities, motivating their work towards the same goal, and ii) foster the design of hybrid approaches that can quickly adapt to new information (as in SML) without forgetting previous knowledge (as in CL). We conclude the paper with a motivating example and a set of experiments, highlighting the need for SCL by showing how CL and SML alone struggle in achieving rapid adaptation and knowledge retention.

