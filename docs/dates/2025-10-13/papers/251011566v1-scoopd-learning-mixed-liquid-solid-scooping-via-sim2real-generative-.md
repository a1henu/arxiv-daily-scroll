---
layout: default
title: SCOOP'D: Learning Mixed-Liquid-Solid Scooping via Sim2Real Generative Policy
---

# SCOOP'D: Learning Mixed-Liquid-Solid Scooping via Sim2Real Generative Policy
**arXiv**：[2510.11566v1](https://arxiv.org/abs/2510.11566) · [PDF](https://arxiv.org/pdf/2510.11566.pdf)  
**作者**：Kuanning Wang, Yongchong Gu, Yuqian Fu, Zeyu Shangguan, Sicheng He, Xiangyang Xue, Yanwei Fu, Daniel Seita  

**一句话要点**：提出SCOOP'D方法，通过仿真到真实生成策略学习混合液体固体舀取。

**关键词**：机器人舀取, 仿真到真实, 生成策略, 扩散模型, 可变形物体操作

## 3 点简述
- 核心问题：机器人舀取需处理复杂工具-物体交互和可变形物体动态。
- 方法要点：利用仿真收集演示，通过扩散生成策略模仿观察输入。
- 实验效果：零样本部署在465次试验中表现优异，优于基线方法。

## 摘要（原文）

> Scooping items with tools such as spoons and ladles is common in daily life,
> ranging from assistive feeding to retrieving items from environmental disaster
> sites. However, developing a general and autonomous robotic scooping policy is
> challenging since it requires reasoning about complex tool-object interactions.
> Furthermore, scooping often involves manipulating deformable objects, such as
> granular media or liquids, which is challenging due to their
> infinite-dimensional configuration spaces and complex dynamics. We propose a
> method, SCOOP'D, which uses simulation from OmniGibson (built on NVIDIA
> Omniverse) to collect scooping demonstrations using algorithmic procedures that
> rely on privileged state information. Then, we use generative policies via
> diffusion to imitate demonstrations from observational input. We directly apply
> the learned policy in diverse real-world scenarios, testing its performance on
> various item quantities, item characteristics, and container types. In
> zero-shot deployment, our method demonstrates promising results across 465
> trials in diverse scenarios, including objects of different difficulty levels
> that we categorize as "Level 1" and "Level 2." SCOOP'D outperforms all
> baselines and ablations, suggesting that this is a promising approach to
> acquiring robotic scooping skills. Project page is at
> https://scoopdiff.github.io/.

