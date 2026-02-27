---
layout: default
title: Asymmetric Idiosyncrasies in Multimodal Models
---

# Asymmetric Idiosyncrasies in Multimodal Models
**arXiv**：[2602.22734v1](https://arxiv.org/abs/2602.22734) · [PDF](https://arxiv.org/pdf/2602.22734.pdf)  
**作者**：Muzi Tao, Chufan Shi, Huijuan Wang, Shengbang Tong, Xuezhe Ma  

**一句话要点**：提出基于分类的框架量化字幕模型风格特征及其对文生图系统的影响

**关键词**：多模态模型, 风格特征分析, 文生图系统, 分类框架, 跨模态差异

## 3 点简述
- 研究字幕模型风格特征及其对下游文生图模型的影响
- 设计分类实验：通过生成字幕或对应图像预测源字幕模型
- 发现字幕分类准确率高（99.70%），但图像分类准确率低（≤50%）

## 摘要（原文）

> In this work, we study idiosyncrasies in the caption models and their downstream impact on text-to-image models. We design a systematic analysis: given either a generated caption or the corresponding image, we train neural networks to predict the originating caption model. Our results show that text classification yields very high accuracy (99.70\%), indicating that captioning models embed distinctive stylistic signatures. In contrast, these signatures largely disappear in the generated images, with classification accuracy dropping to at most 50\% even for the state-of-the-art Flux model. To better understand this cross-modal discrepancy, we further analyze the data and find that the generated images fail to preserve key variations present in captions, such as differences in the level of detail, emphasis on color and texture, and the distribution of objects within a scene. Overall, our classification-based framework provides a novel methodology for quantifying both the stylistic idiosyncrasies of caption models and the prompt-following ability of text-to-image systems.

