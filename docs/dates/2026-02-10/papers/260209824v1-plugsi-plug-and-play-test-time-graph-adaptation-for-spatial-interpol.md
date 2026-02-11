---
layout: default
title: PlugSI: Plug-and-Play Test-Time Graph Adaptation for Spatial Interpolation
---

# PlugSI: Plug-and-Play Test-Time Graph Adaptation for Spatial Interpolation
**arXiv**：[2602.09824v1](https://arxiv.org/abs/2602.09824) · [PDF](https://arxiv.org/pdf/2602.09824.pdf)  
**作者**：Xuhang Wu, Zhuoxuan Liang, Wei Li, Xiaohua Jia, Sumi Helal  

**一句话要点**：提出PlugSI框架，通过未知拓扑适配器和时序平衡适配器，增强图空间插值在测试时的自适应能力。

**关键词**：空间插值, 图神经网络, 测试时适应, 传感器网络, 自适应学习

## 3 点简述
- 核心问题：现有图空间插值方法依赖预训练模型，缺乏对测试时新图结构的自适应，且未充分利用测试数据。
- 方法要点：设计未知拓扑适配器（UTA）适应测试时小批量图结构，引入时序平衡适配器（TBA）维持历史共识以指导UTA并防止噪声漂移。
- 实验或效果：实验显示PlugSI可无缝集成现有方法，显著提升性能，如平均绝对误差降低10.81%。

## 摘要（原文）

> With the rapid advancement of IoT and edge computing, sensor networks have become indispensable, driving the need for large-scale sensor deployment. However, the high deployment cost hinders their scalability. To tackle the issues, Spatial Interpolation (SI) introduces virtual sensors to infer readings from observed sensors, leveraging graph structure. However, current graph-based SI methods rely on pre-trained models, lack adaptation to larger and unseen graphs at test-time, and overlook test data utilization. To address these issues, we propose PlugSI, a plug-and-play framework that refines test-time graph through two key innovations. First, we design an Unknown Topology Adapter (UTA) that adapts to the new graph structure of each small-batch at test-time, enhancing the generalization of SI pre-trained models. Second, we introduce a Temporal Balance Adapter (TBA) that maintains a stable historical consensus to guide UTA adaptation and prevent drifting caused by noise in the current batch. Empirically, extensive experiments demonstrate PlugSI can be seamlessly integrated into existing graph-based SI methods and provide significant improvement (e.g., a 10.81% reduction in MAE).

