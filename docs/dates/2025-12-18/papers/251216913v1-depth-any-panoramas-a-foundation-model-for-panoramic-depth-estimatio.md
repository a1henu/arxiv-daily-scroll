---
layout: default
title: Depth Any Panoramas: A Foundation Model for Panoramic Depth Estimation
---

# Depth Any Panoramas: A Foundation Model for Panoramic Depth Estimation
**arXiv**：[2512.16913v1](https://arxiv.org/abs/2512.16913) · [PDF](https://arxiv.org/pdf/2512.16913.pdf)  
**作者**：Xin Lin, Meixi Song, Dizhe Zhang, Wenxuan Lu, Haodong Li, Bo Du, Ming-Hsuan Yang, Truong Nguyen, Lu Qi  

**一句话要点**：提出全景深度估计基础模型，通过数据循环范式提升跨场景距离泛化能力。

**关键词**：全景深度估计, 基础模型, 数据循环范式, 伪标签生成, 零样本泛化, 度量深度预测

## 3 点简述
- 核心问题：全景深度估计需泛化至多样场景距离，面临室内/室外、合成/真实数据域差异。
- 方法要点：采用数据循环范式，结合大规模数据集构建与三阶段伪标签生成，并引入DINOv3-Large骨干及优化模块增强鲁棒性。
- 实验效果：在多个基准测试中表现优异，实现零样本泛化，在真实场景中提供稳健的度量深度预测。

## 摘要（原文）

> In this work, we present a panoramic metric depth foundation model that generalizes across diverse scene distances. We explore a data-in-the-loop paradigm from the view of both data construction and framework design. We collect a large-scale dataset by combining public datasets, high-quality synthetic data from our UE5 simulator and text-to-image models, and real panoramic images from the web. To reduce domain gaps between indoor/outdoor and synthetic/real data, we introduce a three-stage pseudo-label curation pipeline to generate reliable ground truth for unlabeled images. For the model, we adopt DINOv3-Large as the backbone for its strong pre-trained generalization, and introduce a plug-and-play range mask head, sharpness-centric optimization, and geometry-centric optimization to improve robustness to varying distances and enforce geometric consistency across views. Experiments on multiple benchmarks (e.g., Stanford2D3D, Matterport3D, and Deep360) demonstrate strong performance and zero-shot generalization, with particularly robust and stable metric predictions in diverse real-world scenes. The project page can be found at: \href{https://insta360-research-team.github.io/DAP_website/} {https://insta360-research-team.github.io/DAP\_website/}

