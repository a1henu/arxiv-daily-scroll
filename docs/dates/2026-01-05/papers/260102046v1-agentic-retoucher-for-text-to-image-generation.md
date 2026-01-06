---
layout: default
title: Agentic Retoucher for Text-To-Image Generation
---

# Agentic Retoucher for Text-To-Image Generation
**arXiv**：[2601.02046v1](https://arxiv.org/abs/2601.02046) · [PDF](https://arxiv.org/pdf/2601.02046.pdf)  
**作者**：Shaocheng Shen, Jianfeng Liang. Chunlei Cai, Cong Geng, Huiyu Duan, Xiaoyun Zhang, Qiang Hu, Guangtao Zhai  

**一句话要点**：提出Agentic Retoucher框架，通过感知-推理-行动循环解决文本到图像生成中的小尺度失真问题。

**关键词**：文本到图像生成, 失真校正, 分层决策框架, 感知推理行动循环, 局部修复, 数据集构建

## 3 点简述
- 核心问题：现有T2I扩散模型如SDXL和FLUX在肢体、面部等区域存在小尺度失真，现有细化方法成本高或语义漂移。
- 方法要点：设计分层决策框架，包括感知代理定位失真、推理代理进行诊断、行动代理执行局部修复，集成感知证据与可控校正。
- 实验或效果：构建GenBlemish-27K数据集，实验显示在感知质量、失真定位和人类偏好对齐方面优于现有方法。

## 摘要（原文）

> Text-to-image (T2I) diffusion models such as SDXL and FLUX have achieved impressive photorealism, yet small-scale distortions remain pervasive in limbs, face, text and so on. Existing refinement approaches either perform costly iterative re-generation or rely on vision-language models (VLMs) with weak spatial grounding, leading to semantic drift and unreliable local edits. To close this gap, we propose Agentic Retoucher, a hierarchical decision-driven framework that reformulates post-generation correction as a human-like perception-reasoning-action loop. Specifically, we design (1) a perception agent that learns contextual saliency for fine-grained distortion localization under text-image consistency cues, (2) a reasoning agent that performs human-aligned inferential diagnosis via progressive preference alignment, and (3) an action agent that adaptively plans localized inpainting guided by user preference. This design integrates perceptual evidence, linguistic reasoning, and controllable correction into a unified, self-corrective decision process. To enable fine-grained supervision and quantitative evaluation, we further construct GenBlemish-27K, a dataset of 6K T2I images with 27K annotated artifact regions across 12 categories. Extensive experiments demonstrate that Agentic Retoucher consistently outperforms state-of-the-art methods in perceptual quality, distortion localization and human preference alignment, establishing a new paradigm for self-corrective and perceptually reliable T2I generation.

