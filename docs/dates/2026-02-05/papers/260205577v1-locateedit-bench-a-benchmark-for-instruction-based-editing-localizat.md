---
layout: default
title: LocateEdit-Bench: A Benchmark for Instruction-Based Editing Localization
---

# LocateEdit-Bench: A Benchmark for Instruction-Based Editing Localization
**arXiv**：[2602.05577v1](https://arxiv.org/abs/2602.05577) · [PDF](https://arxiv.org/pdf/2602.05577.pdf)  
**作者**：Shiyu Wu, Shuyan Li, Jing Li, Jing Liu, Yequan Wang  

**一句话要点**：提出LocateEdit-Bench基准数据集以评估指令驱动图像编辑的定位方法

**关键词**：图像编辑定位, 指令驱动编辑, 伪造检测基准, 多模型评估, 数据集构建

## 3 点简述
- 现有伪造定位方法主要针对基于修复的篡改，难以应对指令驱动编辑的新范式
- 构建包含231K编辑图像的大规模数据集，涵盖四种前沿编辑模型和三种常见编辑类型
- 设计多指标评估协议，为未来伪造定位方法的发展提供基础

## 摘要（原文）

> Recent advancements in image editing have enabled highly controllable and semantically-aware alteration of visual content, posing unprecedented challenges to manipulation localization. However, existing AI-generated forgery localization methods primarily focus on inpainting-based manipulations, making them ineffective against the latest instruction-based editing paradigms. To bridge this critical gap, we propose LocateEdit-Bench, a large-scale dataset comprising $231$K edited images, designed specifically to benchmark localization methods against instruction-driven image editing. Our dataset incorporates four cutting-edge editing models and covers three common edit types. We conduct a detailed analysis of the dataset and develop two multi-metric evaluation protocols to assess existing localization methods. Our work establishes a foundation to keep pace with the evolving landscape of image editing, thereby facilitating the development of effective methods for future forgery localization. Dataset will be open-sourced upon acceptance.

