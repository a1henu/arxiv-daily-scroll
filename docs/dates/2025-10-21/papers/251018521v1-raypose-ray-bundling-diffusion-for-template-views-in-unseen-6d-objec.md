---
layout: default
title: RayPose: Ray Bundling Diffusion for Template Views in Unseen 6D Object Pose Estimation
---

# RayPose: Ray Bundling Diffusion for Template Views in Unseen 6D Object Pose Estimation
**arXiv**：[2510.18521v1](https://arxiv.org/abs/2510.18521) · [PDF](https://arxiv.org/pdf/2510.18521.pdf)  
**作者**：Junwen Huang, Shishir Reddy Vutukur, Peter KT Yu, Nassir Navab, Slobodan Ilic, Benjamin Busam  

**一句话要点**：提出RayPose方法，通过射线束扩散对齐解决未见物体6D姿态估计中的模板检索问题

**关键词**：6D物体姿态估计, 模板对齐, 扩散模型, 射线束扩散, 未见物体姿态, 几何先验

## 3 点简述
- 核心问题：模板检索失败导致6D物体姿态估计不准确
- 方法要点：将姿态估计重构为射线对齐问题，使用扩散变换器对齐查询图像与模板
- 实验效果：在多个基准数据集上取得与先进方法竞争的结果

## 摘要（原文）

> Typical template-based object pose pipelines estimate the pose by retrieving
> the closest matching template and aligning it with the observed image. However,
> failure to retrieve the correct template often leads to inaccurate pose
> predictions. To address this, we reformulate template-based object pose
> estimation as a ray alignment problem, where the viewing directions from
> multiple posed template images are learned to align with a non-posed query
> image. Inspired by recent progress in diffusion-based camera pose estimation,
> we embed this formulation into a diffusion transformer architecture that aligns
> a query image with a set of posed templates. We reparameterize object rotation
> using object-centered camera rays and model object translation by extending
> scale-invariant translation estimation to dense translation offsets. Our model
> leverages geometric priors from the templates to guide accurate query pose
> inference. A coarse-to-fine training strategy based on narrowed template
> sampling improves performance without modifying the network architecture.
> Extensive experiments across multiple benchmark datasets show competitive
> results of our method compared to state-of-the-art approaches in unseen object
> pose estimation.

