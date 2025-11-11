---
layout: default
title: Federated Learning for Video Violence Detection: Complementary Roles of Lightweight CNNs and Vision-Language Models for Energy-Efficient Use
---

# Federated Learning for Video Violence Detection: Complementary Roles of Lightweight CNNs and Vision-Language Models for Energy-Efficient Use
**arXiv**：[2511.07171v1](https://arxiv.org/abs/2511.07171) · [PDF](https://arxiv.org/pdf/2511.07171.pdf)  
**作者**：Sébastien Thuau, Siba Haidar, Rachid Chelouah  

**一句话要点**：比较轻量CNN与视觉语言模型在联邦学习视频暴力检测中的能效与性能

**关键词**：联邦学习, 视频暴力检测, 能效优化, 视觉语言模型, 3D CNN, LoRA微调

## 3 点简述
- 核心问题：联邦学习视频暴力检测中，大模型部署带来高能耗与隐私挑战。
- 方法要点：对比零-shot VLM、LoRA微调VLM和个性化联邦学习3D CNN策略。
- 实验效果：3D CNN在RWF-2000等数据集上准确率超90%，能耗减半，VLM提升多类准确率。

## 摘要（原文）

> Deep learning-based video surveillance increasingly demands
> privacy-preserving architectures with low computational and environmental
> overhead. Federated learning preserves privacy but deploying large
> vision-language models (VLMs) introduces major energy and sustainability
> challenges. We compare three strategies for federated violence detection under
> realistic non-IID splits on the RWF-2000 and RLVS datasets: zero-shot inference
> with pretrained VLMs, LoRA-based fine-tuning of LLaVA-NeXT-Video-7B, and
> personalized federated learning of a 65.8M-parameter 3D CNN. All methods exceed
> 90% accuracy in binary violence detection. The 3D CNN achieves superior
> calibration (ROC AUC 92.59%) at roughly half the energy cost (240 Wh vs. 570
> Wh) of federated LoRA, while VLMs provide richer multimodal reasoning.
> Hierarchical category grouping (based on semantic similarity and class
> exclusion) boosts VLM multiclass accuracy from 65.31% to 81% on the UCF-Crime
> dataset. To our knowledge, this is the first comparative simulation study of
> LoRA-tuned VLMs and personalized CNNs for federated violence detection, with
> explicit energy and CO2e quantification. Our results inform hybrid deployment
> strategies that default to efficient CNNs for routine inference and selectively
> engage VLMs for complex contextual reasoning.

