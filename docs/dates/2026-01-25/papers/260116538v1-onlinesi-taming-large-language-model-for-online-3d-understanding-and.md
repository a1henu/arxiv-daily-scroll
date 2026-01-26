---
layout: default
title: OnlineSI: Taming Large Language Model for Online 3D Understanding and Grounding
---

# OnlineSI: Taming Large Language Model for Online 3D Understanding and Grounding
**arXiv**：[2601.16538v1](https://arxiv.org/abs/2601.16538) · [PDF](https://arxiv.org/pdf/2601.16538.pdf)  
**作者**：Zixian Liu, Zhaoxi Chen, Liang Pan, Ziwei Liu  

**一句话要点**：提出OnlineSI框架，通过有限空间记忆实现在线3D理解与定位，适用于视频流场景。

**关键词**：在线3D理解, 空间记忆, 多模态大语言模型, 视频流处理, 具身系统

## 3 点简述
- 核心问题：现有MLLM缺乏持续空间理解能力，难以部署于动态现实环境。
- 方法要点：集成3D点云与语义信息，维护有限空间记忆以稳定计算开销。
- 实验或效果：引入Fuzzy F1-Score评估，在两个数据集上验证有效性，推动具身系统应用。

## 摘要（原文）

> In recent years, researchers have increasingly been interested in how to enable Multimodal Large Language Models (MLLM) to possess spatial understanding and reasoning capabilities. However, most existing methods overlook the importance of the ability to continuously work in an ever-changing world, and lack the possibility of deployment on embodied systems in real-world environments. In this work, we introduce OnlineSI, a framework that can continuously improve its spatial understanding of its surroundings given a video stream. Our core idea is to maintain a finite spatial memory to retain past observations, ensuring the computation required for each inference does not increase as the input accumulates. We further integrate 3D point cloud information with semantic information, helping MLLM to better locate and identify objects in the scene. To evaluate our method, we introduce the Fuzzy $F_1$-Score to mitigate ambiguity, and test our method on two representative datasets. Experiments demonstrate the effectiveness of our method, paving the way towards real-world embodied systems.

