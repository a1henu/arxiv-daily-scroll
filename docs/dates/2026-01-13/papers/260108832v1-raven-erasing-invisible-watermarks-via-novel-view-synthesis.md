---
layout: default
title: RAVEN: Erasing Invisible Watermarks via Novel View Synthesis
---

# RAVEN: Erasing Invisible Watermarks via Novel View Synthesis
**arXiv**：[2601.08832v1](https://arxiv.org/abs/2601.08832) · [PDF](https://arxiv.org/pdf/2601.08832.pdf)  
**作者**：Fahad Shamshad, Nils Lukas, Karthik Nandakumar  

**一句话要点**：提出基于视角合成的零样本扩散框架以移除不可见水印

**关键词**：不可见水印移除, 视角合成, 零样本攻击, 扩散模型, 语义保持变换

## 3 点简述
- 揭示不可见水印在语义保持视角变换下的脆弱性
- 利用潜在空间几何变换和视图引导注意力实现零样本水印移除
- 在15种水印方法上实现最先进的抑制效果并保持视觉保真度

## 摘要（原文）

> Invisible watermarking has become a critical mechanism for authenticating AI-generated image content, with major platforms deploying watermarking schemes at scale. However, evaluating the vulnerability of these schemes against sophisticated removal attacks remains essential to assess their reliability and guide robust design. In this work, we expose a fundamental vulnerability in invisible watermarks by reformulating watermark removal as a view synthesis problem. Our key insight is that generating a perceptually consistent alternative view of the same semantic content, akin to re-observing a scene from a shifted perspective, naturally removes the embedded watermark while preserving visual fidelity. This reveals a critical gap: watermarks robust to pixel-space and frequency-domain attacks remain vulnerable to semantic-preserving viewpoint transformations. We introduce a zero-shot diffusion-based framework that applies controlled geometric transformations in latent space, augmented with view-guided correspondence attention to maintain structural consistency during reconstruction. Operating on frozen pre-trained models without detector access or watermark knowledge, our method achieves state-of-the-art watermark suppression across 15 watermarking methods--outperforming 14 baseline attacks while maintaining superior perceptual quality across multiple datasets.

