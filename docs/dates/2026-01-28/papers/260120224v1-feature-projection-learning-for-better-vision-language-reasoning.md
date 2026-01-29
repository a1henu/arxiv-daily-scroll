---
layout: default
title: Feature Projection Learning for Better Vision-Language Reasoning
---

# Feature Projection Learning for Better Vision-Language Reasoning
**arXiv**：[2601.20224v1](https://arxiv.org/abs/2601.20224) · [PDF](https://arxiv.org/pdf/2601.20224.pdf)  
**作者**：Yi Zhang, Weicheng Lin, Liang-Jie Zhang  

**一句话要点**：提出特征投影学习以高效适应CLIP模型至下游视觉语言推理任务

**关键词**：视觉语言预训练模型, 特征投影学习, CLIP适应, 下游任务, 重建误差分类

## 3 点简述
- 问题：现有方法在适应CLIP模型时存在性能有限、参数过多或训练时间长的问题
- 方法：通过投影模型将类原型特征映射到查询图像特征空间，重构特征图并计算重建误差作为分类得分
- 效果：在实验中，FPL方法在准确率上显著超越当前最先进方法

## 摘要（原文）

> Vision-Language Pre-Trained models, notably CLIP, that utilize contrastive learning have proven highly adept at extracting generalizable visual features. To inherit the well-learned knowledge of VLP models for downstream tasks, several approaches aim to adapt them efficiently with limited supervision. However, these methods either suffer from limited performance, excessive learnable parameters, or extended training times, all of which hinder their effectiveness in adapting the CLIP model to downstream tasks. In this work, we propose a simple yet efficient and effective method called \textit{\textbf{F}eature \textbf{P}rojection \textbf{L}earning(FPL)} to address these problems. Specifically, we develop a projection model that projects class prototype features into the query image feature space and reconstructs the query image feature map. The negative average squared reconstruction error is used as the class score. In this way, we transform the classification problem into a feature projection problem. The final output of this method is a combination of the prediction from the projection model and the original pre-trained CLIP. Comprehensive empirical evaluations confirm that FPL delivers superior accuracy, surpassing the current state-of-the-art methods by a substantial margin.

