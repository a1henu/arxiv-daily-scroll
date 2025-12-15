---
layout: default
title: EditMGT: Unleashing Potentials of Masked Generative Transformers in Image Editing
---

# EditMGT: Unleashing Potentials of Masked Generative Transformers in Image Editing
**arXiv**：[2512.11715v1](https://arxiv.org/abs/2512.11715) · [PDF](https://arxiv.org/pdf/2512.11715.pdf)  
**作者**：Wei Chow, Linfeng Li, Lingdong Kong, Zefeng Li, Qi Xu, Hang Song, Tian Ye, Xian Wang, Jinbin Bai, Shilin Xu, Xiangtai Li, Junting Pan, Shaoteng Liu, Ran Zhou, Tianshu Yang, Songhua Liu  

**一句话要点**：提出EditMGT框架，利用掩码生成Transformer解决图像编辑中非目标区域意外修改问题。

**关键词**：图像编辑, 掩码生成Transformer, 局部解码, 注意力机制, 区域保持采样, 高分辨率数据集

## 3 点简述
- 扩散模型全局去噪导致非目标区域意外修改，转向掩码生成Transformer的局部解码范式。
- 基于交叉注意力图精确定位编辑区域，引入区域保持采样限制修改范围。
- 在四个基准测试中，模型参数少于10亿，实现相似性能且编辑速度提升6倍。

## 摘要（原文）

> Recent advances in diffusion models (DMs) have achieved exceptional visual quality in image editing tasks. However, the global denoising dynamics of DMs inherently conflate local editing targets with the full-image context, leading to unintended modifications in non-target regions. In this paper, we shift our attention beyond DMs and turn to Masked Generative Transformers (MGTs) as an alternative approach to tackle this challenge. By predicting multiple masked tokens rather than holistic refinement, MGTs exhibit a localized decoding paradigm that endows them with the inherent capacity to explicitly preserve non-relevant regions during the editing process. Building upon this insight, we introduce the first MGT-based image editing framework, termed EditMGT. We first demonstrate that MGT's cross-attention maps provide informative localization signals for localizing edit-relevant regions and devise a multi-layer attention consolidation scheme that refines these maps to achieve fine-grained and precise localization. On top of these adaptive localization results, we introduce region-hold sampling, which restricts token flipping within low-attention areas to suppress spurious edits, thereby confining modifications to the intended target regions and preserving the integrity of surrounding non-target areas. To train EditMGT, we construct CrispEdit-2M, a high-resolution dataset spanning seven diverse editing categories. Without introducing additional parameters, we adapt a pre-trained text-to-image MGT into an image editing model through attention injection. Extensive experiments across four standard benchmarks demonstrate that, with fewer than 1B parameters, our model achieves similarity performance while enabling 6 times faster editing. Moreover, it delivers comparable or superior editing quality, with improvements of 3.6% and 17.6% on style change and style transfer tasks, respectively.

