---
layout: default
title: Inference-Time Dynamic Modality Selection for Incomplete Multimodal Classification
---

# Inference-Time Dynamic Modality Selection for Incomplete Multimodal Classification
**arXiv**：[2601.22853v1](https://arxiv.org/abs/2601.22853) · [PDF](https://arxiv.org/pdf/2601.22853.pdf)  
**作者**：Siyi Du, Xinzhe Luo, Declan P. O'Regan, Chen Qin  

**一句话要点**：提出DyMo框架，通过推理时动态模态选择解决不完全多模态分类中的丢弃-补全困境。

**关键词**：不完全多模态学习, 动态模态选择, 推理时优化, 多模态分类, 信息集成

## 3 点简述
- 核心问题：不完全多模态数据导致现有方法面临丢弃信息或引入噪声的困境。
- 方法要点：基于任务损失设计可计算奖励函数，动态选择可靠模态并集成，无需已知数据分布。
- 实验或效果：在自然和医学图像数据集上，DyMo显著优于现有不完全/动态多模态方法。

## 摘要（原文）

> Multimodal deep learning (MDL) has achieved remarkable success across various domains, yet its practical deployment is often hindered by incomplete multimodal data. Existing incomplete MDL methods either discard missing modalities, risking the loss of valuable task-relevant information, or recover them, potentially introducing irrelevant noise, leading to the discarding-imputation dilemma. To address this dilemma, in this paper, we propose DyMo, a new inference-time dynamic modality selection framework that adaptively identifies and integrates reliable recovered modalities, fully exploring task-relevant information beyond the conventional discard-or-impute paradigm. Central to DyMo is a novel selection algorithm that maximizes multimodal task-relevant information for each test sample. Since direct estimation of such information at test time is intractable due to the unknown data distribution, we theoretically establish a connection between information and the task loss, which we compute at inference time as a tractable proxy. Building on this, a novel principled reward function is proposed to guide modality selection. In addition, we design a flexible multimodal network architecture compatible with arbitrary modality combinations, alongside a tailored training strategy for robust representation learning. Extensive experiments on diverse natural and medical image datasets show that DyMo significantly outperforms state-of-the-art incomplete/dynamic MDL methods across various missing-data scenarios. Our code is available at https://github.com//siyi-wind/DyMo.

