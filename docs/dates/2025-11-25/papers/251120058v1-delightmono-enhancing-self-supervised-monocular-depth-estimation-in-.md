---
layout: default
title: DeLightMono: Enhancing Self-Supervised Monocular Depth Estimation in Endoscopy by Decoupling Uneven Illumination
---

# DeLightMono: Enhancing Self-Supervised Monocular Depth Estimation in Endoscopy by Decoupling Uneven Illumination
**arXiv**：[2511.20058v1](https://arxiv.org/abs/2511.20058) · [PDF](https://arxiv.org/pdf/2511.20058.pdf)  
**作者**：Mingyang Ou, Haojin Li, Yifeng Zhang, Ke Niu, Zhongxi Qiu, Heng Li, Jiang Liu  

**一句话要点**：提出DeLight-Mono框架，通过解耦不均匀光照增强内窥镜自监督单目深度估计

**关键词**：自监督学习, 单目深度估计, 内窥镜图像, 光照解耦, 联合优化

## 3 点简述
- 内窥镜图像中不均匀光照导致深度估计性能下降，尤其在低强度区域。
- 设计光照-反射-深度模型，使用辅助网络分解图像，并引入联合优化框架和新损失函数。
- 在公共数据集上通过比较和消融研究验证了方法的有效性。

## 摘要（原文）

> Self-supervised monocular depth estimation serves as a key task in the development of endoscopic navigation systems. However, performance degradation persists due to uneven illumination inherent in endoscopic images, particularly in low-intensity regions. Existing low-light enhancement techniques fail to effectively guide the depth network. Furthermore, solutions from other fields, like autonomous driving, require well-lit images, making them unsuitable and increasing data collection burdens. To this end, we present DeLight-Mono - a novel self-supervised monocular depth estimation framework with illumination decoupling. Specifically, endoscopic images are represented by a designed illumination-reflectance-depth model, and are decomposed with auxiliary networks. Moreover, a self-supervised joint-optimizing framework with novel losses leveraging the decoupled components is proposed to mitigate the effects of uneven illumination on depth estimation. The effectiveness of the proposed methods was rigorously verified through extensive comparisons and an ablation study performed on two public datasets.

