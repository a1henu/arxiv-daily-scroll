---
layout: default
title: Learning to Reason in 4D: Dynamic Spatial Understanding for Vision Language Models
---

# Learning to Reason in 4D: Dynamic Spatial Understanding for Vision Language Models
**arXiv**：[2512.20557v1](https://arxiv.org/abs/2512.20557) · [PDF](https://arxiv.org/pdf/2512.20557.pdf)  
**作者**：Shengchao Zhou, Yuxin Chen, Yuying Ge, Wei Huang, Jiehong Lin, Ying Shan, Xiaojuan Qi  

**一句话要点**：提出DSR Suite以解决视觉语言模型在动态空间推理上的不足

**关键词**：动态空间推理, 4D感知训练, 几何选择模块, 视觉语言模型, 多选问答生成

## 3 点简述
- 核心问题：视觉语言模型在动态空间推理方面较弱，缺乏可扩展的4D感知训练资源。
- 方法要点：通过自动化管道生成多选问答对，并设计轻量级几何选择模块集成几何先验。
- 实验或效果：集成DSR-Train和GSM显著提升Qwen2.5-VL-7B的动态空间推理能力，保持通用视频理解准确性。

## 摘要（原文）

> Vision-language models (VLM) excel at general understanding yet remain weak at dynamic spatial reasoning (DSR), i.e., reasoning about the evolvement of object geometry and relationship in 3D space over time, largely due to the scarcity of scalable 4D-aware training resources. To bridge this gap across aspects of dataset, benchmark and model, we introduce DSR Suite. First, we propose an automated pipeline that generates multiple-choice question-answer pairs from in-the-wild videos for DSR. By leveraging modern vision foundation models, the pipeline extracts rich geometric and motion information, including camera poses, local point clouds, object masks, orientations, and 3D trajectories. These geometric cues enable the construction of DSR-Train for learning and further human-refined DSR-Bench for evaluation. Compared with previous works, our data emphasize (i) in-the-wild video sources, (ii) object- and scene-level 3D requirements, (iii) viewpoint transformations, (iv) multi-object interactions, and (v) fine-grained, procedural answers. Beyond data, we propose a lightweight Geometry Selection Module (GSM) to seamlessly integrate geometric priors into VLMs, which condenses question semantics and extracts question-relevant knowledge from pretrained 4D reconstruction priors into a compact set of geometry tokens. This targeted extraction avoids overwhelming the model with irrelevant knowledge. Experiments show that integrating DSR-Train and GSM into Qwen2.5-VL-7B significantly enhances its dynamic spatial reasoning capability, while maintaining accuracy on general video understanding benchmarks.

