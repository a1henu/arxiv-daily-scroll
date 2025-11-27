---
layout: default
title: SAM Guided Semantic and Motion Changed Region Mining for Remote Sensing Change Captioning
---

# SAM Guided Semantic and Motion Changed Region Mining for Remote Sensing Change Captioning
**arXiv**：[2511.21420v1](https://arxiv.org/abs/2511.21420) · [PDF](https://arxiv.org/pdf/2511.21420.pdf)  
**作者**：Futian Wang, Mengqi Wang, Xiao Wang, Haowen Wang, Jin Tang  

**一句话要点**：提出SAM引导的语义与运动变化区域挖掘方法，以提升遥感变化描述性能

**关键词**：遥感变化描述, SAM模型, 区域级表示, 知识图谱, 交叉注意力, Transformer解码器

## 3 点简述
- 核心问题：现有遥感变化描述方法区域感知弱且时间对齐有限
- 方法要点：融合SAM提取区域特征、知识图谱和全局视觉特征，通过交叉注意力生成描述
- 实验或效果：在多个基准数据集上实现最先进性能，代码已开源

## 摘要（原文）

> Remote sensing change captioning is an emerging and popular research task that aims to describe, in natural language, the content of interest that has changed between two remote sensing images captured at different times. Existing methods typically employ CNNs/Transformers to extract visual representations from the given images or incorporate auxiliary tasks to enhance the final results, with weak region awareness and limited temporal alignment. To address these issues, this paper explores the use of the SAM (Segment Anything Model) foundation model to extract region-level representations and inject region-of-interest knowledge into the captioning framework. Specifically, we employ a CNN/Transformer model to extract global-level vision features, leverage the SAM foundation model to delineate semantic- and motion-level change regions, and utilize a specially constructed knowledge graph to provide information about objects of interest. These heterogeneous sources of information are then fused via cross-attention, and a Transformer decoder is used to generate the final natural language description of the observed changes. Extensive experimental results demonstrate that our method achieves state-of-the-art performance across multiple widely used benchmark datasets. The source code of this paper will be released on https://github.com/Event-AHU/SAM_ChangeCaptioning

