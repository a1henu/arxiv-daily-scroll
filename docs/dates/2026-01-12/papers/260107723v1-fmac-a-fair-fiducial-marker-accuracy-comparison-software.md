---
layout: default
title: FMAC: a Fair Fiducial Marker Accuracy Comparison Software
---

# FMAC: a Fair Fiducial Marker Accuracy Comparison Software
**arXiv**：[2601.07723v1](https://arxiv.org/abs/2601.07723) · [PDF](https://arxiv.org/pdf/2601.07723.pdf)  
**作者**：Guillaume J. Laurent, Patrick Sandoz  

**一句话要点**：提出FMAC软件以公平比较基准标记姿态估计精度

**关键词**：基准标记, 姿态估计, 精度比较, 合成图像, 光线追踪, 开源软件

## 3 点简述
- 核心问题：基准标记姿态估计精度比较缺乏公平性，受图像质量影响。
- 方法要点：使用高保真合成图像，基于物理光线追踪渲染，支持相机标准校准系数。
- 实验或效果：应用方法评估已知标记，揭示其姿态估计的优缺点，代码开源。

## 摘要（原文）

> This paper presents a method for carrying fair comparisons of the accuracy of pose estimation using fiducial markers. These comparisons rely on large sets of high-fidelity synthetic images enabling deep exploration of the 6 degrees of freedom. A low-discrepancy sampling of the space allows to check the correlations between each degree of freedom and the pose errors by plotting the 36 pairs of combinations. The images are rendered using a physically based ray tracing code that has been specifically developed to use the standard calibration coefficients of any camera directly. The software reproduces image distortions, defocus and diffraction blur. Furthermore, sub-pixel sampling is applied to sharp edges to enhance the fidelity of the rendered image. After introducing the rendering algorithm and its experimental validation, the paper proposes a method for evaluating the pose accuracy. This method is applied to well-known markers, revealing their strengths and weaknesses for pose estimation. The code is open source and available on GitHub.

