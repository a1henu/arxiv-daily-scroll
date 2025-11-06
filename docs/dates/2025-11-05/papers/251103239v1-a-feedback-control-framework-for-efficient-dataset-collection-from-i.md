---
layout: default
title: A Feedback-Control Framework for Efficient Dataset Collection from In-Vehicle Data Streams
---

# A Feedback-Control Framework for Efficient Dataset Collection from In-Vehicle Data Streams
**arXiv**：[2511.03239v1](https://arxiv.org/abs/2511.03239) · [PDF](https://arxiv.org/pdf/2511.03239.pdf)  
**作者**：Philipp Reis, Philipp Rigoll, Christian Steinhauser, Jacob Langner, Eric Sax  

**一句话要点**：提出FCDC反馈控制框架，以优化车载数据流的高效数据集收集。

**关键词**：数据收集控制, 反馈控制框架, 在线概率模型, 数据集多样性, 车载数据流, 数据冗余减少

## 3 点简述
- 核心问题：传统数据收集为开环方式，导致冗余样本积累、存储低效和泛化能力受限。
- 方法要点：将数据收集建模为闭环控制问题，使用在线概率模型和反馈信号动态调节样本保留。
- 实验或效果：在真实数据流中，数据集平衡性提升25.9%，数据存储减少39.8%。

## 摘要（原文）

> Modern AI systems are increasingly constrained not by model capacity but by
> the quality and diversity of their data. Despite growing emphasis on
> data-centric AI, most datasets are still gathered in an open-loop manner which
> accumulates redundant samples without feedback from the current coverage. This
> results in inefficient storage, costly labeling, and limited generalization. To
> address this, this paper introduces \ac{FCDC}, a paradigm that formulates data
> collection as a closed-loop control problem. \ac{FCDC} continuously
> approximates the state of the collected data distribution using an online
> probabilistic model and adaptively regulates sample retention using based on
> feedback signals such as likelihood and Mahalanobis distance. Through this
> feedback mechanism, the system dynamically balances exploration and
> exploitation, maintains dataset diversity, and prevents redundancy from
> accumulating over time. Besides showcasing the controllability of \ac{FCDC} on
> a synthetic dataset, experiments on a real data stream show that \ac{FCDC}
> produces more balanced datasets by $\SI{25.9}{\percent}$ while reducing data
> storage by $\SI{39.8}{\percent}$. These results demonstrate that data
> collection itself can be actively controlled, transforming collection from a
> passive pipeline stage into a self-regulating, feedback-driven process at the
> core of data-centric AI.

