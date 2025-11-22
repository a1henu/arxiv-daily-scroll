---
layout: default
title: Video-as-Answer: Predict and Generate Next Video Event with Joint-GRPO
---

# Video-as-Answer: Predict and Generate Next Video Event with Joint-GRPO
**arXiv**：[2511.16669v1](https://arxiv.org/abs/2511.16669) · [PDF](https://arxiv.org/pdf/2511.16669.pdf)  
**作者**：Junhao Cheng, Liang Hou, Xin Tao, Jing Liao  

**一句话要点**：提出VANS模型以解决视频作为答案的下一个事件预测问题

**关键词**：视频生成, 下一个事件预测, 强化学习, 视觉语言模型, 视频扩散模型, 多模态对齐

## 3 点简述
- 核心问题：视频生成未充分利用于回答预测性问题，需生成动态视频响应
- 方法要点：使用Joint-GRPO强化学习对齐视觉语言模型和视频扩散模型
- 实验或效果：在程序性和预测性基准上实现最先进性能，并发布数据集和代码

## 摘要（原文）

> While language models have become impactful in many real-world applications, video generation remains largely confined to entertainment. Motivated by video's inherent capacity to demonstrate physical-world information that is difficult to convey through language alone (e.g., imagine teaching someone to tie a tie using only text), we identify an underutilized opportunity to extend video as a new answer modality for Next-Event Prediction (NEP), formalized as Video-Next-Event Prediction (VNEP). While the established NEP task takes a video with a procedural or predictive question as input to predict the next event in text, VNEP requires dynamic video responses. This shift from telling to showing unlocks more intuitive and customized answers for procedural learning and creative exploration. However, this task remains challenging for existing models, as it demands an understanding of multimodal input, instruction-conditioned reasoning, and the generation of video with visual and semantic consistency. To address this, we introduce VANS, a model that leverages reinforcement learning to align a Vision-Language Model (VLM) with a Video Diffusion Model (VDM) for VNEP. The core of VANS is our proposed Joint-GRPO that orchestrates the VLM and VDM to function as a unit. Driven by a shared reward on their respective output, it optimizes the VLM to produce captions that are both accurate and friendly to visualize, while guiding the VDM to generate videos that are faithful to these captions and the input visual context. To enable this learning, we craft VANS-Data-100K, a dedicated dataset for the VNEP task. Experiments on procedural and predictive benchmarks demonstrate that VANS achieves state-of-the-art performance in both video event prediction and visualization. Codes are released in https://github.com/KlingTeam/VANS.

