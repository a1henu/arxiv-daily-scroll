---
layout: default
title: VenusBench-GD: A Comprehensive Multi-Platform GUI Benchmark for Diverse Grounding Tasks
---

# VenusBench-GD: A Comprehensive Multi-Platform GUI Benchmark for Diverse Grounding Tasks
**arXiv**：[2512.16501v1](https://arxiv.org/abs/2512.16501) · [PDF](https://arxiv.org/pdf/2512.16501.pdf)  
**作者**：Beitong Zhou, Zhexiao Huang, Yuan Guo, Zhangxuan Gu, Tianyu Xia, Zichen Luo, Fei Tang, Dehan Kong, Yanyi Shang, Suling Ou, Zhenlin Guo, Changhua Meng, Shuheng Shen  

**一句话要点**：提出VenusBench-GD多平台GUI基准，以解决现有基准数据不足、覆盖窄和平台单一的问题。

**关键词**：GUI基准, 跨平台评估, 分层任务分类, 多模态模型, UI元素标注

## 3 点简述
- 核心问题：现有GUI基准数据量小、领域覆盖窄或平台单一，限制GUI代理能力评估。
- 方法要点：构建大规模跨平台双语基准，覆盖多样应用和UI元素，提出分层任务分类。
- 实验或效果：通用多模态模型在基础任务上媲美专用模型，高级任务仍依赖专用模型但存在过拟合。

## 摘要（原文）

> GUI grounding is a critical component in building capable GUI agents. However, existing grounding benchmarks suffer from significant limitations: they either provide insufficient data volume and narrow domain coverage, or focus excessively on a single platform and require highly specialized domain knowledge. In this work, we present VenusBench-GD, a comprehensive, bilingual benchmark for GUI grounding that spans multiple platforms, enabling hierarchical evaluation for real-word applications. VenusBench-GD contributes as follows: (i) we introduce a large-scale, cross-platform benchmark with extensive coverage of applications, diverse UI elements, and rich annotated data, (ii) we establish a high-quality data construction pipeline for grounding tasks, achieving higher annotation accuracy than existing benchmarks, and (iii) we extend the scope of element grounding by proposing a hierarchical task taxonomy that divides grounding into basic and advanced categories, encompassing six distinct subtasks designed to evaluate models from complementary perspectives. Our experimental findings reveal critical insights: general-purpose multimodal models now match or even surpass specialized GUI models on basic grounding tasks. In contrast, advanced tasks, still favor GUI-specialized models, though they exhibit significant overfitting and poor robustness. These results underscore the necessity of comprehensive, multi-tiered evaluation frameworks.

