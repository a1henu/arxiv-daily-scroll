---
layout: default
title: Generalizable and Adaptive Continual Learning Framework for AI-generated Image Detection
---

# Generalizable and Adaptive Continual Learning Framework for AI-generated Image Detection
**arXiv**：[2601.05580v1](https://arxiv.org/abs/2601.05580) · [PDF](https://arxiv.org/pdf/2601.05580.pdf)  
**作者**：Hanyi Wang, Jun Lan, Yaoyu Kang, Huijia Zhu, Weiqiang Wang, Zhuosheng Zhang, Shilin Wang  

**一句话要点**：提出三阶段领域持续学习框架以解决AI生成图像检测的泛化与适应性问题

**关键词**：AI生成图像检测, 持续学习, 参数高效微调, 数据增强, K-FAC方法, 线性模式连接

## 3 点简述
- 核心问题：AI生成图像检测方法泛化性差，难以适应快速演变的生成模型，威胁信息真实性
- 方法要点：采用参数高效微调、数据增强链和K-FAC方法，结合线性插值策略，实现持续学习和抗遗忘
- 实验或效果：在27个生成模型基准上，离线检测器平均精度提升5.51%，持续学习策略平均准确率达92.20%

## 摘要（原文）

> The malicious misuse and widespread dissemination of AI-generated images pose a significant threat to the authenticity of online information. Current detection methods often struggle to generalize to unseen generative models, and the rapid evolution of generative techniques continuously exacerbates this challenge. Without adaptability, detection models risk becoming ineffective in real-world applications. To address this critical issue, we propose a novel three-stage domain continual learning framework designed for continuous adaptation to evolving generative models. In the first stage, we employ a strategic parameter-efficient fine-tuning approach to develop a transferable offline detection model with strong generalization capabilities. Building upon this foundation, the second stage integrates unseen data streams into a continual learning process. To efficiently learn from limited samples of novel generated models and mitigate overfitting, we design a data augmentation chain with progressively increasing complexity. Furthermore, we leverage the Kronecker-Factored Approximate Curvature (K-FAC) method to approximate the Hessian and alleviate catastrophic forgetting. Finally, the third stage utilizes a linear interpolation strategy based on Linear Mode Connectivity, effectively capturing commonalities across diverse generative models and further enhancing overall performance. We establish a comprehensive benchmark of 27 generative models, including GANs, deepfakes, and diffusion models, chronologically structured up to August 2024 to simulate real-world scenarios. Extensive experiments demonstrate that our initial offline detectors surpass the leading baseline by +5.51% in terms of mean average precision. Our continual learning strategy achieves an average accuracy of 92.20%, outperforming state-of-the-art methods.

