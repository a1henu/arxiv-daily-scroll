---
layout: default
title: PCMind-2.1-Kaiyuan-2B Technical Report
---

# PCMind-2.1-Kaiyuan-2B Technical Report
**arXiv**：[2512.07612v1](https://arxiv.org/abs/2512.07612) · [PDF](https://arxiv.org/pdf/2512.07612.pdf)  
**作者**：Kairong Luo, Zhenbo Sun, Xinyu Shi, Shengqi Chen, Bowen Yu, Yunyi Chen, Chenyi Dang, Hengtao Tao, Hui Wang, Fangming Liu, Kaifeng Lyu, Wenguang Chen  

**一句话要点**：提出PCMind-2.1-Kaiyuan-2B，通过数据基准、选择性重复和多领域课程训练，在资源受限下提升大语言模型训练效率与效果。

**关键词**：大语言模型, 数据基准, 选择性重复, 课程训练, 开源模型, 资源受限训练

## 3 点简述
- 核心问题：开源社区与产业间因闭源高质量数据和训练方法存在知识鸿沟，资源受限下训练效率低。
- 方法要点：采用分位数数据基准法比较异构数据集，多阶段策略选择性重复利用稀疏高质量数据，多领域课程训练按质量排序样本。
- 实验或效果：模型性能与顶尖开源模型竞争，提供可扩展的预训练解决方案，所有资产在Apache 2.0许可下开源。

## 摘要（原文）

> The rapid advancement of Large Language Models (LLMs) has resulted in a significant knowledge gap between the open-source community and industry, primarily because the latter relies on closed-source, high-quality data and training recipes. To address this, we introduce PCMind-2.1-Kaiyuan-2B, a fully open-source 2-billion-parameter model focused on improving training efficiency and effectiveness under resource constraints. Our methodology includes three key innovations: a Quantile Data Benchmarking method for systematically comparing heterogeneous open-source datasets and providing insights on data mixing strategies; a Strategic Selective Repetition scheme within a multi-phase paradigm to effectively leverage sparse, high-quality data; and a Multi-Domain Curriculum Training policy that orders samples by quality. Supported by a highly optimized data preprocessing pipeline and architectural modifications for FP16 stability, Kaiyuan-2B achieves performance competitive with state-of-the-art fully open-source models, demonstrating practical and scalable solutions for resource-limited pretraining. We release all assets (including model weights, data, and code) under Apache 2.0 license at https://huggingface.co/thu-pacman/PCMind-2.1-Kaiyuan-2B.

