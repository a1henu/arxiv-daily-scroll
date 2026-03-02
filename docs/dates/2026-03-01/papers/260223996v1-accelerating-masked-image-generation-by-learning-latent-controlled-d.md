---
layout: default
title: Accelerating Masked Image Generation by Learning Latent Controlled Dynamics
---

# Accelerating Masked Image Generation by Learning Latent Controlled Dynamics
**arXiv**：[2602.23996v1](https://arxiv.org/abs/2602.23996) · [PDF](https://arxiv.org/pdf/2602.23996.pdf)  
**作者**：Kaiwen Zhu, Quansheng Zeng, Yuandong Pu, Shuo Cao, Xiaohui Li, Yi Xin, Qi Qin, Jiayang Li, Yu Qiao, Jinjin Gu, Yihao Liu  

**一句话要点**：提出MIGM-Shortcut以加速掩码图像生成，通过轻量模型学习特征演化动态

**关键词**：掩码图像生成, 加速方法, 轻量模型, 特征演化, 文本到图像生成, 计算效率

## 3 点简述
- 核心问题：掩码图像生成模型因双向注意力多步计算效率低，存在特征冗余
- 方法要点：学习轻量模型结合先前特征和采样令牌，回归特征演化的平均速度场
- 实验或效果：在Lumina-DiMOO上实现超4倍加速，保持质量，提升帕累托前沿

## 摘要（原文）

> Masked Image Generation Models (MIGMs) have achieved great success, yet their efficiency is hampered by the multiple steps of bi-directional attention. In fact, there exists notable redundancy in their computation: when sampling discrete tokens, the rich semantics contained in the continuous features are lost. Some existing works attempt to cache the features to approximate future features. However, they exhibit considerable approximation error under aggressive acceleration rates. We attribute this to their limited expressivity and the failure to account for sampling information. To fill this gap, we propose to learn a lightweight model that incorporates both previous features and sampled tokens, and regresses the average velocity field of feature evolution. The model has moderate complexity that suffices to capture the subtle dynamics while keeping lightweight compared to the original base model. We apply our method, MIGM-Shortcut, to two representative MIGM architectures and tasks. In particular, on the state-of-the-art Lumina-DiMOO, it achieves over 4x acceleration of text-to-image generation while maintaining quality, significantly pushing the Pareto frontier of masked image generation. The code and model weights are available at https://github.com/Kaiwen-Zhu/MIGM-Shortcut.

