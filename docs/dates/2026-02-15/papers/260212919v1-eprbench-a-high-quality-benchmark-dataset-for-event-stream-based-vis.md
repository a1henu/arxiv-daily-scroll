---
layout: default
title: EPRBench: A High-Quality Benchmark Dataset for Event Stream Based Visual Place Recognition
---

# EPRBench: A High-Quality Benchmark Dataset for Event Stream Based Visual Place Recognition
**arXiv**：[2602.12919v1](https://arxiv.org/abs/2602.12919) · [PDF](https://arxiv.org/pdf/2602.12919.pdf)  
**作者**：Xiao Wang, Xingxing Xiong, Jinfeng Gao, Xufeng Lou, Bo Jiang, Si-bao Chen, Yaowei Wang, Yonghong Tian  

**一句话要点**：提出EPRBench数据集以解决事件流视觉地点识别领域缺乏高质量基准的问题

**关键词**：事件流视觉地点识别, 基准数据集, 多模态融合, 大语言模型集成, 可解释性, 视觉感知

## 3 点简述
- 核心问题：事件流视觉地点识别领域缺乏专用数据集，影响算法评估与进展
- 方法要点：构建包含10K事件序列和65K事件帧的高质量基准，支持多模态融合与LLM集成
- 实验或效果：在EPRBench上评估15种先进算法，提出新融合范式提升准确性与可解释性

## 摘要（原文）

> Event stream-based Visual Place Recognition (VPR) is an emerging research direction that offers a compelling solution to the instability of conventional visible-light cameras under challenging conditions such as low illumination, overexposure, and high-speed motion. Recognizing the current scarcity of dedicated datasets in this domain, we introduce EPRBench, a high-quality benchmark specifically designed for event stream-based VPR. EPRBench comprises 10K event sequences and 65K event frames, collected using both handheld and vehicle-mounted setups to comprehensively capture real-world challenges across diverse viewpoints, weather conditions, and lighting scenarios. To support semantic-aware and language-integrated VPR research, we provide LLM-generated scene descriptions, subsequently refined through human annotation, establishing a solid foundation for integrating LLMs into event-based perception pipelines. To facilitate systematic evaluation, we implement and benchmark 15 state-of-the-art VPR algorithms on EPRBench, offering a strong baseline for future algorithmic comparisons. Furthermore, we propose a novel multi-modal fusion paradigm for VPR: leveraging LLMs to generate textual scene descriptions from raw event streams, which then guide spatially attentive token selection, cross-modal feature fusion, and multi-scale representation learning. This framework not only achieves highly accurate place recognition but also produces interpretable reasoning processes alongside its predictions, significantly enhancing model transparency and explainability. The dataset and source code will be released on https://github.com/Event-AHU/Neuromorphic_ReID

