---
layout: default
title: SPOT!: Map-Guided LLM Agent for Unsupervised Multi-CCTV Dynamic Object Tracking
---

# SPOT!: Map-Guided LLM Agent for Unsupervised Multi-CCTV Dynamic Object Tracking
**arXiv**：[2512.20975v1](https://arxiv.org/abs/2512.20975) · [PDF](https://arxiv.org/pdf/2512.20975.pdf)  
**作者**：Yujin Noh, Inho Jake Park, Chigon Hwang  

**一句话要点**：提出SPOT地图引导LLM代理，以解决多CCTV盲区中车辆轨迹连续跟踪问题。

**关键词**：多CCTV跟踪, 盲区预测, 地图引导, LLM代理, 束搜索, CARLA仿真

## 3 点简述
- 核心问题：多CCTV环境中盲区导致车辆ID切换和轨迹丢失，影响实时路径预测可靠性。
- 方法要点：基于地图空间信息和车辆动态，通过束搜索预测盲区后最可能出现的CCTV位置。
- 实验或效果：在CARLA虚拟环境中验证，能准确预测盲区后CCTV，有效维持连续轨迹。

## 摘要（原文）

> CCTV-based vehicle tracking systems face structural limitations in continuously connecting the trajectories of the same vehicle across multiple camera environments. In particular, blind spots occur due to the intervals between CCTVs and limited Fields of View (FOV), which leads to object ID switching and trajectory loss, thereby reducing the reliability of real-time path prediction. This paper proposes SPOT (Spatial Prediction Over Trajectories), a map-guided LLM agent capable of tracking vehicles even in blind spots of multi-CCTV environments without prior training. The proposed method represents road structures (Waypoints) and CCTV placement information as documents based on 2D spatial coordinates and organizes them through chunking techniques to enable real-time querying and inference. Furthermore, it transforms the vehicle's position into the actual world coordinate system using the relative position and FOV information of objects observed in CCTV images. By combining map spatial information with the vehicle's moving direction, speed, and driving patterns, a beam search is performed at the intersection level to derive candidate CCTV locations where the vehicle is most likely to enter after the blind spot. Experimental results based on the CARLA simulator in a virtual city environment confirmed that the proposed method accurately predicts the next appearing CCTV even in blind spot sections, maintaining continuous vehicle trajectories more effectively than existing techniques.

