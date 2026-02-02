---
layout: default
title: Beauty and the Beast: Imperceptible Perturbations Against Diffusion-Based Face Swapping via Directional Attribute Editing
---

# Beauty and the Beast: Imperceptible Perturbations Against Diffusion-Based Face Swapping via Directional Attribute Editing
**arXiv**：[2601.22744v1](https://arxiv.org/abs/2601.22744) · [PDF](https://arxiv.org/pdf/2601.22744.pdf)  
**作者**：Yilong Huang, Songze Li  

**一句话要点**：提出FaceDefense框架，通过方向性属性编辑增强对抗性示例，以防御基于扩散的人脸交换攻击。

**关键词**：人脸交换防御, 扩散模型, 对抗性示例, 属性编辑, 主动防御

## 3 点简述
- 核心问题：现有主动防御方法在扰动大小与保护效果间存在权衡，大扰动扭曲面部结构，小扰动降低防御效果。
- 方法要点：引入扩散损失强化对抗性示例防御力，利用方向性面部属性编辑恢复扰动引起的扭曲，提升视觉不可感知性。
- 实验或效果：通过两阶段交替优化生成最终扰动图像，实验显示在不可感知性和防御效果上显著优于现有方法。

## 摘要（原文）

> Diffusion-based face swapping achieves state-of-the-art performance, yet it also exacerbates the potential harm of malicious face swapping to violate portraiture right or undermine personal reputation. This has spurred the development of proactive defense methods. However, existing approaches face a core trade-off: large perturbations distort facial structures, while small ones weaken protection effectiveness. To address these issues, we propose FaceDefense, an enhanced proactive defense framework against diffusion-based face swapping. Our method introduces a new diffusion loss to strengthen the defensive efficacy of adversarial examples, and employs a directional facial attribute editing to restore perturbation-induced distortions, thereby enhancing visual imperceptibility. A two-phase alternating optimization strategy is designed to generate final perturbed face images. Extensive experiments show that FaceDefense significantly outperforms existing methods in both imperceptibility and defense effectiveness, achieving a superior trade-off.

