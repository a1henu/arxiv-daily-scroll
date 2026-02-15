---
layout: default
title: Variation-aware Flexible 3D Gaussian Editing
---

# Variation-aware Flexible 3D Gaussian Editing
**arXiv**：[2602.11638v1](https://arxiv.org/abs/2602.11638) · [PDF](https://arxiv.org/pdf/2602.11638.pdf)  
**作者**：Hao Qin, Yukai Sun, Meng Wang, Ming Kong, Mengxu Lu, Qiang Zhu  

**一句话要点**：提出VF-Editor以解决3D高斯溅射间接编辑中的不一致性和灵活性限制问题

**关键词**：3D高斯溅射编辑, 变分预测, 知识蒸馏, 原生编辑, 跨视图一致性

## 3 点简述
- 核心问题：间接编辑方法导致跨视图不一致，限制编辑灵活性和效率
- 方法要点：通过前馈预测属性变化，设计变分预测器从2D编辑知识蒸馏，实现高斯基元原生编辑
- 实验或效果：在公开和私有数据集上验证方法有效性和灵活性，揭示间接编辑固有局限

## 摘要（原文）

> Indirect editing methods for 3D Gaussian Splatting (3DGS) have recently witnessed significant advancements. These approaches operate by first applying edits in the rendered 2D space and subsequently projecting the modifications back into 3D. However, this paradigm inevitably introduces cross-view inconsistencies and constrains both the flexibility and efficiency of the editing process. To address these challenges, we present VF-Editor, which enables native editing of Gaussian primitives by predicting attribute variations in a feedforward manner. To accurately and efficiently estimate these variations, we design a novel variation predictor distilled from 2D editing knowledge. The predictor encodes the input to generate a variation field and employs two learnable, parallel decoding functions to iteratively infer attribute changes for each 3D Gaussian. Thanks to its unified design, VF-Editor can seamlessly distill editing knowledge from diverse 2D editors and strategies into a single predictor, allowing for flexible and effective knowledge transfer into the 3D domain. Extensive experiments on both public and private datasets reveal the inherent limitations of indirect editing pipelines and validate the effectiveness and flexibility of our approach.

