---
layout: default
title: CLIP is All You Need for Human-like Semantic Representations in Stable Diffusion
---

# CLIP is All You Need for Human-like Semantic Representations in Stable Diffusion
**arXiv**：[2511.08075v1](https://arxiv.org/abs/2511.08075) · [PDF](https://arxiv.org/pdf/2511.08075.pdf)  
**作者**：Cameron Braunstein, Mariya Toneva, Eddy Ilg  

**一句话要点**：揭示CLIP在Stable Diffusion中主导人类语义表示，而非扩散过程

**关键词**：语义表示, 文本到图像生成, CLIP模型, 扩散模型, 模型探测

## 3 点简述
- 研究Stable Diffusion在文本到图像生成中是否具有人类可理解的语义表示
- 使用回归层探测模型内部表示，预测语义属性并与人类标注比较
- 发现CLIP文本编码决定语义表示，扩散过程仅作为视觉解码器

## 摘要（原文）

> Latent diffusion models such as Stable Diffusion achieve state-of-the-art results on text-to-image generation tasks. However, the extent to which these models have a semantic understanding of the images they generate is not well understood. In this work, we investigate whether the internal representations used by these models during text-to-image generation contain semantic information that is meaningful to humans. To do so, we perform probing on Stable Diffusion with simple regression layers that predict semantic attributes for objects and evaluate these predictions against human annotations. Surprisingly, we find that this success can actually be attributed to the text encoding occurring in CLIP rather than the reverse diffusion process. We demonstrate that groups of specific semantic attributes have markedly different decoding accuracy than the average, and are thus represented to different degrees. Finally, we show that attributes become more difficult to disambiguate from one another during the inverse diffusion process, further demonstrating the strongest semantic representation of object attributes in CLIP. We conclude that the separately trained CLIP vision-language model is what determines the human-like semantic representation, and that the diffusion process instead takes the role of a visual decoder.

