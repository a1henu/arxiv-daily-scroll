---
layout: default
title: SURE: Semi-dense Uncertainty-REfined Feature Matching
---

# SURE: Semi-dense Uncertainty-REfined Feature Matching
**arXiv**：[2603.04869v1](https://arxiv.org/abs/2603.04869) · [PDF](https://arxiv.org/pdf/2603.04869.pdf)  
**作者**：Sicheng Li, Zaiwang Gu, Jie Zhang, Qing Guo, Xudong Jiang, Jun Cheng  

**一句话要点**：提出SURE框架，通过建模不确定性提升半稠密特征匹配的可靠性，以应对大视角变化和无纹理区域挑战。

**关键词**：特征匹配, 不确定性建模, 半稠密匹配, 图像对应, 计算机视觉, 机器人视觉

## 3 点简述
- 核心问题：现有特征匹配方法在大视角变化或无纹理区域易产生高置信度错误匹配，缺乏可靠性估计机制。
- 方法要点：联合预测对应关系和置信度，引入证据头建模偶然和认知不确定性，并设计轻量空间融合模块提升局部特征精度。
- 实验或效果：在多个标准基准测试中，SURE在准确性和效率上均优于现有半稠密匹配模型，代码将开源。

## 摘要（原文）

> Establishing reliable image correspondences is essential for many robotic vision problems. However, existing methods often struggle in challenging scenarios with large viewpoint changes or textureless regions, where incorrect cor- respondences may still receive high similarity scores. This is mainly because conventional models rely solely on fea- ture similarity, lacking an explicit mechanism to estimate the reliability of predicted matches, leading to overconfident errors. To address this issue, we propose SURE, a Semi- dense Uncertainty-REfined matching framework that jointly predicts correspondences and their confidence by modeling both aleatoric and epistemic uncertainties. Our approach in- troduces a novel evidential head for trustworthy coordinate regression, along with a lightweight spatial fusion module that enhances local feature precision with minimal overhead. We evaluated our method on multiple standard benchmarks, where it consistently outperforms existing state-of-the-art semi-dense matching models in both accuracy and efficiency. our code will be available on https://github.com/LSC-ALAN/SURE.

