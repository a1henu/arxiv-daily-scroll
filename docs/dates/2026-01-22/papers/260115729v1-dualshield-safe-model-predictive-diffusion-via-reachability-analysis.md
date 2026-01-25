---
layout: default
title: DualShield: Safe Model Predictive Diffusion via Reachability Analysis for Interactive Autonomous Driving
---

# DualShield: Safe Model Predictive Diffusion via Reachability Analysis for Interactive Autonomous Driving
**arXiv**：[2601.15729v1](https://arxiv.org/abs/2601.15729) · [PDF](https://arxiv.org/pdf/2601.15729.pdf)  
**作者**：Rui Yang, Lei Zheng, Ruoyu Yao, Jun Ma  

**一句话要点**：提出DualShield框架，通过可达性分析确保交互式自动驾驶中扩散模型的安全与动态可行性。

**关键词**：自动驾驶规划, 扩散模型, 可达性分析, 安全屏障, 交互不确定性, 模型预测控制

## 3 点简述
- 核心问题：扩散模型在自动驾驶运动规划中难以强制执行车辆动力学，且依赖其他智能体准确预测，导致不确定交互下存在安全隐患。
- 方法要点：利用Hamilton-Jacobi可达性值函数，既引导扩散去噪过程朝向安全区域，又作为反应式安全屏障修改执行动作以确保安全。
- 实验或效果：在无保护U-turn场景模拟中，相比领先方法，DualShield显著提升了安全性和任务效率。

## 摘要（原文）

> Diffusion models have emerged as a powerful approach for multimodal motion planning in autonomous driving. However, their practical deployment is typically hindered by the inherent difficulty in enforcing vehicle dynamics and a critical reliance on accurate predictions of other agents, making them prone to safety issues under uncertain interactions. To address these limitations, we introduce DualShield, a planning and control framework that leverages Hamilton-Jacobi (HJ) reachability value functions in a dual capacity. First, the value functions act as proactive guidance, steering the diffusion denoising process towards safe and dynamically feasible regions. Second, they form a reactive safety shield using control barrier-value functions (CBVFs) to modify the executed actions and ensure safety. This dual mechanism preserves the rich exploration capabilities of diffusion models while providing principled safety assurance under uncertain and even adversarial interactions. Simulations in challenging unprotected U-turn scenarios demonstrate that DualShield significantly improves both safety and task efficiency compared to leading methods from different planning paradigms under uncertainty.

