---
layout: default
title: LineGraph2Road: Structural Graph Reasoning on Line Graphs for Road Network Extraction
---

# LineGraph2Road: Structural Graph Reasoning on Line Graphs for Road Network Extraction
**arXiv**：[2602.23290v1](https://arxiv.org/abs/2602.23290) · [PDF](https://arxiv.org/pdf/2602.23290.pdf)  
**作者**：Zhengyang Wei, Renzhi Jing, Yiyi He, Jenny Suckale  

**一句话要点**：提出LineGraph2Road框架，通过线图结构推理改进卫星图像道路网络提取

**关键词**：道路网络提取, 图神经网络, 卫星图像分析, 线图变换, 结构推理, 连通性预测

## 3 点简述
- 核心问题：现有方法难以捕捉道路网络的长程依赖和复杂拓扑结构
- 方法要点：将连通性预测转化为稀疏欧几里得图边分类，在线图上应用图Transformer
- 实验效果：在City-scale等三个基准测试中取得TOPO-F1和APLS指标的先进结果

## 摘要（原文）

> The accurate and automatic extraction of roads from satellite imagery is critical for applications in navigation and urban planning, significantly reducing the need for manual annotation. Many existing methods decompose this task into keypoint extraction and connectedness prediction, but often struggle to capture long-range dependencies and complex topologies. Here, we propose LineGraph2Road, a framework that improves connectedness prediction by formulating it as binary classification over edges in a constructed global but sparse Euclidean graph, where nodes are keypoints extracted from segmentation masks and edges connect node pairs within a predefined distance threshold, representing potential road segments. To better learn structural link representation, we transform the original graph into its corresponding line graph and apply a Graph Transformer on it for connectedness prediction. This formulation overcomes the limitations of endpoint-embedding fusion on set-isomorphic links, enabling rich link representations and effective relational reasoning over the global structure. Additionally, we introduce an overpass/underpass head to resolve multi-level crossings and a coupled NMS strategy to preserve critical connections. We evaluate LineGraph2Road on three benchmarks: City-scale, SpaceNet, and Global-scale, and show that it achieves state-of-the-art results on two key metrics, TOPO-F1 and APLS. It also captures fine visual details critical for real-world deployment. We will make our code publicly available.

