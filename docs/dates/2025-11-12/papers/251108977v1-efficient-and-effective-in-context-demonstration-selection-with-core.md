---
layout: default
title: Efficient and Effective In-context Demonstration Selection with Coreset
---

# Efficient and Effective In-context Demonstration Selection with Coreset
**arXiv**：[2511.08977v1](https://arxiv.org/abs/2511.08977) · [PDF](https://arxiv.org/pdf/2511.08977.pdf)  
**作者**：Zihua Wang, Jiarui Wang, Haiyang Xu, Ming Yan, Fei Huang, Xu Yang, Xiu-Shen Wei, Siya Mi, Yu Zhang  

**一句话要点**：提出基于核心集的双重检索框架以解决上下文学习中演示选择效率与效果平衡问题

**关键词**：上下文学习, 演示选择, 核心集, 双重检索, 大型视觉语言模型, 效率优化

## 3 点简述
- 上下文学习演示选择为NP难问题，传统方法效率低或性能差
- 引入核心集构建与双重检索机制，提升多样性与全局选择效率
- 实验显示方法显著优于现有策略，提高上下文学习性能

## 摘要（原文）

> In-context learning (ICL) has emerged as a powerful paradigm for Large Visual Language Models (LVLMs), enabling them to leverage a few examples directly from input contexts. However, the effectiveness of this approach is heavily reliant on the selection of demonstrations, a process that is NP-hard. Traditional strategies, including random, similarity-based sampling and infoscore-based sampling, often lead to inefficiencies or suboptimal performance, struggling to balance both efficiency and effectiveness in demonstration selection. In this paper, we propose a novel demonstration selection framework named Coreset-based Dual Retrieval (CoDR). We show that samples within a diverse subset achieve a higher expected mutual information. To implement this, we introduce a cluster-pruning method to construct a diverse coreset that aligns more effectively with the query while maintaining diversity. Additionally, we develop a dual retrieval mechanism that enhances the selection process by achieving global demonstration selection while preserving efficiency. Experimental results demonstrate that our method significantly improves the ICL performance compared to the existing strategies, providing a robust solution for effective and efficient demonstration selection.

