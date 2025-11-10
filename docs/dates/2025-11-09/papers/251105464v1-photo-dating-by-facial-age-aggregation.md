---
layout: default
title: Photo Dating by Facial Age Aggregation
---

# Photo Dating by Facial Age Aggregation
**arXiv**：[2511.05464v1](https://arxiv.org/abs/2511.05464) · [PDF](https://arxiv.org/pdf/2511.05464.pdf)  
**作者**：Jakub Paplham, Vojtech Franc  

**一句话要点**：提出基于面部年龄聚合的概率框架以估计照片拍摄年份

**关键词**：照片年代估计, 面部年龄聚合, 多脸信息处理, 概率框架, CSFD-1.6M数据集

## 3 点简述
- 核心问题：从图像中估计照片拍摄年份，利用多个人脸信息。
- 方法要点：结合人脸识别、年龄估计模型和职业时间先验进行概率推断。
- 实验或效果：多脸证据聚合提升性能，优于基于场景的基线方法。

## 摘要（原文）

> We introduce a novel method for Photo Dating which estimates the year a
> photograph was taken by leveraging information from the faces of people present
> in the image. To facilitate this research, we publicly release CSFD-1.6M, a new
> dataset containing over 1.6 million annotated faces, primarily from movie
> stills, with identity and birth year annotations. Uniquely, our dataset
> provides annotations for multiple individuals within a single image, enabling
> the study of multi-face information aggregation. We propose a probabilistic
> framework that formally combines visual evidence from modern face recognition
> and age estimation models, and career-based temporal priors to infer the photo
> capture year. Our experiments demonstrate that aggregating evidence from
> multiple faces consistently improves the performance and the approach
> significantly outperforms strong, scene-based baselines, particularly for
> images containing several identifiable individuals.

