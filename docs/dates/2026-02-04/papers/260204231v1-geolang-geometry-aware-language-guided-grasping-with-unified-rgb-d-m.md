---
layout: default
title: GeoLanG: Geometry-Aware Language-Guided Grasping with Unified RGB-D Multimodal Learning
---

# GeoLanG: Geometry-Aware Language-Guided Grasping with Unified RGB-D Multimodal Learning
**arXiv**：[2602.04231v1](https://arxiv.org/abs/2602.04231) · [PDF](https://arxiv.org/pdf/2602.04231.pdf)  
**作者**：Rui Tang, Guankun Wang, Long Bai, Huxin Gao, Jiewen Lai, Chi Kit Ng, Jiazheng Wang, Fan Zhang, Hongliang Ren  

**一句话要点**：提出GeoLanG框架，通过统一RGB-D多模态学习解决杂乱场景中语言引导抓取的挑战

**关键词**：语言引导抓取, RGB-D多模态学习, 几何感知, 端到端框架, 注意力机制

## 3 点简述
- 核心问题：现有方法在杂乱、遮挡或低纹理场景中跨模态融合不足，泛化能力差
- 方法要点：基于CLIP构建端到端多任务框架，引入深度引导几何模块和自适应密集通道集成
- 实验或效果：在OCID-VLG数据集及仿真与真实硬件实验中实现精确鲁棒的抓取

## 摘要（原文）

> Language-guided grasping has emerged as a promising paradigm for enabling robots to identify and manipulate target objects through natural language instructions, yet it remains highly challenging in cluttered or occluded scenes. Existing methods often rely on multi-stage pipelines that separate object perception and grasping, which leads to limited cross-modal fusion, redundant computation, and poor generalization in cluttered, occluded, or low-texture scenes. To address these limitations, we propose GeoLanG, an end-to-end multi-task framework built upon the CLIP architecture that unifies visual and linguistic inputs into a shared representation space for robust semantic alignment and improved generalization. To enhance target discrimination under occlusion and low-texture conditions, we explore a more effective use of depth information through the Depth-guided Geometric Module (DGGM), which converts depth into explicit geometric priors and injects them into the attention mechanism without additional computational overhead. In addition, we propose Adaptive Dense Channel Integration, which adaptively balances the contributions of multi-layer features to produce more discriminative and generalizable visual representations. Extensive experiments on the OCID-VLG dataset, as well as in both simulation and real-world hardware, demonstrate that GeoLanG enables precise and robust language-guided grasping in complex, cluttered environments, paving the way toward more reliable multimodal robotic manipulation in real-world human-centric settings.

