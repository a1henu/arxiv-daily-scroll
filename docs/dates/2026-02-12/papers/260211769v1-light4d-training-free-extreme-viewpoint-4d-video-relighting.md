---
layout: default
title: Light4D: Training-Free Extreme Viewpoint 4D Video Relighting
---

# Light4D: Training-Free Extreme Viewpoint 4D Video Relighting
**arXiv**：[2602.11769v1](https://arxiv.org/abs/2602.11769) · [PDF](https://arxiv.org/pdf/2602.11769.pdf)  
**作者**：Zhenghuang Wu, Kang Chen, Zeyu Zhang, Hao Tang  

**一句话要点**：提出Light4D训练免费框架，实现极端视角下4D视频重照明的时空一致性

**关键词**：4D视频重照明, 训练免费框架, 时间一致性, 极端视角, 扩散模型, 光照控制

## 3 点简述
- 核心问题：4D重照明缺乏配对训练数据，极端视角下难以保持时间一致性。
- 方法要点：引入解耦流引导和时间一致注意力，结合确定性正则化消除闪烁。
- 实验或效果：在-90到90度相机旋转下，实现竞争性的时间一致性和光照保真度。

## 摘要（原文）

> Recent advances in diffusion-based generative models have established a new paradigm for image and video relighting. However, extending these capabilities to 4D relighting remains challenging, due primarily to the scarcity of paired 4D relighting training data and the difficulty of maintaining temporal consistency across extreme viewpoints. In this work, we propose Light4D, a novel training-free framework designed to synthesize consistent 4D videos under target illumination, even under extreme viewpoint changes. First, we introduce Disentangled Flow Guidance, a time-aware strategy that effectively injects lighting control into the latent space while preserving geometric integrity. Second, to reinforce temporal consistency, we develop Temporal Consistent Attention within the IC-Light architecture and further incorporate deterministic regularization to eliminate appearance flickering. Extensive experiments demonstrate that our method achieves competitive performance in temporal consistency and lighting fidelity, robustly handling camera rotations from -90 to 90. Code: https://github.com/AIGeeksGroup/Light4D. Website: https://aigeeksgroup.github.io/Light4D.

