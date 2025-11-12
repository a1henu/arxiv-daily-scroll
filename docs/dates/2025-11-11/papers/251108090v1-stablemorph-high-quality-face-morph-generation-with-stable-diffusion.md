---
layout: default
title: StableMorph: High-Quality Face Morph Generation with Stable Diffusion
---

# StableMorph: High-Quality Face Morph Generation with Stable Diffusion
**arXiv**：[2511.08090v1](https://arxiv.org/abs/2511.08090) · [PDF](https://arxiv.org/pdf/2511.08090.pdf)  
**作者**：Wassim Kabbani, Kiran Raja, Raghavendra Ramachandra, Christoph Busch  

**一句话要点**：提出StableMorph方法以生成高质量人脸融合图像，用于评估生物识别安全。

**关键词**：人脸融合攻击, 扩散模型, 生物识别安全, 图像生成, 攻击检测

## 3 点简述
- 人脸融合攻击威胁生物识别系统，现有方法图像模糊且易检测。
- 基于扩散模型生成无伪影、细节清晰的完整头部融合图像。
- 实验显示图像质量高，能有效欺骗人脸识别系统，提升检测挑战。

## 摘要（原文）

> Face morphing attacks threaten the integrity of biometric identity systems by enabling multiple individuals to share a single identity. To develop and evaluate effective morphing attack detection (MAD) systems, we need access to high-quality, realistic morphed images that reflect the challenges posed in real-world scenarios. However, existing morph generation methods often produce images that are blurry, riddled with artifacts, or poorly constructed making them easy to detect and not representative of the most dangerous attacks. In this work, we introduce StableMorph, a novel approach that generates highly realistic, artifact-free morphed face images using modern diffusion-based image synthesis. Unlike prior methods, StableMorph produces full-head images with sharp details, avoids common visual flaws, and offers unmatched control over visual attributes. Through extensive evaluation, we show that StableMorph images not only rival or exceed the quality of genuine face images but also maintain a strong ability to fool face recognition systems posing a greater challenge to existing MAD solutions and setting a new standard for morph quality in research and operational testing. StableMorph improves the evaluation of biometric security by creating more realistic and effective attacks and supports the development of more robust detection systems.

