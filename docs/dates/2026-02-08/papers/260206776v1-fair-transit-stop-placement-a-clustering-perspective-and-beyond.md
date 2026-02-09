---
layout: default
title: Fair Transit Stop Placement: A Clustering Perspective and Beyond
---

# Fair Transit Stop Placement: A Clustering Perspective and Beyond
**arXiv**：[2602.06776v1](https://arxiv.org/abs/2602.06776) · [PDF](https://arxiv.org/pdf/2602.06776.pdf)  
**作者**：Haris Aziz, Ling Gai, Yuhang Guo, Jeremy Vollen  

**一句话要点**：提出公平聚类与扩展成本算法，以解决公共交通站点放置中的公平性问题。

**关键词**：公共交通站点放置, 公平聚类, 公平性分析, 近似算法, 核心与JR, 实验验证

## 3 点简述
- 研究公共交通站点放置问题，结合公平聚类视角分析公平性。
- 提出扩展成本算法，实现JR的2.414近似，并设计参数化算法平衡JR与核心。
- 实验分析基于小规模拼车数据，验证理论结果。

## 摘要（原文）

> We study the transit stop placement (TrSP) problem in general metric spaces, where agents travel between source-destination pairs and may either walk directly or utilize a shuttle service via selected transit stops. We investigate fairness in TrSP through the lens of justified representation (JR) and the core, and uncover a structural correspondence with fair clustering. Specifically, we show that a constant-factor approximation to proportional fairness in clustering can be used to guarantee a constant-factor biparameterized approximation to core. We establish a lower bound of 1.366 on the approximability of JR, and moreover show that no clustering algorithm can approximate JR within a factor better than 3. Going beyond clustering, we propose the Expanding Cost Algorithm, which achieves a tight 2.414-approximation for JR, but does not give any bounded core guarantee. In light of this, we introduce a parameterized algorithm that interpolates between these approaches, and enables a tunable trade-off between JR and core. Finally, we complement our results with an experimental analysis using small-market public carpooling data.

