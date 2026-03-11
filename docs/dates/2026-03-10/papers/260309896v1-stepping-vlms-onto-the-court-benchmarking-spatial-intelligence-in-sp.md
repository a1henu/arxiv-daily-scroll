---
layout: default
title: Stepping VLMs onto the Court: Benchmarking Spatial Intelligence in Sports
---

# Stepping VLMs onto the Court: Benchmarking Spatial Intelligence in Sports
**arXiv**：[2603.09896v1](https://arxiv.org/abs/2603.09896) · [PDF](https://arxiv.org/pdf/2603.09896.pdf)  
**作者**：Yuchen Yang, Yuqing Shao, Duxiu Huang, Linfeng Dong, Yifei Liu, Suixin Tang, Xiang Zhou, Yuanyuan Gao, Wei Wang, Yue Zhou, Xue Yang, Yanfeng Wang, Xiao Sun, Zhihang Zhong  

**一句话要点**：提出CourtSI数据集与基准，以体育场景评测视觉语言模型的空间智能。

**关键词**：空间智能评测, 体育视觉理解, 视觉语言模型, 数据集构建, 基准测试, 微调优化

## 3 点简述
- 核心问题：现有空间智能基准在体育动态场景中暴露局限性，需针对性评测。
- 方法要点：基于球场几何构建半自动数据引擎，创建大规模体育空间智能数据集CourtSI。
- 实验或效果：评测25个模型显示人机性能差距，微调Qwen3-VL-8B提升23.5个百分点。

## 摘要（原文）

> Sports have long attracted broad attention as they push the limits of human physical and cognitive capabilities. Amid growing interest in spatial intelligence for vision-language models (VLMs), sports provide a natural testbed for understanding high-intensity human motion and dynamic object interactions. To this end, we present CourtSI, the first large-scale spatial intelligence dataset tailored to sports scenarios. CourtSI contains over 1M QA pairs, organized under a holistic taxonomy that systematically covers spatial counting, distance measurement, localization, and relational reasoning, across representative net sports including badminton, tennis, and table tennis. Leveraging well-defined court geometry as metric anchors, we develop a semi-automatic data engine to reconstruct sports scenes, enabling scalable curation of CourtSI. In addition, we introduce CourtSI-Bench, a high-quality evaluation benchmark comprising 3,686 QA pairs with rigorous human verification. We evaluate 25 proprietary and open-source VLMs on CourtSI-Bench, revealing a remaining human-AI performance gap and limited generalization from existing spatial intelligence benchmarks. These findings indicate that sports scenarios expose limitations in spatial intelligence capabilities captured by existing benchmarks. Further, fine-tuning Qwen3-VL-8B on CourtSI improves accuracy on CourtSI-Bench by 23.5 percentage points. The adapted model also generalizes effectively to CourtSI-Ext, an evaluation set built on a similar but unseen sport, and demonstrates enhanced spatial-aware commentary generation. Together, these findings demonstrate that CourtSI provides a scalable pathway toward advancing spatial intelligence of VLMs in sports.

