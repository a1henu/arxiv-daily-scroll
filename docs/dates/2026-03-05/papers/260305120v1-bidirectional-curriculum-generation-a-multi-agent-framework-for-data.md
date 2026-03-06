---
layout: default
title: Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning
---

# Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning
**arXiv**：[2603.05120v1](https://arxiv.org/abs/2603.05120) · [PDF](https://arxiv.org/pdf/2603.05120.pdf)  
**作者**：Boren Hu, Xiao Liu, Boci Peng, Xinping Zhao, Xiaoran Shang, Yun Zhu, Lijun Wu  

**一句话要点**：提出双向课程生成框架以解决数学推理中数据效率低下的问题

**关键词**：数学推理, 课程学习, 数据生成, 多智能体系统, 最优步调定理, 闭环反馈

## 3 点简述
- 核心问题：大规模语言模型数学推理需大量数据，但数据效率低，传统单向课程学习样本利用率不足
- 方法要点：采用多智能体框架，动态生成数据，通过复杂化或简化问题建立闭环反馈，优化学习轨迹
- 实验或效果：基于最优步调定理，显著超越基线，用更少指令样本实现更优推理性能

## 摘要（原文）

> Enhancing mathematical reasoning in Large Language Models typically demands massive datasets, yet data efficiency remains a critical bottleneck. While Curriculum Learning attempts to structure this process, standard unidirectional approaches (simple-to-complex) suffer from inefficient sample utilization: they blindly escalate complexity even when foundational gaps persist, leading to wasted computation on unsolvable problems. To maximize the instructional value of every training sample, we introduce a novel Bidirectional Curriculum Generation framework. Unlike rigid trajectories, our multi-agent ecosystem mimics adaptive pedagogy to establish a closed feedback loop. It dynamically generates data by either complicating problems to challenge the model or, crucially, simplying them to repair specific reasoning failures. This mechanism ensures that the model consumes only the most effective data at any given stage. Grounded in the Optimal Pacing Theorem, our approach optimizes the learning trajectory, significantly outperforming baselines while achieving superior reasoning performance with substantially fewer instruction samples.

