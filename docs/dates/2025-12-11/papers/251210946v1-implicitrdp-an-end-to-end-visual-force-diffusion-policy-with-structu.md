---
layout: default
title: ImplicitRDP: An End-to-End Visual-Force Diffusion Policy with Structural Slow-Fast Learning
---

# ImplicitRDP: An End-to-End Visual-Force Diffusion Policy with Structural Slow-Fast Learning
**arXiv**：[2512.10946v1](https://arxiv.org/abs/2512.10946) · [PDF](https://arxiv.org/pdf/2512.10946.pdf)  
**作者**：Wendi Chen, Han Xue, Yi Wang, Fangyuan Zhou, Jun Lv, Yang Jin, Shirun Tang, Chuan Wen, Cewu Lu  

**一句话要点**：提出ImplicitRDP视觉-力扩散策略，通过结构慢快学习整合视觉规划与力控制，用于接触丰富操作任务。

**关键词**：视觉-力融合, 扩散策略, 结构慢快学习, 接触操作, 端到端学习, 模态正则化

## 3 点简述
- 核心问题：视觉与力信号频率和信息差异大，整合困难，影响接触操作性能。
- 方法要点：采用结构慢快学习处理异步模态，虚拟目标正则化防止模态崩溃，实现端到端策略。
- 实验或效果：在接触丰富任务中优于仅视觉和分层基线，提升反应性和成功率。

## 摘要（原文）

> Human-level contact-rich manipulation relies on the distinct roles of two key modalities: vision provides spatially rich but temporally slow global context, while force sensing captures rapid, high-frequency local contact dynamics. Integrating these signals is challenging due to their fundamental frequency and informational disparities. In this work, we propose ImplicitRDP, a unified end-to-end visual-force diffusion policy that integrates visual planning and reactive force control within a single network. We introduce Structural Slow-Fast Learning, a mechanism utilizing causal attention to simultaneously process asynchronous visual and force tokens, allowing the policy to perform closed-loop adjustments at the force frequency while maintaining the temporal coherence of action chunks. Furthermore, to mitigate modality collapse where end-to-end models fail to adjust the weights across different modalities, we propose Virtual-target-based Representation Regularization. This auxiliary objective maps force feedback into the same space as the action, providing a stronger, physics-grounded learning signal than raw force prediction. Extensive experiments on contact-rich tasks demonstrate that ImplicitRDP significantly outperforms both vision-only and hierarchical baselines, achieving superior reactivity and success rates with a streamlined training pipeline. Code and videos will be publicly available at https://implicit-rdp.github.io.

