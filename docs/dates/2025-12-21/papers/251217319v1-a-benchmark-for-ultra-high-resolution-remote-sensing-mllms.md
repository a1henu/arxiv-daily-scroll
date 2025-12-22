---
layout: default
title: A Benchmark for Ultra-High-Resolution Remote Sensing MLLMs
---

# A Benchmark for Ultra-High-Resolution Remote Sensing MLLMs
**arXiv**：[2512.17319v1](https://arxiv.org/abs/2512.17319) · [PDF](https://arxiv.org/pdf/2512.17319.pdf)  
**作者**：Yunkai Dang, Meiyi Zhu, Donghao Wang, Yizhuo Zhang, Jiacheng Yang, Qi Fan, Yuekun Yang, Wenbin Li, Feng Miao, Yang Gao  

**一句话要点**：提出超高分遥感基准RSHR-Bench以解决现有基准分辨率低和推理任务设计缺陷问题。

**关键词**：超高分遥感, 多模态大模型, 视觉理解基准, 对抗过滤, 遥感推理, 图像描述

## 3 点简述
- 现有遥感多模态大模型基准依赖低分辨率图像，且推理任务设计存在缺陷，导致文本模型也能竞争。
- 构建包含5,329张超高分图像的基准，设计四类任务，覆盖感知和推理，采用对抗过滤和人工验证减少语言先验依赖。
- 评估显示开源、闭源及遥感专用模型在超高分场景下仍存在性能差距，代码已开源。

## 摘要（原文）

> Multimodal large language models (MLLMs) demonstrate strong perception and reasoning performance on existing remote sensing (RS) benchmarks. However, most prior benchmarks rely on low-resolution imagery, and some high-resolution benchmarks suffer from flawed reasoning-task designs. We show that text-only LLMs can perform competitively with multimodal vision-language models on RS reasoning tasks without access to images, revealing a critical mismatch between current benchmarks and the intended evaluation of visual understanding. To enable faithful assessment, we introduce RSHR-Bench, a super-high-resolution benchmark for RS visual understanding and reasoning. RSHR-Bench contains 5,329 full-scene images with a long side of at least 4,000 pixels, with up to about 3 x 10^8 pixels per image, sourced from widely used RS corpora and UAV collections. We design four task families: multiple-choice VQA, open-ended VQA, image captioning, and single-image evaluation. These tasks cover nine perception categories and four reasoning types, supporting multi-turn and multi-image dialog. To reduce reliance on language priors, we apply adversarial filtering with strong LLMs followed by rigorous human verification. Overall, we construct 3,864 VQA tasks, 3,913 image captioning tasks, and 500 fully human-written or verified single-image evaluation VQA pairs. Evaluations across open-source, closed-source, and RS-specific VLMs reveal persistent performance gaps in super-high-resolution scenarios. Code: https://github.com/Yunkaidang/RSHR

