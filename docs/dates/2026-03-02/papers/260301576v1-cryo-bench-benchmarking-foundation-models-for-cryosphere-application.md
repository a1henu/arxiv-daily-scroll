---
layout: default
title: Cryo-Bench: Benchmarking Foundation Models for Cryosphere Applications
---

# Cryo-Bench: Benchmarking Foundation Models for Cryosphere Applications
**arXiv**：[2603.01576v1](https://arxiv.org/abs/2603.01576) · [PDF](https://arxiv.org/pdf/2603.01576.pdf)  
**作者**：Saurabh Kaushik, Lalit Maurya, Beth Tellman  

**一句话要点**：提出Cryo-Bench基准以评估地理基础模型在冰冻圈应用中的性能

**关键词**：冰冻圈应用, 地理基础模型, 基准测试, 少样本学习, 模型微调, 性能评估

## 3 点简述
- 核心问题：缺乏针对冰冻圈应用的地理基础模型评估数据集，限制了其性能基准测试。
- 方法要点：构建Cryo-Bench基准，涵盖冰川、冰湖、海冰和冰裂前沿等多传感器数据，评估14个模型。
- 实验或效果：在冻结编码器下，UNet平均mIoU最高为66.38；少样本设置中，DOFA和TerraMind优于UNet；全微调需优化学习率以提升性能。

## 摘要（原文）

> Geo-Foundation Models (GFMs) have been evaluated across diverse Earth observation task including multiple domains and have demonstrated strong potential of producing reliable maps even with sparse labels. However, benchmarking GFMs for Cryosphere applications has remained limited, primarily due to the lack of suitable evaluation datasets. To address this gap, we introduce \textbf{Cryo-Bench}, a benchmark compiled to evaluate GFM performance across key Cryospheric components. Cryo-Bench includes debris-covered glaciers, glacial lakes, sea ice, and calving fronts, spanning multiple sensors and broad geographic regions. We evaluate 14 GFMs alongside UNet and ViT baselines to assess their advantages, limitations, and optimal usage strategies. With a frozen encoder, UNet achieves the highest average mIoU of \textbf{66.38}, followed by TerraMind at \textbf{64.02} across five evluation dataset included in Cryo-Bench. In the few-shot setting (10\% input data), GFMs such as DOFA and TerraMind outperform UNet, achieving mIoU scores of \textbf{59.53}, \textbf{56.62}, and \textbf{56.60}, respectively, comapred to U-Net's 56.60. When fully finetuning GFMs, we observe inconsistent performance across datasets and models. However, tuning learning rate along with finetuning substantially improves GFM performance. For example, evaluation on two representative datasets (GLID and CaFFe) shows an average relative improvement of \textbf{12.77\%}. Despite having minimal Cryosphere representation in their pretraining data, GFMs exhibit notable domain adaptation capabilities and produce meaningful results across tasks. Based on our findings, We recommend encoder fine-tuning with hyperparameter optimization optimization to achieve the best possible performance, while using frozen encoders when users need quick results without extensive experimentation.(\href{https://github.com/Sk-2103/Cryo-Bench}{GitHub}).

