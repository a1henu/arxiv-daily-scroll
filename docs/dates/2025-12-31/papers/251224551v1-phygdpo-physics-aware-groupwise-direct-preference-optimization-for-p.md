---
layout: default
title: PhyGDPO: Physics-Aware Groupwise Direct Preference Optimization for Physically Consistent Text-to-Video Generation
---

# PhyGDPO: Physics-Aware Groupwise Direct Preference Optimization for Physically Consistent Text-to-Video Generation
**arXiv**：[2512.24551v1](https://arxiv.org/abs/2512.24551) · [PDF](https://arxiv.org/pdf/2512.24551.pdf)  
**作者**：Yuanhao Cai, Kunpeng Li, Menglin Jia, Jialiang Wang, Junzhe Sun, Feng Liang, Weifeng Chen, Felix Juefei-Xu, Chu Wang, Ali Thabet, Xiaoliang Dai, Xuan Ju, Alan Yuille, Ji Hou  

**一句话要点**：提出PhyGDPO框架以解决文本到视频生成中的物理一致性挑战

**关键词**：文本到视频生成, 物理一致性, 偏好优化, 视觉语言模型, 数据集构建, 高效训练

## 3 点简述
- 核心问题：现有文本到视频方法难以遵循物理定律，且缺乏物理交互训练数据
- 方法要点：构建PhyAugPipe数据管道收集大规模物理视频数据集，并设计PhyGDPO框架结合物理奖励优化
- 实验或效果：在PhyGenBench和VideoPhy2基准上显著优于开源方法，提升物理一致性

## 摘要（原文）

> Recent advances in text-to-video (T2V) generation have achieved good visual quality, yet synthesizing videos that faithfully follow physical laws remains an open challenge. Existing methods mainly based on graphics or prompt extension struggle to generalize beyond simple simulated environments or learn implicit physical reasoning. The scarcity of training data with rich physics interactions and phenomena is also a problem. In this paper, we first introduce a Physics-Augmented video data construction Pipeline, PhyAugPipe, that leverages a vision-language model (VLM) with chain-of-thought reasoning to collect a large-scale training dataset, PhyVidGen-135K. Then we formulate a principled Physics-aware Groupwise Direct Preference Optimization, PhyGDPO, framework that builds upon the groupwise Plackett-Luce probabilistic model to capture holistic preferences beyond pairwise comparisons. In PhyGDPO, we design a Physics-Guided Rewarding (PGR) scheme that embeds VLM-based physics rewards to steer optimization toward physical consistency. We also propose a LoRA-Switch Reference (LoRA-SR) scheme that eliminates memory-heavy reference duplication for efficient training. Experiments show that our method significantly outperforms state-of-the-art open-source methods on PhyGenBench and VideoPhy2. Please check our project page at https://caiyuanhao1998.github.io/project/PhyGDPO for more video results. Our code, models, and data will be released at https://github.com/caiyuanhao1998/Open-PhyGDPO

