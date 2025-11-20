---
layout: default
title: GeoVista: Web-Augmented Agentic Visual Reasoning for Geolocalization
---

# GeoVista: Web-Augmented Agentic Visual Reasoning for Geolocalization
**arXiv**：[2511.15705v1](https://arxiv.org/abs/2511.15705) · [PDF](https://arxiv.org/pdf/2511.15705.pdf)  
**作者**：Yikun Wang, Zuyan Liu, Ziyi Wang, Pengfei Liu, Han Hu, Yongming Rao  

**一句话要点**：提出GeoVista代理模型以解决地理定位任务中的视觉推理与网络搜索集成问题

**关键词**：地理定位, 代理视觉推理, 工具集成, 强化学习, 基准构建, 网络搜索

## 3 点简述
- 核心问题：现有代理视觉推理模型缺乏通用性，地理定位任务需高分辨率图像和网络搜索验证
- 方法要点：集成图像放大和网络搜索工具，采用监督微调与强化学习训练管道
- 实验或效果：在GeoBench基准上超越开源模型，性能接近闭源模型如Gemini-2.5-flash

## 摘要（原文）

> Current research on agentic visual reasoning enables deep multimodal understanding but primarily focuses on image manipulation tools, leaving a gap toward more general-purpose agentic models. In this work, we revisit the geolocalization task, which requires not only nuanced visual grounding but also web search to confirm or refine hypotheses during reasoning. Since existing geolocalization benchmarks fail to meet the need for high-resolution imagery and the localization challenge for deep agentic reasoning, we curate GeoBench, a benchmark that includes photos and panoramas from around the world, along with a subset of satellite images of different cities to rigorously evaluate the geolocalization ability of agentic models. We also propose GeoVista, an agentic model that seamlessly integrates tool invocation within the reasoning loop, including an image-zoom-in tool to magnify regions of interest and a web-search tool to retrieve related web information. We develop a complete training pipeline for it, including a cold-start supervised fine-tuning (SFT) stage to learn reasoning patterns and tool-use priors, followed by a reinforcement learning (RL) stage to further enhance reasoning ability. We adopt a hierarchical reward to leverage multi-level geographical information and improve overall geolocalization performance. Experimental results show that GeoVista surpasses other open-source agentic models on the geolocalization task greatly and achieves performance comparable to closed-source models such as Gemini-2.5-flash and GPT-5 on most metrics.

