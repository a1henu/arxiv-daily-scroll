---
layout: default
title: Beyond Seen Bounds: Class-Centric Polarization for Single-Domain Generalized Deep Metric Learning
---

# Beyond Seen Bounds: Class-Centric Polarization for Single-Domain Generalized Deep Metric Learning
**arXiv**：[2601.09121v1](https://arxiv.org/abs/2601.09121) · [PDF](https://arxiv.org/pdf/2601.09121.pdf)  
**作者**：Xin Yuan, Meiqi Wan, Wei Liu, Xin Xu, Zheng Wang  

**一句话要点**：提出CenterPolar框架，通过类中心极化策略解决单域广义深度度量学习中的类别与域偏移问题。

**关键词**：单域广义深度度量学习, 类中心极化, 域偏移泛化, 离心扩展, 向心约束, 未见类别识别

## 3 点简述
- 核心问题：单域广义深度度量学习面临测试时类别和域的双重偏移，现有方法生成样本集中于类代理附近，难以模拟实际广泛域偏移。
- 方法要点：CenterPolar包含离心扩展和向心约束两阶段，动态扩展并约束域分布，以学习更泛化的度量模型。
- 实验或效果：在多个数据集上验证优于现有方法，代码将在接受后发布。

## 摘要（原文）

> Single-domain generalized deep metric learning (SDG-DML) faces the dual challenge of both category and domain shifts during testing, limiting real-world applications. Therefore, aiming to learn better generalization ability on both unseen categories and domains is a realistic goal for the SDG-DML task. To deliver the aspiration, existing SDG-DML methods employ the domain expansion-equalization strategy to expand the source data and generate out-of-distribution samples. However, these methods rely on proxy-based expansion, which tends to generate samples clustered near class proxies, failing to simulate the broad and distant domain shifts encountered in practice. To alleviate the problem, we propose CenterPolar, a novel SDG-DML framework that dynamically expands and constrains domain distributions to learn a generalizable DML model for wider target domain distributions. Specifically, \textbf{CenterPolar} contains two collaborative class-centric polarization phases: (1) Class-Centric Centrifugal Expansion ($C^3E$) and (2) Class-Centric Centripetal Constraint ($C^4$). In the first phase, $C^3E$ drives the source domain distribution by shifting the source data away from class centroids using centrifugal expansion to generalize to more unseen domains. In the second phase, to consolidate domain-invariant class information for the generalization ability to unseen categories, $C^4$ pulls all seen and unseen samples toward their class centroids while enforcing inter-class separation via centripetal constraint. Extensive experimental results on widely used CUB-200-2011 Ext., Cars196 Ext., DomainNet, PACS, and Office-Home datasets demonstrate the superiority and effectiveness of our CenterPolar over existing state-of-the-art methods. The code will be released after acceptance.

