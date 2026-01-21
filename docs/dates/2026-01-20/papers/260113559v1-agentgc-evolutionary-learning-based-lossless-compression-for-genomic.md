---
layout: default
title: AgentGC: Evolutionary Learning-based Lossless Compression for Genomics Data with LLM-driven Multiple Agent
---

# AgentGC: Evolutionary Learning-based Lossless Compression for Genomics Data with LLM-driven Multiple Agent
**arXiv**：[2601.13559v1](https://arxiv.org/abs/2601.13559) · [PDF](https://arxiv.org/pdf/2601.13559.pdf)  
**作者**：Sun Hui, Ding Yanfeng, Huidong Ma, Chang Xu, Keyan Jin, Lizheng Zu, Cheng Zhong, xiaoguang Liu, Gang Wang, Wentong Cai  

**一句话要点**：提出AgentGC，一种基于进化学习的无损压缩方法，用于基因组数据，通过LLM驱动的多智能体解决建模、适应性和界面问题。

**关键词**：基因组数据压缩, 进化学习, 多智能体系统, 大语言模型, 无损压缩, 联合优化

## 3 点简述
- 核心问题：现有基于学习的方法在基因组数据压缩中建模层次低、适应性有限且界面不友好。
- 方法要点：采用三层多智能体架构，结合LLM进行算法-数据集-系统联合优化，支持压缩比、吞吐量和平衡三种模式。
- 实验或效果：在9个数据集上对比14个基线，平均压缩比提升约16%，吞吐量提升最高达9.23倍。

## 摘要（原文）

> Lossless compression has made significant advancements in Genomics Data (GD) storage, sharing and management. Current learning-based methods are non-evolvable with problems of low-level compression modeling, limited adaptability, and user-unfriendly interface. To this end, we propose AgentGC, the first evolutionary Agent-based GD Compressor, consisting of 3 layers with multi-agent named Leader and Worker. Specifically, the 1) User layer provides a user-friendly interface via Leader combined with LLM; 2) Cognitive layer, driven by the Leader, integrates LLM to consider joint optimization of algorithm-dataset-system, addressing the issues of low-level modeling and limited adaptability; and 3) Compression layer, headed by Worker, performs compression & decompression via a automated multi-knowledge learning-based compression framework. On top of AgentGC, we design 3 modes to support diverse scenarios: CP for compression-ratio priority, TP for throughput priority, and BM for balanced mode. Compared with 14 baselines on 9 datasets, the average compression ratios gains are 16.66%, 16.11%, and 16.33%, the throughput gains are 4.73x, 9.23x, and 9.15x, respectively.

