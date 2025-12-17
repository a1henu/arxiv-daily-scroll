---
layout: default
title: Consistent Instance Field for Dynamic Scene Understanding
---

# Consistent Instance Field for Dynamic Scene Understanding
**arXiv**：[2512.14126v1](https://arxiv.org/abs/2512.14126) · [PDF](https://arxiv.org/pdf/2512.14126.pdf)  
**作者**：Junyi Wu, Van Nguyen Nguyen, Benjamin Planche, Jiachen Tao, Changchang Sun, Zhongpai Gao, Zhenghao Zhao, Anwesa Choudhuri, Gengyu Zhang, Meng Zheng, Feiran Wang, Terrence Chen, Yan Yan, Ziyan Wu  

**一句话要点**：提出一致实例场以解决动态场景理解中离散跟踪和视角依赖问题

**关键词**：动态场景理解, 一致实例场, 可变形3D高斯, 新视角全景分割, 开放词汇4D查询

## 3 点简述
- 核心问题：动态场景理解需处理时空连续性和对象身份一致性，现有方法依赖离散跟踪或视角依赖特征。
- 方法要点：基于可变形3D高斯建模一致实例场，分离可见性和对象身份，通过可微分光栅化学习辐射和语义信息。
- 实验或效果：在HyperNeRF和Neu3D数据集上，在新视角全景分割和开放词汇4D查询任务中显著优于先进方法。

## 摘要（原文）

> We introduce Consistent Instance Field, a continuous and probabilistic spatio-temporal representation for dynamic scene understanding. Unlike prior methods that rely on discrete tracking or view-dependent features, our approach disentangles visibility from persistent object identity by modeling each space-time point with an occupancy probability and a conditional instance distribution. To realize this, we introduce a novel instance-embedded representation based on deformable 3D Gaussians, which jointly encode radiance and semantic information and are learned directly from input RGB images and instance masks through differentiable rasterization. Furthermore, we introduce new mechanisms to calibrate per-Gaussian identities and resample Gaussians toward semantically active regions, ensuring consistent instance representations across space and time. Experiments on HyperNeRF and Neu3D datasets demonstrate that our method significantly outperforms state-of-the-art methods on novel-view panoptic segmentation and open-vocabulary 4D querying tasks.

