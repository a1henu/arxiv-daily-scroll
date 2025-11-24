---
layout: default
title: One-Step Diffusion Transformer for Controllable Real-World Image Super-Resolution
---

# One-Step Diffusion Transformer for Controllable Real-World Image Super-Resolution
**arXiv**：[2511.17138v1](https://arxiv.org/abs/2511.17138) · [PDF](https://arxiv.org/pdf/2511.17138.pdf)  
**作者**：Yushun Fang, Yuxiang Chen, Shibo Yin, Qiang Hu, Jiangchao Yao, Ya Zhang, Xiaoyun Zhang, Yanfeng Wang  

**一句话要点**：提出ODTSR以解决真实世界图像超分辨率中保真度与可控性的平衡问题

**关键词**：图像超分辨率, 扩散模型, 可控生成, 一步推理, 噪声混合流, 保真度训练

## 3 点简述
- 核心问题：多步扩散方法生成多样但保真度低，一步方法保真度高但可控性差
- 方法要点：引入噪声混合视觉流设计，结合可调噪声和一致噪声，实现一步推理
- 实验或效果：在通用Real-ISR和中文场景文本超分辨率上达到SOTA，无需特定数据集训练

## 摘要（原文）

> Recent advances in diffusion-based real-world image super-resolution (Real-ISR) have demonstrated remarkable perceptual quality, yet the balance between fidelity and controllability remains a problem: multi-step diffusion-based methods suffer from generative diversity and randomness, resulting in low fidelity, while one-step methods lose control flexibility due to fidelity-specific finetuning. In this paper, we present ODTSR, a one-step diffusion transformer based on Qwen-Image that performs Real-ISR considering fidelity and controllability simultaneously: a newly introduced visual stream receives low-quality images (LQ) with adjustable noise (Control Noise), and the original visual stream receives LQs with consistent noise (Prior Noise), forming the Noise-hybrid Visual Stream (NVS) design. ODTSR further employs Fidelity-aware Adversarial Training (FAA) to enhance controllability and achieve one-step inference. Extensive experiments demonstrate that ODTSR not only achieves state-of-the-art (SOTA) performance on generic Real-ISR, but also enables prompt controllability on challenging scenarios such as real-world scene text image super-resolution (STISR) of Chinese characters without training on specific datasets.

