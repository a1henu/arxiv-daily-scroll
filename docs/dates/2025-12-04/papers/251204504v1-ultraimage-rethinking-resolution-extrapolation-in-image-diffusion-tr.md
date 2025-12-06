---
layout: default
title: UltraImage: Rethinking Resolution Extrapolation in Image Diffusion Transformers
---

# UltraImage: Rethinking Resolution Extrapolation in Image Diffusion Transformers
**arXiv**：[2512.04504v1](https://arxiv.org/abs/2512.04504) · [PDF](https://arxiv.org/pdf/2512.04504.pdf)  
**作者**：Min Zhao, Bokai Yan, Xue Yang, Hongzhou Zhu, Jintao Zhang, Shilong Liu, Chongxuan Li, Jun Zhu  

**一句话要点**：提出UltraImage框架，通过频率校正和自适应注意力解决图像扩散变换器分辨率外推中的内容重复和质量下降问题。

**关键词**：图像扩散变换器, 分辨率外推, 位置嵌入分析, 注意力机制优化, 高分辨率图像生成

## 3 点简述
- 核心问题：图像扩散变换器在分辨率外推时出现内容重复和质量下降，源于位置嵌入的周期性主导频率和注意力稀释。
- 方法要点：采用递归主导频率校正约束周期，并引入熵引导自适应注意力集中以优化局部和全局注意力。
- 实验或效果：在Qwen-Image和Flux上优于现有方法，能生成高达6K*6K图像，减少重复并提升视觉保真度。

## 摘要（原文）

> Recent image diffusion transformers achieve high-fidelity generation, but struggle to generate images beyond these scales, suffering from content repetition and quality degradation. In this work, we present UltraImage, a principled framework that addresses both issues. Through frequency-wise analysis of positional embeddings, we identify that repetition arises from the periodicity of the dominant frequency, whose period aligns with the training resolution. We introduce a recursive dominant frequency correction to constrain it within a single period after extrapolation. Furthermore, we find that quality degradation stems from diluted attention and thus propose entropy-guided adaptive attention concentration, which assigns higher focus factors to sharpen local attention for fine detail and lower ones to global attention patterns to preserve structural consistency. Experiments show that UltraImage consistently outperforms prior methods on Qwen-Image and Flux (around 4K) across three generation scenarios, reducing repetition and improving visual fidelity. Moreover, UltraImage can generate images up to 6K*6K without low-resolution guidance from a training resolution of 1328p, demonstrating its extreme extrapolation capability. Project page is available at \href{https://thu-ml.github.io/ultraimage.github.io/}{https://thu-ml.github.io/ultraimage.github.io/}.

