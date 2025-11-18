---
layout: default
title: Shedding Light on VLN Robustness: A Black-box Framework for Indoor Lighting-based Adversarial Attack
---

# Shedding Light on VLN Robustness: A Black-box Framework for Indoor Lighting-based Adversarial Attack
**arXiv**：[2511.13132v1](https://arxiv.org/abs/2511.13132) · [PDF](https://arxiv.org/pdf/2511.13132.pdf)  
**作者**：Chenyang Li, Wenbing Tang, Yihao Huang, Sinong Simon Zhan, Ming Hu, Xiaojun Jia, Yang Liu  

**一句话要点**：提出室内光照对抗攻击框架，揭示视觉语言导航在真实光照变化下的脆弱性

**关键词**：视觉语言导航, 对抗攻击, 室内光照, 黑盒框架, 鲁棒性评估

## 3 点简述
- 核心问题：视觉语言导航代理在真实室内光照变化下的鲁棒性不足，现有攻击方法不实用
- 方法要点：设计黑盒攻击框架，通过静态和动态光照变化干扰导航决策
- 实验或效果：在多个任务中显著提高失败率，降低轨迹效率，暴露新漏洞

## 摘要（原文）

> Vision-and-Language Navigation (VLN) agents have made remarkable progress, but their robustness remains insufficiently studied. Existing adversarial evaluations often rely on perturbations that manifest as unusual textures rarely encountered in everyday indoor environments. Errors under such contrived conditions have limited practical relevance, as real-world agents are unlikely to encounter such artificial patterns. In this work, we focus on indoor lighting, an intrinsic yet largely overlooked scene attribute that strongly influences navigation. We propose Indoor Lighting-based Adversarial Attack (ILA), a black-box framework that manipulates global illumination to disrupt VLN agents. Motivated by typical household lighting usage, we design two attack modes: Static Indoor Lighting-based Attack (SILA), where the lighting intensity remains constant throughout an episode, and Dynamic Indoor Lighting-based Attack (DILA), where lights are switched on or off at critical moments to induce abrupt illumination changes. We evaluate ILA on two state-of-the-art VLN models across three navigation tasks. Results show that ILA significantly increases failure rates while reducing trajectory efficiency, revealing previously unrecognized vulnerabilities of VLN agents to realistic indoor lighting variations.

