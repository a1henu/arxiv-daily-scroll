---
layout: default
title: Abstracting Robot Manipulation Skills via Mixture-of-Experts Diffusion Policies
---

# Abstracting Robot Manipulation Skills via Mixture-of-Experts Diffusion Policies
**arXiv**：[2601.21251v1](https://arxiv.org/abs/2601.21251) · [PDF](https://arxiv.org/pdf/2601.21251.pdf)  
**作者**：Ce Hao, Xuanran Zhai, Yaohua Liu, Harold Soh  

**一句话要点**：提出技能专家混合扩散策略以解决多任务机器人操作中模型扩展成本高的问题

**关键词**：机器人操作, 扩散策略, 专家混合, 多任务学习, 技能重用

## 3 点简述
- 核心问题：扩散策略在多任务场景下扩展模型规模和演示成本高
- 方法要点：学习紧凑正交技能基，使用粘性路由组合任务相关专家动作
- 实验或效果：在仿真和真实平台验证，实现更高成功率和更低推理成本

## 摘要（原文）

> Diffusion-based policies have recently shown strong results in robot manipulation, but their extension to multi-task scenarios is hindered by the high cost of scaling model size and demonstrations. We introduce Skill Mixture-of-Experts Policy (SMP), a diffusion-based mixture-of-experts policy that learns a compact orthogonal skill basis and uses sticky routing to compose actions from a small, task-relevant subset of experts at each step. A variational training objective supports this design, and adaptive expert activation at inference yields fast sampling without oversized backbones. We validate SMP in simulation and on a real dual-arm platform with multi-task learning and transfer learning tasks, where SMP achieves higher success rates and markedly lower inference cost than large diffusion baselines. These results indicate a practical path toward scalable, transferable multi-task manipulation: learn reusable skills once, activate only what is needed, and adapt quickly when tasks change.

