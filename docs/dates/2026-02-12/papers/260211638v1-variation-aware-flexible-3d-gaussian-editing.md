---
layout: default
title: Variation-aware Flexible 3D Gaussian Editing
---

# Variation-aware Flexible 3D Gaussian Editing
**arXiv**：[2602.11638v1](https://arxiv.org/abs/2602.11638) · [PDF](https://arxiv.org/pdf/2602.11638.pdf)  
**作者**：Hao Qin, Yukai Sun, Meng Wang, Ming Kong, Mengxu Lu, Qiang Zhu  

**一句话要点**：提出VF-Editor以直接编辑3D高斯原语，解决间接编辑中的视图不一致和灵活性限制问题。

**关键词**：3D高斯溅射, 直接编辑, 变化预测, 知识蒸馏, 跨视图一致性, 属性变化

## 3 点简述
- 核心问题：间接编辑3D高斯溅射导致跨视图不一致，限制编辑灵活性和效率。
- 方法要点：设计前馈变化预测器，从2D编辑知识蒸馏，生成变化场并迭代推断3D高斯属性变化。
- 实验或效果：在公开和私有数据集上验证间接编辑的局限性，展示方法的有效性和灵活性。

## 摘要（原文）

> Indirect editing methods for 3D Gaussian Splatting (3DGS) have recently witnessed significant advancements. These approaches operate by first applying edits in the rendered 2D space and subsequently projecting the modifications back into 3D. However, this paradigm inevitably introduces cross-view inconsistencies and constrains both the flexibility and efficiency of the editing process. To address these challenges, we present VF-Editor, which enables native editing of Gaussian primitives by predicting attribute variations in a feedforward manner. To accurately and efficiently estimate these variations, we design a novel variation predictor distilled from 2D editing knowledge. The predictor encodes the input to generate a variation field and employs two learnable, parallel decoding functions to iteratively infer attribute changes for each 3D Gaussian. Thanks to its unified design, VF-Editor can seamlessly distill editing knowledge from diverse 2D editors and strategies into a single predictor, allowing for flexible and effective knowledge transfer into the 3D domain. Extensive experiments on both public and private datasets reveal the inherent limitations of indirect editing pipelines and validate the effectiveness and flexibility of our approach.

