---
layout: default
title: FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning
---

# FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning
**arXiv**：[2603.05506v1](https://arxiv.org/abs/2603.05506) · [PDF](https://arxiv.org/pdf/2603.05506.pdf)  
**作者**：Weijie Lyu, Ming-Hsuan Yang, Zhixin Shu  

**一句话要点**：提出FaceCam系统，通过尺度感知条件化实现单目人像视频的自定义相机轨迹生成。

**关键词**：人像视频生成, 相机控制, 尺度感知表示, 视频生成模型, 多视图训练

## 3 点简述
- 核心问题：现有基于大视频生成模型的相机控制方法在人像视频中常因尺度模糊或3D重建错误导致几何失真和视觉伪影。
- 方法要点：设计面向人脸的尺度感知相机变换表示，无需3D先验，结合合成相机运动和多镜头拼接策略训练视频生成模型。
- 实验或效果：在Ava-256数据集和多样真实视频上验证，FaceCam在相机可控性、视觉质量、身份和运动保持方面表现优越。

## 摘要（原文）

> We introduce FaceCam, a system that generates video under customizable camera trajectories for monocular human portrait video input. Recent camera control approaches based on large video-generation models have shown promising progress but often exhibit geometric distortions and visual artifacts on portrait videos due to scale-ambiguous camera representations or 3D reconstruction errors. To overcome these limitations, we propose a face-tailored scale-aware representation for camera transformations that provides deterministic conditioning without relying on 3D priors. We train a video generation model on both multi-view studio captures and in-the-wild monocular videos, and introduce two camera-control data generation strategies: synthetic camera motion and multi-shot stitching, to exploit stationary training cameras while generalizing to dynamic, continuous camera trajectories at inference time. Experiments on Ava-256 dataset and diverse in-the-wild videos demonstrate that FaceCam achieves superior performance in camera controllability, visual quality, identity and motion preservation.

