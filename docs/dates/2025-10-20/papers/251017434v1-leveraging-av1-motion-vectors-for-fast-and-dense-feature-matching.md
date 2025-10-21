---
layout: default
title: Leveraging AV1 motion vectors for Fast and Dense Feature Matching
---

# Leveraging AV1 motion vectors for Fast and Dense Feature Matching
**arXiv**：[2510.17434v1](https://arxiv.org/abs/2510.17434) · [PDF](https://arxiv.org/pdf/2510.17434.pdf)  
**作者**：Julien Zouein, Hossein Javidnia, François Pitié, Anil Kokaram  

**一句话要点**：利用AV1运动矢量实现快速密集特征匹配，作为资源高效的前端方法

**关键词**：运动矢量利用, 密集特征匹配, 压缩域处理, 结构从运动, 资源优化, 视频分析

## 3 点简述
- 核心问题：传统特征匹配方法如SIFT计算密集，资源消耗大，难以扩展到长视频。
- 方法要点：重新利用AV1压缩域的运动矢量，生成密集亚像素对应和余弦一致性过滤的短轨迹。
- 实验效果：在短视频上，匹配密度高，重建点数达46万-62万，重投影误差0.51-0.53像素。

## 摘要（原文）

> We repurpose AV1 motion vectors to produce dense sub-pixel correspondences
> and short tracks filtered by cosine consistency. On short videos, this
> compressed-domain front end runs comparably to sequential SIFT while using far
> less CPU, and yields denser matches with competitive pairwise geometry. As a
> small SfM demo on a 117-frame clip, MV matches register all images and
> reconstruct 0.46-0.62M points at 0.51-0.53,px reprojection error; BA time grows
> with match density. These results show compressed-domain correspondences are a
> practical, resource-efficient front end with clear paths to scaling in full
> pipelines.

