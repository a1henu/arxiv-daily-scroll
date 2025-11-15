---
layout: default
title: Robust Object Detection with Pseudo Labels from VLMs using Per-Object Co-teaching
---

# Robust Object Detection with Pseudo Labels from VLMs using Per-Object Co-teaching
**arXiv**：[2511.09955v1](https://arxiv.org/abs/2511.09955) · [PDF](https://arxiv.org/pdf/2511.09955.pdf)  
**作者**：Uday Bhaskar, Rishabh Bhattacharya, Avinash Patel, Sarthak Khoche, Praveen Anil Kulkarni, Naresh Manwani  

**一句话要点**：提出基于每对象协同教学的伪标签训练方法，以解决自动驾驶中视觉语言模型检测噪声问题。

**关键词**：伪标签训练, 每对象协同教学, 零样本检测, 噪声过滤, 自动驾驶, YOLO模型

## 3 点简述
- 核心问题：视觉语言模型零样本检测存在高延迟和幻觉预测，不适合直接部署。
- 方法要点：使用两个YOLO模型通过每对象损失值协同过滤噪声边界框进行训练。
- 实验效果：在KITTI数据集上mAP@0.5从31.12%提升至46.61%，并保持实时检测。

## 摘要（原文）

> Foundation models, especially vision-language models (VLMs), offer compelling zero-shot object detection for applications like autonomous driving, a domain where manual labelling is prohibitively expensive. However, their detection latency and tendency to hallucinate predictions render them unsuitable for direct deployment. This work introduces a novel pipeline that addresses this challenge by leveraging VLMs to automatically generate pseudo-labels for training efficient, real-time object detectors. Our key innovation is a per-object co-teaching-based training strategy that mitigates the inherent noise in VLM-generated labels. The proposed per-object coteaching approach filters noisy bounding boxes from training instead of filtering the entire image. Specifically, two YOLO models learn collaboratively, filtering out unreliable boxes from each mini-batch based on their peers' per-object loss values. Overall, our pipeline provides an efficient, robust, and scalable approach to train high-performance object detectors for autonomous driving, significantly reducing reliance on costly human annotation. Experimental results on the KITTI dataset demonstrate that our method outperforms a baseline YOLOv5m model, achieving a significant mAP@0.5 boost ($31.12\%$ to $46.61\%$) while maintaining real-time detection latency. Furthermore, we show that supplementing our pseudo-labelled data with a small fraction of ground truth labels ($10\%$) leads to further performance gains, reaching $57.97\%$ mAP@0.5 on the KITTI dataset. We observe similar performance improvements for the ACDC and BDD100k datasets.

