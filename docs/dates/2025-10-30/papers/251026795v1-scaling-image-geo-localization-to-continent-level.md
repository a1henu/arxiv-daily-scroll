---
layout: default
title: Scaling Image Geo-Localization to Continent Level
---

# Scaling Image Geo-Localization to Continent Level
**arXiv**：[2510.26795v1](https://arxiv.org/abs/2510.26795) · [PDF](https://arxiv.org/pdf/2510.26795.pdf)  
**作者**：Philipp Lindenberger, Paul-Edouard Sarlin, Jan Hosang, Matteo Balice, Marc Pollefeys, Simon Lynen, Eduard Trulls  

**一句话要点**：提出混合方法实现大洲尺度细粒度图像地理定位

**关键词**：图像地理定位, 细粒度检索, 代理分类, 航空图像嵌入, 大规模数据集

## 3 点简述
- 全球图像地理定位因数据量大和覆盖不足而效率低下
- 结合代理分类和航空图像嵌入，学习丰富特征表示
- 在欧洲数据集上，68%以上查询定位误差小于200米

## 摘要（原文）

> Determining the precise geographic location of an image at a global scale
> remains an unsolved challenge. Standard image retrieval techniques are
> inefficient due to the sheer volume of images (>100M) and fail when coverage is
> insufficient. Scalable solutions, however, involve a trade-off: global
> classification typically yields coarse results (10+ kilometers), while
> cross-view retrieval between ground and aerial imagery suffers from a domain
> gap and has been primarily studied on smaller regions. This paper introduces a
> hybrid approach that achieves fine-grained geo-localization across a large
> geographic expanse the size of a continent. We leverage a proxy classification
> task during training to learn rich feature representations that implicitly
> encode precise location information. We combine these learned prototypes with
> embeddings of aerial imagery to increase robustness to the sparsity of
> ground-level data. This enables direct, fine-grained retrieval over areas
> spanning multiple countries. Our extensive evaluation demonstrates that our
> approach can localize within 200m more than 68\% of queries of a dataset
> covering a large part of Europe. The code is publicly available at
> https://scaling-geoloc.github.io.

