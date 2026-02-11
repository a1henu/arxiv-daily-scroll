---
layout: default
title: UniVTAC: A Unified Simulation Platform for Visuo-Tactile Manipulation Data Generation, Learning, and Benchmarking
---

# UniVTAC: A Unified Simulation Platform for Visuo-Tactile Manipulation Data Generation, Learning, and Benchmarking
**arXiv**：[2602.10093v1](https://arxiv.org/abs/2602.10093) · [PDF](https://arxiv.org/pdf/2602.10093.pdf)  
**作者**：Baijun Chen, Weijie Wan, Tianxing Chen, Xianda Guo, Congsheng Xu, Yuanyang Qi, Haojie Zhang, Longyan Wu, Tianling Xu, Zixuan Li, Yizhe Wu, Rui Li, Xiaokang Yang, Ping Luo, Wei Sui, Yao Mu  

**一句话要点**：提出UniVTAC统一仿真平台，以解决触觉数据获取难和评估平台缺失问题

**关键词**：触觉感知, 机器人操作, 仿真平台, 数据生成, 基准测试, 视觉-触觉编码器

## 3 点简述
- 核心问题：触觉感知对接触丰富操作至关重要，但物理世界数据获取成本高且缺乏统一评估平台
- 方法要点：基于仿真支持多种触觉传感器，生成可扩展可控的交互数据，并训练触觉中心编码器
- 实验或效果：集成编码器在基准测试中平均成功率提升17.1%，真实世界实验任务成功率提高25%

## 摘要（原文）

> Robotic manipulation has seen rapid progress with vision-language-action (VLA) policies. However, visuo-tactile perception is critical for contact-rich manipulation, as tasks such as insertion are difficult to complete robustly using vision alone. At the same time, acquiring large-scale and reliable tactile data in the physical world remains costly and challenging, and the lack of a unified evaluation platform further limits policy learning and systematic analysis. To address these challenges, we propose UniVTAC, a simulation-based visuo-tactile data synthesis platform that supports three commonly used visuo-tactile sensors and enables scalable and controllable generation of informative contact interactions. Based on this platform, we introduce the UniVTAC Encoder, a visuo-tactile encoder trained on large-scale simulation-synthesized data with designed supervisory signals, providing tactile-centric visuo-tactile representations for downstream manipulation tasks. In addition, we present the UniVTAC Benchmark, which consists of eight representative visuo-tactile manipulation tasks for evaluating tactile-driven policies. Experimental results show that integrating the UniVTAC Encoder improves average success rates by 17.1% on the UniVTAC Benchmark, while real-world robotic experiments further demonstrate a 25% improvement in task success. Our webpage is available at https://univtac.github.io/.

