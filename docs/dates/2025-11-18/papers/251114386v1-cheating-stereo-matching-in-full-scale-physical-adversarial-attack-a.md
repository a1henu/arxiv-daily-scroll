---
layout: default
title: Cheating Stereo Matching in Full-scale: Physical Adversarial Attack against Binocular Depth Estimation in Autonomous Driving
---

# Cheating Stereo Matching in Full-scale: Physical Adversarial Attack against Binocular Depth Estimation in Autonomous Driving
**arXiv**：[2511.14386v1](https://arxiv.org/abs/2511.14386) · [PDF](https://arxiv.org/pdf/2511.14386.pdf)  
**作者**：Kangqiao Zhao, Shuo Huai, Xurui Song, Jun Luo  

**一句话要点**：提出纹理化3D物理对抗攻击以欺骗自动驾驶中的双目深度估计

**关键词**：物理对抗攻击, 双目深度估计, 立体匹配, 自动驾驶安全, 3D渲染优化

## 3 点简述
- 核心问题：双目深度估计模型对物理对抗攻击的脆弱性未知，现有攻击多基于2D补丁
- 方法要点：使用全局伪装纹理的3D物理对抗示例，结合立体匹配渲染模块优化对齐
- 实验或效果：评估显示攻击能有效误导模型产生错误深度信息，提升隐蔽性和杀伤力

## 摘要（原文）

> Though deep neural models adopted to realize the perception of autonomous driving have proven vulnerable to adversarial examples, known attacks often leverage 2D patches and target mostly monocular perception. Therefore, the effectiveness of Physical Adversarial Examples (PAEs) on stereo-based binocular depth estimation remains largely unexplored. To this end, we propose the first texture-enabled physical adversarial attack against stereo matching models in the context of autonomous driving. Our method employs a 3D PAE with global camouflage texture rather than a local 2D patch-based one, ensuring both visual consistency and attack effectiveness across different viewpoints of stereo cameras. To cope with the disparity effect of these cameras, we also propose a new 3D stereo matching rendering module that allows the PAE to be aligned with real-world positions and headings in binocular vision. We further propose a novel merging attack that seamlessly blends the target into the environment through fine-grained PAE optimization. It has significantly enhanced stealth and lethality upon existing hiding attacks that fail to get seamlessly merged into the background. Extensive evaluations show that our PAEs can successfully fool the stereo models into producing erroneous depth information.

