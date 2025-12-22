---
layout: default
title: Visually Prompted Benchmarks Are Surprisingly Fragile
---

# Visually Prompted Benchmarks Are Surprisingly Fragile
**arXiv**：[2512.17875v1](https://arxiv.org/abs/2512.17875) · [PDF](https://arxiv.org/pdf/2512.17875.pdf)  
**作者**：Haiwen Feng, Long Lian, Lisa Dunlap, Jiahao Shu, XuDong Wang, Renhao Wang, Trevor Darrell, Alane Suhr, Angjoo Kanazawa  

**一句话要点**：揭示视觉提示基准的脆弱性并提出VPBench以稳定评估视觉语言模型

**关键词**：视觉语言模型评估, 视觉提示基准, 模型脆弱性, 视觉标记设计, 数据集规模影响, JPEG压缩效应

## 3 点简述
- 核心问题：视觉提示基准中视觉标记细节（如颜色、大小）和数据集规模对模型性能排名有显著影响，导致评估不稳定
- 方法要点：通过评估九种视觉语言模型，分析视觉标记设计、数据集大小和低层推理选择（如JPEG压缩）对基准结果的影响
- 实验或效果：创建VPBench基准，包含16种视觉标记变体，以减轻脆弱性，提升评估可靠性

## 摘要（原文）

> A key challenge in evaluating VLMs is testing models' ability to analyze visual content independently from their textual priors. Recent benchmarks such as BLINK probe visual perception through visual prompting, where questions about visual content are paired with coordinates to which the question refers, with the coordinates explicitly marked in the image itself. While these benchmarks are an important part of VLM evaluation, we find that existing models are surprisingly fragile to seemingly irrelevant details of visual prompting: simply changing a visual marker from red to blue can completely change rankings among models on a leaderboard. By evaluating nine commonly-used open- and closed-source VLMs on two visually prompted tasks, we demonstrate how details in benchmark setup, including visual marker design and dataset size, have a significant influence on model performance and leaderboard rankings. These effects can even be exploited to lift weaker models above stronger ones; for instance, slightly increasing the size of the visual marker results in open-source InternVL3-8B ranking alongside or better than much larger proprietary models like Gemini 2.5 Pro. We further show that low-level inference choices that are often ignored in benchmarking, such as JPEG compression levels in API calls, can also cause model lineup changes. These details have substantially larger impacts on visually prompted benchmarks than on conventional semantic VLM evaluations. To mitigate this instability, we curate existing datasets to create VPBench, a larger visually prompted benchmark with 16 visual marker variants. VPBench and additional analysis tools are released at https://lisadunlap.github.io/vpbench/.

