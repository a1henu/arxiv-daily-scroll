---
layout: default
title: Can You Trust What You See? Alpha Channel No-Box Attacks on Video Object Detection
---

# Can You Trust What You See? Alpha Channel No-Box Attacks on Video Object Detection
**arXiv**：[2510.19574v1](https://arxiv.org/abs/2510.19574) · [PDF](https://arxiv.org/pdf/2510.19574.pdf)  
**作者**：Ariana Yi, Ce Zhou, Liyang Xiao, Qiben Yan  

**一句话要点**：提出Alpha-Cloak无盒攻击，利用RGBA视频alpha通道欺骗视频目标检测器

**关键词**：无盒对抗攻击, 视频目标检测, alpha通道, 视觉隐形, 多模态模型安全

## 3 点简述
- 核心问题：视频目标检测器在无盒设置下易受对抗攻击，alpha通道漏洞未受关注
- 方法要点：通过alpha通道融合恶意与良性视频，实现视觉隐形且无需模型信息
- 实验或效果：在多种检测器和模型中攻击成功率100%，揭示新安全威胁

## 摘要（原文）

> As object detection models are increasingly deployed in cyber-physical
> systems such as autonomous vehicles (AVs) and surveillance platforms, ensuring
> their security against adversarial threats is essential. While prior work has
> explored adversarial attacks in the image domain, those attacks in the video
> domain remain largely unexamined, especially in the no-box setting. In this
> paper, we present {\alpha}-Cloak, the first no-box adversarial attack on object
> detectors that operates entirely through the alpha channel of RGBA videos.
> {\alpha}-Cloak exploits the alpha channel to fuse a malicious target video with
> a benign video, resulting in a fused video that appears innocuous to human
> viewers but consistently fools object detectors. Our attack requires no access
> to model architecture, parameters, or outputs, and introduces no perceptible
> artifacts. We systematically study the support for alpha channels across common
> video formats and playback applications, and design a fusion algorithm that
> ensures visual stealth and compatibility. We evaluate {\alpha}-Cloak on five
> state-of-the-art object detectors, a vision-language model, and a multi-modal
> large language model (Gemini-2.0-Flash), demonstrating a 100% attack success
> rate across all scenarios. Our findings reveal a previously unexplored
> vulnerability in video-based perception systems, highlighting the urgent need
> for defenses that account for the alpha channel in adversarial settings.

