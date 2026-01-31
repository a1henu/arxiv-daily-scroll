---
layout: default
title: Hypernetwork-Based Adaptive Aggregation for Multimodal Multiple-Instance Learning in Predicting Coronary Calcium Debulking
---

# Hypernetwork-Based Adaptive Aggregation for Multimodal Multiple-Instance Learning in Predicting Coronary Calcium Debulking
**arXiv**：[2601.21479v1](https://arxiv.org/abs/2601.21479) · [PDF](https://arxiv.org/pdf/2601.21479.pdf)  
**作者**：Kaito Shiku, Ichika Seo, Tetsuya Matoba, Rissei Hino, Yasuhiro Nakano, Ryoma Bise  

**一句话要点**：提出基于超网络的自适应聚合变换器，用于预测冠状动脉钙化减容的多模态多示例学习。

**关键词**：多模态学习, 多示例学习, 自适应聚合, 超网络, 医学图像分析, 冠状动脉钙化

## 3 点简述
- 核心问题：从CT图像估计冠状动脉钙化减容必要性，需结合患者表格数据调整决策。
- 方法要点：使用超网络根据表格数据自适应修改特征聚合策略，处理多模态MIL任务。
- 实验或效果：在临床数据集上验证了方法的有效性，代码已公开。

## 摘要（原文）

> In this paper, we present the first attempt to estimate the necessity of debulking coronary artery calcifications from computed tomography (CT) images. We formulate this task as a Multiple-instance Learning (MIL) problem. The difficulty of this task lies in that physicians adjust their focus and decision criteria for device usage according to tabular data representing each patient's condition. To address this issue, we propose a hypernetwork-based adaptive aggregation transformer (HyperAdAgFormer), which adaptively modifies the feature aggregation strategy for each patient based on tabular data through a hypernetwork. The experiments using the clinical dataset demonstrated the effectiveness of HyperAdAgFormer. The code is publicly available at https://github.com/Shiku-Kaito/HyperAdAgFormer.

