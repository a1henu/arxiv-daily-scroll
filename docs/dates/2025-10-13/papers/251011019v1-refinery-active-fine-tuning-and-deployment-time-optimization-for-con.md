---
layout: default
title: Refinery: Active Fine-tuning and Deployment-time Optimization for Contact-Rich Policies
---

# Refinery: Active Fine-tuning and Deployment-time Optimization for Contact-Rich Policies
**arXiv**：[2510.11019v1](https://arxiv.org/abs/2510.11019) · [PDF](https://arxiv.org/pdf/2510.11019.pdf)  
**作者**：Bingjie Tang, Iretiayo Akinola, Jie Xu, Bowen Wen, Dieter Fox, Gaurav S. Sukhatme, Fabio Ramos, Abhishek Gupta, Yashraj Narang  

**一句话要点**：提出Refinery框架以优化接触丰富策略的微调与部署

**关键词**：机器人装配, 模拟学习, 贝叶斯优化, 高斯混合模型, 策略微调, 部署优化

## 3 点简述
- 核心问题：模拟学习策略在多样化初始条件下性能方差高，影响工业应用
- 方法要点：结合贝叶斯优化微调策略和高斯混合模型采样部署初始化
- 实验或效果：仿真成功率提升至91.51%，支持多部件链式组装

## 摘要（原文）

> Simulation-based learning has enabled policies for precise, contact-rich
> tasks (e.g., robotic assembly) to reach high success rates (~80%) under high
> levels of observation noise and control error. Although such performance may be
> sufficient for research applications, it falls short of industry standards and
> makes policy chaining exceptionally brittle. A key limitation is the high
> variance in individual policy performance across diverse initial conditions. We
> introduce Refinery, an effective framework that bridges this performance gap,
> robustifying policy performance across initial conditions. We propose Bayesian
> Optimization-guided fine-tuning to improve individual policies, and Gaussian
> Mixture Model-based sampling during deployment to select initializations that
> maximize execution success. Using Refinery, we improve mean success rates by
> 10.98% over state-of-the-art methods in simulation-based learning for robotic
> assembly, reaching 91.51% in simulation and comparable performance in the real
> world. Furthermore, we demonstrate that these fine-tuned policies can be
> chained to accomplish long-horizon, multi-part
> assembly$\unicode{x2013}$successfully assembling up to 8 parts without
> requiring explicit multi-step training.

