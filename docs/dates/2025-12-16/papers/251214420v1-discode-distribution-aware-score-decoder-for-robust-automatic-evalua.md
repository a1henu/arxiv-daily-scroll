---
layout: default
title: DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning
---

# DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning
**arXiv**：[2512.14420v1](https://arxiv.org/abs/2512.14420) · [PDF](https://arxiv.org/pdf/2512.14420.pdf)  
**作者**：Nakamasa Inoue, Kanoko Goto, Masanari Oi, Martyna Gruszka, Mahiro Ukai, Takumi Hirose, Yusuke Sekikawa  

**一句话要点**：提出DISCODE方法以解决大视觉语言模型在图像描述评估中的领域偏移鲁棒性问题。

**关键词**：图像描述评估, 大视觉语言模型, 领域偏移鲁棒性, 测试时自适应, 无参考评估指标, 多域基准

## 3 点简述
- 核心问题：大视觉语言模型在图像描述评估中，尤其在领域偏移场景下，难以生成与人类判断一致的鲁棒评分。
- 方法要点：引入分布感知分数解码器DISCODE，采用测试时自适应评估，通过高斯先验分布和ATT损失提升评分估计鲁棒性。
- 实验或效果：在MCEval新基准和四个现有基准上，DISCODE作为无参考评估指标达到最先进性能。

## 摘要（原文）

> Large vision-language models (LVLMs) have shown impressive performance across a broad range of multimodal tasks. However, robust image caption evaluation using LVLMs remains challenging, particularly under domain-shift scenarios. To address this issue, we introduce the Distribution-Aware Score Decoder (DISCODE), a novel finetuning-free method that generates robust evaluation scores better aligned with human judgments across diverse domains. The core idea behind DISCODE lies in its test-time adaptive evaluation approach, which introduces the Adaptive Test-Time (ATT) loss, leveraging a Gaussian prior distribution to improve robustness in evaluation score estimation. This loss is efficiently minimized at test time using an analytical solution that we derive. Furthermore, we introduce the Multi-domain Caption Evaluation (MCEval) benchmark, a new image captioning evaluation benchmark covering six distinct domains, designed to assess the robustness of evaluation metrics. In our experiments, we demonstrate that DISCODE achieves state-of-the-art performance as a reference-free evaluation metric across MCEval and four representative existing benchmarks.

