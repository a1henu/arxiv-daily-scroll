---
layout: default
title: SA-IQA: Redefining Image Quality Assessment for Spatial Aesthetics with Multi-Dimensional Rewards
---

# SA-IQA: Redefining Image Quality Assessment for Spatial Aesthetics with Multi-Dimensional Rewards
**arXiv**：[2512.05098v1](https://arxiv.org/abs/2512.05098) · [PDF](https://arxiv.org/pdf/2512.05098.pdf)  
**作者**：Yuan Gao, Jin Song  

**一句话要点**：提出SA-IQA框架，通过多维度奖励评估室内场景的空间美学质量。

**关键词**：图像质量评估, 空间美学, 多模态大语言模型, 强化学习, 基准数据集

## 3 点简述
- 现有IQA方法缺乏对室内场景的系统美学评估，聚焦肖像和艺术图像。
- 引入空间美学范式，基于布局、和谐、光照和失真四维度构建SA-BENCH基准。
- SA-IQA在SA-BENCH上显著优于现有方法，并应用于AIGC优化和图像筛选任务。

## 摘要（原文）

> In recent years, Image Quality Assessment (IQA) for AI-generated images (AIGI) has advanced rapidly; however, existing methods primarily target portraits and artistic images, lacking a systematic evaluation of interior scenes. We introduce Spatial Aesthetics, a paradigm that assesses the aesthetic quality of interior images along four dimensions: layout, harmony, lighting, and distortion. We construct SA-BENCH, the first benchmark for spatial aesthetics, comprising 18,000 images and 50,000 precise annotations. Employing SA-BENCH, we systematically evaluate current IQA methodologies and develop SA-IQA, through MLLM fine-tuning and a multidimensional fusion approach, as a comprehensive reward framework for assessing spatial aesthetics. We apply SA-IQA to two downstream tasks: (1) serving as a reward signal integrated with GRPO reinforcement learning to optimize the AIGC generation pipeline, and (2) Best-of-N selection to filter high-quality images and improve generation quality. Experiments indicate that SA-IQA significantly outperforms existing methods on SA-BENCH, setting a new standard for spatial aesthetics evaluation. Code and dataset will be open-sourced to advance research and applications in this domain.

