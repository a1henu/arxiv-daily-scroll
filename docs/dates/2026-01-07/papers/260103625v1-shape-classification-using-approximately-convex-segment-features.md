---
layout: default
title: Shape Classification using Approximately Convex Segment Features
---

# Shape Classification using Approximately Convex Segment Features
**arXiv**：[2601.03625v1](https://arxiv.org/abs/2601.03625) · [PDF](https://arxiv.org/pdf/2601.03625.pdf)  
**作者**：Bimal Kumar Ray  

**一句话要点**：提出基于近似凸段特征排序的形状分类方法，以消除对象对齐需求。

**关键词**：形状分类, 近似凸段特征, 特征排序, 边界归一化, 相似性度量

## 3 点简述
- 核心问题：现有基于描述性特征的物体分类技术依赖对象对齐来计算相似性，限制了应用灵活性。
- 方法要点：通过归一化边界、分割为近似凸段并按长度排序，提取长度、极点数、面积等特征袋进行相似性度量。
- 实验或效果：在数据集上测试，观察到可接受的结果，验证了方法的有效性。

## 摘要（原文）

> The existing object classification techniques based on descriptive features rely on object alignment to compute the similarity of objects for classification. This paper replaces the necessity of object alignment through sorting of feature. The object boundary is normalized and segmented into approximately convex segments and the segments are then sorted in descending order of their length. The segment length, number of extreme points in segments, area of segments, the base and the width of the segments - a bag of features - is used to measure the similarity between image boundaries. The proposed method is tested on datasets and acceptable results are observed.

