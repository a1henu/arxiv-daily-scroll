---
layout: default
title: BLINK-Twice: You see, but do you observe? A Reasoning Benchmark on Visual Perception
---

# BLINK-Twice: You see, but do you observe? A Reasoning Benchmark on Visual Perception
**arXiv**：[2510.09361v1](https://arxiv.org/abs/2510.09361) · [PDF](https://arxiv.org/pdf/2510.09361.pdf)  
**作者**：Junyan Ye, Dongzhi Jiang, Jun He, Baichuan Zhou, Zilong Huang, Zhiyuan Yan, Hongsheng Li, Conghui He, Weijia Li  
**一句话要点**：提出BLINK-Twice基准以评估多模态大模型在视觉感知推理中的能力

**关键词**：多模态大语言模型, 视觉推理基准, 感知任务, 对抗图像对, 推理链评估, 模型性能分析

## 3 点简述
- 现有基准多关注语言推理，视觉输入常被替代，缺乏视觉中心推理评估
- 基准包含七类视觉挑战、自然对抗图像对和标注推理链，强调从视觉内容推理
- 评估20个领先模型，发现现有推理策略不稳定，重复观察和主动交互可提升性能

## 摘要（原文）

> Recently, Multimodal Large Language Models (MLLMs) have made rapid progress,
> particularly in enhancing their reasoning capabilities. However, existing
> reasoning benchmarks still primarily assess language-based reasoning, often
> treating visual input as replaceable context. To address this gap, we introduce
> BLINK-Twice, a vision-centric reasoning benchmark grounded in challenging
> perceptual tasks. Instead of relying on external knowledge, our tasks require
> models to reason from visual content alone, shifting the focus from
> language-based to image-grounded reasoning. Compared to prior perception
> benchmarks, it moves beyond shallow perception ("see") and requires
> fine-grained observation and analytical reasoning ("observe"). BLINK-Twice
> integrates three core components: seven types of visual challenges for testing
> visual reasoning, natural adversarial image pairs that enforce reliance on
> visual content, and annotated reasoning chains for fine-grained evaluation of
> the reasoning process rather than final answers alone. We evaluate 20 leading
> MLLMs, including 12 foundation models and 8 reasoning-enhanced models.
> BLINK-Twice poses a significant challenge to current models. While existing
> reasoning strategies in the language space-such as chain-of-thought or
> self-criticism can improve performance, they often result in unstable and
> redundant reasoning. We observe that repeated image observation improves
> performance across models, and active visual interaction, as demonstrated by
> models like o3, highlights the need for a new paradigm for vision reasoning.
> The dataset is publicly available at https://github.com/PicoTrex/BLINK-Twice

