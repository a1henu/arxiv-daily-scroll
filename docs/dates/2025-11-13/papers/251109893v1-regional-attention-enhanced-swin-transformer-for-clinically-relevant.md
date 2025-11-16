---
layout: default
title: Regional Attention-Enhanced Swin Transformer for Clinically Relevant Medical Image Captioning
---

# Regional Attention-Enhanced Swin Transformer for Clinically Relevant Medical Image Captioning
**arXiv**：[2511.09893v1](https://arxiv.org/abs/2511.09893) · [PDF](https://arxiv.org/pdf/2511.09893.pdf)  
**作者**：Zubia Naz, Farhan Asghar, Muhammad Ishfaq Hussain, Yahya Hadadi, Muhammad Aasim Rafique, Wookjin Choi, Moongu Jeon  

**一句话要点**：提出区域注意力增强Swin-BART模型以提升医学图像描述临床准确性

**关键词**：医学图像描述, 区域注意力, Swin-BART模型, ROCO数据集, 语义保真度, 临床报告支持

## 3 点简述
- 核心问题：自动化医学图像描述需生成诊断性叙述，支持报告工作流。
- 方法要点：集成Swin-BART编码器-解码器，添加轻量级区域注意力模块增强诊断区域。
- 实验或效果：在ROCO数据集上实现SOTA语义保真度，ROUGE和BERTScore显著提升。

## 摘要（原文）

> Automated medical image captioning translates complex radiological images into diagnostic narratives that can support reporting workflows. We present a Swin-BART encoder-decoder system with a lightweight regional attention module that amplifies diagnostically salient regions before cross-attention. Trained and evaluated on ROCO, our model achieves state-of-the-art semantic fidelity while remaining compact and interpretable. We report results as mean$\pm$std over three seeds and include $95\%$ confidence intervals. Compared with baselines, our approach improves ROUGE (proposed 0.603, ResNet-CNN 0.356, BLIP2-OPT 0.255) and BERTScore (proposed 0.807, BLIP2-OPT 0.645, ResNet-CNN 0.623), with competitive BLEU, CIDEr, and METEOR. We further provide ablations (regional attention on/off and token-count sweep), per-modality analysis (CT/MRI/X-ray), paired significance tests, and qualitative heatmaps that visualize the regions driving each description. Decoding uses beam search (beam size $=4$), length penalty $=1.1$, $no\_repeat\_ngram\_size$ $=3$, and max length $=128$. The proposed design yields accurate, clinically phrased captions and transparent regional attributions, supporting safe research use with a human in the loop.

