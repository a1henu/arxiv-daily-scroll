---
layout: default
title: Diffusion priors enhanced velocity model building from time-lag images using a neural operator
---

# Diffusion priors enhanced velocity model building from time-lag images using a neural operator
**arXiv**：[2512.23375v1](https://arxiv.org/abs/2512.23375) · [PDF](https://arxiv.org/pdf/2512.23375.pdf)  
**作者**：Xiao Ma, Mohammad Hasyim Taufik, Tariq Alkhalifah  

**一句话要点**：提出结合生成模型与神经算子的框架，高效构建高分辨率速度模型

**关键词**：速度模型构建, 神经算子, 生成模型, 时滞图像, 地下成像, 深度学习

## 3 点简述
- 核心问题：传统速度模型构建方法计算成本高、耗时，影响地下成像精度。
- 方法要点：使用神经算子作为前向映射，快速生成时滞图像，并嵌入生成模型作为正则化器提升分辨率。
- 实验或效果：合成和现场数据实验验证了该方法的有效性，能获得更清晰、高分辨率的速度模型。

## 摘要（原文）

> Velocity model building serves as a crucial component for achieving high precision subsurface imaging. However, conventional velocity model building methods are often computationally expensive and time consuming. In recent years, with the rapid advancement of deep learning, particularly the success of generative models and neural operators, deep learning based approaches that integrate data and their statistics have attracted increasing attention in addressing the limitations of traditional methods. In this study, we propose a novel framework that combines generative models with neural operators to obtain high resolution velocity models efficiently. Within this workflow, the neural operator functions as a forward mapping operator to rapidly generate time lag reverse time migration (RTM) extended images from the true and migration velocity models. In this framework, the neural operator is acting as a surrogate for modeling followed by migration, which uses the true and migration velocities, respectively. The trained neural operator is then employed, through automatic differentiation, to gradually update the migration velocity placed in the true velocity input channel with high resolution components so that the output of the network matches the time lag images of observed data obtained using the migration velocity. By embedding a generative model, trained on a high-resolution velocity model distribution, which corresponds to the true velocity model distribution used to train the neural operator, as a regularizer, the resulting predictions are cleaner with higher resolution information. Both synthetic and field data experiments demonstrate the effectiveness of the proposed generative neural operator based velocity model building approach.

