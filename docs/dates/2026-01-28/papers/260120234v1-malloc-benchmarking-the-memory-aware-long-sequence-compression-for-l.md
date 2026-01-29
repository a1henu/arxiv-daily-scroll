---
layout: default
title: MALLOC: Benchmarking the Memory-aware Long Sequence Compression for Large Sequential Recommendation
---

# MALLOC: Benchmarking the Memory-aware Long Sequence Compression for Large Sequential Recommendation
**arXiv**：[2601.20234v1](https://arxiv.org/abs/2601.20234) · [PDF](https://arxiv.org/pdf/2601.20234.pdf)  
**作者**：Qihang Yu, Kairui Fu, Zhaocheng Du, Yuxuan Si, Kaiyuan Li, Weihao Zhao, Zhicheng Zhang, Jieming Zhu, Quanyu Dai, Zhenhua Dong, Shengyu Zhang, Kun Kuang, Fei Wu  

**一句话要点**：提出MALLOC基准以解决大规模序列推荐中内存感知长序列压缩问题

**关键词**：序列推荐, 内存压缩, 基准测试, 长序列依赖, 大规模推荐系统

## 3 点简述
- 核心问题：大规模推荐系统因长序列依赖导致内存存储开销巨大，现有方法忽视空间成本
- 方法要点：系统分类并集成内存管理技术至先进推荐器，构建可复现评估平台
- 实验或效果：通过准确性、效率和复杂性实验验证MALLOC在推进大规模推荐中的可靠性

## 摘要（原文）

> The scaling law, which indicates that model performance improves with increasing dataset and model capacity, has fueled a growing trend in expanding recommendation models in both industry and academia. However, the advent of large-scale recommenders also brings significantly higher computational costs, particularly under the long-sequence dependencies inherent in the user intent of recommendation systems. Current approaches often rely on pre-storing the intermediate states of the past behavior for each user, thereby reducing the quadratic re-computation cost for the following requests. Despite their effectiveness, these methods often treat memory merely as a medium for acceleration, without adequately considering the space overhead it introduces. This presents a critical challenge in real-world recommendation systems with billions of users, each of whom might initiate thousands of interactions and require massive memory for state storage. Fortunately, there have been several memory management strategies examined for compression in LLM, while most have not been evaluated on the recommendation task. To mitigate this gap, we introduce MALLOC, a comprehensive benchmark for memory-aware long sequence compression. MALLOC presents a comprehensive investigation and systematic classification of memory management techniques applicable to large sequential recommendations. These techniques are integrated into state-of-the-art recommenders, enabling a reproducible and accessible evaluation platform. Through extensive experiments across accuracy, efficiency, and complexity, we demonstrate the holistic reliability of MALLOC in advancing large-scale recommendation. Code is available at https://anonymous.4open.science/r/MALLOC.

