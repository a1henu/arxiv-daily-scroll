---
layout: default
title: PanoSAMic: Panoramic Image Segmentation from SAM Feature Encoding and Dual View Fusion
---

# PanoSAMic: Panoramic Image Segmentation from SAM Feature Encoding and Dual View Fusion
**arXiv**：[2601.07447v1](https://arxiv.org/abs/2601.07447) · [PDF](https://arxiv.org/pdf/2601.07447.pdf)  
**作者**：Mahdi Chamseddine, Didier Stricker, Jason Rambach  

**一句话要点**：提出PanoSAMic，通过SAM特征编码与双视图融合实现全景图像语义分割

**关键词**：全景图像分割, SAM特征编码, 多模态融合, 球形注意力, 双视图融合, 语义分割

## 3 点简述
- 核心问题：现有基础模型未针对球形全景图像优化，存在失真和边缘不连续问题
- 方法要点：修改SAM编码器输出多阶段特征，引入空间模态融合模块和球形注意力双视图融合解码器
- 实验或效果：在Stanford2D3DS和Matterport3D数据集上实现RGB、RGB-D等模态的SotA结果

## 摘要（原文）

> Existing image foundation models are not optimized for spherical images having been trained primarily on perspective images. PanoSAMic integrates the pre-trained Segment Anything (SAM) encoder to make use of its extensive training and integrate it into a semantic segmentation model for panoramic images using multiple modalities. We modify the SAM encoder to output multi-stage features and introduce a novel spatio-modal fusion module that allows the model to select the relevant modalities and best features from each modality for different areas of the input. Furthermore, our semantic decoder uses spherical attention and dual view fusion to overcome the distortions and edge discontinuity often associated with panoramic images. PanoSAMic achieves state-of-the-art (SotA) results on Stanford2D3DS for RGB, RGB-D, and RGB-D-N modalities and on Matterport3D for RGB and RGB-D modalities. https://github.com/dfki-av/PanoSAMic

