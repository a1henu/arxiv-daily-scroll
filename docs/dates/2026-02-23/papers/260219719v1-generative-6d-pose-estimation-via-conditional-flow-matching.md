---
layout: default
title: Generative 6D Pose Estimation via Conditional Flow Matching
---

# Generative 6D Pose Estimation via Conditional Flow Matching
**arXiv**：[2602.19719v1](https://arxiv.org/abs/2602.19719) · [PDF](https://arxiv.org/pdf/2602.19719.pdf)  
**作者**：Amir Hamza, Davide Boscaini, Weihang Li, Benjamin Busam, Fabio Poiesi  

**一句话要点**：提出Flose方法，通过条件流匹配解决6D姿态估计中的对称性和特征缺失问题。

**关键词**：6D姿态估计, 条件流匹配, 生成模型, 去噪过程, BOP基准

## 3 点简述
- 现有方法在物体对称性或局部特征缺失时性能受限，Flose将6D姿态估计建模为条件流匹配问题。
- Flose结合几何和外观语义特征进行去噪，并集成RANSAC处理异常值，以提升姿态推断的准确性。
- 在BOP基准的五个数据集上验证，Flose平均召回率提升4.5%，优于先前方法。

## 摘要（原文）

> Existing methods for instance-level 6D pose estimation typically rely on neural networks that either directly regress the pose in $\mathrm{SE}(3)$ or estimate it indirectly via local feature matching. The former struggle with object symmetries, while the latter fail in the absence of distinctive local features. To overcome these limitations, we propose a novel formulation of 6D pose estimation as a conditional flow matching problem in $\mathbb{R}^3$. We introduce Flose, a generative method that infers object poses via a denoising process conditioned on local features. While prior approaches based on conditional flow matching perform denoising solely based on geometric guidance, Flose integrates appearance-based semantic features to mitigate ambiguities caused by object symmetries. We further incorporate RANSAC-based registration to handle outliers. We validate Flose on five datasets from the established BOP benchmark. Flose outperforms prior methods with an average improvement of +4.5 Average Recall. Project Website : https://tev-fbk.github.io/Flose/

