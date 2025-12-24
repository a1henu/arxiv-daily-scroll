---
layout: default
title: Evolutionary Neural Architecture Search with Dual Contrastive Learning
---

# Evolutionary Neural Architecture Search with Dual Contrastive Learning
**arXiv**：[2512.20112v1](https://arxiv.org/abs/2512.20112) · [PDF](https://arxiv.org/pdf/2512.20112.pdf)  
**作者**：Xian-Rong Zhang, Yue-Jiao Gong, Wei-Neng Chen, Jun Zhang  

**一句话要点**：提出双对比学习进化神经架构搜索，以有限计算预算提升预测器精度

**关键词**：进化神经架构搜索, 对比学习, 神经预测器, 计算效率, 自监督学习, 性能预测

## 3 点简述
- 核心问题：进化神经架构搜索中，训练数据收集成本高，需在有限计算预算下实现高精度预测器。
- 方法要点：采用两阶段对比学习，先自监督学习架构表示，再微调预测相对性能以指导进化搜索。
- 实验或效果：在NASBench数据集上超越基线，真实ECG任务中性能提升约2.5个百分点，仅需7.7 GPU天。

## 摘要（原文）

> Evolutionary Neural Architecture Search (ENAS) has gained attention for automatically designing neural network architectures. Recent studies use a neural predictor to guide the process, but the high computational costs of gathering training data -- since each label requires fully training an architecture -- make achieving a high-precision predictor with { limited compute budget (i.e., a capped number of fully trained architecture-label pairs)} crucial for ENAS success. This paper introduces ENAS with Dual Contrastive Learning (DCL-ENAS), a novel method that employs two stages of contrastive learning to train the neural predictor. In the first stage, contrastive self-supervised learning is used to learn meaningful representations from neural architectures without requiring labels. In the second stage, fine-tuning with contrastive learning is performed to accurately predict the relative performance of different architectures rather than their absolute performance, which is sufficient to guide the evolutionary search. Across NASBench-101 and NASBench-201, DCL-ENAS achieves the highest validation accuracy, surpassing the strongest published baselines by 0.05\% (ImageNet16-120) to 0.39\% (NASBench-101). On a real-world ECG arrhythmia classification task, DCL-ENAS improves performance by approximately 2.5 percentage points over a manually designed, non-NAS model obtained via random search, while requiring only 7.7 GPU-days.

