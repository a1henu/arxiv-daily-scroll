---
layout: default
title: Better Tokens for Better 3D: Advancing Vision-Language Modeling in 3D Medical Imaging
---

# Better Tokens for Better 3D: Advancing Vision-Language Modeling in 3D Medical Imaging
**arXiv**：[2510.20639v1](https://arxiv.org/abs/2510.20639) · [PDF](https://arxiv.org/pdf/2510.20639.pdf)  
**作者**：Ibrahim Ethem Hamamci, Sezgin Er, Suprosanna Shit, Hadrien Reynaud, Dong Yang, Pengfei Guo, Marc Edgar, Daguang Xu, Bernhard Kainz, Bjoern Menze  

**一句话要点**：提出BTB3D方法以解决3D医学影像中高分辨率长序列的视觉-语言建模问题

**关键词**：3D医学影像, 视觉-语言建模, 体积标记化, 因果卷积, 报告生成, 文本到图像合成

## 3 点简述
- 核心问题：当前方法在高分辨率长序列3D医学影像中，视觉编码器与临床语言不匹配，且切片级标记化模糊精细解剖结构
- 方法要点：采用因果卷积编码器-解码器，统一2D和3D训练推理，生成紧凑的频率感知体积标记
- 实验或效果：在报告生成和文本到CT合成任务中，显著提升BLEU分数、临床F1，并大幅降低FID和FVD

## 摘要（原文）

> Recent progress in vision-language modeling for 3D medical imaging has been
> fueled by large-scale computed tomography (CT) corpora with paired free-text
> reports, stronger architectures, and powerful pretrained models. This has
> enabled applications such as automated report generation and text-conditioned
> 3D image synthesis. Yet, current approaches struggle with high-resolution,
> long-sequence volumes: contrastive pretraining often yields vision encoders
> that are misaligned with clinical language, and slice-wise tokenization blurs
> fine anatomy, reducing diagnostic performance on downstream tasks. We introduce
> BTB3D (Better Tokens for Better 3D), a causal convolutional encoder-decoder
> that unifies 2D and 3D training and inference while producing compact,
> frequency-aware volumetric tokens. A three-stage training curriculum enables
> (i) local reconstruction, (ii) overlapping-window tiling, and (iii)
> long-context decoder refinement, during which the model learns from short slice
> excerpts yet generalizes to scans exceeding 300 slices without additional
> memory overhead. BTB3D sets a new state-of-the-art on two key tasks: it
> improves BLEU scores and increases clinical F1 by 40% over CT2Rep, CT-CHAT, and
> Merlin for report generation; and it reduces FID by 75% and halves FVD compared
> to GenerateCT and MedSyn for text-to-CT synthesis, producing anatomically
> consistent 512*512*241 volumes. These results confirm that precise
> three-dimensional tokenization, rather than larger language backbones alone, is
> essential for scalable vision-language modeling in 3D medical imaging. The
> codebase is available at: https://github.com/ibrahimethemhamamci/BTB3D

