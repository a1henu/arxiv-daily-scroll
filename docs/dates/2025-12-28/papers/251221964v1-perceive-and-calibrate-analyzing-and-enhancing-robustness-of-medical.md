---
layout: default
title: Perceive and Calibrate: Analyzing and Enhancing Robustness of Medical Multi-Modal Large Language Models
---

# Perceive and Calibrate: Analyzing and Enhancing Robustness of Medical Multi-Modal Large Language Models
**arXiv**：[2512.21964v1](https://arxiv.org/abs/2512.21964) · [PDF](https://arxiv.org/pdf/2512.21964.pdf)  
**作者**：Dunyuan XU, Xikai Yang, Yaoqian Li, Juzheng Miao, Jinpeng Li, Pheng-Ann Heng  

**一句话要点**：提出无需训练的IMC框架，通过感知-校准原则增强医疗多模态大语言模型对图像和文本噪声的鲁棒性。

**关键词**：医疗多模态大语言模型, 鲁棒性增强, 无需训练校准, 图像噪声处理, 文本噪声处理, 感知-校准原则

## 3 点简述
- 核心问题：医疗MLLMs对真实世界输入扰动（如图像伪影和文本错误）敏感，影响临床适用性，且现有研究不足。
- 方法要点：引入IMC框架，包括视觉模态的PDC（利用自身编码器识别噪声并校准）和文本模态的SMS（基于自评估的多代理系统精炼噪声文本）。
- 实验或效果：在包含11种噪声的基准测试中，方法在多个模态上达到最先进性能，提升临床场景鲁棒性。

## 摘要（原文）

> Medical Multi-modal Large Language Models (MLLMs) have shown promising clinical performance. However, their sensitivity to real-world input perturbations, such as imaging artifacts and textual errors, critically undermines their clinical applicability. Systematic analysis of such noise impact on medical MLLMs remains largely unexplored. Furthermore, while several works have investigated the MLLMs' robustness in general domains, they primarily focus on text modality and rely on costly fine-tuning. They are inadequate to address the complex noise patterns and fulfill the strict safety standards in medicine. To bridge this gap, this work systematically analyzes the impact of various perturbations on medical MLLMs across both visual and textual modalities. Building on our findings, we introduce a training-free Inherent-enhanced Multi-modal Calibration (IMC) framework that leverages MLLMs' inherent denoising capabilities following the perceive-and-calibrate principle for cross-modal robustness enhancement. For the visual modality, we propose a Perturbation-aware Denoising Calibration (PDC) which leverages MLLMs' own vision encoder to identify noise patterns and perform prototype-guided feature calibration. For text denoising, we design a Self-instantiated Multi-agent System (SMS) that exploits the MLLMs' self-assessment capabilities to refine noisy text through a cooperative hierarchy of agents. We construct a benchmark containing 11 types of noise across both image and text modalities on 2 datasets. Experimental results demonstrate our method achieves the state-of-the-art performance across multiple modalities, showing potential to enhance MLLMs' robustness in real clinical scenarios.

