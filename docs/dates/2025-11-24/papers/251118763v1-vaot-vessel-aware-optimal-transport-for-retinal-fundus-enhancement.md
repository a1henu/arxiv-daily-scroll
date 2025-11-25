---
layout: default
title: VAOT: Vessel-Aware Optimal Transport for Retinal Fundus Enhancement
---

# VAOT: Vessel-Aware Optimal Transport for Retinal Fundus Enhancement
**arXiv**：[2511.18763v1](https://arxiv.org/abs/2511.18763) · [PDF](https://arxiv.org/pdf/2511.18763.pdf)  
**作者**：Xuanzhao Dong, Wenhui Zhu, Yujian Xiong, Xiwen Chen, Hao Wang, Xin Li, Jiajun Cheng, Zhipeng Wang, Shao Tang, Oana Dumitrascu, Yalin Wang  

**一句话要点**：提出VAOT框架以解决视网膜眼底图像增强中血管结构失真问题

**关键词**：视网膜眼底增强, 最优传输, 血管结构保持, 无配对学习, 图像分割

## 3 点简述
- 核心问题：无配对增强方法易扭曲血管拓扑和端点完整性，影响临床诊断。
- 方法要点：结合最优传输目标与骨架和端点感知正则化，保持血管结构。
- 实验或效果：在合成退化基准和下游分割任务中优于现有方法，代码已开源。

## 摘要（原文）

> Color fundus photography (CFP) is central to diagnosing and monitoring retinal disease, yet its acquisition variability (e.g., illumination changes) often degrades image quality, which motivates robust enhancement methods. Unpaired enhancement pipelines are typically GAN-based, however, they can distort clinically critical vasculature, altering vessel topology and endpoint integrity. Motivated by these structural alterations, we propose Vessel-Aware Optimal Transport (\textbf{VAOT}), a framework that combines an optimal-transport objective with two structure-preserving regularizers: (i) a skeleton-based loss to maintain global vascular connectivity and (ii) an endpoint-aware loss to stabilize local termini. These constraints guide learning in the unpaired setting, reducing noise while preserving vessel structure. Experimental results on synthetic degradation benchmark and downstream evaluations in vessel and lesion segmentation demonstrate the superiority of the proposed methods against several state-of-the art baselines. The code is available at https://github.com/Retinal-Research/VAOT

