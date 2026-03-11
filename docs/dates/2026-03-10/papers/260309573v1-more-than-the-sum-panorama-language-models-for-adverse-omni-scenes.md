---
layout: default
title: More than the Sum: Panorama-Language Models for Adverse Omni-Scenes
---

# More than the Sum: Panorama-Language Models for Adverse Omni-Scenes
**arXiv**：[2603.09573v1](https://arxiv.org/abs/2603.09573) · [PDF](https://arxiv.org/pdf/2603.09573.pdf)  
**作者**：Weijia Fan, Ruiping Liu, Jiale Wei, Yufan Chen, Junwei Zheng, Zichao Zeng, Jiaming Zhang, Qiufu Li, Linlin Shen, Rainer Stiefelhagen  

**一句话要点**：提出全景-语言建模范式以解决全景场景下视觉语言模型理解不足的问题

**关键词**：全景视觉语言模型, 全景稀疏注意力, 全景视觉问答, 全景场景理解, 即插即用模块

## 3 点简述
- 现有视觉语言模型基于针孔图像，忽略全景的全局空间关系
- 引入全景-语言建模范式，开发即插即用全景稀疏注意力模块
- 构建PanoVQA数据集，实验显示在挑战性全景场景中实现优越鲁棒性和整体推理

## 摘要（原文）

> Existing vision-language models (VLMs) are tailored for pinhole imagery, stitching multiple narrow field-of-view inputs to piece together a complete omni-scene understanding. Yet, such multi-view perception overlooks the holistic spatial and contextual relationships that a single panorama inherently preserves. In this work, we introduce the Panorama-Language Modeling (PLM)paradigm, a unified $360^\circ$ vision-language reasoning that is more than the sum of its pinhole counterparts. Besides, we present PanoVQA, a large-scale panoramic VQA dataset that involves adverse omni-scenes, enabling comprehensive reasoning under object occlusions and driving accidents. To establish a foundation for PLM, we develop a plug-and-play panoramic sparse attention module that allows existing pinhole-based VLMs to process equirectangular panoramas without retraining. Extensive experiments demonstrate that our PLM achieves superior robustness and holistic reasoning under challenging omni-scenes, yielding understanding greater than the sum of its narrow parts. Project page: https://github.com/InSAI-Lab/PanoVQA.

