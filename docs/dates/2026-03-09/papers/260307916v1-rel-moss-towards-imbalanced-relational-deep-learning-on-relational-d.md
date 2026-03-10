---
layout: default
title: Rel-MOSS: Towards Imbalanced Relational Deep Learning on Relational Databases
---

# Rel-MOSS: Towards Imbalanced Relational Deep Learning on Relational Databases
**arXiv**：[2603.07916v1](https://arxiv.org/abs/2603.07916) · [PDF](https://arxiv.org/pdf/2603.07916.pdf)  
**作者**：Jun Yin, Peng Huo, Bangguo Zhu, Hao Yan, Senzhang Wang, Shirui Pan, Chengqi Zhang  

**一句话要点**：提出Rel-MOSS以解决关系数据库中实体分类的类别不平衡问题

**关键词**：关系深度学习, 类别不平衡, 图神经网络, 过采样, 实体分类, 关系数据库

## 3 点简述
- 核心问题：现有关系深度学习忽视关系数据不平衡，导致少数实体表征不足
- 方法要点：设计关系门控控制器和关系引导少数合成器，调制邻居消息并过采样
- 实验或效果：在12个数据集上优于现有方法，平衡准确率和G-均值平均提升达2.46%和4.00%

## 摘要（原文）

> In recent advances, to enable a fully data-driven learning paradigm on relational databases (RDB), relational deep learning (RDL) is proposed to structure the RDB as a heterogeneous entity graph and adopt the graph neural network (GNN) as the predictive model. However, existing RDL methods neglect the imbalance problem of relational data in RDBs and risk under-representing the minority entities, leading to an unusable model in practice. In this work, we investigate, for the first time, class imbalance problem in RDB entity classification and design the relation-centric minority synthetic over-sampling GNN (Rel-MOSS), in order to fill a critical void in the current literature. Specifically, to mitigate the issue of minority-related information being submerged by majority counterparts, we design the relation-wise gating controller to modulate neighborhood messages from each individual relation type. Based on the relational-gated representations, we further propose the relation-guided minority synthesizer for over-sampling, which integrates the entity relational signatures to maintain relational consistency. Extensive experiments on 12 entity classification datasets provide compelling evidence for the superiority of Rel-MOSS, yielding an average improvement of up to 2.46% and 4.00% in terms of Balanced Accuracy and G-Mean, compared with SOTA RDL methods and classic methods for handling class imbalance.

