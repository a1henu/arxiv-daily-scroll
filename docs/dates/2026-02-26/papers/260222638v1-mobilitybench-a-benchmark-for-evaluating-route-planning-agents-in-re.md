---
layout: default
title: MobilityBench: A Benchmark for Evaluating Route-Planning Agents in Real-World Mobility Scenarios
---

# MobilityBench: A Benchmark for Evaluating Route-Planning Agents in Real-World Mobility Scenarios
**arXiv**：[2602.22638v1](https://arxiv.org/abs/2602.22638) · [PDF](https://arxiv.org/pdf/2602.22638.pdf)  
**作者**：Zhiheng Song, Jingshuai Zhang, Chuan Qin, Chao Wang, Chao Chen, Longfei Xu, Kaikui Liu, Xiangxiang Chu, Hengshu Zhu  

**一句话要点**：提出MobilityBench基准以评估现实世界移动场景中的路线规划智能体

**关键词**：路线规划基准, 大语言模型评估, 移动场景, 可复现性, 多维度评估

## 3 点简述
- 核心问题：现实世界移动场景中LLM路线规划智能体评估缺乏系统性，受制于多样需求和非确定性服务。
- 方法要点：基于真实用户查询构建基准，设计确定性API重放沙盒确保可复现性，提出多维度评估协议。
- 实验或效果：评估显示模型在基础任务上表现良好，但在偏好约束路线规划上存在显著不足。

## 摘要（原文）

> Route-planning agents powered by large language models (LLMs) have emerged as a promising paradigm for supporting everyday human mobility through natural language interaction and tool-mediated decision making. However, systematic evaluation in real-world mobility settings is hindered by diverse routing demands, non-deterministic mapping services, and limited reproducibility. In this study, we introduce MobilityBench, a scalable benchmark for evaluating LLM-based route-planning agents in real-world mobility scenarios. MobilityBench is constructed from large-scale, anonymized real user queries collected from Amap and covers a broad spectrum of route-planning intents across multiple cities worldwide. To enable reproducible, end-to-end evaluation, we design a deterministic API-replay sandbox that eliminates environmental variance from live services. We further propose a multi-dimensional evaluation protocol centered on outcome validity, complemented by assessments of instruction understanding, planning, tool use, and efficiency. Using MobilityBench, we evaluate multiple LLM-based route-planning agents across diverse real-world mobility scenarios and provide an in-depth analysis of their behaviors and performance. Our findings reveal that current models perform competently on Basic information retrieval and Route Planning tasks, yet struggle considerably with Preference-Constrained Route Planning, underscoring significant room for improvement in personalized mobility applications. We publicly release the benchmark data, evaluation toolkit, and documentation at https://github.com/AMAP-ML/MobilityBench .

