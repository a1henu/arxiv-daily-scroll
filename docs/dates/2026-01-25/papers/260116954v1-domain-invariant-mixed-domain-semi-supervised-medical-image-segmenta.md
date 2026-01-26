---
layout: default
title: Domain-invariant Mixed-domain Semi-supervised Medical Image Segmentation with Clustered Maximum Mean Discrepancy Alignment
---

# Domain-invariant Mixed-domain Semi-supervised Medical Image Segmentation with Clustered Maximum Mean Discrepancy Alignment
**arXiv**：[2601.16954v1](https://arxiv.org/abs/2601.16954) · [PDF](https://arxiv.org/pdf/2601.16954.pdf)  
**作者**：Ba-Thinh Lam, Thanh-Huy Nguyen, Hoang-Thien Nguyen, Quang-Khai Bui-Tran, Nguyen Lan Vi Vu, Phat K. Huynh, Ulas Bagci, Min Xu  

**一句话要点**：提出基于聚类最大均值差异对齐的域不变混合域半监督医学图像分割框架，以解决标注稀缺和未知多域差异问题。

**关键词**：医学图像分割, 半监督学习, 域适应, 聚类对齐, 最大均值差异, 混合域处理

## 3 点简述
- 核心问题：医学图像分割中标注稀缺且数据来自多扫描器或中心，导致未知域标签和严重域差异。
- 方法要点：结合复制粘贴机制增强数据多样性，使用聚类最大均值差异块对齐未标记特征与标记锚点，促进域不变表示。
- 实验或效果：在Fundus和M&Ms基准测试中超越现有半监督和域适应方法，实现鲁棒精确分割。

## 摘要（原文）

> Deep learning has shown remarkable progress in medical image semantic segmentation, yet its success heavily depends on large-scale expert annotations and consistent data distributions. In practice, annotations are scarce, and images are collected from multiple scanners or centers, leading to mixed-domain settings with unknown domain labels and severe domain gaps. Existing semi-supervised or domain adaptation approaches typically assume either a single domain shift or access to explicit domain indices, which rarely hold in real-world deployment. In this paper, we propose a domain-invariant mixed-domain semi-supervised segmentation framework that jointly enhances data diversity and mitigates domain bias. A Copy-Paste Mechanism (CPM) augments the training set by transferring informative regions across domains, while a Cluster Maximum Mean Discrepancy (CMMD) block clusters unlabeled features and aligns them with labeled anchors via an MMD objective, encouraging domain-invariant representations. Integrated within a teacher-student framework, our method achieves robust and precise segmentation even with very few labeled examples and multiple unknown domain discrepancies. Experiments on Fundus and M&Ms benchmarks demonstrate that our approach consistently surpasses semi-supervised and domain adaptation methods, establishing a potential solution for mixed-domain semi-supervised medical image segmentation.

