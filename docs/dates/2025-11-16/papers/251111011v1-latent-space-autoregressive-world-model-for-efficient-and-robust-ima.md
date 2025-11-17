---
layout: default
title: Latent-Space Autoregressive World Model for Efficient and Robust Image-Goal Navigation
---

# Latent-Space Autoregressive World Model for Efficient and Robust Image-Goal Navigation
**arXiv**：[2511.11011v1](https://arxiv.org/abs/2511.11011) · [PDF](https://arxiv.org/pdf/2511.11011.pdf)  
**作者**：Zhiwei Zhang, Hui Zhang, Xieyuanli Chen, Kaihong Huang, Chenghao Shi, Huimin Lu  

**一句话要点**：提出轻量级潜在空间自回归世界模型以高效解决图像目标导航问题

**关键词**：图像目标导航, 潜在空间模型, 自回归预测, 高效规划, 世界模型

## 3 点简述
- 传统导航依赖精确定位与建图，计算成本高且效率低
- 模型在潜在空间预测未来状态并规划路径，显著提升训练与推理效率
- 实验显示导航成功率提升35%，路径长度指标提升11%，效率优势显著

## 摘要（原文）

> Traditional navigation methods rely heavily on accurate localization and mapping. In contrast, world models that capture environmental dynamics in latent space have opened up new perspectives for navigation tasks, enabling systems to move beyond traditional multi-module pipelines. However, world model often suffers from high computational costs in both training and inference. To address this, we propose LS-NWM - a lightweight latent space navigation world model that is trained and operates entirely in latent space, compared to the state-of-the-art baseline, our method reduces training time by approximately 3.2x and planning time by about 447x,while further improving navigation performance with a 35% higher SR and an 11% higher SPL. The key idea is that accurate pixel-wise environmental prediction is unnecessary for navigation. Instead, the model predicts future latent states based on current observational features and action inputs, then performs path planning and decision-making within this compact representation, significantly improving computational efficiency. By incorporating an autoregressive multi-frame prediction strategy during training, the model effectively captures long-term spatiotemporal dependencies, thereby enhancing navigation performance in complex scenarios. Experimental results demonstrate that our method achieves state-of-the-art navigation performance while maintaining a substantial efficiency advantage over existing approaches.

