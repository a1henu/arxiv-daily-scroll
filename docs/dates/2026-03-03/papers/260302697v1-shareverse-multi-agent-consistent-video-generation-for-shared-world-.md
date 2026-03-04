---
layout: default
title: ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling
---

# ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling
**arXiv**：[2603.02697v1](https://arxiv.org/abs/2603.02697) · [PDF](https://arxiv.org/pdf/2603.02697.pdf)  
**作者**：Jiayi Zhu, Jianing Zhang, Yiying Yang, Wei Cheng, Xiaoyun Yuan  

**一句话要点**：提出ShareVerse框架，通过多代理交互实现共享世界建模的视频生成

**关键词**：多代理视频生成, 共享世界建模, 跨代理注意力, 空间拼接策略, CARLA仿真数据集

## 3 点简述
- 核心问题：现有视频生成方法缺乏多代理交互的统一共享世界建模支持
- 方法要点：构建大规模多代理交互数据集，采用空间拼接策略和跨代理注意力块
- 实验或效果：支持49帧大规模视频生成，准确感知动态代理位置，实现共享世界一致性

## 摘要（原文）

> This paper presents ShareVerse, a video generation framework enabling multi-agent shared world modeling, addressing the gap in existing works that lack support for unified shared world construction with multi-agent interaction. ShareVerse leverages the generation capability of large video models and integrates three key innovations: 1) A dataset for large-scale multi-agent interactive world modeling is built on the CARLA simulation platform, featuring diverse scenes, weather conditions, and interactive trajectories with paired multi-view videos (front/ rear/ left/ right views per agent) and camera data. 2) We propose a spatial concatenation strategy for four-view videos of independent agents to model a broader environment and to ensure internal multi-view geometric consistency. 3) We integrate cross-agent attention blocks into the pretrained video model, which enable interactive transmission of spatial-temporal information across agents, guaranteeing shared world consistency in overlapping regions and reasonable generation in non-overlapping regions. ShareVerse, which supports 49-frame large-scale video generation, accurately perceives the position of dynamic agents and achieves consistent shared world modeling.

