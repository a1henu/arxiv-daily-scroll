---
layout: default
title: Finding NeMO: A Geometry-Aware Representation of Template Views for Few-Shot Perception
---

# Finding NeMO: A Geometry-Aware Representation of Template Views for Few-Shot Perception
**arXiv**：[2602.04343v1](https://arxiv.org/abs/2602.04343) · [PDF](https://arxiv.org/pdf/2602.04343.pdf)  
**作者**：Sebastian Jung, Leonard Klüpfel, Rudolph Triebel, Maximilian Durner  

**一句话要点**：提出NeMO表示法，以几何感知的模板视图实现少样本物体感知

**关键词**：少样本物体感知, 几何感知表示, 6DoF姿态估计, 物体中心表示, 多任务学习, BOP基准

## 3 点简述
- 核心问题：训练中未见物体的检测、分割和6DoF姿态估计，需少样本和无需相机参数
- 方法要点：编码器从少量RGB模板生成稀疏点云，解码器结合查询图像输出密集预测
- 实验或效果：在BOP基准上取得竞争性结果，支持多任务且无需目标数据重训练

## 摘要（原文）

> We present Neural Memory Object (NeMO), a novel object-centric representation that can be used to detect, segment and estimate the 6DoF pose of objects unseen during training using RGB images. Our method consists of an encoder that requires only a few RGB template views depicting an object to generate a sparse object-like point cloud using a learned UDF containing semantic and geometric information. Next, a decoder takes the object encoding together with a query image to generate a variety of dense predictions. Through extensive experiments, we show that our method can be used for few-shot object perception without requiring any camera-specific parameters or retraining on target data. Our proposed concept of outsourcing object information in a NeMO and using a single network for multiple perception tasks enhances interaction with novel objects, improving scalability and efficiency by enabling quick object onboarding without retraining or extensive pre-processing. We report competitive and state-of-the-art results on various datasets and perception tasks of the BOP benchmark, demonstrating the versatility of our approach. https://github.com/DLR-RM/nemo

