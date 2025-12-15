---
layout: default
title: Task-Specific Distance Correlation Matching for Few-Shot Action Recognition
---

# Task-Specific Distance Correlation Matching for Few-Shot Action Recognition
**arXiv**：[2512.11340v1](https://arxiv.org/abs/2512.11340) · [PDF](https://arxiv.org/pdf/2512.11340.pdf)  
**作者**：Fei Long, Yao Zhang, Jiaming Lv, Jiangtao Xie, Peihua Li  

**一句话要点**：提出TS-FSAR框架，通过任务特定距离相关匹配和引导侧网络解决少样本动作识别中的非线性依赖和优化难题。

**关键词**：少样本动作识别, 距离相关匹配, CLIP微调, 非线性依赖建模, 任务特定学习

## 3 点简述
- 现有方法依赖余弦相似度，难以捕捉非线性帧间依赖和任务特定线索。
- 引入α-距离相关匹配和任务原型，建模线性与非线性依赖，实现任务特定匹配。
- 在五个基准测试中表现优于先前方法，验证了框架的有效性。

## 摘要（原文）

> Few-shot action recognition (FSAR) has recently made notable progress through set matching and efficient adaptation of large-scale pre-trained models. However, two key limitations persist. First, existing set matching metrics typically rely on cosine similarity to measure inter-frame linear dependencies and then perform matching with only instance-level information, thus failing to capture more complex patterns such as nonlinear relationships and overlooking task-specific cues. Second, for efficient adaptation of CLIP to FSAR, recent work performing fine-tuning via skip-fusion layers (which we refer to as side layers) has significantly reduced memory cost. However, the newly introduced side layers are often difficult to optimize under limited data conditions. To address these limitations, we propose TS-FSAR, a framework comprising three components: (1) a visual Ladder Side Network (LSN) for efficient CLIP fine-tuning; (2) a metric called Task-Specific Distance Correlation Matching (TS-DCM), which uses $α$-distance correlation to model both linear and nonlinear inter-frame dependencies and leverages a task prototype to enable task-specific matching; and (3) a Guiding LSN with Adapted CLIP (GLAC) module, which regularizes LSN using the adapted frozen CLIP to improve training for better $α$-distance correlation estimation under limited supervision. Extensive experiments on five widely-used benchmarks demonstrate that our TS-FSAR yields superior performance compared to prior state-of-the-arts.

