---
layout: default
title: TripleFDS: Triple Feature Disentanglement and Synthesis for Scene Text Editing
---

# TripleFDS: Triple Feature Disentanglement and Synthesis for Scene Text Editing
**arXiv**：[2511.13399v1](https://arxiv.org/abs/2511.13399) · [PDF](https://arxiv.org/pdf/2511.13399.pdf)  
**作者**：Yuchen Bao, Yiting Wang, Wenjian Huang, Haowei Wang, Shen Chen, Taiping Yao, Shouhong Ding, Jianguo Zhang  

**一句话要点**：提出TripleFDS框架以解决场景文本编辑中的特征解耦与合成问题

**关键词**：场景文本编辑, 特征解耦, 图像合成, 对比学习, 正交正则化, SCB数据集

## 3 点简述
- 核心问题：场景文本编辑中文本风格、内容和背景特征解耦不完整，限制可控性和视觉一致性。
- 方法要点：使用SCB Group数据集，通过组间对比正则化和组内多特征正交性实现三特征解耦与合成。
- 实验或效果：在主流基准上达到SSIM 44.54和ACC 93.58%，支持风格替换和背景转移等新操作。

## 摘要（原文）

> Scene Text Editing (STE) aims to naturally modify text in images while preserving visual consistency, the decisive factors of which can be divided into three parts, i.e., text style, text content, and background. Previous methods have struggled with incomplete disentanglement of editable attributes, typically addressing only one aspect - such as editing text content - thus limiting controllability and visual consistency. To overcome these limitations, we propose TripleFDS, a novel framework for STE with disentangled modular attributes, and an accompanying dataset called SCB Synthesis. SCB Synthesis provides robust training data for triple feature disentanglement by utilizing the "SCB Group", a novel construct that combines three attributes per image to generate diverse, disentangled training groups. Leveraging this construct as a basic training unit, TripleFDS first disentangles triple features, ensuring semantic accuracy through inter-group contrastive regularization and reducing redundancy through intra-sample multi-feature orthogonality. In the synthesis phase, TripleFDS performs feature remapping to prevent "shortcut" phenomena during reconstruction and mitigate potential feature leakage. Trained on 125,000 SCB Groups, TripleFDS achieves state-of-the-art image fidelity (SSIM of 44.54) and text accuracy (ACC of 93.58%) on the mainstream STE benchmarks. Besides superior performance, the more flexible editing of TripleFDS supports new operations such as style replacement and background transfer. Code: https://github.com/yusenbao01/TripleFDS

