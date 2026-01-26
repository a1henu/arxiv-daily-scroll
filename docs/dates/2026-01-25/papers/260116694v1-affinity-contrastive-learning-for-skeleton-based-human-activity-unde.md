---
layout: default
title: Affinity Contrastive Learning for Skeleton-based Human Activity Understanding
---

# Affinity Contrastive Learning for Skeleton-based Human Activity Understanding
**arXiv**：[2601.16694v1](https://arxiv.org/abs/2601.16694) · [PDF](https://arxiv.org/pdf/2601.16694.pdf)  
**作者**：Hongda Liu, Yunfan Liu, Min Ren, Lin Sui, Yunlong Wang, Zhenan Sun  

**一句话要点**：提出亲和性对比学习网络以解决骨架动作理解中类间相似性利用不足和异常正样本影响问题。

**关键词**：骨架动作理解, 对比学习, 亲和性度量, 动态温度调度, 超类学习, 异常样本处理

## 3 点简述
- 核心问题：现有方法未充分利用类间结构相似性，且忽略异常正样本对特征判别的影响。
- 方法要点：引入亲和性度量优化相似性计算，形成活动超类以提供更丰富的对比信号，并采用动态温度调度和基于边界的对比策略。
- 实验或效果：在多个数据集上验证了方法在动作识别、步态识别和行人重识别中的优越性。

## 摘要（原文）

> In skeleton-based human activity understanding, existing methods often adopt the contrastive learning paradigm to construct a discriminative feature space. However, many of these approaches fail to exploit the structural inter-class similarities and overlook the impact of anomalous positive samples. In this study, we introduce ACLNet, an Affinity Contrastive Learning Network that explores the intricate clustering relationships among human activity classes to improve feature discrimination. Specifically, we propose an affinity metric to refine similarity measurements, thereby forming activity superclasses that provide more informative contrastive signals. A dynamic temperature schedule is also introduced to adaptively adjust the penalty strength for various superclasses. In addition, we employ a margin-based contrastive strategy to improve the separation of hard positive and negative samples within classes. Extensive experiments on NTU RGB+D 60, NTU RGB+D 120, Kinetics-Skeleton, PKU-MMD, FineGYM, and CASIA-B demonstrate the superiority of our method in skeleton-based action recognition, gait recognition, and person re-identification. The source code is available at https://github.com/firework8/ACLNet.

