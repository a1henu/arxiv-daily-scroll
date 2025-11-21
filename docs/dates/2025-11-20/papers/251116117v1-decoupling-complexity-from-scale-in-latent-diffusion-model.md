---
layout: default
title: Decoupling Complexity from Scale in Latent Diffusion Model
---

# Decoupling Complexity from Scale in Latent Diffusion Model
**arXiv**：[2511.16117v1](https://arxiv.org/abs/2511.16117) · [PDF](https://arxiv.org/pdf/2511.16117.pdf)  
**作者**：Tianxiong Zhong, Xingye Tian, Xuebo Wang, Boyuan Jiang, Xin Tao, Pengfei Wan  

**一句话要点**：提出DCS-LDM以解耦视觉生成中信息复杂度与尺度，实现灵活计算-质量权衡。

**关键词**：潜在扩散模型, 视觉生成, 多尺度解码, 分层潜在空间, 计算-质量权衡

## 3 点简述
- 现有潜在扩散模型将内容复杂度与尺度耦合，导致潜在表示效率低下。
- DCS-LDM构建分层尺度无关潜在空间，通过多级令牌建模复杂度，支持任意分辨率解码。
- 实验显示DCS-LDM性能媲美先进方法，支持多尺度高质量生成和渐进式生成。

## 摘要（原文）

> Existing latent diffusion models typically couple scale with content complexity, using more latent tokens to represent higher-resolution images or higher-frame rate videos. However, the latent capacity required to represent visual data primarily depends on content complexity, with scale serving only as an upper bound. Motivated by this observation, we propose DCS-LDM, a novel paradigm for visual generation that decouples information complexity from scale. DCS-LDM constructs a hierarchical, scale-independent latent space that models sample complexity through multi-level tokens and supports decoding to arbitrary resolutions and frame rates within a fixed latent representation. This latent space enables DCS-LDM to achieve a flexible computation-quality tradeoff. Furthermore, by decomposing structural and detailed information across levels, DCS-LDM supports a progressive coarse-to-fine generation paradigm. Experimental results show that DCS-LDM delivers performance comparable to state-of-the-art methods while offering flexible generation across diverse scales and visual qualities.

