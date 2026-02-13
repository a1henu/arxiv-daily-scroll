---
layout: default
title: A Generic Framework for Fair Consensus Clustering in Streams
---

# A Generic Framework for Fair Consensus Clustering in Streams
**arXiv**：[2602.11500v1](https://arxiv.org/abs/2602.11500) · [PDF](https://arxiv.org/pdf/2602.11500.pdf)  
**作者**：Diptarka Chakraborty, Kushagra Chatterjee, Debarati Das, Tien-Long Nguyen  

**一句话要点**：提出流式公平共识聚类的通用框架，实现对数存储下的常数因子近似。

**关键词**：流式聚类, 公平共识聚类, 近似算法, 通用框架, k-中值聚类

## 3 点简述
- 研究流式模型中的公平共识聚类问题，输入聚类序列到达且内存有限。
- 设计通用框架，结合最近公平聚类与聚类拟合，提升近似保证。
- 框架公平无关，适用于多种公平定义，并扩展至k-中值共识聚类。

## 摘要（原文）

> Consensus clustering seeks to combine multiple clusterings of the same dataset, potentially derived by considering various non-sensitive attributes by different agents in a multi-agent environment, into a single partitioning that best reflects the overall structure of the underlying dataset. Recent work by Chakraborty et al, introduced a fair variant under proportionate fairness and obtained a constant-factor approximation by naively selecting the best closest fair input clustering; however, their offline approach requires storing all input clusterings, which is prohibitively expensive for most large-scale applications.
>   In this paper, we initiate the study of fair consensus clustering in the streaming model, where input clusterings arrive sequentially and memory is limited. We design the first constant-factor algorithm that processes the stream while storing only a logarithmic number of inputs. En route, we introduce a new generic algorithmic framework that integrates closest fair clustering with cluster fitting, yielding improved approximation guarantees not only in the streaming setting but also when revisited offline. Furthermore, the framework is fairness-agnostic: it applies to any fairness definition for which an approximately close fair clustering can be computed efficiently. Finally, we extend our methods to the more general k-median consensus clustering problem.

