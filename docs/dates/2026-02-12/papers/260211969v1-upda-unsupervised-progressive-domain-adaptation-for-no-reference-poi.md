---
layout: default
title: UPDA: Unsupervised Progressive Domain Adaptation for No-Reference Point Cloud Quality Assessment
---

# UPDA: Unsupervised Progressive Domain Adaptation for No-Reference Point Cloud Quality Assessment
**arXiv**：[2602.11969v1](https://arxiv.org/abs/2602.11969) · [PDF](https://arxiv.org/pdf/2602.11969.pdf)  
**作者**：Bingxu Xie, Fang Zhou, Jincan Wu, Yonghui Liu, Weiqing Li, Zhiyong Su  

**一句话要点**：提出无监督渐进域适应框架UPDA以解决无参考点云质量评估的跨域性能下降问题。

**关键词**：无参考点云质量评估, 域适应, 渐进对齐, 特征融合, 跨域学习

## 3 点简述
- 核心问题：无参考点云质量评估模型在训练与测试数据分布不同时性能显著下降。
- 方法要点：采用两阶段粗到细对齐，包括基于质量差异的粗粒度对齐和感知融合的细粒度对齐。
- 实验或效果：实验验证UPDA能有效提升跨域场景下的评估性能，代码已开源。

## 摘要（原文）

> While no-reference point cloud quality assessment (NR-PCQA) approaches have achieved significant progress over the past decade, their performance often degrades substantially when a distribution gap exists between the training (source domain) and testing (target domain) data. However, to date, limited attention has been paid to transferring NR-PCQA models across domains. To address this challenge, we propose the first unsupervised progressive domain adaptation (UPDA) framework for NR-PCQA, which introduces a two-stage coarse-to-fine alignment paradigm to address domain shifts. At the coarse-grained stage, a discrepancy-aware coarse-grained alignment method is designed to capture relative quality relationships between cross-domain samples through a novel quality-discrepancy-aware hybrid loss, circumventing the challenges of direct absolute feature alignment. At the fine-grained stage, a perception fusion fine-grained alignment approach with symmetric feature fusion is developed to identify domain-invariant features, while a conditional discriminator selectively enhances the transfer of quality-relevant features. Extensive experiments demonstrate that the proposed UPDA effectively enhances the performance of NR-PCQA methods in cross-domain scenarios, validating its practical applicability. The code is available at https://github.com/yokeno1/UPDA-main.

