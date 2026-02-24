---
layout: default
title: Decoupling Defense Strategies for Robust Image Watermarking
---

# Decoupling Defense Strategies for Robust Image Watermarking
**arXiv**：[2602.20053v1](https://arxiv.org/abs/2602.20053) · [PDF](https://arxiv.org/pdf/2602.20053.pdf)  
**作者**：Jiahui Chen, Zehang Deng, Zeyu Zhang, Chaoyang Li, Lianchen Jia, Lifeng Sun  

**一句话要点**：提出AdvMark两阶段微调框架，通过解耦防御策略提升图像水印的鲁棒性和图像质量。

**关键词**：图像水印, 对抗训练, 鲁棒性优化, 两阶段微调, 图像质量保护

## 3 点简述
- 核心问题：传统联合优化方法在对抗攻击和再生攻击下鲁棒性有限，且会降低干净图像准确率。
- 方法要点：第一阶段针对对抗攻击，通过条件更新解码器的对抗训练保护编码器；第二阶段针对失真和再生攻击，采用带约束的图像优化和早停策略。
- 实验或效果：在失真、再生和对抗攻击下，准确率分别提升最高达29%、33%和46%，同时保持高图像质量。

## 摘要（原文）

> Deep learning-based image watermarking, while robust against conventional distortions, remains vulnerable to advanced adversarial and regeneration attacks. Conventional countermeasures, which jointly optimize the encoder and decoder via a noise layer, face 2 inevitable challenges: (1) decrease of clean accuracy due to decoder adversarial training and (2) limited robustness due to simultaneous training of all three advanced attacks. To overcome these issues, we propose AdvMark, a novel two-stage fine-tuning framework that decouples the defense strategies. In stage 1, we address adversarial vulnerability via a tailored adversarial training paradigm that primarily fine-tunes the encoder while only conditionally updating the decoder. This approach learns to move the image into a non-attackable region, rather than modifying the decision boundary, thus preserving clean accuracy. In stage 2, we tackle distortion and regeneration attacks via direct image optimization. To preserve the adversarial robustness gained in stage 1, we formulate a principled, constrained image loss with theoretical guarantees, which balances the deviation from cover and previous encoded images. We also propose a quality-aware early-stop to further guarantee the lower bound of visual quality. Extensive experiments demonstrate AdvMark outperforms with the highest image quality and comprehensive robustness, i.e. up to 29\%, 33\% and 46\% accuracy improvement for distortion, regeneration and adversarial attacks, respectively.

