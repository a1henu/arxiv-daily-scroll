---
layout: default
title: ELLMob: Event-Driven Human Mobility Generation with Self-Aligned LLM Framework
---

# ELLMob: Event-Driven Human Mobility Generation with Self-Aligned LLM Framework
**arXiv**：[2603.07946v1](https://arxiv.org/abs/2603.07946) · [PDF](https://arxiv.org/pdf/2603.07946.pdf)  
**作者**：Yusong Wang, Chuang Yang, Jiawei Wang, Xiaohang Xu, Jiayi Xu, Dongyuan Li, Chuan Xiao, Renhe Jiang  

**一句话要点**：提出ELLMob自对齐LLM框架，以解决事件驱动的人类移动生成中习惯与约束的竞争问题。

**关键词**：人类移动生成, 事件驱动轨迹, 自对齐LLM, 模糊痕迹理论, 轨迹数据集

## 3 点简述
- 核心问题：现有LLM方法难以生成大规模社会事件期间的偏离移动轨迹，缺乏事件标注数据集和框架处理习惯与约束的竞争。
- 方法要点：基于模糊痕迹理论提取习惯模式与事件约束的竞争理性，通过自对齐迭代生成既符合习惯又响应事件的轨迹。
- 实验或效果：在台风、疫情和奥运会事件上构建首个事件标注数据集，ELLMob在实验中优于现有基线，验证其有效性。

## 摘要（原文）

> Human mobility generation aims to synthesize plausible trajectory data, which is widely used in urban system research. While Large Language Model-based methods excel at generating routine trajectories, they struggle to capture deviated mobility during large-scale societal events. This limitation stems from two critical gaps: (1) the absence of event-annotated mobility datasets for design and evaluation, and (2) the inability of current frameworks to reconcile competitions between users' habitual patterns and event-imposed constraints when making trajectory decisions. This work addresses these gaps with a twofold contribution. First, we construct the first event-annotated mobility dataset covering three major events: Typhoon Hagibis, COVID-19, and the Tokyo 2021 Olympics. Second, we propose ELLMob, a self-aligned LLM framework that first extracts competing rationales between habitual patterns and event constraints, based on Fuzzy-Trace Theory, and then iteratively aligns them to generate trajectories that are both habitually grounded and event-responsive. Extensive experiments show that ELLMob wins state-of-the-art baselines across all events, demonstrating its effectiveness. Our codes and datasets are available at https://github.com/deepkashiwa20/ELLMob.

