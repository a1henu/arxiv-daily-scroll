---
layout: default
title: Exact Recovery in the Data Block Model
---

# Exact Recovery in the Data Block Model
**arXiv**：[2602.05852v1](https://arxiv.org/abs/2602.05852) · [PDF](https://arxiv.org/pdf/2602.05852.pdf)  
**作者**：Amir R. Asadi, Akbar Davoodi, Ramin Javadi, Farzad Parvaresh  

**一句话要点**：提出Chernoff-TV散度以解决数据块模型中社区检测的精确恢复问题

**关键词**：社区检测, 数据块模型, 精确恢复, Chernoff-TV散度, 阈值分析, 节点数据

## 3 点简述
- 研究数据块模型中的精确恢复问题，结合图连接性和节点数据
- 引入Chernoff-TV散度，刻画精确恢复的尖锐阈值并提供高效算法
- 通过仿真验证阈值，展示节点数据作为辅助信息在社区检测中的优势

## 摘要（原文）

> Community detection in networks is a fundamental problem in machine learning and statistical inference, with applications in social networks, biological systems, and communication networks. The stochastic block model (SBM) serves as a canonical framework for studying community structure, and exact recovery, identifying the true communities with high probability, is a central theoretical question. While classical results characterize the phase transition for exact recovery based solely on graph connectivity, many real-world networks contain additional data, such as node attributes or labels. In this work, we study exact recovery in the Data Block Model (DBM), an SBM augmented with node-associated data, as formalized by Asadi, Abbe, and Verdú (2017). We introduce the Chernoff--TV divergence and use it to characterize a sharp exact recovery threshold for the DBM. We further provide an efficient algorithm that achieves this threshold, along with a matching converse result showing impossibility below the threshold. Finally, simulations validate our findings and demonstrate the benefits of incorporating vertex data as side information in community detection.

