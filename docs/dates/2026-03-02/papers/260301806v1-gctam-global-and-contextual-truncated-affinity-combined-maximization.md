---
layout: default
title: GCTAM: Global and Contextual Truncated Affinity Combined Maximization Model For Unsupervised Graph Anomaly Detection
---

# GCTAM: Global and Contextual Truncated Affinity Combined Maximization Model For Unsupervised Graph Anomaly Detection
**arXiv**：[2603.01806v1](https://arxiv.org/abs/2603.01806) · [PDF](https://arxiv.org/pdf/2603.01806.pdf)  
**作者**：Xiong Zhang, Hong Peng, Zhenli He, Cheng Xie, Xin Jin, Hua Jiang  

**一句话要点**：提出GCTAM模型，结合全局与上下文截断亲和力最大化，以改进无监督图异常检测

**关键词**：图异常检测, 无监督学习, 截断亲和力最大化, 上下文截断, 全局截断, 社交图分析

## 3 点简述
- 现有TAM方法使用刚性阈值截断异常节点，忽略节点特异性和高阶亲和力，导致截断效率低
- GCTAM通过上下文截断降低异常节点亲和力，全局截断增强正常节点亲和力，实现更精准的异常识别
- 在Amazon和YelpChi等真实数据集上，相比先前方法提升15%~20%，并在大规模数据集上表现优异

## 摘要（原文）

> Anomalies often occur in real-world information networks/graphs, such as malevolent users, malicious comments, banned users, and fake news in social graphs. The latest graph anomaly detection methods use a novel mechanism called truncated affinity maximization (TAM) to detect anomaly nodes without using any label information and achieve impressive results. TAM maximizes the affinities among the normal nodes while truncating the affinities of the anomalous nodes to identify the anomalies. However, existing TAM-based methods truncate suspicious nodes according to a rigid threshold that ignores the specificity and high-order affinities of different nodes. This inevitably causes inefficient truncations from both normal and anomalous nodes, limiting the effectiveness of anomaly detection. To this end, this paper proposes a novel truncation model combining contextual and global affinity to truncate the anomalous nodes. The core idea of the work is to use contextual truncation to decrease the affinity of anomalous nodes, while global truncation increases the affinity of normal nodes. Extensive experiments on massive real-world datasets show that our method surpasses peer methods in most graph anomaly detection tasks. In highlights, compared with previous state-of-the-art methods, the proposed method has +15\% $\sim$ +20\% improvements in two famous real-world datasets, Amazon and YelpChi. Notably, our method works well in large datasets, Amazin-all and YelpChi-all, and achieves the best results, while most previous models cannot complete the tasks.

