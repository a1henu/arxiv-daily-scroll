---
layout: default
title: DiffFace-Edit: A Diffusion-Based Facial Dataset for Forgery-Semantic Driven Deepfake Detection Analysis
---

# DiffFace-Edit: A Diffusion-Based Facial Dataset for Forgery-Semantic Driven Deepfake Detection Analysis
**arXiv**：[2601.13551v1](https://arxiv.org/abs/2601.13551) · [PDF](https://arxiv.org/pdf/2601.13551.pdf)  
**作者**：Feng Ding, Wenhui Yi, Xinan He, Mengyao Xiao, Jianfeng Xu, Jianqiang Du  

**一句话要点**：提出DiffFace-Edit数据集以解决细粒度区域篡改和检测器规避样本在深度伪造检测中的分析需求

**关键词**：深度伪造检测, 人脸篡改数据集, 细粒度区域编辑, 检测器规避样本, 跨域评估, 生成模型分析

## 3 点简述
- 核心问题：现有AI生成人脸数据集缺乏细粒度区域篡改样本，且未研究真实与篡改样本间拼接攻击对检测器的影响
- 方法要点：构建包含超200万AI生成假图像的DiffFace-Edit数据集，覆盖八个面部区域编辑及多种组合，并分析检测器规避样本
- 实验或效果：进行数据集全面分析，提出结合IMDL方法的跨域评估，数据集将公开可用

## 摘要（原文）

> Generative models now produce imperceptible, fine-grained manipulated faces, posing significant privacy risks. However, existing AI-generated face datasets generally lack focus on samples with fine-grained regional manipulations. Furthermore, no researchers have yet studied the real impact of splice attacks, which occur between real and manipulated samples, on detectors. We refer to these as detector-evasive samples. Based on this, we introduce the DiffFace-Edit dataset, which has the following advantages: 1) It contains over two million AI-generated fake images. 2) It features edits across eight facial regions (e.g., eyes, nose) and includes a richer variety of editing combinations, such as single-region and multi-region edits. Additionally, we specifically analyze the impact of detector-evasive samples on detection models. We conduct a comprehensive analysis of the dataset and propose a cross-domain evaluation that combines IMDL methods. Dataset will be available at https://github.com/ywh1093/DiffFace-Edit.

