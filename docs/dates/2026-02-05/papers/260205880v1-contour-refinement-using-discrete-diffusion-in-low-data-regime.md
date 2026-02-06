---
layout: default
title: Contour Refinement using Discrete Diffusion in Low Data Regime
---

# Contour Refinement using Discrete Diffusion in Low Data Regime
**arXiv**：[2602.05880v1](https://arxiv.org/abs/2602.05880) · [PDF](https://arxiv.org/pdf/2602.05880.pdf)  
**作者**：Fei Yu Guan, Ian Keefe, Sophie Wilkinson, Daniel D. B. Perrakis, Steven Waslander  

**一句话要点**：提出轻量级离散扩散轮廓细化方法，用于低数据场景下的鲁棒边界检测。

**关键词**：边界检测, 低数据学习, 离散扩散, 轮廓细化, 轻量级模型, 医学影像

## 3 点简述
- 核心问题：在低数据场景下，不规则和半透明物体的边界检测任务缺乏研究，且面临标注数据稀缺和计算资源有限。
- 方法要点：采用带自注意力层的CNN架构，基于分割掩码迭代去噪稀疏轮廓表示，通过简化扩散过程和定制模型提升低数据效能与推理效率。
- 实验或效果：在KVASIR数据集上优于多个SOTA基线，在HAM10K和自定义野火数据集上表现竞争性，推理帧率提升3.5倍。

## 摘要（原文）

> Boundary detection of irregular and translucent objects is an important problem with applications in medical imaging, environmental monitoring and manufacturing, where many of these applications are plagued with scarce labeled data and low in situ computational resources. While recent image segmentation studies focus on segmentation mask alignment with ground-truth, the task of boundary detection remains understudied, especially in the low data regime. In this work, we present a lightweight discrete diffusion contour refinement pipeline for robust boundary detection in the low data regime. We use a Convolutional Neural Network(CNN) architecture with self-attention layers as the core of our pipeline, and condition on a segmentation mask, iteratively denoising a sparse contour representation. We introduce multiple novel adaptations for improved low-data efficacy and inference efficiency, including using a simplified diffusion process, a customized model architecture, and minimal post processing to produce a dense, isolated contour given a dataset of size <500 training images. Our method outperforms several SOTA baselines on the medical imaging dataset KVASIR, is competitive on HAM10K and our custom wildfire dataset, Smoke, while improving inference framerate by 3.5X.

