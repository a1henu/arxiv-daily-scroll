---
layout: default
title: LocateEdit-Bench: A Benchmark for Instruction-Based Editing Localization
---

# LocateEdit-Bench: A Benchmark for Instruction-Based Editing Localization
**arXiv**：[2602.05577v1](https://arxiv.org/abs/2602.05577) · [PDF](https://arxiv.org/pdf/2602.05577.pdf)  
**作者**：Shiyu Wu, Shuyan Li, Jing Li, Jing Liu, Yequan Wang  

**一句话要点**：提出LocateEdit-Bench基准以评估指令驱动图像编辑的定位方法

**关键词**：图像编辑定位, 指令驱动编辑, 伪造检测基准, 数据集构建, 多模型评估

## 3 点简述
- 核心问题：现有伪造定位方法不适用于指令驱动编辑，存在技术差距
- 方法要点：构建大规模数据集，包含231K编辑图像，覆盖四种模型和三种编辑类型
- 实验或效果：设计多指标评估协议，分析数据集，为未来定位方法开发奠定基础

## 摘要（原文）

> Recent advancements in image editing have enabled highly controllable and semantically-aware alteration of visual content, posing unprecedented challenges to manipulation localization. However, existing AI-generated forgery localization methods primarily focus on inpainting-based manipulations, making them ineffective against the latest instruction-based editing paradigms. To bridge this critical gap, we propose LocateEdit-Bench, a large-scale dataset comprising $231$K edited images, designed specifically to benchmark localization methods against instruction-driven image editing. Our dataset incorporates four cutting-edge editing models and covers three common edit types. We conduct a detailed analysis of the dataset and develop two multi-metric evaluation protocols to assess existing localization methods. Our work establishes a foundation to keep pace with the evolving landscape of image editing, thereby facilitating the development of effective methods for future forgery localization. Dataset will be open-sourced upon acceptance.

