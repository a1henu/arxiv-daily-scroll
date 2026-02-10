---
layout: default
title: GEBench: Benchmarking Image Generation Models as GUI Environments
---

# GEBench: Benchmarking Image Generation Models as GUI Environments
**arXiv**：[2602.09007v1](https://arxiv.org/abs/2602.09007) · [PDF](https://arxiv.org/pdf/2602.09007.pdf)  
**作者**：Haodong Li, Jingwei Wu, Quan Sun, Guopeng Li, Juanxi Tian, Huanyu Zhang, Yanlin Lai, Ruichuan An, Hongbo Peng, Yuhong Dai, Chenxi Li, Chunmei Qing, Jia Wang, Ziyang Meng, Zheng Ge, Xiangyu Zhang, Daxin Jiang  

**一句话要点**：提出GEBench基准以评估图像生成模型在GUI环境中的动态交互与时间一致性

**关键词**：GUI生成基准, 时间一致性评估, 图像生成模型, 交互逻辑, 视觉质量

## 3 点简述
- 现有基准缺乏对GUI状态转换和时间一致性的评估
- GEBench包含700个样本和GE-Score五维指标
- 实验显示模型在多步交互中时间一致性和空间定位表现不佳

## 摘要（原文）

> Recent advancements in image generation models have enabled the prediction of future Graphical User Interface (GUI) states based on user instructions. However, existing benchmarks primarily focus on general domain visual fidelity, leaving the evaluation of state transitions and temporal coherence in GUI-specific contexts underexplored. To address this gap, we introduce GEBench, a comprehensive benchmark for evaluating dynamic interaction and temporal coherence in GUI generation. GEBench comprises 700 carefully curated samples spanning five task categories, covering both single-step interactions and multi-step trajectories across real-world and fictional scenarios, as well as grounding point localization. To support systematic evaluation, we propose GE-Score, a novel five-dimensional metric that assesses Goal Achievement, Interaction Logic, Content Consistency, UI Plausibility, and Visual Quality. Extensive evaluations on current models indicate that while they perform well on single-step transitions, they struggle significantly with maintaining temporal coherence and spatial grounding over longer interaction sequences. Our findings identify icon interpretation, text rendering, and localization precision as critical bottlenecks. This work provides a foundation for systematic assessment and suggests promising directions for future research toward building high-fidelity generative GUI environments. The code is available at: https://github.com/stepfun-ai/GEBench.

