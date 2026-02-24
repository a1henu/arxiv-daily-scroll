---
layout: default
title: Open-vocabulary 3D scene perception in industrial environments
---

# Open-vocabulary 3D scene perception in industrial environments
**arXiv**：[2602.19823v1](https://arxiv.org/abs/2602.19823) · [PDF](https://arxiv.org/pdf/2602.19823.pdf)  
**作者**：Keno Moenck, Adrian Philip Florea, Julian Koch, Thorsten Schüppstuhl  

**一句话要点**：提出免训练开放词汇3D感知流程，以提升工业场景中对象分割的泛化能力。

**关键词**：开放词汇3D感知, 工业场景分割, 免训练流程, 超点合并, 视觉语言基础模型

## 3 点简述
- 核心问题：现有开放词汇方法依赖非工业数据集预训练模型，在工业对象上泛化性能差。
- 方法要点：基于语义特征合并预计算超点生成掩码，避免使用预训练分割模型。
- 实验或效果：在工业车间场景中评估IndustrialCLIP，定性结果显示成功分割工业对象。

## 摘要（原文）

> Autonomous vision applications in production, intralogistics, or manufacturing environments require perception capabilities beyond a small, fixed set of classes. Recent open-vocabulary methods, leveraging 2D Vision-Language Foundation Models (VLFMs), target this task but often rely on class-agnostic segmentation models pre-trained on non-industrial datasets (e.g., household scenes). In this work, we first demonstrate that such models fail to generalize, performing poorly on common industrial objects. Therefore, we propose a training-free, open-vocabulary 3D perception pipeline that overcomes this limitation. Instead of using a pre-trained model to generate instance proposals, our method simply generates masks by merging pre-computed superpoints based on their semantic features. Following, we evaluate the domain-adapted VLFM "IndustrialCLIP" on a representative 3D industrial workshop scene for open-vocabulary querying. Our qualitative results demonstrate successful segmentation of industrial objects.

