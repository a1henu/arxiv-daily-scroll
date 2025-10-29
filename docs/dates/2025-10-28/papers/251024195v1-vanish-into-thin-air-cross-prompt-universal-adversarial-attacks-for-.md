---
layout: default
title: Vanish into Thin Air: Cross-prompt Universal Adversarial Attacks for SAM2
---

# Vanish into Thin Air: Cross-prompt Universal Adversarial Attacks for SAM2
**arXiv**：[2510.24195v1](https://arxiv.org/abs/2510.24195) · [PDF](https://arxiv.org/pdf/2510.24195.pdf)  
**作者**：Ziqi Zhou, Yifan Hu, Yufei Song, Zijing Li, Shengshan Hu, Leo Yu Zhang, Dezhong Yao, Long Zheng, Hai Jin  

**一句话要点**：提出UAP-SAM2以解决SAM2模型在跨提示通用对抗攻击中的鲁棒性问题

**关键词**：通用对抗攻击, 视频分割, 语义偏差, 跨提示转移, SAM2模型, 鲁棒性分析

## 3 点简述
- 核心问题：SAM2模型在视频分割中面临提示依赖和跨帧语义纠缠的鲁棒性挑战
- 方法要点：设计目标扫描策略和双语义偏差框架，优化通用对抗扰动
- 实验或效果：在六个数据集上验证，显著优于现有攻击方法

## 摘要（原文）

> Recent studies reveal the vulnerability of the image segmentation foundation
> model SAM to adversarial examples. Its successor, SAM2, has attracted
> significant attention due to its strong generalization capability in video
> segmentation. However, its robustness remains unexplored, and it is unclear
> whether existing attacks on SAM can be directly transferred to SAM2. In this
> paper, we first analyze the performance gap of existing attacks between SAM and
> SAM2 and highlight two key challenges arising from their architectural
> differences: directional guidance from the prompt and semantic entanglement
> across consecutive frames. To address these issues, we propose UAP-SAM2, the
> first cross-prompt universal adversarial attack against SAM2 driven by dual
> semantic deviation. For cross-prompt transferability, we begin by designing a
> target-scanning strategy that divides each frame into k regions, each randomly
> assigned a prompt, to reduce prompt dependency during optimization. For
> effectiveness, we design a dual semantic deviation framework that optimizes a
> UAP by distorting the semantics within the current frame and disrupting the
> semantic consistency across consecutive frames. Extensive experiments on six
> datasets across two segmentation tasks demonstrate the effectiveness of the
> proposed method for SAM2. The comparative results show that UAP-SAM2
> significantly outperforms state-of-the-art (SOTA) attacks by a large margin.

