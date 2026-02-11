---
layout: default
title: DexImit: Learning Bimanual Dexterous Manipulation from Monocular Human Videos
---

# DexImit: Learning Bimanual Dexterous Manipulation from Monocular Human Videos
**arXiv**：[2602.10105v1](https://arxiv.org/abs/2602.10105) · [PDF](https://arxiv.org/pdf/2602.10105.pdf)  
**作者**：Juncheng Mu, Sizhe Yang, Yiming Bao, Hojin Bae, Tianming Wei, Linning Xu, Boyi Li, Huazhe Xu, Jiangmiao Pang  

**一句话要点**：提出DexImit框架，从单目人类视频生成机器人数据以解决双手灵巧操作数据稀缺问题

**关键词**：双手灵巧操作, 视频到机器人数据转换, 本体差距, 零样本部署, 数据增强

## 3 点简述
- 核心问题：双手灵巧操作数据稀缺，人类视频与机器人存在本体差距，直接预训练困难
- 方法要点：四阶段流程，包括重建手物交互、分解子任务、合成轨迹和数据增强
- 实验或效果：能处理工具使用、长时程和精细操作任务，支持零样本真实世界部署

## 摘要（原文）

> Data scarcity fundamentally limits the generalization of bimanual dexterous manipulation, as real-world data collection for dexterous hands is expensive and labor-intensive. Human manipulation videos, as a direct carrier of manipulation knowledge, offer significant potential for scaling up robot learning. However, the substantial embodiment gap between human hands and robotic dexterous hands makes direct pretraining from human videos extremely challenging. To bridge this gap and unleash the potential of large-scale human manipulation video data, we propose DexImit, an automated framework that converts monocular human manipulation videos into physically plausible robot data, without any additional information. DexImit employs a four-stage generation pipeline: (1) reconstructing hand-object interactions from arbitrary viewpoints with near-metric scale; (2) performing subtask decomposition and bimanual scheduling; (3) synthesizing robot trajectories consistent with the demonstrated interactions; (4) comprehensive data augmentation for zero-shot real-world deployment. Building on these designs, DexImit can generate large-scale robot data based on human videos, either from the Internet or video generation models. DexImit is capable of handling diverse manipulation tasks, including tool use (e.g., cutting an apple), long-horizon tasks (e.g., making a beverage), and fine-grained manipulations (e.g., stacking cups).

