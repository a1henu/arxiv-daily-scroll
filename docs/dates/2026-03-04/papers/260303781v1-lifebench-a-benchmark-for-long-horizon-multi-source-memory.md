---
layout: default
title: LifeBench: A Benchmark for Long-Horizon Multi-Source Memory
---

# LifeBench: A Benchmark for Long-Horizon Multi-Source Memory
**arXiv**：[2603.03781v1](https://arxiv.org/abs/2603.03781) · [PDF](https://arxiv.org/pdf/2603.03781.pdf)  
**作者**：Zihao Cheng, Weixin Wang, Yu Zhao, Ziyang Ren, Jiaxuan Chen, Ruiyang Xu, Shuai Huang, Yang Chen, Guowei Li, Mengshi Wang, Yi Xie, Ren Zhu, Zeren Jiang, Keda Lu, Yihong Li, Xiaoliang Wang, Liwei Liu, Cam-Tu Nguyen  

**一句话要点**：提出LifeBench基准以解决长时程多源记忆推理的评估难题

**关键词**：长时程记忆, 多源记忆推理, 事件模拟, 认知科学, 基准测试, 数据合成

## 3 点简述
- 现有记忆基准主要针对陈述性记忆，缺乏非陈述性记忆的推理评估
- 通过真实世界先验和事件层次结构，确保数据质量和可扩展性
- 实验显示顶级记忆系统准确率仅55.2%，突显基准的挑战性

## 摘要（原文）

> Long-term memory is fundamental for personalized agents capable of accumulating knowledge, reasoning over user experiences, and adapting across time. However, existing memory benchmarks primarily target declarative memory, specifically semantic and episodic types, where all information is explicitly presented in dialogues. In contrast, real-world actions are also governed by non-declarative memory, including habitual and procedural types, and need to be inferred from diverse digital traces. To bridge this gap, we introduce Lifebench, which features densely connected, long-horizon event simulation. It pushes AI agents beyond simple recall, requiring the integration of declarative and non-declarative memory reasoning across diverse and temporally extended contexts. Building such a benchmark presents two key challenges: ensuring data quality and scalability. We maintain data quality by employing real-world priors, including anonymized social surveys, map APIs, and holiday-integrated calendars, thus enforcing fidelity, diversity and behavioral rationality within the dataset. Towards scalability, we draw inspiration from cognitive science and structure events according to their partonomic hierarchy; enabling efficient parallel generation while maintaining global coherence. Performance results show that top-tier, state-of-the-art memory systems reach just 55.2\% accuracy, highlighting the inherent difficulty of long-horizon retrieval and multi-source integration within our proposed benchmark. The dataset and data synthesis code are available at https://github.com/1754955896/LifeBench.

