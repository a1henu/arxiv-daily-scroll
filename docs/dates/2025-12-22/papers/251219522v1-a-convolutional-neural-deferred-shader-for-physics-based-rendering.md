---
layout: default
title: A Convolutional Neural Deferred Shader for Physics Based Rendering
---

# A Convolutional Neural Deferred Shader for Physics Based Rendering
**arXiv**：[2512.19522v1](https://arxiv.org/abs/2512.19522) · [PDF](https://arxiv.org/pdf/2512.19522.pdf)  
**作者**：Zhuo He, Yingdong Ru, Qianying Liu, Paul Henderson, Nicolas Pugeault  

**一句话要点**：提出基于物理的神经延迟着色管道pbnds+，利用卷积神经网络减少参数并提升着色与重光照性能。

**关键词**：神经渲染, 延迟着色, 卷积神经网络, 能量正则化, 物理基础渲染

## 3 点简述
- 核心问题：MLP参数多导致计算资源高、训练复杂、渲染性能下降，数据驱动方法需大量数据且易忽略暗场景。
- 方法要点：采用卷积神经网络减少参数，引入能量正则化限制暗光照下的模型反射。
- 实验或效果：在着色与重光照任务中优于经典基线、先进神经着色模型和基于扩散的方法。

## 摘要（原文）

> Recent advances in neural rendering have achieved impressive results on photorealistic shading and relighting, by using a multilayer perceptron (MLP) as a regression model to learn the rendering equation from a real-world dataset. Such methods show promise for photorealistically relighting real-world objects, which is difficult to classical rendering, as there is no easy-obtained material ground truth. However, significant challenges still remain the dense connections in MLPs result in a large number of parameters, which requires high computation resources, complicating the training, and reducing performance during rendering. Data driven approaches require large amounts of training data for generalization; unbalanced data might bias the model to ignore the unusual illumination conditions, e.g. dark scenes. This paper introduces pbnds+: a novel physics-based neural deferred shading pipeline utilizing convolution neural networks to decrease the parameters and improve the performance in shading and relighting tasks; Energy regularization is also proposed to restrict the model reflection during dark illumination. Extensive experiments demonstrate that our approach outperforms classical baselines, a state-of-the-art neural shading model, and a diffusion-based method.

