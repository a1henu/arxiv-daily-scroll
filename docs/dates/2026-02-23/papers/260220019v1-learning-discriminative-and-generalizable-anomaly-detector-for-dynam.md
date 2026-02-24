---
layout: default
title: Learning Discriminative and Generalizable Anomaly Detector for Dynamic Graph with Limited Supervision
---

# Learning Discriminative and Generalizable Anomaly Detector for Dynamic Graph with Limited Supervision
**arXiv**：[2602.20019v1](https://arxiv.org/abs/2602.20019) · [PDF](https://arxiv.org/pdf/2602.20019.pdf)  
**作者**：Yuxing Tian, Yiyan Qi, Fengran Mo, Weixu Zhang, Jian Guo, Jian-Yun Nie  

**一句话要点**：提出基于残差表示与双边界优化的动态图异常检测框架，以解决有限监督下的泛化问题。

**关键词**：动态图异常检测, 有限监督学习, 残差表示, 双边界优化, 泛化能力, 模型无关框架

## 3 点简述
- 核心问题：动态图异常检测中，标注异常稀缺导致现有方法泛化能力差或边界模糊。
- 方法要点：通过残差编码捕获异常信号，结合限制损失和双边界优化学习鲁棒判别边界。
- 实验或效果：在多种评估设置下，框架表现出优越性能，提升对未见异常的泛化能力。

## 摘要（原文）

> Dynamic graph anomaly detection (DGAD) is critical for many real-world applications but remains challenging due to the scarcity of labeled anomalies. Existing methods are either unsupervised or semi-supervised: unsupervised methods avoid the need for labeled anomalies but often produce ambiguous boundary, whereas semi-supervised methods can overfit to the limited labeled anomalies and generalize poorly to unseen anomalies. To address this gap, we consider a largely underexplored problem in DGAD: learning a discriminative boundary from normal/unlabeled data, while leveraging limited labeled anomalies \textbf{when available} without sacrificing generalization to unseen anomalies. To this end, we propose an effective, generalizable, and model-agnostic framework with three main components: (i) residual representation encoding that capture deviations between current interactions and their historical context, providing anomaly-relevant signals; (ii) a restriction loss that constrain the normal representations within an interval bounded by two co-centered hyperspheres, ensuring consistent scales while keeping anomalies separable; (iii) a bi-boundary optimization strategy that learns a discriminative and robust boundary using the normal log-likelihood distribution modeled by a normalizing flow. Extensive experiments demonstrate the superiority of our framework across diverse evaluation settings.

