---
layout: default
title: Universal Anti-forensics Attack against Image Forgery Detection via Multi-modal Guidance
---

# Universal Anti-forensics Attack against Image Forgery Detection via Multi-modal Guidance
**arXiv**：[2602.06530v1](https://arxiv.org/abs/2602.06530) · [PDF](https://arxiv.org/pdf/2602.06530.pdf)  
**作者**：Haipeng Li, Rongxuan Peng, Anwei Luo, Shunquan Tan, Changsheng Chen, Anastasia Antsiferova  

**一句话要点**：提出ForgeryEraser框架，通过多模态引导执行通用反取证攻击以削弱AIGC检测器性能。

**关键词**：反取证攻击, AIGC检测, 视觉语言模型, 多模态引导, 伪造图像, 特征空间

## 3 点简述
- 核心问题：现有AIGC检测器评估忽略反取证攻击，导致实际应用中的鲁棒性不足。
- 方法要点：利用视觉语言模型共享特征空间，设计多模态引导损失，将伪造图像嵌入推向真实文本锚点以消除伪造痕迹。
- 实验或效果：在全局合成和局部编辑基准上，显著降低先进AIGC检测器性能，并诱导可解释模型生成与真实图像一致的解释。

## 摘要（原文）

> The rapid advancement of AI-Generated Content (AIGC) technologies poses significant challenges for authenticity assessment. However, existing evaluation protocols largely overlook anti-forensics attack, failing to ensure the comprehensive robustness of state-of-the-art AIGC detectors in real-world applications. To bridge this gap, we propose ForgeryEraser, a framework designed to execute universal anti-forensics attack without access to the target AIGC detectors. We reveal an adversarial vulnerability stemming from the systemic reliance on Vision-Language Models (VLMs) as shared backbones (e.g., CLIP), where downstream AIGC detectors inherit the feature space of these publicly accessible models. Instead of traditional logit-based optimization, we design a multi-modal guidance loss to drive forged image embeddings within the VLM feature space toward text-derived authentic anchors to erase forgery traces, while repelling them from forgery anchors. Extensive experiments demonstrate that ForgeryEraser causes substantial performance degradation to advanced AIGC detectors on both global synthesis and local editing benchmarks. Moreover, ForgeryEraser induces explainable forensic models to generate explanations consistent with authentic images for forged images. Our code will be made publicly available.

