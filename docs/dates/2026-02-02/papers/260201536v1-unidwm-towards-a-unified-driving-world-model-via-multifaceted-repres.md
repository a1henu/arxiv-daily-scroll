---
layout: default
title: UniDWM: Towards a Unified Driving World Model via Multifaceted Representation Learning
---

# UniDWM: Towards a Unified Driving World Model via Multifaceted Representation Learning
**arXiv**：[2602.01536v1](https://arxiv.org/abs/2602.01536) · [PDF](https://arxiv.org/pdf/2602.01536.pdf)  
**作者**：Shuai Liu, Siheng Ren, Xiaoyao Zhu, Quanmin Liang, Zefeng Li, Qiang Li, Xin Hu, Kai Huang  

**一句话要点**：提出UniDWM统一驾驶世界模型，通过多面表示学习提升自动驾驶在复杂环境中的规划能力。

**关键词**：自动驾驶规划, 世界模型, 多面表示学习, 条件扩散变换器, 4D重建

## 3 点简述
- 核心问题：自动驾驶需在复杂环境中进行可靠高效规划，需模型能推理场景几何、外观和动态。
- 方法要点：构建结构和动态感知的潜在世界表示，结合重建与生成框架，使用条件扩散变换器预测未来演化。
- 实验或效果：在轨迹规划、4D重建和生成任务中验证有效性，展示多面世界表示作为统一驾驶智能基础的潜力。

## 摘要（原文）

> Achieving reliable and efficient planning in complex driving environments requires a model that can reason over the scene's geometry, appearance, and dynamics. We present UniDWM, a unified driving world model that advances autonomous driving through multifaceted representation learning. UniDWM constructs a structure- and dynamic-aware latent world representation that serves as a physically grounded state space, enabling consistent reasoning across perception, prediction, and planning. Specifically, a joint reconstruction pathway learns to recover the scene's structure, including geometry and visual texture, while a collaborative generation framework leverages a conditional diffusion transformer to forecast future world evolution within the latent space. Furthermore, we show that our UniDWM can be deemed as a variation of VAE, which provides theoretical guidance for the multifaceted representation learning. Extensive experiments demonstrate the effectiveness of UniDWM in trajectory planning, 4D reconstruction and generation, highlighting the potential of multifaceted world representations as a foundation for unified driving intelligence. The code will be publicly available at https://github.com/Say2L/UniDWM.

