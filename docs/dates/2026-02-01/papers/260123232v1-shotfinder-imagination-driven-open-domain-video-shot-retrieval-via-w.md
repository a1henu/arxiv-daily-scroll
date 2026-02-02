---
layout: default
title: ShotFinder: Imagination-Driven Open-Domain Video Shot Retrieval via Web Search
---

# ShotFinder: Imagination-Driven Open-Domain Video Shot Retrieval via Web Search
**arXiv**：[2601.23232v1](https://arxiv.org/abs/2601.23232) · [PDF](https://arxiv.org/pdf/2601.23232.pdf)  
**作者**：Tao Yu, Haopeng Jin, Hao Wang, Shenghua Chai, Yujia Yang, Junhao Gong, Jiaming Guo, Minghui Zhang, Xinlong Chen, Zhenghao Zhang, Yuxuan Zhou, Yanpei Gong, YuanCheng Liu, Yiming Ding, Kangwei Zeng, Pengfei Yang, Zhongtian Luo, Yufei Xiong, Shanbin Zhang, Shaoxiong Cheng, Huang Ruilin, Li Shuo, Yuxi Niu, Xinyuan Zhang, Yueya Xu, Jie Mao, Ruixuan Ji, Yaru Zhao, Mingchen Zhang, Jiabing Yang, Jiaqi Liu, YiFan Zhang, Hongzhu Yi, Xinming Wang, Cheng Zhong, Xiao Ma, Zhang Zhang, Yan Huang, Liang Wang  

**一句话要点**：提出ShotFinder基准与检索流程，以解决开放域视频镜头检索中缺乏系统评估的问题。

**关键词**：开放域视频检索, 镜头检索基准, 多模态大模型, 时序定位, 可控约束

## 3 点简述
- 核心问题：开放域视频镜头检索缺乏系统基准，涉及复杂时空语义与可控约束。
- 方法要点：构建基准并设计三阶段检索流程，包括查询扩展、候选检索和时序定位。
- 实验或效果：实验显示模型性能远低于人类，颜色和视觉风格约束是主要挑战。

## 摘要（原文）

> In recent years, large language models (LLMs) have made rapid progress in information retrieval, yet existing research has mainly focused on text or static multimodal settings. Open-domain video shot retrieval, which involves richer temporal structure and more complex semantics, still lacks systematic benchmarks and analysis. To fill this gap, we introduce ShotFinder, a benchmark that formalizes editing requirements as keyframe-oriented shot descriptions and introduces five types of controllable single-factor constraints: Temporal order, Color, Visual style, Audio, and Resolution. We curate 1,210 high-quality samples from YouTube across 20 thematic categories, using large models for generation with human verification. Based on the benchmark, we propose ShotFinder, a text-driven three-stage retrieval and localization pipeline: (1) query expansion via video imagination, (2) candidate video retrieval with a search engine, and (3) description-guided temporal localization. Experiments on multiple closed-source and open-source models reveal a significant gap to human performance, with clear imbalance across constraints: temporal localization is relatively tractable, while color and visual style remain major challenges. These results reveal that open-domain video shot retrieval is still a critical capability that multimodal large models have yet to overcome.

