---
layout: default
title: Cytoarchitecture in Words: Weakly Supervised Vision-Language Modeling for Human Brain Microscopy
---

# Cytoarchitecture in Words: Weakly Supervised Vision-Language Modeling for Human Brain Microscopy
**arXiv**：[2602.23088v1](https://arxiv.org/abs/2602.23088) · [PDF](https://arxiv.org/pdf/2602.23088.pdf)  
**作者**：Matthew Sutton, Katrin Amunts, Timo Dickscheid, Christian Schiffer  

**一句话要点**：提出标签介导的弱监督视觉-语言建模方法，以解决人脑显微图像中配对图像-文本数据稀缺的问题。

**关键词**：弱监督学习, 视觉-语言建模, 人脑显微图像, 细胞构筑学, 标签介导方法, 自然语言接口

## 3 点简述
- 核心问题：人脑显微图像分析中，配对图像-文本数据稀缺，限制了自然语言接口的开发。
- 方法要点：通过标签自动从文献挖掘描述作为合成标题，连接视觉基础模型与大型语言模型进行训练。
- 实验或效果：在57个脑区中，方法能生成合理描述，准确率达90.6%，并支持开放集使用。

## 摘要（原文）

> Foundation models increasingly offer potential to support interactive, agentic workflows that assist researchers during analysis and interpretation of image data. Such workflows often require coupling vision to language to provide a natural-language interface. However, paired image-text data needed to learn this coupling are scarce and difficult to obtain in many research and clinical settings. One such setting is microscopic analysis of cell-body-stained histological human brain sections, which enables the study of cytoarchitecture: cell density and morphology and their laminar and areal organization. Here, we propose a label-mediated method that generates meaningful captions from images by linking images and text only through a label, without requiring curated paired image-text data. Given the label, we automatically mine area descriptions from related literature and use them as synthetic captions reflecting canonical cytoarchitectonic attributes. An existing cytoarchitectonic vision foundation model (CytoNet) is then coupled to a large language model via an image-to-text training objective, enabling microscopy regions to be described in natural language. Across 57 brain areas, the resulting method produces plausible area-level descriptions and supports open-set use through explicit rejection of unseen areas. It matches the cytoarchitectonic reference label for in-scope patches with 90.6% accuracy and, with the area label masked, its descriptions remain discriminative enough to recover the area in an 8-way test with 68.6% accuracy. These results suggest that weak, label-mediated pairing can suffice to connect existing biomedical vision foundation models to language, providing a practical recipe for integrating natural-language in domains where fine-grained paired annotations are scarce.

