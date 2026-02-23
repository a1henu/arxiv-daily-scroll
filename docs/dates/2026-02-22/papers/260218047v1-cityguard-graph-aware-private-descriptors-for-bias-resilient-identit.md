---
layout: default
title: CityGuard: Graph-Aware Private Descriptors for Bias-Resilient Identity Search Across Urban Cameras
---

# CityGuard: Graph-Aware Private Descriptors for Bias-Resilient Identity Search Across Urban Cameras
**arXiv**：[2602.18047v1](https://arxiv.org/abs/2602.18047) · [PDF](https://arxiv.org/pdf/2602.18047.pdf)  
**作者**：Rong Fu, Wenxin Zhang, Yibo Meng, Jia Yee Tan, Jiaxuan Lu, Rui Lu, Jiekai Wu, Zhaolu Kang, Simon Fong  

**一句话要点**：提出CityGuard，一种图感知私有描述符框架，用于跨城市摄像头的偏置弹性身份搜索

**关键词**：人员重识别, 隐私保护, 图神经网络, 差分隐私, 城市监控, 跨摄像头检索

## 3 点简述
- 核心问题：跨分布式摄像头的人员重识别需处理视角、遮挡和域偏移，同时遵守数据保护规则，防止共享原始图像。
- 方法要点：集成分散自适应度量学习、空间条件注意力和差分私有嵌入，结合紧凑近似索引，实现隐私保护下的高效检索。
- 实验效果：在Market-1501等基准测试中，检索精度和查询吞吐量优于基线，验证了隐私关键城市身份匹配的实用性。

## 摘要（原文）

> City-scale person re-identification across distributed cameras must handle severe appearance changes from viewpoint, occlusion, and domain shift while complying with data protection rules that prevent sharing raw imagery. We introduce CityGuard, a topology-aware transformer for privacy-preserving identity retrieval in decentralized surveillance. The framework integrates three components. A dispersion-adaptive metric learner adjusts instance-level margins according to feature spread, increasing intra-class compactness. Spatially conditioned attention injects coarse geometry, such as GPS or deployment floor plans, into graph-based self-attention to enable projectively consistent cross-view alignment using only coarse geometric priors without requiring survey-grade calibration. Differentially private embedding maps are coupled with compact approximate indexes to support secure and cost-efficient deployment. Together these designs produce descriptors robust to viewpoint variation, occlusion, and domain shifts, and they enable a tunable balance between privacy and utility under rigorous differential-privacy accounting. Experiments on Market-1501 and additional public benchmarks, complemented by database-scale retrieval studies, show consistent gains in retrieval precision and query throughput over strong baselines, confirming the practicality of the framework for privacy-critical urban identity matching.

