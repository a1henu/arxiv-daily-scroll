---
layout: default
title: SynAD: Enhancing Real-World End-to-End Autonomous Driving Models through Synthetic Data Integration
---

# SynAD: Enhancing Real-World End-to-End Autonomous Driving Models through Synthetic Data Integration
**arXiv**：[2510.24052v1](https://arxiv.org/abs/2510.24052) · [PDF](https://arxiv.org/pdf/2510.24052.pdf)  
**作者**：Jongsuk Kim, Jaeyoung Lee, Gyojin Han, Dongjae Lee, Minki Jeong, Junmo Kim  

**一句话要点**：提出SynAD框架，通过合成数据集成增强端到端自动驾驶模型

**关键词**：端到端自动驾驶, 合成数据集成, 鸟瞰图特征, 多智能体场景, 安全性能增强

## 3 点简述
- 核心问题：真实世界数据限制训练场景多样性，合成场景缺乏指定自车和传感器输入。
- 方法要点：在多智能体合成场景中指定自车，使用Map-to-BEV网络生成鸟瞰图特征。
- 实验或效果：实验显示SynAD有效整合组件，显著提升安全性能。

## 摘要（原文）

> Recent advancements in deep learning and the availability of high-quality
> real-world driving datasets have propelled end-to-end autonomous driving.
> Despite this progress, relying solely on real-world data limits the variety of
> driving scenarios for training. Synthetic scenario generation has emerged as a
> promising solution to enrich the diversity of training data; however, its
> application within E2E AD models remains largely unexplored. This is primarily
> due to the absence of a designated ego vehicle and the associated sensor
> inputs, such as camera or LiDAR, typically provided in real-world scenarios. To
> address this gap, we introduce SynAD, the first framework designed to enhance
> real-world E2E AD models using synthetic data. Our method designates the agent
> with the most comprehensive driving information as the ego vehicle in a
> multi-agent synthetic scenario. We further project path-level scenarios onto
> maps and employ a newly developed Map-to-BEV Network to derive bird's-eye-view
> features without relying on sensor inputs. Finally, we devise a training
> strategy that effectively integrates these map-based synthetic data with real
> driving data. Experimental results demonstrate that SynAD effectively
> integrates all components and notably enhances safety performance. By bridging
> synthetic scenario generation and E2E AD, SynAD paves the way for more
> comprehensive and robust autonomous driving models.

