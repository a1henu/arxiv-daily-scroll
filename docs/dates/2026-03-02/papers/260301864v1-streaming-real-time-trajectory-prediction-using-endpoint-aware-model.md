---
layout: default
title: Streaming Real-Time Trajectory Prediction Using Endpoint-Aware Modeling
---

# Streaming Real-Time Trajectory Prediction Using Endpoint-Aware Modeling
**arXiv**：[2603.01864v1](https://arxiv.org/abs/2603.01864) · [PDF](https://arxiv.org/pdf/2603.01864.pdf)  
**作者**：Alexander Prutsch, David Schinagl, Horst Possegger  

**一句话要点**：提出基于端点感知建模的流式实时轨迹预测方法，以解决自动驾驶连续场景下的低延迟预测需求。

**关键词**：轨迹预测, 流式处理, 端点感知建模, 自动驾驶, 实时推理, 时序上下文

## 3 点简述
- 核心问题：现有轨迹预测多基于快照式独立处理，缺乏连续时序上下文，难以满足自动驾驶实时流式数据需求。
- 方法要点：利用先前预测的轨迹端点作为锚点，提取针对性场景编码，无需迭代优化或分段解码，实现轻量高效预测。
- 实验或效果：在Argoverse~2基准上达到最先进的流式预测结果，显著降低推理延迟，适合实际部署。

## 摘要（原文）

> Future trajectories of neighboring traffic agents have a significant influence on the path planning and decision-making of autonomous vehicles. While trajectory forecasting is a well-studied field, research mainly focuses on snapshot-based prediction, where each scenario is treated independently of its global temporal context. However, real-world autonomous driving systems need to operate in a continuous setting, requiring real-time processing of data streams with low latency and consistent predictions over successive timesteps. We leverage this continuous setting to propose a lightweight yet highly accurate streaming-based trajectory forecasting approach. We integrate valuable information from previous predictions with a novel endpoint-aware modeling scheme. Our temporal context propagation uses the trajectory endpoints of the previous forecasts as anchors to extract targeted scenario context encodings. Our approach efficiently guides its scene encoder to extract highly relevant context information without needing refinement iterations or segment-wise decoding. Our experiments highlight that our approach effectively relays information across consecutive timesteps. Unlike methods using multi-stage refinement processing, our approach significantly reduces inference latency, making it well-suited for real-world deployment. We achieve state-of-the-art streaming trajectory prediction results on the Argoverse~2 multi-agent and single-agent benchmarks, while requiring substantially fewer resources.

