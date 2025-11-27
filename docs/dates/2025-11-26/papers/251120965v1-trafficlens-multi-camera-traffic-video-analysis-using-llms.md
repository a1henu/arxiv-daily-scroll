---
layout: default
title: TrafficLens: Multi-Camera Traffic Video Analysis Using LLMs
---

# TrafficLens: Multi-Camera Traffic Video Analysis Using LLMs
**arXiv**：[2511.20965v1](https://arxiv.org/abs/2511.20965) · [PDF](https://arxiv.org/pdf/2511.20965.pdf)  
**作者**：Md Adnan Arefeen, Biplob Debnath, Srimat Chakradhar  

**一句话要点**：提出TrafficLens算法以解决多摄像头交通视频分析效率问题

**关键词**：多摄像头视频分析, 交通监控, 视觉语言模型, 序列处理, 对象相似性检测, 效率优化

## 3 点简述
- 核心问题：多摄像头交通视频数据量大，视频转文本过程耗时，影响实时分析。
- 方法要点：采用序列化VLM处理，利用摄像头重叠区域和对象相似性检测减少冗余。
- 实验或效果：真实数据集测试显示，转换时间减少高达4倍，信息准确性保持。

## 摘要（原文）

> Traffic cameras are essential in urban areas, playing a crucial role in intelligent transportation systems. Multiple cameras at intersections enhance law enforcement capabilities, traffic management, and pedestrian safety. However, efficiently managing and analyzing multi-camera feeds poses challenges due to the vast amount of data. Analyzing such huge video data requires advanced analytical tools. While Large Language Models (LLMs) like ChatGPT, equipped with retrieval-augmented generation (RAG) systems, excel in text-based tasks, integrating them into traffic video analysis demands converting video data into text using a Vision-Language Model (VLM), which is time-consuming and delays the timely utilization of traffic videos for generating insights and investigating incidents. To address these challenges, we propose TrafficLens, a tailored algorithm for multi-camera traffic intersections. TrafficLens employs a sequential approach, utilizing overlapping coverage areas of cameras. It iteratively applies VLMs with varying token limits, using previous outputs as prompts for subsequent cameras, enabling rapid generation of detailed textual descriptions while reducing processing time. Additionally, TrafficLens intelligently bypasses redundant VLM invocations through an object-level similarity detector. Experimental results with real-world datasets demonstrate that TrafficLens reduces video-to-text conversion time by up to $4\times$ while maintaining information accuracy.

