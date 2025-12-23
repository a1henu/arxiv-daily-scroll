---
layout: default
title: Deep Learning for Unrelated-Machines Scheduling: Handling Variable Dimensions
---

# Deep Learning for Unrelated-Machines Scheduling: Handling Variable Dimensions
**arXiv**：[2512.19527v1](https://arxiv.org/abs/2512.19527) · [PDF](https://arxiv.org/pdf/2512.19527.pdf)  
**作者**：Diego Hitzges, Guillaume Sagnol  

**一句话要点**：提出基于深度学习的离线调度方法，处理无关并行机调度中的可变维度问题。

**关键词**：无关并行机调度, 深度学习调度, 可变维度处理, 离线调度优化, 神经网络架构

## 3 点简述
- 核心问题：无关并行机调度中，作业和机器数量可变，且每对作业-机器处理时间独特，导致特征维度动态变化。
- 方法要点：设计神经网络架构，受NLP启发，一次性处理完整输入，支持任意规模调度，目标是最小化完工时间和加权延迟。
- 实验或效果：在8作业4机器实例上训练，成本仅比最优高2.51%；在最多100作业10机器配置中，平均成本比高级调度规则低22.22%。

## 摘要（原文）

> Deep learning has been effectively applied to many discrete optimization problems. However, learning-based scheduling on unrelated parallel machines remains particularly difficult to design. Not only do the numbers of jobs and machines vary, but each job-machine pair has a unique processing time, dynamically altering feature dimensions. We propose a novel approach with a neural network tailored for offline deterministic scheduling of arbitrary sizes on unrelated machines. The goal is to minimize a complex objective function that includes the makespan and the weighted tardiness of jobs and machines. Unlike existing online approaches, which process jobs sequentially, our method generates a complete schedule considering the entire input at once. The key contribution of this work lies in the sophisticated architecture of our model. By leveraging various NLP-inspired architectures, it effectively processes any number of jobs and machines with varying feature dimensions imposed by unrelated processing times. Our approach enables supervised training on small problem instances while demonstrating strong generalization to much larger scheduling environments. Trained and tested on instances with 8 jobs and 4 machines, costs were only 2.51% above optimal. Across all tested configurations of up to 100 jobs and 10 machines, our network consistently outperformed an advanced dispatching rule, which incurred 22.22% higher costs on average. As our method allows fast retraining with simulated data and adaptation to various scheduling conditions, we believe it has the potential to become a standard approach for learning-based scheduling on unrelated machines and similar problem environments.

