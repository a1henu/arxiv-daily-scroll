---
layout: default
title: Beyond Endpoints: Path-Centric Reasoning for Vectorized Off-Road Network Extraction
---

# Beyond Endpoints: Path-Centric Reasoning for Vectorized Off-Road Network Extraction
**arXiv**：[2512.10416v1](https://arxiv.org/abs/2512.10416) · [PDF](https://arxiv.org/pdf/2512.10416.pdf)  
**作者**：Wenfei Guan, Jilin Mei, Tong Shen, Xumin Wu, Shuo Wang, Cheng Min, Yu Hu  

**一句话要点**：提出路径中心框架MaGRoad和数据集WildRoad，以解决越野环境矢量路网提取的挑战。

**关键词**：矢量路网提取, 越野环境, 路径中心推理, 多尺度聚合, 数据集构建, 快速推理

## 3 点简述
- 核心问题：现有模型在越野场景中因稀疏端点推理和拓扑错误而表现不佳。
- 方法要点：引入路径中心框架，沿候选路径聚合多尺度视觉证据以稳健推断连通性。
- 实验或效果：在WildRoad基准上达到先进性能，推理速度提升约2.5倍。

## 摘要（原文）

> Deep learning has advanced vectorized road extraction in urban settings, yet off-road environments remain underexplored and challenging. A significant domain gap causes advanced models to fail in wild terrains due to two key issues: lack of large-scale vectorized datasets and structural weakness in prevailing methods. Models such as SAM-Road employ a node-centric paradigm that reasons at sparse endpoints, making them fragile to occlusions and ambiguous junctions in off-road scenes, leading to topological errors.This work addresses these limitations in two complementary ways. First, we release WildRoad, a gloabal off-road road network dataset constructed efficiently with a dedicated interactive annotation tool tailored for road-network labeling. Second, we introduce MaGRoad (Mask-aware Geodesic Road network extractor), a path-centric framework that aggregates multi-scale visual evidence along candidate paths to infer connectivity robustly.Extensive experiments show that MaGRoad achieves state-of-the-art performance on our challenging WildRoad benchmark while generalizing well to urban datasets. A streamlined pipeline also yields roughly 2.5x faster inference, improving practical applicability. Together, the dataset and path-centric paradigm provide a stronger foundation for mapping roads in the wild.

