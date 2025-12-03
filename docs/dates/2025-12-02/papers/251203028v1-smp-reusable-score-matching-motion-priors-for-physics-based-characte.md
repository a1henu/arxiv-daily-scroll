---
layout: default
title: SMP: Reusable Score-Matching Motion Priors for Physics-Based Character Control
---

# SMP: Reusable Score-Matching Motion Priors for Physics-Based Character Control
**arXiv**：[2512.03028v1](https://arxiv.org/abs/2512.03028) · [PDF](https://arxiv.org/pdf/2512.03028.pdf)  
**作者**：Yuxuan Mu, Ziyu Zhang, Yi Shi, Minami Matsumoto, Kotaro Imamura, Guy Tevet, Chuan Guo, Michael Taylor, Chang Shu, Pengcheng Xi, Xue Bin Peng  

**一句话要点**：提出可重用分数匹配运动先验，基于扩散模型提升物理角色控制自然性

**关键词**：运动先验, 分数匹配, 扩散模型, 物理角色控制, 可重用奖励

## 3 点简述
- 核心问题：对抗模仿学习先验需针对每个新控制器重新训练，限制重用性并需保留参考数据
- 方法要点：利用预训练运动扩散模型和分数蒸馏采样，构建任务无关可重用运动先验作为奖励函数
- 实验或效果：在多样化物理人形控制任务中，生成高质量运动，可组合风格合成新风格

## 摘要（原文）

> Data-driven motion priors that can guide agents toward producing naturalistic behaviors play a pivotal role in creating life-like virtual characters. Adversarial imitation learning has been a highly effective method for learning motion priors from reference motion data. However, adversarial priors, with few exceptions, need to be retrained for each new controller, thereby limiting their reusability and necessitating the retention of the reference motion data when training on downstream tasks. In this work, we present Score-Matching Motion Priors (SMP), which leverages pre-trained motion diffusion models and score distillation sampling (SDS) to create reusable task-agnostic motion priors. SMPs can be pre-trained on a motion dataset, independent of any control policy or task. Once trained, SMPs can be kept frozen and reused as general-purpose reward functions to train policies to produce naturalistic behaviors for downstream tasks. We show that a general motion prior trained on large-scale datasets can be repurposed into a variety of style-specific priors. Furthermore SMP can compose different styles to synthesize new styles not present in the original dataset. Our method produces high-quality motion comparable to state-of-the-art adversarial imitation learning methods through reusable and modular motion priors. We demonstrate the effectiveness of SMP across a diverse suite of control tasks with physically simulated humanoid characters. Video demo available at https://youtu.be/ravlZJteS20

