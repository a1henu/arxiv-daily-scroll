---
layout: default
title: BFS-PO: Best-First Search for Large Reasoning Models
---

# BFS-PO: Best-First Search for Large Reasoning Models
**arXiv**：[2602.14917v1](https://arxiv.org/abs/2602.14917) · [PDF](https://arxiv.org/pdf/2602.14917.pdf)  
**作者**：Fiorenzo Parascandolo, Wenhui Tan, Enver Sangineto, Ruihua Song, Rita Cucchiara  

**一句话要点**：提出BFS-PO强化学习算法以解决大型推理模型过思考问题

**关键词**：大型推理模型, 强化学习, 最佳优先搜索, 过思考问题, 推理链优化

## 3 点简述
- 大型推理模型在推理任务中常因过思考导致计算成本高和输出冗长
- BFS-PO采用最佳优先搜索和回溯机制，训练中生成更短答案以学习简洁推理
- 实验表明BFS-PO能同时提高模型准确性和缩短答案长度

## 摘要（原文）

> Large Reasoning Models (LRMs) such as OpenAI o1 and DeepSeek-R1 have shown excellent performance in reasoning tasks using long reasoning chains. However, this has also led to a significant increase of computational costs and the generation of verbose output, a phenomenon known as overthinking. The tendency to overthinking is often exacerbated by Reinforcement Learning (RL) algorithms such as GRPO/DAPO. In this paper, we propose BFS-PO, an RL algorithm which alleviates this problem using a Best-First Search exploration strategy. Specifically, BFS-PO looks for the shortest correct answer using a backtracking mechanism based on maximum entropy nodes. By generating progressively shorter responses during training, BFS-PO learns to produce concise reasoning chains. Using different benchmarks and base LRMs, we show that BFS-PO can simultaneously increase the LRM accuracy and shorten its answers.

