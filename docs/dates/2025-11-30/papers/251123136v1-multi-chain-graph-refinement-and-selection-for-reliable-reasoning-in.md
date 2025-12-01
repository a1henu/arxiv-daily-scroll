---
layout: default
title: Multi-chain Graph Refinement and Selection for Reliable Reasoning in Large Language Models
---

# Multi-chain Graph Refinement and Selection for Reliable Reasoning in Large Language Models
**arXiv**：[2511.23136v1](https://arxiv.org/abs/2511.23136) · [PDF](https://arxiv.org/pdf/2511.23136.pdf)  
**作者**：Yujiao Yang, Jing Lian, Linhui Li  

**一句话要点**：提出多链图精炼与选择框架以增强大语言模型的可靠推理能力

**关键词**：大语言模型推理, 图结构推理, 多链精炼, 验证策略, 推理效率提升

## 3 点简述
- 核心问题：现有推理增强方法存在多样性不足、冗余分支和跨路径整合与纠错能力弱的问题
- 方法要点：通过生成多样推理轨迹、复合验证、构建关系图并计算累积成功率来选择和精炼答案
- 实验或效果：在六个基准数据集上平均准确率达82.9%，优于基线2.1%，并在24点游戏中实现100%准确率和13.6倍加速

## 摘要（原文）

> The complex reasoning ability of Large Language Models (LLMs) poses a critical bottleneck for their practical applications. Test-time expansion methods such as Tree-of-Thought (ToT) and Graph-of-Thought (GoT) enhance reasoning by introducing intermediate reasoning structures, tree search, or graph-based exploration mechanisms. However, their reasoning strategies suffer from limited diversity, redundant search branches, and inadequate integration and error correction across heterogeneous reasoning paths. To address these limitations, we propose a novel reasoning framework called Multi-chain Graph Refinement & Selection (MGRS), which first generates multiple diverse reasoning trajectories for a given problem, refines candidate responses using a composite self- and cross-verification strategy, then constructs a reasoning relation graph and estimates the success rate of intermediate nodes, and finally computes cumulative success rates to select the most reliable answer and corresponding reasoning trajectory. Experimental results demonstrate that MGRS significantly advances both the reasoning capability and computational efficiency of reasoning enhancement methods. Across six benchmark datasets spanning four distinct tasks, MGRS achieves an average accuracy of 82.9%, outperforming state-of-the-art baselines by a clear margin of 2.1%. Remarkably, on the 24-point game, MGRS attains 100% accuracy for the first time, while delivering a 13.6x speed-up compared to the leading Forest of Thoughts framework.

