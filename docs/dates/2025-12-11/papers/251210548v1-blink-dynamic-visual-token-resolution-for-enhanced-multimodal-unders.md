---
layout: default
title: Blink: Dynamic Visual Token Resolution for Enhanced Multimodal Understanding
---

# Blink: Dynamic Visual Token Resolution for Enhanced Multimodal Understanding
**arXiv**：[2512.10548v1](https://arxiv.org/abs/2512.10548) · [PDF](https://arxiv.org/pdf/2512.10548.pdf)  
**作者**：Yuchen Feng, Zhenyu Zhang, Naibin Gu, Yilong Chen, Peng Fu, Zheng Lin, Shuohuan Wang, Yu Sun, Hua Wu, Weiping Wang, Haifeng Wang  

**一句话要点**：提出Blink动态视觉令牌分辨率框架，以增强多模态大语言模型的视觉感知能力。

**关键词**：多模态大语言模型, 视觉感知增强, 动态令牌分辨率, 显著性引导, 令牌超分辨率, 自适应计算

## 3 点简述
- 核心问题：多模态大语言模型视觉感知有限，缺乏人类动态扫描和聚焦显著区域的能力。
- 方法要点：通过显著性引导扫描和动态令牌分辨率模块，在单次前向传播中模拟人类眨眼过程，自适应分配计算资源。
- 实验或效果：广泛实验验证Blink能有效提升视觉感知和多模态理解性能，实现高效自适应增强。

## 摘要（原文）

> Multimodal large language models (MLLMs) have achieved remarkable progress on various vision-language tasks, yet their visual perception remains limited. Humans, in comparison, perceive complex scenes efficiently by dynamically scanning and focusing on salient regions in a sequential "blink-like" process. Motivated by this strategy, we first investigate whether MLLMs exhibit similar behavior. Our pilot analysis reveals that MLLMs naturally attend to different visual regions across layers and that selectively allocating more computation to salient tokens can enhance visual perception. Building on this insight, we propose Blink, a dynamic visual token resolution framework that emulates the human-inspired process within a single forward pass. Specifically, Blink includes two modules: saliency-guided scanning and dynamic token resolution. It first estimates the saliency of visual tokens in each layer based on the attention map, and extends important tokens through a plug-and-play token super-resolution (TokenSR) module. In the next layer, it drops the extended tokens when they lose focus. This dynamic mechanism balances broad exploration and fine-grained focus, thereby enhancing visual perception adaptively and efficiently. Extensive experiments validate Blink, demonstrating its effectiveness in enhancing visual perception and multimodal understanding.

