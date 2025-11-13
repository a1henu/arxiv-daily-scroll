---
layout: default
title: AuthSig: Safeguarding Scanned Signatures Against Unauthorized Reuse in Paperless Workflows
---

# AuthSig: Safeguarding Scanned Signatures Against Unauthorized Reuse in Paperless Workflows
**arXiv**：[2511.08967v1](https://arxiv.org/abs/2511.08967) · [PDF](https://arxiv.org/pdf/2511.08967.pdf)  
**作者**：RuiQiang Zhang, Zehua Ma, Guanjie Wang, Chang Liu, Hengyi Wang, Weiming Zhang  

**一句话要点**：提出AuthSig框架，通过生成模型和水印保护扫描签名免遭未授权重用

**关键词**：电子签名保护, 生成模型, 数字水印, 数据增强, 身份认证

## 3 点简述
- 静态扫描签名易被恶意复制和重用，缺乏可靠验证机制
- 基于生成模型和水印，通过风格嵌入隐式编码认证信息
- 实验显示在数字和打印扫描场景下提取准确率超98%

## 摘要（原文）

> With the deepening trend of paperless workflows, signatures as a means of identity authentication are gradually shifting from traditional ink-on-paper to electronic formats.Despite the availability of dynamic pressure-sensitive and PKI-based digital signatures, static scanned signatures remain prevalent in practice due to their convenience. However, these static images, having almost lost their authentication attributes, cannot be reliably verified and are vulnerable to malicious copying and reuse. To address these issues, we propose AuthSig, a novel static electronic signature framework based on generative models and watermark, which binds authentication information to the signature image. Leveraging the human visual system's insensitivity to subtle style variations, AuthSig finely modulates style embeddings during generation to implicitly encode watermark bits-enforcing a One Signature, One Use policy.To overcome the scarcity of handwritten signature data and the limitations of traditional augmentation methods, we introduce a keypoint-driven data augmentation strategy that effectively enhances style diversity to support robust watermark embedding. Experimental results show that AuthSig achieves over 98% extraction accuracy under both digital-domain distortions and signature-specific degradations, and remains effective even in print-scan scenarios.

