---
layout: default
title: XPRESS: X-Band Radar Place Recognition via Elliptical Scan Shaping
---

# XPRESS: X-Band Radar Place Recognition via Elliptical Scan Shaping
**arXiv**：[2511.08863v1](https://arxiv.org/abs/2511.08863) · [PDF](https://arxiv.org/pdf/2511.08863.pdf)  
**作者**：Hyesu Jang, Wooseong Yang, Ayoung Kim, Dongje Lee, Hanguen Kim  

**一句话要点**：提出XPRESS算法以解决X波段雷达在海上自主导航中的位置识别问题

**关键词**：X波段雷达, 位置识别, 海上自主导航, 物体密度规则, 雷达检测降级, 鲁棒检索

## 3 点简述
- 核心问题：X波段雷达分辨率低、信息不足，限制其在自主导航中的应用
- 方法要点：采用基于物体密度的候选选择规则和故意降级检测以提升鲁棒性
- 实验或效果：在公共和自采数据集上评估，性能优于现有雷达位置识别方法

## 摘要（原文）

> X-band radar serves as the primary sensor on maritime vessels, however, its application in autonomous navigation has been limited due to low sensor resolution and insufficient information content. To enable X-band radar-only autonomous navigation in maritime environments, this paper proposes a place recognition algorithm specifically tailored for X-band radar, incorporating an object density-based rule for efficient candidate selection and intentional degradation of radar detections to achieve robust retrieval performance. The proposed algorithm was evaluated on both public maritime radar datasets and our own collected dataset, and its performance was compared against state-of-the-art radar place recognition methods. An ablation study was conducted to assess the algorithm's performance sensitivity with respect to key parameters.

