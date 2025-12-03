---
layout: default
title: SwarmDiffusion: End-To-End Traversability-Guided Diffusion for Embodiment-Agnostic Navigation of Heterogeneous Robots
---

# SwarmDiffusion: End-To-End Traversability-Guided Diffusion for Embodiment-Agnostic Navigation of Heterogeneous Robots
**arXiv**：[2512.02851v1](https://arxiv.org/abs/2512.02851) · [PDF](https://arxiv.org/pdf/2512.02851.pdf)  
**作者**：Iana Zhura, Sausar Karaf, Faryal Batool, Nipun Dhananjaya Weerakkodi Mudalige, Valerii Serpiva, Ali Alridha Abdulkarim, Aleksey Fedoseev, Didar Seyidov, Amjad Hajira, Dzmitry Tsetserukou  

**一句话要点**：提出SwarmDiffusion以解决异构机器人导航中视觉可通行性估计与轨迹生成的端到端统一问题

**关键词**：视觉可通行性估计, 端到端扩散模型, 异构机器人导航, 轨迹生成, 无提示学习, 轻量级推理

## 3 点简述
- 现有VLM方法依赖手工提示，泛化性差，且仅输出可通行图，轨迹生成需外部规划器
- SwarmDiffusion是轻量级扩散模型，从单RGB图像联合预测可通行性并生成可行轨迹，无需标注或规划器路径
- 在室内环境和两种机器人平台上实现80-100%导航成功率，推理时间0.09秒，仅需500样本适应新机器人

## 摘要（原文）

> Visual traversability estimation is critical for autonomous navigation, but existing VLM-based methods rely on hand-crafted prompts, generalize poorly across embodiments, and output only traversability maps, leaving trajectory generation to slow external planners. We propose SwarmDiffusion, a lightweight end-to-end diffusion model that jointly predicts traversability and generates a feasible trajectory from a single RGB image. To remove the need for annotated or planner-produced paths, we introduce a planner-free trajectory construction pipeline based on randomized waypoint sampling, Bezier smoothing, and regularization enforcing connectivity, safety, directionality, and path thinness. This enables learning stable motion priors without demonstrations. SwarmDiffusion leverages VLM-derived supervision without prompt engineering and conditions the diffusion process on a compact embodiment state, producing physically consistent, traversable paths that transfer across different robot platforms. Across indoor environments and two embodiments (quadruped and aerial), the method achieves 80-100\% navigation success and 0.09 s inference, and adapts to a new robot using only-500 additional visual samples. It generalizes reliably to unseen environments in simulation and real-world trials, offering a scalable, prompt-free approach to unified traversability reasoning and trajectory generation.

