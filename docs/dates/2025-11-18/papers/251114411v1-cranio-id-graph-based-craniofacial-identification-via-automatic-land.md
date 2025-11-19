---
layout: default
title: Cranio-ID: Graph-Based Craniofacial Identification via Automatic Landmark Annotation in 2D Multi-View X-rays
---

# Cranio-ID: Graph-Based Craniofacial Identification via Automatic Landmark Annotation in 2D Multi-View X-rays
**arXiv**：[2511.14411v1](https://arxiv.org/abs/2511.14411) · [PDF](https://arxiv.org/pdf/2511.14411.pdf)  
**作者**：Ravi Shankar Prasad, Nandani Sharma, Dinesh Singh  

**一句话要点**：提出Cranio-ID框架，通过自动标注和图形匹配解决法医颅面识别中的不可靠性问题

**关键词**：颅面识别, 自动标志点标注, 图形表示, 跨模态匹配, 法医科学

## 3 点简述
- 核心问题：传统颅骨标志点定位方法耗时且不可靠，缺乏大规模验证
- 方法要点：使用YOLO-pose自动标注标志点，并构建图形进行跨模态匹配
- 实验或效果：在S2F和CUHK数据集上验证，显著提升可靠性和准确性

## 摘要（原文）

> In forensic craniofacial identification and in many biomedical applications, craniometric landmarks are important. Traditional methods for locating landmarks are time-consuming and require specialized knowledge and expertise. Current methods utilize superimposition and deep learning-based methods that employ automatic annotation of landmarks. However, these methods are not reliable due to insufficient large-scale validation studies. In this paper, we proposed a novel framework Cranio-ID: First, an automatic annotation of landmarks on 2D skulls (which are X-ray scans of faces) with their respective optical images using our trained YOLO-pose models. Second, cross-modal matching by formulating these landmarks into graph representations and then finding semantic correspondence between graphs of these two modalities using cross-attention and optimal transport framework. Our proposed framework is validated on the S2F and CUHK datasets (CUHK dataset resembles with S2F dataset). Extensive experiments have been conducted to evaluate the performance of our proposed framework, which demonstrates significant improvements in both reliability and accuracy, as well as its effectiveness in cross-domain skull-to-face and sketch-to-face matching in forensic science.

