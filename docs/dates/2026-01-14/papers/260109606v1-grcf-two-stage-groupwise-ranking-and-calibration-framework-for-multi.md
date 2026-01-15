---
layout: default
title: GRCF: Two-Stage Groupwise Ranking and Calibration Framework for Multimodal Sentiment Analysis
---

# GRCF: Two-Stage Groupwise Ranking and Calibration Framework for Multimodal Sentiment Analysis
**arXiv**：[2601.09606v1](https://arxiv.org/abs/2601.09606) · [PDF](https://arxiv.org/pdf/2601.09606.pdf)  
**作者**：Manning Gao, Leheng Zhang, Shiqin Han, Haifeng Hu, Yuncheng Jiang, Sijie Mai  

**一句话要点**：提出GRCF以解决多模态情感分析中排序学习框架的适应性不足问题

**关键词**：多模态情感分析, 排序学习, 动态边界, 分数校准, 泛化能力

## 3 点简述
- 核心问题：现有成对排序方法对样本重要性分配均匀且使用静态排序边界，导致难以聚焦难排序样本和反映情感组间语义距离差异。
- 方法要点：采用两阶段框架，第一阶段引入优势加权动态边界排序损失构建细粒度序结构，第二阶段使用MAE目标校准预测分数。
- 实验或效果：在回归基准上达到最先进性能，并扩展至分类任务如幽默和讽刺检测，展示强泛化能力。

## 摘要（原文）

> Most Multimodal Sentiment Analysis research has focused on point-wise regression. While straightforward, this approach is sensitive to label noise and neglects whether one sample is more positive than another, resulting in unstable predictions and poor correlation alignment. Pairwise ordinal learning frameworks emerged to address this gap, capturing relative order by learning from comparisons. Yet, they introduce two new trade-offs: First, they assign uniform importance to all comparisons, failing to adaptively focus on hard-to-rank samples. Second, they employ static ranking margins, which fail to reflect the varying semantic distances between sentiment groups. To address this, we propose a Two-Stage Group-wise Ranking and Calibration Framework (GRCF) that adapts the philosophy of Group Relative Policy Optimization (GRPO). Our framework resolves these trade-offs by simultaneously preserving relative ordinal structure, ensuring absolute score calibration, and adaptively focusing on difficult samples. Specifically, Stage 1 introduces a GRPO-inspired Advantage-Weighted Dynamic Margin Ranking Loss to build a fine-grained ordinal structure. Stage 2 then employs an MAE-driven objective to align prediction magnitudes. To validate its generalizability, we extend GRCF to classification tasks, including multimodal humor detection and sarcasm detection. GRCF achieves state-of-the-art performance on core regression benchmarks, while also showing strong generalizability in classification tasks.

